import click
from yaff.rules import Rule

@click.command()
def main():
    r = Rule(action='accept')
    print(f'Command run {r}')

if __name__ == '__main__':
    main()