# -*- coding: utf-8 -*-

#=========================================================
# Clase: Simhash
#
# Autor: Antonio Paya Gonzalez
#
#=========================================================

from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division

from bag_of_words import BagOfWords
import binascii
import argparse
from heapq import heapify, heappop
from nltk import ngrams

def simhash(line, restrictiveness, ngram=0):
    """Realiza simhash

    :param line: texto
    :param restrictiveness
    :param ngram: numero de ngramas
    :return:
    """
    if(ngram < 0):
        bag = BagOfWords(text=line)
        if len(bag) == 0:
            return None
        hashes = calculate_hashes(bag.values, restrictiveness)
        return hashes
    else:
        bag = ngrams(line.split(), ngram)
        hashes = calculate_hashes([' '.join(x) for x in bag], restrictiveness)
        return hashes


def calculate_hashes(bag, restrictiveness):
    hashes = [binascii.crc32(x.encode("utf-8")) & 0xffffffff for x in bag]
    heapify(hashes)  # ordenar de pequeño a mayor
    simh = 0
    if(len(hashes) <= restrictiveness):
        for i in range(len(hashes)):  # nos quedamos con los restrictiveness mas pequeños
            simh ^= heappop(hashes)  # hacer xor de todos con todos
        return simh
    else:
        for i in range (restrictiveness): # nos quedamos con los restrictiveness mas pequeños
            simh ^= heappop(hashes) # hacer xor de todos con todos
        return simh


def parse_args():
    parser = argparse.ArgumentParser(description='SimHash')
    parser.add_argument("texts", help="Texts file")
    parser.add_argument(
        "-r",
        "--restrictiveness",
        type=int,
        default=10,
        help="Use %(default)s hashes")
    parser.add_argument(
        "-l",
        "--lines",
        type=int,
        default=10000,
        help="Lines to parse from file")
    args = parser.parse_args()
    return args

