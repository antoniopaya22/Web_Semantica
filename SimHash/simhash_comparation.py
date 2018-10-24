# -*- encoding:utf-8 -*-

# Verisión con bags-of-words

from __future__ import print_function
from __future__ import unicode_literals

import gzip
import json
from simhash import simhash, parse_args

def main(args):
    index = {}
    cont = args.lines
    with gzip.open(args.texts) as f:
        for line in f:
            cont = cont -1
            if (cont == 0): break
            line = line.decode("utf-8")
            line = line.strip()
            data = json.loads(line)
            if data["_source"]["lang"] != "en":
                continue
            line = data["_source"]["text"]
            # print(b"DEBUG line = {}".format(line.encode("utf-8")))
            hash = simhash(line, args.restrictiveness)
            if hash is None:
                continue
            try:
                index[hash].append(line)
            except:
                index[hash] = [line]
    for _, lines in index.iteritems():
        if len(lines) > 1:
            print("\n\n\n")
            print("FOUND:")
            for line in lines:
                print(">" * 80)
                print(line.encode("utf-8"))
                print("<" * 80)


if __name__ == '__main__':
    exit(main(parse_args()))