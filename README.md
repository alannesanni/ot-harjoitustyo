# Pong-peli

Pelaajan on laudan avulla tarkoitus estää palloa osumasta ruudun alareunaan. Pisteen saa aina, kun osuu laudalla palloon. Pelaajan on kirjoitettava pelin alussa käyttäjänimi, jonka avulla pidetään kirjaa suurimman tuloksen saaneista pelaajista.

## Dokumentaatio
- [Vaatimusmäärittely](https://github.com/alannesanni/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)
- [Changelog](https://github.com/alannesanni/ot-harjoitustyo/blob/master/dokumentaatio/changelog.md)
- [Työaikakirjanpito](https://github.com/alannesanni/ot-harjoitustyo/blob/master/dokumentaatio/tyoaikakirjanpito.md)
- [Arkkitehtuuri](https://github.com/alannesanni/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)

## Invoke komennot
Pelin voi aloittaa komennolla: 
`poerty run invoke start`

Testit suoritetaan komennolla: 
`poetry run invoke test`

Testikattavuusraportin saa komennolla: 
`poetry run invoke coverage-report`

Pylint-tarkistuksen voi suorittaa komennolla:
`poetry run invoke lint`
