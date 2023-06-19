from typer.testing import CliRunner
from strcrypt.cli import app
import pytest


@pytest.mark.parametrize("algo,s,hashed", [("blake2b", "strcrypt", "64efba29a2767205792546d2ebc4967ed62b5c75f36d1072a35784426c098535d50a9ad63de4df1f4ff0b8a6a653b1f666a4859258fbcc9c0eb519ecb55d2349"),
                                           ("blake2s", "strcrypt", "fe425df4949c761e1136169cc9f1fbac2f3dcefea185c6a8ca9e5a5af0caa748"),
                                           ("md5", "strcrypt", "0dff5df377d7fa45c7bea35d6f960f34"),
                                           ("sha1", "strcrypt", "3e54945fb6a458ab661f0417647f0508aeaaa271"),
                                           ("sha224", "strcrypt", "3e87fbba6ff763986ad2683b59202ba38467edb2c2eaebdde539fcc5"),
                                           ("sha256", "strcrypt", "f3783b7851d7f107922fed631fe2a2c7c680203484425baf250f1837fb42d5dd"),
                                           ("sha384", "strcrypt", "1b47afc1ff9688631bc19218f3254619253bac61869f8d6527ed6c782213a139195bc16eaccd316cf9ab196c5e1ab899"),
                                           ("sha512", "strcrypt", "1be0748f8f23cbff052f735b6dbb924f5b6a8e9f7297690b245e253706d4dbce3b33ddca9126d40b0a1b2af200b3f333d738add1719b44e2f6f0a1c425095c55"),
                                           ("sha3_224", "strcrypt", "51c07aa0234599c91880135721311bbc83909d4c15077afb7a2179dd"),
                                           ("sha3_256", "strcrypt", "7f963cd296d195564a2d1aaec8c007d055bb7ac63dd9a6c48f457e9d2f6a4130"),
                                           ("sha3_384", "strcrypt", "8a2d73b60ecfdb03a1cf0a9dbf0899ec8f3b5db3ceead41496651ccd61248967e9a246064ddcd290fb3e23b876bb7050"),
                                           ("sha3_512", "strcrypt", "a49e13c072ca0e8dfc9f49ef9343dc5563dfc611b2c1f6b870dbd54196824096be0f911eb6a04c3a344f585c7ce98342c45ce9ec364780deb9dade3fcf3d019f"),
                                           ])
def test_hash(algo: str, s: str, hashed: str):
    result = CliRunner().invoke(app, ["hash", algo, s])
    assert result.exit_code == 0
    assert result.stdout.strip() == hashed


@pytest.mark.parametrize("algo,s,hashed", [("blake2b", "strcrypt", "64efba29a2767205792546d2ebc4967ed62b5c75f36d1072a35784426c098535d50a9ad63de4df1f4ff0b8a6a653b1f666a4859258fbcc9c0eb519ecb55d2349"),
                                           ("blake2s", "strcrypt", "fe425df4949c761e1136169cc9f1fbac2f3dcefea185c6a8ca9e5a5af0caa748"),
                                           ("md5", "strcrypt", "0dff5df377d7fa45c7bea35d6f960f34"),
                                           ("sha1", "strcrypt", "3e54945fb6a458ab661f0417647f0508aeaaa271"),
                                           ("sha224", "strcrypt", "3e87fbba6ff763986ad2683b59202ba38467edb2c2eaebdde539fcc5"),
                                           ("sha256", "strcrypt", "f3783b7851d7f107922fed631fe2a2c7c680203484425baf250f1837fb42d5dd"),
                                           ("sha384", "strcrypt", "1b47afc1ff9688631bc19218f3254619253bac61869f8d6527ed6c782213a139195bc16eaccd316cf9ab196c5e1ab899"),
                                           ("sha512", "strcrypt", "1be0748f8f23cbff052f735b6dbb924f5b6a8e9f7297690b245e253706d4dbce3b33ddca9126d40b0a1b2af200b3f333d738add1719b44e2f6f0a1c425095c55"),
                                           ("sha3_224", "strcrypt", "51c07aa0234599c91880135721311bbc83909d4c15077afb7a2179dd"),
                                           ("sha3_256", "strcrypt", "7f963cd296d195564a2d1aaec8c007d055bb7ac63dd9a6c48f457e9d2f6a4130"),
                                           ("sha3_384", "strcrypt", "8a2d73b60ecfdb03a1cf0a9dbf0899ec8f3b5db3ceead41496651ccd61248967e9a246064ddcd290fb3e23b876bb7050"),
                                           ("sha3_512", "strcrypt", "a49e13c072ca0e8dfc9f49ef9343dc5563dfc611b2c1f6b870dbd54196824096be0f911eb6a04c3a344f585c7ce98342c45ce9ec364780deb9dade3fcf3d019f"),
                                           ])
def test_hash_from_stdin(algo: str, s: str, hashed: str):
    result = CliRunner().invoke(app, ["hash", algo], input=s)
    assert result.exit_code == 0
    assert result.stdout.strip() == hashed
