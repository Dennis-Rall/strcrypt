from typer.testing import CliRunner
from strcrypt.cli import app

def test_hash():
    result = CliRunner().invoke(app, ["hash", "sha1", "abc"])
    assert result.exit_code == 0
    assert result.stdout.strip() == "abc"

def test_hash_from_stdin():
    result = CliRunner().invoke(app, ["hash", "sha1"], input="abc")
    assert result.exit_code == 0
    assert result.stdout.strip() == "abc"
