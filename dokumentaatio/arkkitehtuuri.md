
#### Pong sovelluslogiikan luokkakaavio :

```mermaid
classDiagram
    Pong -- Paddle
    Pong -- Ball
    Pong -- Score
    Ball <|-- Collisions
    Paddle <|-- Collisions


```

#### Pelin eri näkymien kulku / main-funktio sekvenssikaaviona:

```mermaid
sequenceDiagram
  participant main
  participant start
  participant pong
  participant gameover
  participant scoreboard
  
  main ->>start: Start(screen)
  start -->>main:  
  main ->>pong: Pong(screen)
  pong -->>main: 
  main ->>gameover: GameOver(pong, screen, database)
  
  main ->> start: start.loop()
  start -->>main: (käyttäjä painaa enter) 
  main ->>pong: pong.loop()
  pong -->>main: (peli hävitään)
  main ->>gameover: gameover.loop()
  gameover ->>scoreboard: Scoreboard(screen, database).loop(), (käyttäjä painaa välilyöntiä)
  scoreboard -->> gameover: (käyttäjä painaa enter)
  gameover -->>main: (käyttäjä painaa enter)
  
```
Kaavio kuvaa main-funktion eri näkymiä vaihtelevaa silmukkaa. Kaaviossa esitetty silmukka alkaa viimeisen kohdan jälkeen alusta ja jatkuu, kunnes käyttäjä sulkee ohjelman.  
