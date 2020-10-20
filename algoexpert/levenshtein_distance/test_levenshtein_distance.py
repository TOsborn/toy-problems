from levenshtein_distance import levenshteinDistance, levenshteinDistance2
import pytest

def test_levenshteinDistance_1():
    assert levenshteinDistance('abc', 'yabd') == 2

def test_levenshteinDistance_one_empty():
    assert levenshteinDistance('', 'asdf') == 4

def test_levenshteinDistance_both_empty():
    assert levenshteinDistance('', '') == 0

def test_levenshteinDistance_all_same():
    assert levenshteinDistance("aaaa", "bbbb") == 4

def test_levenshteinDistance_arbitrary():
    str1 = 'asdfnnginqwnasdgb'
    str2 = 'bnasietnasdgvndfasnasd'

    assert levenshteinDistance(str1, str2) == levenshteinDistance2(str1, str2)