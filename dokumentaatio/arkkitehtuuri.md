# Arkkitehtuurikuvaus
## Kansioiden rakenne
**ui** : sisältää käyttöliittymään liittyvän koodin

**entities** : sisältää objekteista vastaavan koodin ja pong-luokan, joka vastaa pelilogiikasta ja pelinäkymän käyttöliittymästä

**repositories** : sisätää tiedon tallennukseen liittyvän koodin

## Käyttöliittymä
Käyttöliittymän eri näkymät:
* Aloitus
* Asetukset
* Pelaus
* Lopetus
* Tulostaulu
Jokainen näistä on toteutettu omana luokkanaan. Pelausnäytön käyttöliittymää en saanut erotettua pelilogiikasta, joten siitä vastaava Pong-luokka sijaitsee entities kansiossa. Muut käyttöliittymän luokat sijaitsevat ui-kansiossa.
Index.py tiedostossa sijaitseva main-funktio vastaa siitä, mikä päänäkymistä (aloitus, pelaus, lopetus) näkyy milloinkin. Asetukset näkymään pääsee aloitusnäkymästä vastaavasta luokasta ja tulostaulu näkymään pääsee lopetusnäkymästä vastaavasta luokasta.


### Pelin eri näkymien kulku / main-funktio sekvenssikaaviona:

```mermaid
sequenceDiagram
  participant main
  participant start
  participant settings_screen
  participant pong
  participant gameover
  participant scoreboard
  
  main ->>start: Start(screen, settings)
  start -->>main:  
  main ->>pong: Pong(screen, settings)
  pong -->>main: 
  main ->>gameover: GameOver(pong, screen, database)
  
  main ->> start: start.loop()
  start -->>settings_screen: SettingsScreen(screen, settings).loop(), (käyttäjä painaa hiirellä settings nappia)
  settings_screen -->> start: (käyttäjä painaa enter)
  start -->>main: (käyttäjä painaa enter) 
  main ->>pong: pong.loop()
  pong -->>main: (peli hävitään)
  main ->>gameover: gameover.loop()
  gameover -->>scoreboard: Scoreboard(screen, database).loop(), (käyttäjä painaa välilyöntiä)
  scoreboard -->> gameover: (käyttäjä painaa enter)
  gameover -->>main: (käyttäjä painaa enter)
  
```
Kaavio kuvaa main-funktion eri näkymiä vaihtelevaa silmukkaa. Kaaviossa esitetty silmukka alkaa viimeisen kohdan jälkeen alusta ja jatkuu, kunnes käyttäjä sulkee ohjelman.  


### Pong pelilogiikan luokkakaavio :

```mermaid
classDiagram
    Pong -- Paddle
    Settings --|> Pong
    Pong -- Ball
    Pong -- Score
    Ball <|-- Collisions
    Paddle <|-- Collisions


```

## Tulosten tallennus
Kansio repositories luokka ScoreDatabase vastaa tulosten tallentamisesta. ScoreDatabase-luokan funktio *add_socre* tallentaa tietoa SQLite-tietokantaan, jonka tiedostonimi on highscores.db.
Tietokannassa on yksi taulu, joka sisältää sarakkeet käyttääjänimelle ja saadulle tulokselle.
ScoreDatabase-luokassa on funktio *get_top_5*, joka palauttaa listana viisi parasta tulosta järjestyksessä parhaasta huonoimpaan. Tätä funktiota käytetään tulostaulun käyttöliittymästä vastaavassa ScoreBoard-luokassa.

Pääkansiossa on empty_database.py tiedosto, jonka ajamalla tietokanta voidaan tyhjentää.

#### Tulosten tallennus ja haku sekvenssikaaviona
Kun peli on aloitusnäkymässä, etenee tietojen tallennus seuraavasti:
```mermaid
sequenceDiagram
  actor User
  participant näkymä
  participant settings
  participant scoredatabase
  participant scoreboard
  
  User ->> settings: "kirjoita käyttäjänimi"
  settings -->> User:  
  User ->> näkymä: "paina enter"
  näkymä ->> scoredatabase: ScoreDatabase(get_database_connection()).add_score(settings.username, pong.score.points)
  scoredatabase -->> näkymä:  
  näkymä ->> scoreboard: ScoreBoard(screen, get_database_connection()).loop()
  scoreboard ->> scoredatabase: get_top_5()
  scoredatabase -->> scoreboard: lista viidestä parhaasta tuloksesta ja käyttäjänimestä
  scoreboard ->> scoreboard: draw_screen()
```
Kaaviossa havainnoidaan vain tietojen tallennkusen kulkua, joten siinä ei oteta kantaa siihen millä päänäkymällä ollaan milläkin hetkellä.

