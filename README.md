# Pong-peli

Pelaajan on laudan avulla tarkoitus estää palloa osumasta ruudun alareunaan. Lauta liikkuu nuolinäppäinten avulla. Pisteen saa aina, kun osuu laudalla palloon. Pelaajan on kirjoitettava pelin alussa käyttäjänimi, jonka avulla pidetään kirjaa suurimman tuloksen saaneista pelaajista.

## Release
- [Viikko 7](https://github.com/alannesanni/ot-harjoitustyo/releases/tag/viikko7)
- [Viikko 6](https://github.com/alannesanni/ot-harjoitustyo/releases/tag/viikko6)
- [Viikko 5](https://github.com/alannesanni/ot-harjoitustyo/releases/tag/viikko5)

## Dokumentaatio
- [Käyttöohje](https://github.com/alannesanni/ot-harjoitustyo/blob/master/dokumentaatio/kayttoohje.md)
- [Vaatimusmäärittely](https://github.com/alannesanni/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)
- [Changelog](https://github.com/alannesanni/ot-harjoitustyo/blob/master/dokumentaatio/changelog.md)
- [Työaikakirjanpito](https://github.com/alannesanni/ot-harjoitustyo/blob/master/dokumentaatio/tyoaikakirjanpito.md)
- [Arkkitehtuuri](https://github.com/alannesanni/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)
- [Testausdokumentti](https://github.com/alannesanni/ot-harjoitustyo/blob/master/dokumentaatio/testausdokumentti.md)

## Pelin pelaaminen
Asenna ensin riippuvuudet komennolla:
`poerty install`

Käynnistä peli komennolla:
`poetry run invoke start`

Tietokannan voi tyhjentää komennolla:
`poetry run invoke empty-database`

## Invoke komennot
Pelin voi käynnistää komennolla: 
`poerty run invoke start`

Testit suoritetaan komennolla: 
`poetry run invoke test`

Testikattavuusraportin saa komennolla: 
`poetry run invoke coverage-report`

Pylint-tarkistuksen voi suorittaa komennolla:
`poetry run invoke lint`

Tietokannan voi tyhjentää komennolla:
`poetry run invoke empty-database`
