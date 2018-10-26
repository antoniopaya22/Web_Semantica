# -*- coding: utf-8 -*-

#=========================================================
# Score to csv
#   -> Exporta a un csv los resultados de ejecutar
#      score_simhash_implementation.py con diferentes
#      parametros.
#
# Autor: Antonio Paya Gonzalez
#
#=========================================================

from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division

import csv
import argparse
from score_simhash_implementation import score_implementation

def main(args):
    try:
        python_file = args.file
        if python_file.endswith(".py"):
            python_file = python_file[:-3]
        implementation = __import__(python_file)
        simhash = implementation.simhash
        file = args.csv
    except ImportError:
        print("Unable to import: {}".format(args.file))
        return 1
    except AttributeError:
        print("The Python file must define simhash: {}".format(args.file))
        return 1
    write_csv(simhash,file)

def write_csv(simhash,file):
    with open(file, 'wb') as csvfile:
        writer = csv.writer(csvfile, delimiter=str(';'), quotechar=str('|'), quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['Restrictiveness', 'NGram', 'Score'])
        for r in range(1, 20):
            for ngram in range(1, 10):
                score = score_implementation(simhash, r, ngram)
                writer.writerow([r, ngram, score])

def parse_args():
    parser = argparse.ArgumentParser(description='Export scores to csv')
    parser.add_argument("file", help="Python simhash file")
    parser.add_argument("csv", help="Csv name file (without .csv)")
    args = parser.parse_args()
    return args

if __name__ == '__main__':
    exit(main(parse_args()))