# Pong-pelin käyttöohje
Lataa koneellesi pelin viimeisin releasen lähdekoodi, johon löydät linkin README:sta.

## Pelin avaaminen
Asenna ensin riippuvuudet komennolla:
`poerty install`

Käynnistä peli komennolla:
`poetry run invoke start`

Tietokannan voi tyhjentää komennolla:
`poetry run invoke empty-database`

## Pelin pelaaminen
**Käynnistäessäsi pelin pääset pelin etusivulle.**
**Etusivulla voit kirjoittaa käyttäjänimesi, jonka perusteella tuloksesi tallennetaan. 
Klikkaamalla hiirellä *settings* nappia pääset muuttamaan pelin asetuksia.**

*Näppäinkomennot:*

*esc*: sulkee pelin

*enter*: aloittaa pelin



**Asetukset sivulla voit muuttaa pallon ja laudan värejä klikkaamalla hiirellä haluamaasi väriä.
Myös laudan ohjaustapaa voi muuttaa samalla tavalla.**

*Näppäinkomennot:*

*enter*: ohjaa sinut takaisin etusivulle



**Pelinäkymässä voit liikuttaa lautaa asetuksissa valitsemallasi tavalla. 
Saat pisteen aina kun osut laudalla palloon.**

**Jos pallo pääsee tippumaan alareunaan, häviät pelin ja siirrty lopetusnäytölle.
Lopetusnäytöllä sinulle näytetään saamasi pisteet.**

*Näppäinkomennot:*

*enter* : ohjaa sinut takaisin aloitusnäytölle

*esc* : sulkee pelin 

*space* : ohjaa sinut tulostaulunäytölle



**Tulostaulunäytöllä näet 5 parasta suoritusta pelissä.**

*Näppäinkomennot:*

*enter* : ohjaa sinut takaisin lopetusnäytölle
*esc* : sulkee pelin



**Voit sulkea pelin missä vain vaiheessa painamalla hiirellä oikeassa yläkulmassa olevaa rastia.**

