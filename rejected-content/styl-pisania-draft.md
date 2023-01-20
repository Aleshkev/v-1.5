# Styl pisania

## Aspekty techniczne

Wszystko co tutaj ma robić się automatycznie to ambitne cele, nie do końca jeszcze zrealizowane.

### Przypisy

Przypisy tworzy się przez _de facto_ standardową składnię Markdowna: `^[treść]`, lub `[^id]` i potem w osobnym paragrafie `[^id]: treść` – wtedy można umieścić wiele paragrafów treści za pomocą wcięcia.

Przypisy są na marginesie jeżeli ekran czytelnika jest dostatecznie szeroki i włączony jest JavaScript, w innym razie wyświetlają się po elemencie, w którym się znalazły. Jeżeli na marginesie, ich górny bok jest wyrównany do miejsca w paragrafie, gdzie się znalazły w kodzie źródłowym – _kotwicy._

Jest to osiągane przez dodanie w HTML-u w paragrafie kotwicy połączonej z elementem `<aside>`, umieszczonym za paragrafem, przez wspólny atrybut. JavaScript ustawia górną pozycję Y na górną pozycję Y kotwicy, rozwiązując konflikty gdy dwa przypisy na siebie nachodzą.

Przypisy mają lekko mniejszą czcionkę (75-80% em) niż reszta tekstu.

### Język elementów

Dowolny element, jeżeli wszystkie słowa w środku, z dużą pewnością heurystycznego algorytmu, występują w jakimś innym języku, ma ustawiony ten język.

Dzięki temu zamiast `<em lang="en">competitive programming</em>` można pisać `_competitive programming_` – zostanie stworzony przez Markdowna element `em`, dla którego obowiązuje ta zasada. Wydzielanie języka to więc tylko kwestia stworzenia elementu, gdzie jest potrzebny, np. `<span>opinion piece</span>`.

Oczywiście nadal można dla pewności ustawiać `lang="xx"`.

### Typografia

Biorąc pod uwagę język każdego elementu, automatycznie wstawiane/zastępowane są znaki:

- `&shy;` w środkach wyrazów (hyfenizacja/myślnikowanie),
- spacje przez `&nbsp;` po samotnych literach.
- `""` przez „”,
- `''` przez »« – nie ma w ASCII lepszego znaku, a ten jest używany też w j. angielskim; tak jest też w ReStructuredTexcie.

Może być tak, że cudzysłowy muszą być zamknięte w tym samym elemencie, w którym zostały otwarte, np. `*"x*"` może nie skutkować tym samym co `*„x*”`.

Cudzysłowy na początku i końcu linii wychodzą na margines (wisząca interpunkcja).

Nie ma żadnej substytucji dla znaków °, ′ i ″, ponieważ rzadko występują w j. polskim. Należy pisać `15&deg;` lub `1&prime;20&Prime;` dla 15°, 1′20″.

Automatycznie zastępowane są symbole:

- `--` przez –, `---` przez —;
- `...` przez …;
- `-->` przez →, `<--` przez ←;
- spacje w sytuacjach jak `1 000 000` przez `&numsp;` – do dzielenia liczb nie należy używać `,` ani `.`.

Między zdaniami jest jedna spacja.

### Czcionki

Podkreślenia (głównie łączy) mają odpowiednią, zbalansowaną grubość.

Czcionka ma ligatury. Czcionka jest kernowana (`text-rendering: optimizeLegibility`).

Dostosowywane, szczególnie w tytułach, są odstępy międzyliterowe i interlinia. Przy niektórych początkowych znakach w tytułach ustawiany jest lekko ujemny `text-indent`.

Z czcionki usuwane są niepotrzebne, rzadko używane znaki oraz takie, które lepiej wyglądają w czcionce niżej w stosie.

Cyfry używają formy wersalikowej _(old-style numerals),_ w przeciwieństwie do cyfr nautycznych _(lining numerals)._

Cyfry w tabelkach mają wszystkie tę samą szerokość.

### Stylizowanie

Usuwane są puste paragrafy. Jeżeli zostały stworzone przez kotwicę przypisu, jest ona przełożona na początek kolejnego niepustego paragrafu.

Słowa pochylone lub pogrubione bezpośrednio dotykające znaków interpunkcyjnych pochylają lub pogrubiają również ten znak interpunkcyjny.

Paragraf poprzedzony bezpośrednio innym paragrafem jest wizualnie oddzielony jedynie wcięciem (dokładnie 1 em), nie odstępem.

Listy poprzedzone bezpośrednio paragrafem nie są od niego oddzielone odstępem.

Listy nieuporządkowane używają znaków myślników, nie punktów. Jeżeliby już ich używały, nie byłyby to domyślne punkty tylko lepiej zbalansowane.

Wcięcia list są magiczne i nie mam pojęcia jak je dobrać, żeby to najlepiej wyglądało, jakby ktoś wiedział to proszę pomóc. Brak wcięcia nie jest rozwiązaniem.

### Blokowy i wewnątrzliniowy kod

Wszystkie zasady typograficzne nie obowiązują w kodzie, nic nie jest w nim automatycznie zastępowane.

Czcionka powinna mieć wyrównany _x-height_ do głównej czcionki – także w tytułach.

Kolorowanie składni wykonywane jest w profesjonalny sposób, np. Syntectem, lub w mniej profesjonalny sposób dla szybko tworzonej własnej składni, np. highlight.js-em.

Bloki kodu mogą mieć maks. 70 znaków, potem nie mieszczą się w kolumnie tekstu.

### Ostrzeżenia

System ostrzega, jeżeli w jakimś dokumencie jest niezbalansowana ilość nawiasów.

### Rzeczy, których nienawidzę czytać, więc obiecuję też nie pisać

- kwiatki /w znaczeniu ładne przykłady, przypadki/
- zupełnie inna bajka
- zdroworozsądkowy
- atencyjny/atencjusz
- utracjusz
- triumwirrat
