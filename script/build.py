import argparse
import dataclasses
import datetime
import itertools
import logging
import os
import pathlib
import re
import shutil
import subprocess
from typing import *

import jinja2
import webassets.ext.jinja2
import yaml

import functional_transforms
import typography

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

HTML = NewType('HTML', str)


@dataclasses.dataclass
class Article:
    source: pathlib.Path
    lang: str = ""
    author: HTML = ""
    date: Optional[datetime.date] = None
    revised: Optional[datetime.date] = None
    title: HTML = ""
    content: HTML = ""

    def __repr__(self):
        return f"<{self.title.replace('­', '')}>"


class Site:
    def __init__(self, article_filter: Optional[str], release: bool, minimal: bool):
        self.article_filter = article_filter
        self.release = release
        self.minimal = minimal

        self.source_dir = pathlib.Path("content/")
        self.output_dir = pathlib.Path("a/")
        self.script_dir = pathlib.Path(__file__).parent
        self.theme_dir = pathlib.Path("theme/")

        self.articles = []

        self.environment = jinja2.Environment(
            loader=jinja2.PackageLoader(__name__, os.path.relpath(self.theme_dir, self.script_dir)),
            extensions=[webassets.ext.jinja2.AssetsExtension],
            autoescape=False)
        self.environment.filters["as_absolute_url"] = self.as_absolute_url
        self.environment.assets_environment = webassets.Environment(
            str(self.output_dir), "/" + str(self.output_dir),
            load_path=[str(self.theme_dir)])
        self.environment.assets_environment.url_expire = False
        self.environment.assets_environment.debug = not self.release
        self.article_template = self.environment.get_template("article.html")
        self.index_template = self.environment.get_template("index.html")

        self.resources: Dict[pathlib.Path, pathlib.Path] = {}
        for directory, subdirectories, files in os.walk(self.source_dir):
            for file in files:
                self.add_resource(pathlib.Path(directory) / file)

        if self.release and self.output_dir.is_dir():
            shutil.rmtree(self.output_dir)

        self.index = self.source_dir / "index"
        self.add_resource(self.index, virtual=True)

        self.load_articles()
        for article in self.articles:
            log.info(f"Load {article.source}")
            self.load_article_data(article)

        self.articles.sort(key=lambda article: article.date, reverse=True)

        for article in self.articles:
            self.render_article(article)

        self.render_index()

    def add_resource(self, source_file: pathlib.Path, virtual: bool = False):
        o = source_file
        if source_file.suffix == ".md" or virtual:
            o = (self.output_dir / os.path.relpath(str(source_file), self.source_dir)).with_suffix(".html")
        self.resources[source_file] = o
        os.makedirs(o.parent, exist_ok=True)

    def as_absolute_url(self, source_file: pathlib.Path):
        p = self.resources[source_file]
        p = p.parent if p.name == "index.html" else p
        p = p.with_suffix("") if p.suffix == ".html" and self.release else p
        return "/" + str(p).replace("\\", "/")

    def load_articles(self):
        for file in self.resources.keys():
            if file.suffix != ".md":
                continue
            if self.article_filter and self.article_filter not in file.name:
                continue
            if file.name.endswith("-draft" + file.suffix) and self.minimal:
                continue

            match = re.fullmatch(r"([0-9]{4})-([0-9]{2})-([0-9]{2})-(.*)\.md", file.name)
            date = datetime.date.today()
            if match:
                *date, slug = match.groups()
                date = datetime.date(*map(int, date))

            self.articles.append(Article(file, date=date))

    @staticmethod
    def extract_metadata(md_source: str) -> Tuple[Dict[str, Any], str]:
        metadata_match = re.fullmatch(r"---\n(.*?)---\n(.*)", md_source, re.DOTALL)
        if metadata_match:
            return yaml.safe_load(metadata_match.group(1)), metadata_match.group(2)
        return {}, md_source

    def load_article_data(self, article):
        md_source = article.source.read_text("utf-8")
        metadata, md_source = self.extract_metadata(md_source)

        article.lang = metadata.get("lang", "pl")
        article.author = metadata.get("author", f'<a href="{self.as_absolute_url(self.index)}">Jonasz Aleszkiewicz</a>')
        article.revised = metadata.get("revised", None)
        assert article.revised is None or isinstance(article.revised, datetime.date)

        p = subprocess.run(['node', str(self.script_dir / 'markdown.js')],
                           input=md_source.encode("utf-8"), capture_output=True)
        assert not p.stderr, p.stderr.decode("utf-8")

        soup = functional_transforms.get_soup(p.stdout.decode("utf-8"))
        article.title = functional_transforms.extract_title(soup)
        functional_transforms.resolve_hrefs(soup, article.source, self.as_absolute_url)
        article.content = str(soup)

    def render_something(self, source: pathlib.Path, template: jinja2.Template, data: Dict[str, Any]):
        log.info(f"Render {source}")
        output_file = self.resources[source]
        soup = functional_transforms.get_soup(template.render(**data, site=self))
        functional_transforms.handle_images(soup)
        if self.release:
            typography.detect_lang(soup)
        typography.prevent_orphans(soup)
        typography.insert_soft_hyphens(soup)
        typography.readjust_dialog_spacing(soup)
        s = str(soup)
        # if self.release:
        #     s = htmlmin.minify(s)
        output_file.write_text(s, "utf-8")

    def render_article(self, article: Article):
        self.render_something(article.source, self.article_template, dict(article=article))

    def render_index(self):
        self.render_something(self.index, self.index_template, dict())


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Build the site. Use -rm for release mode.")
    parser.add_argument("--only", "-l", help="build only articles with paths containing this text")
    parser.add_argument("--release", "-r", action="store_true", help="final build to upload online")
    parser.add_argument("--minimal", "-m", action="store_true", help="skip unfinished articles")

    args = parser.parse_args()
    Site(args.only, args.release, args.minimal)
