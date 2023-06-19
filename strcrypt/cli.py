import typer
from typing import Annotated, Optional
import sys
from strcrypt.algorithms import HashingAlgorithms, EncodingAlgorithms, DecodingAlgorithms
from strcrypt.service import encode_str, decode_str, hash_str

app = typer.Typer()

@app.command("hash")
def hash_func(algo: Annotated[HashingAlgorithms, typer.Argument(...)],s: Annotated[Optional[str], typer.Argument(...)] = None) -> None:
    # https://github.com/tiangolo/typer/issues/345
    if s is None:
        s = sys.stdin.read().strip()
    hashed = hash_str(algo, s)
    print(hashed)

@app.command()
def encode(algo: Annotated[EncodingAlgorithms, typer.Argument(...)],s: Annotated[Optional[str], typer.Argument(...)] = None) -> None:
    # https://github.com/tiangolo/typer/issues/345
    if s is None:
        s = sys.stdin.read().strip()
    encoded = encode_str(algo, s)
    print(encoded)

@app.command()
def decode(algo: Annotated[DecodingAlgorithms, typer.Argument(...)],s: Annotated[Optional[str], typer.Argument(...)] = None) -> None:
    # https://github.com/tiangolo/typer/issues/345
    if s is None:
        s = sys.stdin.read().strip()
    decoded = decode_str(algo, s)
    print(decoded)


def main():
    app()

if __name__ == "__main__":
    main()
