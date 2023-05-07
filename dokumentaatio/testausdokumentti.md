# Testausdokumentti
Ohjelmaa on testattu automatisoiduilla unittesteillä ja manuaalisella testauksella.

## Automatisoidut unittestit


### Testikattavuus
Testikattavuudesta on jätetty pois käyttöliittymää käsittelevä koodi. Pelin testauksen haaraumakattavuus on 70%. 

![image](https://user-images.githubusercontent.com/128046458/236689280-803dfad0-967c-48b9-a7a5-6103988799b1.png)
*Pong.py* tiedosto sisältää sovelluslogiikkaa ja pelausnäkymän käyttöliittymää hallinnoivan koodin, joten sitä ei ole testattu automatisoiduilla testeillä. 

Automaattiset testit löytyvät kansiosta *src/tests.*

## Manuaalinen testaus

* Peli on ladattu githubista ja sitä on testattu manuaalisesti Linux-ympäristössä.

* Pelin kaikkia eri asetuksia ja vaikeustasoja on testattu. Myös kaikki käyttöohjeesta löytyvät näppäinkomennot on testattu.
