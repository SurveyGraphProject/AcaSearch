from acasearch import *

def test_search():
    res = arxiv_search('attention is all you need', n=1)
    assert res is not None