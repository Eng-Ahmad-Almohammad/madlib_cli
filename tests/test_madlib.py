
from madlib_cli.madlib import *



def test_read_template():
    actual = read_template()
    expected = 'h'
    assert len(actual)>=len(expected)


def test_parse():
    actual = parse('Hello world {Ahmad}')
    expected = 'Hello world {0}'
    assert actual==expected



