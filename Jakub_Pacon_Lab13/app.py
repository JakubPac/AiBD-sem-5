from textblob import TextBlob
from typing import Tuple, List

def hello(name):
    output = f'Hello {name}'
    return output


def extract_sentiment(text):
    text = TextBlob(text)

    return text.sentiment.polarity

def text_contain_word(word: str, text: str):
    return word in text

def quickSort(J: List[float]) -> List [float]:
    if len(J)==0:
        return []
    def quicksort1(tab: List[float], start: int, stop: int) -> None:

        
        l = start
        m = stop
        pivot = tab[int(((stop-start)/2)+start)]
        while l<m:
            while tab[l] < pivot:
                l=l+1
            while tab[m] > pivot:
                m=m-1
            if l<=m:
                tab[l], tab[m] = tab[m], tab[l]
                l=l+1
                m=m-1
            else:
                break
        if start<m:
            quicksort1(tab, start, m)
        if  l < stop:
            quicksort1(tab, l, stop)
    tab1=J[:]
    start=0
    stop=len(J) - 1
    quicksort1(tab1, start, stop)
    return tab1
 