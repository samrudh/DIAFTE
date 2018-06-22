# -*- coding: utf-8 -*-
"""
Author: kirankunapuli
Email: kirankunapuli@dbs.com
Description: Returns similarity score between 2 values.
Date Created: 21-Jun-2018
"""

from difflib import SequenceMatcher
try:
    import distance
except Exception as e:
    print("Can only use similar function")


def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()


def similar_levenshtein(a, b):
    return distance.levenshtein(a, b)


def similar_sorensen(a, b):
    return (1 - distance.sorensen(a, b))


def similar_jaccard(a, b):
    return (1 - distance.jaccard(a, b))


if __name__ == "__main__":
    aa = "Hashim Ahmad"
    bb = "Hashim Ahmed"
    print("Similarity score between", aa, "and", bb, "is:", similar(aa, bb))
    print("Levenshtein Similarity score between", aa,
          "and", bb, "is:", similar_levenshtein(aa, bb))
    print("Sorensen Similarity score between", aa,
          "and", bb, "is:", similar_sorensen(aa, bb))
    print("Jaccard Similarity score between", aa,
          "and", bb, "is:", similar_jaccard(aa, bb))
