# WalterWordlistNL
A Dutch password-list generator

# Voorbeelen
![a](https://user-images.githubusercontent.com/33218378/157703090-36bc9515-0e41-495c-8bbf-9fc6dcf9969f.png)

Je kunt ook zelf woorden toevoegen aan de generator:
```py
--prewords aardappel,banaan,druiven  # Voegt prefix woorden toe
--midwords 123,01,1337  # Voor die dingen die mensen achter hun wachtwoord plakken
--endwords ***,%,@  # Sommige mensen doen symbolen achter hun wachtwoord
--sort  # Gebruik deze als je een gesorteerde output wilt
--test  # Laat je de wachtwoorden notatie zien en je kunt checken of alles goed is
```
Voorbeeld:
We hebben iemand gevonden met de naam: "Henk" en zijn favoriete fruit is een "Banaan"

En hij vindt de BMW model nummer 4403i interresant.
```py
python start.py --prewords Henk,Banaan,BMW --midwords 4403,4403i --test
>> Bestand wwNL-278k.txt opgeslagen
```
![image](https://user-images.githubusercontent.com/33218378/157706439-5fc814b9-1c47-42a9-8bc1-122a7c40487e.png)


# Setup
> Installeer Python 3 van officiele website

> pip3 install -r requirements.txt

> python start.py --help

yes
