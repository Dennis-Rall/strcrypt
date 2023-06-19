from typer.testing import CliRunner
from strcrypt.cli import app
import pytest


@pytest.mark.parametrize("algo,decoded,s", [
    ("a85", "strcrypt", "F*)G4Ed;VG"),
    ("base16", "strcrypt", "7374726372797074"),
    ("base32", "strcrypt", "ON2HEY3SPFYHI==="),
    ("base32hex", "strcrypt", "EDQ74ORIF5O78==="),
    ("base64", "strcrypt", "c3RyY3J5cHQ="),
    ("base85", "strcrypt", "b98cJa(Qrc"),
    ("hexlify", "strcrypt", "7374726372797074"),
])
def test_decode(algo: str, decoded: str, s: str):
    result = CliRunner().invoke(app, ["decode", algo, s])
    assert result.exit_code == 0
    assert result.stdout.strip() == decoded


@pytest.mark.parametrize("algo,decoded,s", [
    ("a85", "strcrypt", "F*)G4Ed;VG"),
    ("base16", "strcrypt", "7374726372797074"),
    ("base32", "strcrypt", "ON2HEY3SPFYHI==="),
    ("base32hex", "strcrypt", "EDQ74ORIF5O78==="),
    ("base64", "strcrypt", "c3RyY3J5cHQ="),
    ("base85", "strcrypt", "b98cJa(Qrc"),
    ("hexlify", "strcrypt", "7374726372797074"),
])
def test_decode_from_stdin(algo: str, decoded: str, s: str):
    result = CliRunner().invoke(app, ["decode", algo], input=s)
    assert result.exit_code == 0
    assert result.stdout.strip() == decoded
