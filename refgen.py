#!/usr/bin/env python3

# Author: Nikolay A. Merezhko (norn), 2022
#
# Script for generate references for load packages arhives
# from NPM registry

import json

with open('normalize.json') as fr: strings = fr.read().split('\n')[:-1]

with open('references.txt', 'w') as fw:
  for string in strings:
    data = json.loads(string)
    tail = data['id'].split('/')
    try:
      fw.write(f'https://registry.npmjs.org/{data["id"]}/-/{tail[1]}-{data["latest_version"]}.tgz\n')
    except:
      fw.write(f'https://registry.npmjs.org/{data["id"]}/-/{tail[0]}-{data["latest_version"]}.tgz\n')

