import numpy as np

class Util:
    @staticmethod
    # Maakt wat variaties op de wachtwoorden
    def getCapitalPermutations(words):
        return np.concatenate([(word, word.upper(), word.lower(), word.capitalize())
                               for word in words])

class Wordlist:
    def __init__(self,
                 preWords:tuple=None,
                 midWords:tuple=None,
                 endWords:tuple=None,
                 sorting:bool=False,
                 filename:str="wwNL",
                 ):
        # De officiele oplossing voor lijst-type parameter mutability oplossen is 2 lines
        # maar ik vond een manier met 1-line yesss
        preWords = {None: []}.get(preWords, preWords)
        midWords = {None: []}.get(midWords, midWords)
        endWords = {None: []}.get(endWords, endWords)
        self.filename = filename

        # Start woorden (Het grootste stuk van een wachtwoord)
        self._preWords = set(Util.getCapitalPermutations((
            *preWords,
            # Basis dingen
            "welkom",
            "hallo",
            "wachtwoord",
            "beveiliging",
            "geheim",
            "veilig",
            "1234hoedjevanpapier",
            "1234HoedjeVanPapier",
            "vakantie",
            "weekend",
            # Seizoenen
            "herfst",
            "winter",
            "lente",
            "zomer",
            # Maanden
            "januari",
            "februari",
            "maart",
            "april",
            "mei",
            "juni",
            "juli",
            "augustus",
            "september",
            "oktober",
            "november",
            "december",
            # Dag-namen
            "MaanDag",
            "DinsDag",
            "WoensDag",
            "DonderDag",
            "VrijDag",
            "ZaterDag",
            "ZonDag",
            # Voetbal clubs
            "Feyenoord",
            "SC Heerenveen",
            "SCHeerenveen",
            "Ajax",
            "PSV",
            "FC Twente",
            "FCTwente",
            "Vitesse",
            "SC Cambuur",
            "SCCambuur",
            # Bekendheden
            "WillemAlexander",
            "Willem-Alexander",
            "Willem",
            "Alexander",
            "Maxima",
            "Rutte",
            "Geert",
            "GeertWilders",
            "Wilders",
            "Beatrix",
            # Artiesten / Performers
            "Vengaboys",
            "ArminVanBuuren",
            "MartinGarrix",
            "Martin",
            "Garrix",
            "MaxVerstappen",
            "Verstappen",
        )))
        # Achtervoegsel (Dingen zoals 01 of 123 om net te voldoen aan eisen zoals 8-tekens)
        self._midWords = {
            *midWords,
            # Blank, anders kunnen losse preWords niet gebruikt worden
            ""
            # Makkelijk om te typen
            "123",
            # Dit getal staat voor iets ongepasts - https://en.wikipedia.org/wiki/69
            "69",
            # Weed getal - https://www.urbandictionary.com/define.php?term=420
            "420",
            # Elite getal - https://www.urbandictionary.com/define.php?term=1337
            "1337",
            # Afkomstig van een Dragon-ball Z meme - https://en.wikipedia.org/wiki/It%27s_Over_9000!
            "9000",
            "9001",
            # 0 - 52 want er zijn 52 weken in een jaar
            *map(lambda x: f"{x}".rjust(2, "0"), range(0, 53)),
            *map(lambda x: f"{x}", range(0, 53)),
            # Wachtwoorden met datums staan altijd ergens voor
            # En meestal is het verjaardagen, geboorte datums enz,
            # Dus alles binnen 100 jaar van vandaag is goed
            *map(lambda x: f"{x}", range(1900, 2101)),
        }
        # Extra's (Sommige mensen denken dat 1 symbool toevoegen het wachtwoord goed maakt)
        self._endWords = {
            *endWords,
            # Blank
            "",
            # Meest veelvoorkomende symboolen in wachtwoorden
            "!",
            "@",
            "#",
            # Dit gebeurt als je 123 indrukt met shift
            "!@#",
        }
        # set() wordt hier niet gebruikt voor deduplicatie maar om het een __len__ te geven
        # ⚠ Door set() is de volgorde elke keer willekeurig
        self.wordlist = set((
            # Dit is 2x sneller dan string formatting
            pre + mid + end
            for pre in self._preWords
            for mid in self._midWords
            for end in self._endWords
        ))
        if sorting:
            self.wordlist = sorted(self.wordlist)

    def writeFile(self):
        fn = f"{self.filename}-{int(len(self.wordlist)/1000)}k.txt"
        with open(fn, "w") as f:
            f.write("\n".join(self.wordlist))
        print(f"Bestand {fn} opgeslagen")

    @property
    # Laat wachtwoorden in notatie zien
    def passwordsNotation(self):
        return (f"[{'/'.join(sorted(self._preWords))}]\n"
                f"[{'/'.join(sorted(self._midWords))}]\n"
                f"[{'/'.join(sorted(self._endWords))}]")
