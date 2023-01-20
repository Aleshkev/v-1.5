
import build

build.Site(None, True, False)

from pathlib import Path

for p in Path("a/").glob("*.html"):
    p.write_text(p.read_text("utf-8").replace("/a/", "/v-1.5/").replace("/a\"", "/v-1.5\"").replace("/content/", "/v-1/"), "utf-8")

from os import system

system("cp -r content/ a/archive/")
