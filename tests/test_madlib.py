
from madlib_cli.madlib import *



def test_read_template():
    actual = read_template()
    expected = 'h'
    assert len(actual)>=len(expected)


def test_parse():
    actual = parse('Hello world {Ahmad}')
    expected = 'Hello world {0}'
    assert actual==expected


def test_merge():
    """
    For testing you should replace this list with the list on top of code answers = ['Ahmad','Hadi'] 
    """
    string = 'Hello world {0} and {1}'
    actual = merge(string)
    expected = 'Hello world Ahmad and Hadi'
    assert actual==expected

