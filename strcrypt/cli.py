import typer
from typing import Annotated, Optional
import sys
from strcrypt.algorithms import HashAlgorithms, EncodingAlgorithms, DecodingAlgorithms

app = typer.Typer()

@app.command("hash")
def hash_func(algortihms: Annotated[HashAlgorithms, typer.Argument(...)],s: Annotated[Optional[str], typer.Argument(...)] = None) -> None:
    # https://github.com/tiangolo/typer/issues/345
    if s is None:
        s = sys.stdin.read().strip()
    print(s)

@app.command()
def encode(algortihms: Annotated[EncodingAlgorithms, typer.Argument(...)],s: Annotated[Optional[str], typer.Argument(...)] = None) -> None:
    # https://github.com/tiangolo/typer/issues/345
    if s is None:
        s = sys.stdin.read().strip()
    print(s)

@app.command()
def decode(algortihms: Annotated[DecodingAlgorithms, typer.Argument(...)],s: Annotated[Optional[str], typer.Argument(...)] = None) -> None:
    # https://github.com/tiangolo/typer/issues/345
    if s is None:
        s = sys.stdin.read().strip()
    print(s)


def main():
    app()

if __name__ == "__main__":
    main()
