import click
from app import Wordlist

@click.command()
@click.option('--prewords', "-p", "-1", default="", help="Prefix, comma-gesepereerde lijst van woorden zoals (geheim, wachtwoord, aardappel) etc", type=str)
@click.option("--midwords", "-m", "-2", default="", help="Midfix, comma-gesepereerde lijst van dingen zoals (123, 01, 9001)", type=str)
@click.option("--endwords", "-e", "-3", default="", help="Suffix, comma-gesepereerde lijst van dingen zoals (!, @, !@#)", type=str)
@click.option("--sorted", "-s", default=False, help="Of je de woordenlijst gesorteerd wilt hebben", is_flag=True)
@click.option("--output", "-o", default="wwNL", help="Output filename. formaat: {output}-??k.txt")
@click.option("--test", "--dry-run", "-t", default=False, help="Laat je zien wat voor wachtwoorden gegenereerd zouden worden", is_flag=True)

def cli(prewords, midwords, endwords, sorted, output, test):
    wordlist = Wordlist(preWords=tuple(prewords.split(",")),
                        midWords=tuple(midwords.split(",")),
                        endWords=tuple(endwords.split(",")),
                        sorting=sorted,
                        filename=output)
    if test:
        print(wordlist.passwordsNotation)
        print(f"Aantal wachtwoorden: {len(wordlist.wordlist)}")
    else:
        wordlist.writeFile()

if __name__ == '__main__':
    cli()