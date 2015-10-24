#!/usr/bin/env python3
import json
import os


"""
This makes the json files human-readable, by 1) formatting them 2) allowing JP characters
"""
if __name__ == '__main__':
    basedir = os.path.abspath(os.path.dirname(__file__))
    files = [f for f in os.listdir(basedir) if f.endswith('.json') and not f.startswith('_')]

    for fn in files:
        with open(os.path.join(basedir, fn)) as inf, open(os.path.join(basedir, '_' + fn), 'w') as outf:
            json.dump(json.load(inf), outf, ensure_ascii=False, indent='\t')
