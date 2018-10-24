# -*- coding: utf-8 -*-

#=========================================================
# Motor de búsqueda
#
# Autor: Antonio Paya Gonzalez
#
#=========================================================

from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division

from bag_of_words import BagOfWords
import argparse

def coef_dice(bag1,bag2):
    return 2.0*len(bag1.intersection(bag2))/(len(bag1)+len(bag2))

def coef_jaccard(bag1,bag2):
    return len(bag1.intersection(bag2)) / len(bag1.union(bag2))

def coef_cosine(bag1,bag2):
    return len(bag1.intersection(bag2)) / (len(bag1)*len(bag2))

def coef_overlapping(bag1,bag2):
    return len(bag1.intersection(bag2)) / min(len(bag1), len(bag2))


def load_lines(file):
    """Usa un generador para leer un archivo largo de forma lazy
    """
    while True:
        data = file.readline()
        if not data:
            break
        yield data

def process_file(file):
    """Procesa el fichero
    """
    try:
        with open(file) as file_handler:
            texts = []
            for line in load_lines(file_handler):
                texts.append(BagOfWords(line))
            return texts
    except (IOError, OSError):
        print("Error opening / processing file")
        return None

def find_best_text(q,t,coef):
    values = {}
    for text in t:
        values[text] = coef(text, q)
    obj = sorted(values.iteritems(), key=lambda (k, v): (v, k))[-1]
    return obj

def search(query,texts):
    #Dice
    best_text = find_best_text(query,texts,coef_dice)
    print("Dice {}".format(best_text[1]))
    print(str(best_text[0].text))
    #Jaccard
    best_text = find_best_text(query, texts, coef_jaccard)
    print("Jaccard {}".format(best_text[1]))
    print(str(best_text[0].text))
    #Coseno
    best_text = find_best_text(query, texts, coef_cosine)
    print("Coseno {}".format(best_text[1]))
    print(str(best_text[0].text))
    #Coeficiente de solapamiento
    best_text = find_best_text(query, texts, coef_overlapping)
    print("Overlapping {}".format(best_text[1]))
    print(str(best_text[0].text))


def parse_args():
    parser = argparse.ArgumentParser(description='Motor_Busqueda')
    parser.add_argument("texts", help="Texts file")
    parser.add_argument("queries", help="Queries file")
    args = parser.parse_args()
    return args

def main(args):
    texts = process_file(args.texts)
    queries = process_file(args.queries)
    for query in queries:
        print ("===========")
        print ("Query:")
        print ("\t{}".format(unicode(query.text, errors='ignore')))
        print("------------")
        search(query,texts)


if __name__ == '__main__':
    main(parse_args())