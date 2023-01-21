from app import extract_sentiment
from app import text_contain_word
from app import hello
import pytest
from app import quickSort
from timeit import timeit
import random


def test_hello():
    got = hello("Aleksandra")
    want = "Hello Aleksandra"

    assert got == want

testdata1 = ["I think today will be a great day"]

@pytest.mark.parametrize('sample', testdata1)
def test_extract_sentiment(sample):

    sentiment = extract_sentiment(sample)

    assert sentiment > 0

testdata2 = [
    ('There is a duck in this text', 'duck', True),
    ('There is nothing here', 'duck', False)
    ]

@pytest.mark.parametrize('sample, word, expected_output', testdata2)
def test_text_contain_word(sample, word, expected_output):

    assert text_contain_word(word, sample) == expected_output
 
listpos = [i for i in range(500)]
listlos = random.sample(range(0, 500), 500)
listrow = 500*[1]

def test_quicksort():  
    t1_quick = timeit("quickSort(listpos)", number=1000, globals=globals())/1000
    t2_quick = timeit("quickSort(listlos)", number=1000, globals=globals())/1000
    t3_quick = timeit("quickSort(listrow)", number=1000, globals=globals())/1000
    return t1_quick, t2_quick, t3_quick

testdata6=[([],[])]
@pytest.mark.parametrize('sample, sorted_sample', testdata6)
def test_empty(sample,sorted_sample):
    assert quickSort(sample)==sorted_sample

testdata7=[([2],[2])]
@pytest.mark.parametrize('sample, sorted_sample', testdata7)
def test_oneelement(sample,sorted_sample):
    assert quickSort(sample)==sorted_sample

testdata8=[([2,-7],[-7,2])]
@pytest.mark.parametrize('sample, sorted_sample', testdata8)
def test_twoelement(sample,sorted_sample):
    assert quickSort(sample)==sorted_sample

a=random.sample(range(-1000, 1000), 2000)
testdata9=[(a,sorted(a))]

@pytest.mark.parametrize('sample, sorted_sample', testdata9)
def test_moreelement(sample,sorted_sample):
    assert quickSort(sample)==sorted_sample


b=random.sample(range(-10000, 10000), 20000)
testdata9=[(b,sorted(b))]

@pytest.mark.parametrize('sample, sorted_sample', testdata9)
def test_final(sample,sorted_sample):
    assert quickSort(sample)==sorted_sample