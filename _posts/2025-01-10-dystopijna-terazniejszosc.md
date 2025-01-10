---
layout: post
title:  "Dystopijna Teraźniejszość #001: Kampanie reklamowe na Facebooku"
date:   2025-01-10 19:59:00 +0100
categories: Dystopijna terazniejszość
obrazki: /assets/images/2025-01-10-DT01/
---

> TL;DR: Kampanie reklamowe na Facebooku mogą działać w dość nieoczekiwany sposób...

Na początku małe ogłoszenie: seria wpisów `Dystopijna Teraźniejszość` którą teraz zaczynam, ma na celu pokazanie pewnych problemów około-technologicznych w raczej przyziemny sposób. Będzie tu trochę o korporacjach, algorytmach śledzących, prywatności, AI i tego typu *ciekawych* tematach.

## Słowem wstępu

> *"Na Facebooku są teraz tylko AI, starzy ludzie, patusy i boty"*
>
> ~ parafrazowany cytat kolegi

Opinie jak powyższa wydają się dość skrajne, ale obecnie często można się z nimi spotkać. Czy słusznie? Podrążmy ten temat.

Najpierw kontekst. Kumpel napisał mi, że jego znajoma założyła sobie na Facebooku stronę, na której promuje swoje lekcje języka niemieckiego. Pomysł na biznes - niezły. Ale wiadomo - trzeba dotrzeć do klientów, żeby zarobić. Racjonalnym pomysłem zdaje się promowanie wpisów przez reklamy. Mnóstwo osób i marek to robi, żeby budować zasięgi[^1]. Zdaje się, że ma to sens: za dość rozsądne kwoty można zdobyć nieosiągalne w inny sposób zasięgi.

## Wpis sponsorowany i komentarze pod nim

Jednak praktyka pokazuje, że pogłoski o śmierci Facebooka i teoria martwego internetu[^2] mogą nie być aż tak oderwane od rzeczywistości. Przyjrzyjmy się na przykładzie tego konkretnego, promowanego postu:

![Zrzut ekranu opisywanego wpisu strony Blaubeere Schule]({{page.obrazki}}wpis.png "Zrzut ekranu opisywanego wpisu strony Blaubeere Schule")

Na pierwszy rzut oka - nic specjalnego. Lekcje niemieckiego, w dodatku z reklamą w porę. W końcu "nowy rok, nowy ja" - pewnie sporo osób wpadło na pomysł, żeby z tej okazji nauczyć się nowego języka.

Można spokojnie przyjąć, że ta kampania reklamowa na Facebooku miała na celu przyciągnięcie konkretnej grupy odbiorców, mianowicie:

> osoby zainteresowane wzięciem udziału w płatnych lekcjach języka niemieckiego u tej konkretnej osoby we Wrocławiu

Teraz pomyślmy jak algorytm. Mamy słowo-klucz: `język niemiecki`. Z jakimi hasłami powiązać ten zwrot, żeby zbudować zasięgi? Może `Niemcy`, `Niemiec`, coś w ten deseń? Za proste. Furory chyba nie zrobi. To może coś bardziej angażującego? Dajmy na to, dobrze znany wszystkim Polakom zwrot: `Für Deutschland`[^3].

Nawet, jeżeli algorytm nie dobrał takiego słowa-klucza, to zdaje się że trafił w grupę docelową, na którą ten konkretny zwrot działa jak płachta na byka. Spójrzmy w komentarze pod wpisem:

![Pierwsza pula komentarzy]({{page.obrazki}}/komentarze1.png "Pierwsza pula komentarzy")

![Druga pula komentarzy]({{page.obrazki}}/komentarze2.png "Druga pula komentarzy")

Ciekawe, co?

## Ewaluacja skuteczności

Teraz zadajmy sobie kilka pytań, przechodząc od szczegółu, do ogółu.

> Czy komentującymi są osoby, które byłyby zainteresowane wzięciem udziału w płatnych lekcjach języka niemieckiego u tej konkretnej osoby?

*Nie wygląda na to. Komentujący mają w profilach miejsca z dala od Wrocławia - np. województwo podkarpackie.*

> Czy komentującymi są osoby, które byłyby zainteresowane wzięciem udziału w płatnych lekcjach języka niemieckiego?

*Nie wygląda na to. Komentujący zdają się mieć \*ekhem\* pewne uprzedzenia do tego języka.*

> Czy komentującymi są osoby, które byłyby zainteresowane tematem wpisu?

*Nie wygląda na to. Jak ma się polityka do lekcji języka?*

Chyba mamy trzykrotne pudło. To może trzeba bardziej ogólnie...

## Czy komentującymi są osoby?

Z ciekawości, przejrzałem trochę dogłębniej kilkanaście profili spośród tych, które skomentowały wpis. W przypadku wielu z nich widać wspólne cechy, takie jak:

- brak zdjęcia profilowego lub bardzo generyczne zdjęcie profilowe,
- bardzo krótka lub bardzo długa lista znajomych,
- przypadkowa lokalizacja,
- wpisy na profilu widoczne publicznie (dla każdego - znajomych lub nieznajomych),
- wpisy na profilu wyłącznie w kontekście politycznym (brak jakiejkolwiek prywaty).

Ciekawe. Właśnie takie cechy często przedstawia się, jako oznaki, że dane konto może być botem lub trollem[^4] [^5]. Nie bez powodu. Przecież i tak niewiele osób wie, czym miałyby się wyróżniać *trolle* na tle innych profili. A przecież cele *trolli*  są na ogół czysto polityczne. Proste.

Idąc dalej, spędziłem trochę czasu analizując kilkanaście profili i doszedłem do dwóch wniosków:

1. Istnieją silne przesłanki by uznać, że większość politycznych komentarzy pod tym wpisem napisały właśnie *trolle*.
2. Bardzo trudno odróżnić *trolla* od niezbyt rozgarniętej osoby zaangażowanej w aferki polityczne - zwłaszcza, że ta druga jest zazwyczaj podpuszczana przez tego pierwszego.

W takim razie, pytanie brzmi: czy komentujący ten wpis to *trolle*?

Niestety, na to nie mogę i nie chcę jednoznacznie odpowiedzieć. Wiele na to wskazuje, jednak moja wiedza z zakresu informatyki śledczej (OSINT) nie pozwala mi przedstawić jednoznacznych dowodów. A nie chcę rzucać bezpodstawnych oskarżeń w stronę osób, które zostały po prostu wmanipulowane w polityczne wojenki.

Oczywiście, można teraz uznać że biję tu pianę o nic, ale tak naprawdę to nie chcę popadać w efekt Krugera-Dunniga i bawić się w detektywa, nie mając ku temu technicznych ani prawnych możliwości. Chcę jednak skłonić swoich czytelników do zastanowienia się nad tą opcją: że może nie wszyscy, którzy są na Facebooku, faktycznie istnieją?

## Wnioski

Po tym wszystkim, można jeszcze zadać ostatnie pytanie: "no dobra, i co z tego?". Otóż:

1. **Przykład tej kampanii reklamowej pokazuje, że algorytm Facebooka całkiem skutecznie zderza ze sobą kompletnie niedopasowane, kontrowersyjne grupy, żeby generować "zaangażowanie"**. Czy ma w tym interes? Oczywiście! Cały model biznesowy Facebooka polega na tym, żeby generować jak najwięcej kliknięć i przyciągać ludzi na jak najdłużej. Dlatego właśnie nie warto angażować się tam w awantury. Człowiek się tylko nakręci, a ktoś inny na tym zarabia.

2. **Mimo wszystko, ta reklama mogła mieć sens.** Z tego co rozumiem, zasięgi strony nieco wzrosły ze względu na zaangażowanie - co wypromowało post na tablicach innych, bardziej "normalnych" osób. Czy zadziałało to w taki sposób, w jaki mogła oczekiwać autorka strony? Raczej nie. Wygląda więc na to, że użeranie się z komentarzami takimi jak pokazane wyżej to coś, co trzeba mieć na uwadze, wykupując reklamy na Facebooku.

3. **Parafrazowany cytat z początku wpisu zdaje się być uzasadniony.** Czy Facebook to teraz AI, starzy ludzie, patusy i boty? Ujmę to tak: można mieć ku temu przesłanki, przy czym te dwie ostatnie grupy dość trudno od siebie odróżnić.

Na koniec, pozwolę sobie na mema. Miłego wieczoru!

![alt text]({{page.obrazki}}mem.png)

## Przypisy

[^1]: Swoją drogą, kompletnie się temu nie dziwię. Fanpage jednego z moich blogów, mimo około setki polubień, w szczytowych momentach notował raptem kilkanaście wyświetleń postów. Dlatego przestałem go prowadzić.
[^2]: Teoria martwego internetu głosi, że w internecie nie ma ludzi, a wszystko co widzimy, jest generowane przez boty. Osobiście uważam, że do tego jeszcze nie doszliśmy, ale wraz z rozwojem AI jesteśmy na dobrej drodze.
[^3]: Dla jasności - nikt spoza Facebooka tak naprawdę nie wie, jak *dokładnie* działa algorytm Facebooka. Mówiąc *dokładnie*, mam na myśli specyfikację techniczną. Dlatego moje uproszczenie jest dobre jak każde inne.
[^4]: Bardzo przystępnym źródłem wiedzy jest strona <https://spotthetroll.org/> - niestety, dostępna wyłącznie w języku angielskim.
[^5]: Dla mniej wtajemniczonych: *troll* to określenie na osobę, która w dyskusji ma na celu jedynie podkręcanie emocji i sprowadzenie całej rozmowy do poziomu bezsensownej awantury. Dawniej *trolle* na ogół byli znudzonymi nastolatkami. Obecnie, często są to osoby opłacane do szerzenia konkretnej narracji w internecie. Dobrym źródłem wiedzy na ten temat jest książka "Trolle Putina", którą napisała finlandzka redaktorka Jessikka Aro.
