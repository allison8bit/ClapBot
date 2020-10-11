import clap_converter


def test_clap():
    test_string = "the quick red fox jumps over the lazy dog"
    expected = ":clap: THE :clap: QUICK :clap: RED :clap: FOX :clap: JUMPS :clap: OVER :clap: THE :clap: LAZY :clap: DOG :clap:"

    assert clap_converter.clapify(test_string) == expected
