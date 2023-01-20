---
tags: meta, blog, projekt życia
revised: 2019-08-09
---


# _Showcase_ tagów tudzież elementów wybieranych elementarnego systemu tworzenia treści

Wydaje mi się, że każda strona będzie miała mnei więcej taką strukturę. Zaczyna się od krótkiego wstępu.

Ponieważ mam blog i odczuwam potrzebę wypełnienia go nieinteresująco specyficznymi postami, zacznę od tematu, w którym jestem ekspertem: programu, którego samemu stworzyłem.

# (_text_) _Hello_;.,.!

---

Oto jest pargagraf, po którym następuje oczekiwana przez wszystkich lista. Można zadbać, żeby była bardzo ładna i przejrzysta, a najlepiej zajmowała przynajmniej jedną całą linię:
- przedmiot 1
- To jest drugie statycznych stronach nadal może być JavaScript wykonywany po stronie klienta, więc nie są statyczne pod wszystkimi względami -- chociaż nie polecane jest dodawanie za dużej ich ilości, gdyż jako jedną z zalet wymieniłem wcześniej wydajność.
- To jest linia 3. Jak widać, bardzo ładna.

Oto jest pargagraf, po którym następuje oczekiwana przez wszystkich lista. Można zadbać, żeby była bardzo ładna i przejrzysta, a najlepiej zajmowała przynajmniej jedną całą linię:
1. przedmiot 1
2. To jest drugie statycznych stronach nadal może być JavaScript wykonywany po stronie klienta, więc nie są statyczne pod wszystkimi względami -- chociaż nie polecane jest dodawanie za dużej ich ilości, gdyż jako jedną z zalet wymieniłem wcześniej wydajność.
3. To jest linia 3. Jak widać, bardzo ładna.

## Dlaczego renderuję strony?

### Ponieważ.

Ostatnio popularne wśród deweloperów są [generatory statycznych stron](https://www.staticgen.com).^[Jeżeli wiecie co to jest, możecie pominąć tę sekcję, będzie dla was trochę patronizująca.] Tworzą one pliki HTML gotowe do wysłania każdemu użytkownikomi witryny, bez potrzeby zaawansowanego serwera -- wystarczy, że będzie on wysyłał odpowiednie pliki.^[Hello]

![To jest niesamowita wieża.](https://static01.nyt.com/images/2019/10/27/opinion/00mit1-08/00mit1-08-superJumbo.jpg?quality=90&auto=webp)

Oznacza to, że taki serwer jest wydajny, bezpieczny i tani -- w istocie na tyle tani, że niektóre firmy zapewniają darmowy każdemu użytkownikowi. Przykładem jest [GitHub Pages](https://pages.github.com), którego ja w tym momencie osobiście używam. (Dlatego URL mojej strony zawiera `github.io`, ale da się to łatwo rozwiązać wykupując własną domenę.)

### Inna przyczyna?

W statycznych stronach nadal może być JavaScript wykonywany po stronie klienta, więc nie są statyczne pod wszystkimi względami -- chociaż nie polecane jest dodawanie za dużej ich ilości, gdyż jako jedną z zalet wymieniłem wcześniej wydajność.

---

Dla mnie najważniejsze jest to, że gdy raz wyrenderuję stronę, nic się nie może dalej zepsuć. Serwer nie scrashuje w środku nocy pozbawiając świat moich światłych przemyśleń na jego temat.

## Dlaczego stworzyłem własny system renderowania stron?

Dzięki prostemu procesowi szukania odpowiedniej technologii do moich potrzeb, który powinienem kiedyś opatentować:
1. Stwórz listę wymagań, gdzie każde brzmi rozsądnie, ale są nierealistyczne gdy jest ich dostatecznie dużo, np.:
    - Stwórz biblioteka musi być w Pythonie (żebym umiał napisać rozszerzenia),
    
        Takie punkty mogą mieć więcej niż 1 paragraf.
    - nie może być jedynie portem biblioteki w innym języku (bo wtedy API jest nie-Pythonowe),
    - musi być popularna i ostatnio aktualizowana (żeby było wsparcie jakby coś poszło nie tak), 
    - kod musi być na GitHubie (lubię GitHuba),
    - pisanie treści oczywiście w Markdownie z dobrymi rozszerzeniami, np. do matematyki. ^[O tym dlaczego mimo wszystkich jego wad wolę Markdowna od ReStructuredTexta czy AsciiDoca napiszę innym razem]
2. Przechodź po liście wszystkich technologii porównując każdą z wymaganiami, odrzucając wszystkie po kolei.

Przede wszystkim, mogę stworzyć np. taki blok:^[Notatka (paragraf)]

```cpp
        1         2         3         4         5         6
///////////////////////////////////////////////////////////
#include <iostream>

int main(int argc, char *argv[]) {

  /* An annoying "Hello World" example */
  for (auto i = 0; i < 0xFFFF; i++)
    cout << "Hello, World!" << endl;

  char c = '\n';
  unordered_map <string, vector<string> > m;
  m["key"] = "\\\\"; // this is an error

  return -2e3 + 12l;
}
```

Naprawdę imponujące.^[Notatka (paragraf)]^[Notatka #2]^[Notatka #3]

> Oto jest cytat. Myślę, że dobrze by było, jakby `<cite/>` było wyrównane do prawej.^[Notatka (cytat)]
>
>
> <cite> --- Jonasz Aleszkiewicz</cite>

To jest tabelka, ona może być *bardzo* szeroka:^[Notatka (paragraf)]

| Syntax      | Description | Test Text     |
| :---        |    :----:   |          ---: |
| Header      | Title^[Notatka] | Here's this   |
| Paragraph   | Text        | And more      |

- How to manage stress.
- How to relate to millenials.

1. The first item
2. The second item
3. The third item

> This is the most important thing I have to say
>
> <cite> — John Ford

Historia wszelkiego społeczeństwa dotychczasowego jest historią walk klasowych.

Wolny i niewolnik, patrycjusz i plebejusz, pan feudalny i chłop-poddany, majster cechowy i czeladnik, krótko mówiąc, ciemiężyciele i uciemiężeni pozostawali w stałym do siebie przeciwieństwie, prowadzili nieustanną, to ukrytą, to jawną walkę, - walkę, która za każdym razem kończyła się rewolucyjnym przekształceniem całego społeczeństwa, lub też wspólną zagładą walczących klas.

```
///////////////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////////////
###############################################################################
wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww
```

W poprzednich epokach historycznych znajdujemy prawie wszędzie zupełne rozczłonkowanie społeczeństwa na rozmaite stany, całą drabinę hierarchiczną różnorodnych stanowisk społecznych. W starożytnym Rzymie mamy patrycjuszów, rycerzy, plebejuszów, niewolników; w wiekach średnich - panów feudalnych, wasali, mieszczan cechowych, czeladników, chłopów-poddanych i ponadto jeszcze wewnątrz prawie każdej z tych klas znowu odrębną hierarchię. ^[Wyrosłe z upadku społeczeństwa feudalnego nowoczesne społeczeństwo burżuazyjne nie zniosło przeciwieństw klasowych. Zastąpiło ono jedynie dawne klasy, dawne warunki ucisku, dawne formy walki przez nowe.]

Z chłopów-poddanych średniowiecza wyszli mieszczanie grodowi pierwszych miast, z mieszczan grodowych rozwinęły się pierwsze elementy burżuazyjne.

Odkrycie Ameryki i drogi morskiej dokoła Afryki otworzyło przed rosnącą burżuazją nowe tereny. Rynek wschodnioindyjski i chiński, kolonizacja Ameryki, wymiana z koloniami, pomnożę' nic środków wymiany i w ogóle towarów wywołały nieznany ni-gdy przedtem rozkwit handlu, żeglugi, przemysłu, a tym samym spowodowały szybki rozwój czynnika rewolucyjnego w rozpadającym się społeczeństwie feudalnym. ^[Nasza epoka, epoka burżuazji, wyróżnia się jednakże tym, ze uprościła przeciwieństwa klasowe. Całe społeczeństwo rozszczepia się coraz bardziej i bardziej na dwa wielkie wrogie obozy, na dwie wielkie, wręcz przeciwstawne sobie klasy: burżuazję i proletariat.]


---

Dotychczasowy feudalny czyli cechowy sposób produkcji przemysłowej nie wystarczał już do zaspokojenia wzrastającego wraz z nowymi rynkami zapotrzebowania. Miejsce jego zajął przemysł rękodzielniczy. Majstrowie cechowi zostali wyparci przez przemysłowy stan średni; podział pracy pomiędzy rozmaitymi korporacjami cechowymi ustąpił miejsca podziałowi pracy wewnątrz poszczególnego warsztatu.

> Ale wciąż rosły rynki, stale wzrastało zapotrzebowanie. Przemysł rękodzielniczy również już nic wystarczał. Wówczas para i maszyna zrewolucjonizowały produkcję przemysłową. Miejsce przemysłu rękodzielniczego zajął nowoczesny wielki przemysł, miejsce przemysłowego stanu średniego zajęli przemysłowcy-milionerzy, dowódcy całych armii przemysłowych, współcześni burżua.
>
> Wielki przemysł stworzył rynek światowy, przygotowany przez odkrycie Ameryki. Rynek światowy wywołał niebywały rozwój handlu, żeglugi, środków komunikacji lądowej. Rozwój ten wpłynął z kolei na rozrost przemysłu, i w tym samym stopniu, w jakim rozwijał się przemysł, handel, żegluga, koleje żelazne, w tym samym stopniu rozwijała się burżuazją, mnożyła swoje kapitały, spychała w cień wszystkie klasy odziedziczone po średniowieczu.

Widzimy zatem, że współczesna burżuazja sama jest wytworem długiego procesu rozwojowego, szeregu przewrotów w sposobie produkcji i wymiany.

Każdemu z tych **szczebli rozwoju burżuazji** towarzyszył odpowiedni postęp polityczny Stan uciemiężony pod panowaniem panów feudalnych, uzbrojone i samorządne zrzeszenie w komunie, tu - niezależna republika miejska, ówdzie - podatniczy stan trzeci monarchii, później, w okresie przemysłu rękodzielniczego, przeciwwaga szlachty w monarchii stanowej albo absolutnej i główna podstawa wielkich monarchii w ogóle, - oto są stopnie, które przeszła burżuazją w swoim rozwoju; wreszcie od czasu powstania wielkiego przemysłu i rynku światowego burżuazją wywalczyła sobie wyłączne panowanie polityczne w nowoczesnym państwie parlamentarnym. Współczesna **władza państwowa** jest jedynie komitetem, zarządzającym wspólnymi interesami całej klasy burżuazyjnej.

> Możemy wyróżnić trzy klasy:
> - patrycjusze
> - robotnicy
> - niewolnicy
> - kapitaliści.

Burżuazją odegrała w historii rolę w najwyższym stopniu rewolucyjną.

Burżuazją, tam gdzie doszła do władzy, zburzyła wszystkie feudalne, patriarchalne, idylliczne stosunki. Pozrywała bezlitośnie wielorakie węzły feudalne, które przywiązywały człowieka do jego „naturalnego zwierzchnika" i nie pozostawiła między ludźmi żadnego innego węzła, prócz nagiego interesu, prócz wyzutej z wszelkiego sentymentu ,,zapłaty gotówką". Świątobliwe porywy zbożnego marzycielstwa, rycerskiego zapału, mieszczańskiego sentymentalizmu zatopiła w lodowatej wodzie egoistycznego wyrachowania. Godność osobistą zamieniła w wartość wymienną, a na miejsce niezliczonych, uwierzytelnionych dokumentami, uczciwie uzyskanych wolności, postawiła jedyną, pozbawioną wszelkich skrupułów wolność handlu. Słowem, na miejsce wyzysku, osłoniętego złudzeniami religijnymi i politycznymi, postawiła wyzysk jawny, bezwstydny, bezpośredni, nagi.

Burżuazja odarła z aureoli świętości wszystkie rodzaje zajęć, które cieszyły się dotychczas szacunkiem i na które spoglądano z trwożną czcią. Lekarza, prawnika, księdza, poetę, uczonego, zamieniła w swoich płatnych, najemnych robotników.

Burżuazja zdarła ze stosunków rodzinnych ich rzewnie sentymentalną zasłonę i sprowadziła je do nagiego stosunku pieniężnego.

Burżuazja wykazała, jak przejawy brutalnej siły, którymi tak zachwyca reakcję średniowiecze, znajdowały właściwe uzupełnienie w najgnuśniejszym próżniactwie. Dopiero burżuazja dowiodła, co jest w stanie zdziałać czynność ludzka. Dokonała ona całkiem innych cudów, niż zbudowanie piramid egipskich, wodociągów rzymskich i katedr gotyckich, odbyła pochody zgoła inne niż wędrówki ludów i wyprawy krzyżowe.

Burżuazja nie może istnieć bez nieustannego rewolucjonizowania narzędzi produkcji, a więc stosunków produkcji, a więc całokształtu stosunków społecznych. Natomiast pierwszym warunkiem istnienia wszystkich dawniejszych klas przemysłowych było zachowanie bez zmiany starego sposobu produkcji. Ciągły przewrót w produkcji, bezustanne wstrząsanie wszystkimi stosunkami społecznymi, wieczna niepewność i wieczny ruch - wyróżniają epokę burżuazyjną spośród wszystkich innych. Wszystkie stężałe, zaśniedziałe stosunki, wraz z nieodłącznymi od nich z dawien dawna uświęconymi pojęciami i poglądami ulegają rozkładowi, wszystkie nowopowstałe starzeją się, zanim zdążą skostnieć. Wszystko co stanowe i znieruchomiałe znika, wszelkie świętości zostają sprofanowane i ludzie są nareszcie zmuszeni patrzeć trzeźwym okiem na swe stanowisko życiowe, na swoje wzajemne stosunki. v

Potrzeba coraz szerszego zbytu dla swych produktów gna burżuazję po całej kuli ziemskiej. Wszędzie musi się ona zagnieździć, wszędzie ugruntować, wszędzie zadzierzgnąć stosunki.

Przez eksploatację rynku światowego burżuazja nadała produkcji i spożyciu wszystkich krajów charakter kosmopolityczny. Ku wielkiemu żalowi reakcjonistów usunęła spod nóg przemysłu podstawę narodową. Odwieczne narodowe gałęzie przemysłu uległy zniszczeniu i ulegają mu codziennie w dalszym ciągu. Zostają one wyparte przez nowe gałęzie przemysłu, których wprowadzenie staje się kwestią życia dla wszystkich narodów cywilizowanych, przez gałęzie przemysłu, które przerabiają już nie miejscowe, lecz sprowadzane z najodleglejszych stref surowce i których fabrykaty spożywane są nie tylko w danym kraju, lecz także we wszystkich częściach świata. Miejsce dawnych potrzeb, zaspokajanych przez wyroby krajowe, zajmują nowe, wymagające dla swego zaspokojenia produktów najodleglejszych krajów i klimatów. Dawna miejscowa i narodowa samowystarczalność i zasklepienie ustępują miejsca wszechstronnym stosunkom wzajemnym i wszechstronnej współzależności narodów. I podobnie jak w produkcji materialnej, dzieje się w produkcji duchowej. Wytwory duchowe poszczególnych narodów stają się ogólnym dorobkiem. Jednostronność i ograniczoność narodowa staje się rzeczą coraz bardziej niemożliwą, i z wielu literatur narodowych i miejscowych powstaje jedna literatura światowa.

Dzięki szybkiemu doskonaleniu wszelkich narzędzi produkcji, dzięki niezwykłemu ułatwieniu komunikacji, burżuazja wciąga w prąd cywilizacji wszystkie, nawet najbardziej barbarzyńskie narody. Taniość jej towarów jest tą ciężką artylerią, za pomocą której burzy ona wszystkie mury chińskie, zmusza do kapitulacji najbardziej zaciekłą nienawiść barbarzyńców do cudzoziemców. Pod groźbą zagłady, zniewala ona wszystkie narody do przyswojenia sobie burżuazyjnego sposobu produkcji, zniewala je do wprowadzenia u siebie tzw. cywilizacji, tj. do stania się burżua. Słowem, stwarza sobie świat na obraz i podobieństwo swoje.

Burżuazja podporządkowała wieś panowaniu miasta. Stworzyła olbrzymie miasta, zwiększyła w wysokim stopniu liczbę ludności miejskiej w przeciwieństwie do wiejskiej i wyrwała w ten sposób znaczną część ludności z idiotyzmu życia wiejskiego. Podobnie jak wieś od miasta, uzależniła ona kraje barbarzyńskie i półbarbarzyńskie od krajów cywilizowanych, narody chłopskie od narodów burżuazyjnych, Wschód od Zachodu.

Burżuazja znosi coraz bardziej rozdrobnienie środków produkcji, posiadania i ludności. Skupiła ona ludność, scentralizowała środki produkcji i skoncentrowała własność w niewielu rękach. Nieuniknionym tego następstwem była centralizacja polityczna. Niezawisłe, zaledwie sprzymierzone z sobą prowincje o odrębnych interesach, ustawach, rządach i cłach zostały zespolone w jeden naród, jeden rząd, jedno ustawodawstwo, jeden narodowy interes klasowy, jedną linię celną.

W ciągu swego stuletniego zaledwie panowania klasowego burżuazja stworzyła siły wytwórcze bardziej masowe i potężne, niż wszystkie pokolenia poprzednie razem wzięte. Ujarzmienie sił przyrody, rozpowszechnienie maszyn, zastosowanie chemii w przemyśle i rolnictwie, żegluga parowa, koleje żelazne, telegrafy elektryczne, przysposobienie pod uprawę całych części świata, uspławnienie rzek, całe jakby spod ziemi wyczarowane masy ludności - które z poprzednich stuleci przypuszczało, że takie siły wytwórcze drzemią w łonie pracy społecznej/

Widzieliśmy zatem:, środki produkcji i wymiany, na których podłożu ukształtowała się burżuazja, zostały wytworzone w społeczeństwie feudalnym. Na pewnym szczeblu rozwoju tych środków produkcji i wymiany, warunki, w których odbywała się produkcja i wymiana w społeczeństwie feudalnym, feudalna organizacja rolnictwa i rękodzielnictwa, słowem feudalne stosunki własności przestały odpowiadać rozwiniętym już siłom wytwórczym. Hamowały one produkcję, zamiast jej sprzyjać. Zamieniły się one w jej okowy. Musiały być zburzone i zostały zburzone.

Miejsce ich zajęła wolna konkurencja z odpowiadającym jej ustrojem społecznym i politycznym, z ekonomicznym i politycznym panowaniem klasy burżuazji.

W oczach naszych odbywa się podobny ruch. Burżuazyjne stosunki produkcji i wymiany, burżuazyjne stosunki własności, współczesne społeczeństwo burżuazyjne, które wyczarowało tak potężne środki produkcji i wymiany, podobne jest do czarnoksiężnika, który nie może już opanować wywołanych przez się potęg podziemnych. Od dziesięcioleci dzieje przemysłu i handlu są tylko dziejami buntu nowoczesnych sił wytwórczych przeciw nowoczesnym stosunkom produkcji, przeciw stosunkom własności, które są warunkami istnienia burżuazji i jej panowania. Dość wymienić kryzysy handlowe, które, ponawiając %ę periodycznie, coraz groźniej stawiają pod znakiem zapytania istnienie całego społeczeństwa burżuazyjnego. W czasie kryzysów handlowych ulega regularnie zniszczeniu nie tylko znaczna część wytworzonych produktów, ale także stworzonych już sił wytwórczych. W czasie kryzysów wybucha epidemia społeczna, która wszystkim poprzednim epokom wydałaby się niedorzecznością - epidemia nadprodukcji. Społeczeństwo zostaje gwałtownie cofnięte do stanu nagle powstałego barbarzyństwa, jak gdyby klęska głodowa, powszechna niszczycielska wojna pozbawiły je wszelkich środków utrzymania; przemysł, handel wydają się unicestwione, a dlaczego? Dlatego, że społeczeństwo posiada zbyt wiele cywilizacji, zbyt wiele środków utrzymania, zbyt wiele przemysłu, zbyt wiele handlu. Siły wytwórcze, którymi ono rozporządza, nie służą już więcej rozwojowi burżuazyjnych stosunków własności; przeciwnie, stały się one nazbyt dla tych stosunków potężne, są przez nie hamowane; skoro zaś tylko zaporę tę przezwyciężają, wprawiają całe społeczeństwo burżuazyjne w stan nieładu, zagrażają istnieniu burżuazyjnej własności. Stosunki burżuazyjne stały się zbyt ciasne dla wchłonięcia wytworzonego przez nie bogactwa. W jaki sposób przezwycięża burżuazja kryzysy? Z jednej strony przez przymusowe niszczenie masy sił wytwórczych; z drugiej strony, przez podbicie nowych rynków i gruntowniejszą eksploatację dawnych. W jaki więc sposób? W ten sposób, że przygotowuje kryzysy bardziej wszechstronne i potężne i zmniejsza środki zapobiegania kryzysom.

Oręż, za pomocą którego burżuazja powaliła feudalizm, zwraca się teraz przeciw samej burżuazji.

Ale burżuazja nie tylko wykuła oręż, który jej niesie zagładę; stworzyła ona także ludzi, którzy tym orężem pokierują - nowoczesnych robotników - proletariuszy.

W; tej samej mierze, w jakiej rozwija się burżuazja, tj. kapitał, rozwija się proletariat, klasa nowoczesnych robotników, którzy dopóty tylko żyją, dopóki znajdują pracę, i dopóty tylko znajdują pracę, dopóki ich praca pomnaża kapitał. Ci robotnicy, zmuszeni sprzedawać się od sztuki, są towarem, jak wszelki inny artykuł handlu, toteż na równi z innymi towarami podlegają wszelkim zmiennościom konkurencji, wszelkim wahaniom rynku.

Praca proletariuszy zatraciła na skutek rozpowszechnienia maszyn i podziału pracy wszelkie cechy samodzielności, a wraz z tym wszelki powab dla robotników. Robotnik staje się prostym dodatkiem do -maszyny, od którego wymagane są tylko czynności najprostsze, najbardziej jednostajne, do wyuczenia się najłatwiejsze. Wydatki na robotnika ograniczają się zatem niemal wyłącznie do środków żywności, niezbędnych do jego utrzymania i przedłużenia jego gatunku. Ale cena wszelkiego towaru, a więc również pracy i, równa się kosztom jego produkcji. Dlatego też w tym samym stopniu, w jakim praca staje się coraz bardziej odstręczająca, zmniejsza się płaca zarobkowa. Co więcej, w tym samym stopniu, w jakim rośnie zastosowanie maszyn i podział pracy, zwiększa się także masa pracy, bądź wskutek pomnożenia godzin pracy, bądź też wskutek zwiększenia pracy wymaganej w danym okresie czasu, przyśpieszenia biegu maszyn itd.

Nowoczesny przemysł przekształcił drobny warsztat patriarchalnego majstra w wielką fabrykę przemysłowego kapitalisty. Masy robotnicze, stłoczone w fabryce, organizowane są po żołniersku. Jako prości szeregowcy przemysłu, robotnicy oddani są pod dozór całej hierarchii podoficerów i oficerów. Są niewolnikami nie tylko klasy burżuazyjnej, państwa burżuazyjnego, są co dzień, co godzinę ujarzmiani przez maszynę, przez dozorcę, a przede wszystkim przez każdego burżua-fabrykanta. Despotyzm ten jest tym bardziej małostkowy, nienawistny, jątrzący, im jawniej proklamuje on zysk jako swój cel.

Im mniej zręczności i siły wymaga praca ręczna, tj. - im bardziej rozwija się współczesny przemysł, tym bardziej praca mężczyzn jest wypierana przez pracę kobiet. W stosunku do klasy robotniczej różnice płci i wieku nie mają już żadnego znaczenia społecznego. Istnieją już tylko narzędzia pracy, które zależnie od płci i wieku rozmaite powodują koszty.

Gdy wyzysk robotnika przez fabrykanta o tyle dobiegł końca, że robotnik otrzymuje w gotówce swoją płacę zarobkową, rzucają się nań inne odłamy burżuazji - kamienicznik, sklepikarz, lichwiarz itd.

Dotychczasowe drobne stany średnie - drobni przemysłowcy, kupcy i rentierzy, rzemieślnicy i chłopi, wszystkie te klasy spychane są do szeregów proletariatu, po części dlatego, że ich drobny kapitał nie wystarcza do prowadzenia wielkiego przedsiębiorstwa przemysłowego i nie wytrzymuje konkurencji z większymi kapitalistami, po części zaś dlatego, że ich zręczność traci na wartości wobec nowych sposobów produkcji. W, ten sposób proletariat rekrutuje się ze wszystkich klas ludności.

Proletariat przebywa różne stopnie rozwoju. Jego walka z burżuazją rozpoczyna się wraz z jego istnieniem.

Z początku walczą poszczególni robotnicy, potem robotnicy jednej fabryki, następnie robotnicy jednej gałęzi pracy w jednej miejscowości przeciw poszczególnemu burżua, który ich bezpośrednio wyzyskuje. Swe ataki zwracają oni nie tylko przeciw burżuazyjnym stosunkom produkcji, zwracają je przeciw samym narzędziom produkcji; niszczą konkurujące towary zagraniczne, rozbijają maszyny, podpalają fabryki, usiłują wywalczyć na nowo bezpowrotnie minione stanowisko średniowiecznego robotnika.

Na tym szczeblu robotnicy stanowią masę,, rozproszoną po całym kraju i rozdrobnioną przez konkurencję. Masowe zespolenie się robotników nie jest jeszcze wynikiem ich własnego zjednoczenia, lecz wynikiem zjednoczenia burżuazji, która dla osiągnięcia własnych celów politycznych musi - i na razie może jeszcze - wprawiać w ruch cały proletariat. Na tym więc szczeblu proletariusze zwalczają nie swych własnych wrogów, lecz wrogów swoich wrogów - pozostałości monarchii absolutnej, właścicieli ziemskich, nieprzemysłowych burżua, drobnych burżua. Cały ruch historyczny jest w ten sposób skoncentrowany w rękach burżuazji, każde tą drogą osiągnięte zwycięstwo jest zwycięstwem burżuazji.

Ale wraz ze wzrostem przemysłu proletariat nie tylko powiększa się liczebnie; jest on stłaczany w coraz większe masy, siła jego rośnie i coraz bardziej czuje on tę siłę. Interesy, warunki życiowe w łonie proletariatu wyrównują się coraz bardziej w miarę tego, jak maszyna zaciera coraz bardziej różnice w pracy i spycha płacę roboczą prawie wszędzie do jednakowo niskiego poziomu. Wzmagająca się konkurencja burżua między sobą i wynikające stąd kryzysy handlowe powodują coraz większe wahania płacy zarobkowej; postępujące coraz szybciej bezustanne 'doskonalenie maszyn czyni całe położenie życiowe robotników coraz bardziej niepewnym; starcia pomiędzy poszczególnym robotnikiem a poszczególnym burżua przybierają coraz bardziej charakter starć między dwiema klasami. Robotnicy zaczynają od tworzenia zjednoczeń przeciwko" burżua; jednoczą się dla obrony swej płacy zarobkowej. Tworzą nawet trwałe stowarzyszenia, celem przygotowania środków na wypadek możliwych starć. Tu i ówdzie walka przechodzi w powstania.

Od czasu do czasu robotnicy odnoszą zwycięstwo, ale tylko przejściowe. Właściwym wynikiem ich Walk jest nie bezpośrednie powodzenie, lecz coraz szerzej sięgające jednoczenie się robotników. Sprzyjają mu rosnące środki komunikacji, wytwarzane przez wielki przemysł i stwarzające łączność między robotnikami różnych miejscowości. Ale właśnie łączności potrzeba, by liczne walki lokalne, noszące wszędzie jednakowy charakter, scentralizować w walkę ogólnokrajową, w walkę klas. Ale wszelka walka klasowa jest walką polityczną. I to zjednoczenie, dla którego mieszczanom średniowiecza z ich drogami wiejskimi trzeba było stuleci, proletariat nowoczesny osiąga dzięki kolejom żelaznym w ciągu niewielu lat.

To organizowanie się proletariuszy w klasę, a tym samym w partię polityczną, jest każdej chwili na nowo rozsadzane przez konkurencję pomiędzy samymi robotnikami. Ale odradza się ono wciąż na nowo, coraz mocniej, trwałej, potężniej. Zmusza ono do uznania poszczególnych interesów robotniczych drogą ustaw, wykorzystując w tym celu rozłamy wewnętrzne wśród burżuazji. Tak na przykład ustawa o 10-godzinnym dniu pracy w Anglii.

W ogóle starcia w łonie starego społeczeństwa sprzyjają w rozmaity sposób rozwojowi proletariatu. Burżuazja znajduje się w ciągłej walce: z początku przeciwko arystokracji, później przeciw częściom samej burżuazji, których interesy popadają w sprzeczność z postępem przemysłu; stale przeciw burżuazji wszystkich innych krajów. We wszystkich tych walkach burżuazja zmuszona jest odwoływać się do proletariatu, uciekać się do jego pomocy i wciągać go w ten sposób do ruchu politycznego. Sama zatem przekazuje proletariatowi pierwiastki własnego wykształcenia, tj. broń przeciw sobie samej.

Następnie, jak widzieliśmy, wskutek postępu przemysłu całe odłamy klasy panującej spychane są do szeregów proletariatu, lub co najmniej zagrożone w swych warunkach życiowych. Również one zasilają proletariat licznymi pierwiastkami wykształcenia.

Wreszcie, w czasach, kiedy walka klasowa zbliża się ku rozstrzygnięciu, proces rozkładu wewnątrz klasy panującej, wewnątrz całego starego społeczeństwa przybiera charakter tak gwałtowny, tak jaskrawy, że drobna część klasy panującej zrywa z nią i przyłącza się do klasy rewolucyjnej, do tej klasy, do której należy przyszłość. 'Podobnie przeto jak dawniej część szlachty przeszła do burżuazji, tak obecnie część burżuazji przechodzi do proletariatu, a mianowicie część burżua-ideologów, którzy wznieśli się do teoretycznego zrozumienia całego ruchu dziejowego.

Spośród wszystkich klas, które są dziś przeciwstawne burżuazji, jedynie proletariat jest klasą rzeczywiście rewolucyjną. Pozostałe klasy upadają i giną wraz z rozwojem wielkiego przemysłu, proletariat jest tego przemysłu nieodłącznym wytworem.

Stany średnie: drobny przemysłowiec, drobny kupiec, rzemieślnik, chłop - wszystkie one zwalczają burżuazję po to, by uchronić od zagłady swoje istnienie, jako stanów średnich. Są one zatem nie rewolucyjne, lecz konserwatywne. Więcej nawet, są reakcyjne, usiłują obrócić wstecz koło historii. O ile są rewolucyjne, to tylko w obliczu oczekującego je przejścia do szeregów proletariatu, to bronią nie swych obecnych, lecz swoich przyszłych interesów, to porzucają własny punkt widzenia, aby przyjąć punkt widzenia proletariatu.

Lumpenproletariat, ten bierny wytwór gnicia najniższych warstw starego społeczeństwa, bywa tu i ówdzie wtrącany do ruchu przez rewolucję proletariacką, wskutek całego jednak swego położenia życiowego jest skłonniejszy do sprzedawania się jako narzędzie knowań reakcyjnych.

Warunki życiowe starego społeczeństwa są już unicestwione w warunkach życiowych proletariatu. Proletariusz jest pozbawiony własności; jego stosunek do żony i dzieci nie ma już nic wspólnego z burżuazyjnymi stosunkami rodzinnymi; współczesna praca przemysłowa, współczesne ujarzmienie proletariusza przez kapitał, jednakowe w Anglii jak i we Francji, w Ameryce, jak i w Niemczech, starło zeń wszelki charakter narodowy. Prawo, moralność, religia są dlań pewną ilością określonych przesądów burżuazyjnych, poza którymi ukrywa się pewna ilość określonych interesów burżuazji.

Wszystkie dawne klasy, które zdobywały władzę, starały się zabezpieczyć uzyskane już przez siebie stanowisko życiowe drogą podporządkowania całego społeczeństwa warunkom swego wzbogacenia się. Proletariusze mogą opanować społeczne siły wytwórcze tylko znosząc swój własny dotychczasowy sposób przyswajania, a przez to samo i cały dotychczasowy sposób przywłaszczenia. Proletariusze nie mają nic swojego do zabezpieczenia, muszą natomiast zburzyć wszystko, co dotychczas zabezpieczało i ochraniało własność prywatną.

Wszelkie ruchy dotychczasowe były ruchami mniejszości lub w interesie mniejszości. Ruch proletariacki jest samodzielnym ruchem olbrzymiej większości w interesie olbrzymiej większości. Proletariat, najniższa warstwa społeczeństwa obecnego, nie może się podnieść, nie może się wyprostować, nie wysadzając w powietrze całej nadbudowy warstw, stanowiących społeczeństwo oficjalne.

Aczkolwiek nie w treści, to jednak w swej formie walka proletariatu przeciw burżuazji jest przede wszystkim walką narodową. Proletariat każdego poszczególnego kraju musi, rzecz naturalna, rozprawić się przede wszystkim ze swoją własną burżuazją. ^[Dając zarys najogólniejszych faz rozwoju proletariatu, śledziliśmy przebieg mniej lub więcej utajonej wojny domowej w łonie istniejącego społeczeństwa, aż do punktu, kiedy wybucha ona otwartą rewolucją i kiedy proletariat, przez obalenie przemocą burżuazji, ugruntowuje swe panowanie.]

Wszelkie społeczeństwa dotychczasowe opierały się, jak widzieliśmy, na przeciwieństwie klas uciskających i klas uciskanych. Ale po to, by można było uciskać pewną klasę, trzeba zapewnić jej warunki, w których mogłaby ona wlec przynajmniej niewolniczy żywot. Chłop-poddany wydźwignął się w warunkach poddaństwa na członka gminy, podobnie jak drobnomieszczanin pod jarzmem feudalnego absolutyzmu na burżua. W przeciwieństwie do tego, współczesny robotnik, zamiast podnosić się wraz z postępem przemysłu, spychany jest coraz bardziej poniżej warunków istnienia swej własnej klasy. Robotnik staje się nędzarzem i pauperyzm rozwija się jeszcze szybciej niż ludność i bogactwo. Ujawnia się tu wyraźnie, że burżuazją jest niezdolna do pozostawania nadal klasą panującą społeczeństwa i do narzucania społeczeństwu warunków istnienia swej klasy jako normy regulującej. Jest ona niezdolna do panowania, gdyż jest niezdolna do zapewnienia swemu niewolnikowi egzystencji bodaj \%ramach jego niewolnictwa, gdyż jest zmuszona spychać go do takiego stanu, przy którym musi go żywić, zamiast być przezeń żywiona. Społeczeństwo nie może już istnieć pod jej panowaniem, to znaczy, - jej istnienie nie daje się nadal pogodzić ze społeczeństwem.

Podstawowym warunkiem istnienia i panowania klasy burżuazji - jest nagromadzanie bogactwa w ręku osób prywatnych, tworzenie i pomnażanie kapitału; warunkiem istnienia kapitału jest praca najemna. Praca najemna opiera się wyłącznie na konkurencji robotników pomiędzy sobą. Postęp przemysłu, którego burżuazją jest bezwolnym i biernym nosicielem, stawia na miejsce izolacji robotników, wskutek konkurencji, ich rewolucyjne zespolenie za pomocą stowarzyszenia. Wraz z rozwojem wielkiego przemysłu usuwa? się przeto spod nóg burżuazji sama podstawa, na której wytwarza ona i przywłaszcza sobie produkty. Wytwarza ona przede wszystkim swoich własnych grabarzy. Jej zagłada i zwycięstwo proletariatu są jednakowo nieuniknione.

