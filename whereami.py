#!/usr/bin/env python3

import sys
import json
import time
import argparse

try:
    parser = argparse.ArgumentParser(prog='whereami',
        description='script to show information about grab npm-package popularity')
    parser.add_argument('-b', '--base', default='./npm-all.json',
        help='path to base file (default ./npm-all.json)')
    parser.add_argument('-l', '--last', default='./.last_package',
        help='path to last package log file (default ./.last_package)')
    parser.add_argument('-t', '--timeout', default=5, type=int,
        help='timeout to upade data (default 5 sec)')
    
    properties = parser.parse_args(sys.argv[1:])
    BASE = properties.base
    LAST = properties.last
    TIMEOUT = properties.timeout
    
    with open(BASE) as frb: data = json.loads(frb.read())
    
    index = -1
    while True:
        with open(LAST) as frl: last = frl.read()
        for note in data['rows']:
            if note['id'] == last:
                if index == data['rows'].index(note) == index:
                    continue
                else:
                    index = data['rows'].index(note)
                    print('Precessed {0} packages from {1}. Current: {2}'
                        .format(index, data['total_rows'], last))
                    time.sleep(TIMEOUT)
except KeyboardInterrupt:
    print('Exit from whereami')
