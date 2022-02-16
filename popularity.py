#!/usr/bin/env python3

# Author: Nikolay A. Merezhkon (norn), 2021
#
# Module for loading info about NPM-packages
# with dependence of them popularity

import json
import requests

REGISTRY_URL = 'https://registry.npmjs.org/'
POPULARITY_URL ='https://api.npmjs.org/downloads/point/last-year/'
MIN_POPULARITY_LEVEL = 1000
START_ID = '@arisan/hubble'
SKIP_IDS = bool(START_ID)
TIMEOUT = 60
LAST_PACKAGE_LOG = './.last_package'
BASE_NAME = 'base.json'

print('Load known packages...')
with open('npm-all.json') as fr: data = json.loads(fr.read())
print(f'Total {data["total_rows"]} packages')
print(f'Minimum donloads: {MIN_POPULARITY_LEVEL}')

try:
    with open(LAST_PACKAGE_LOG) as fr:
        START_ID = fr.read()
        if not START_ID[-1].isalpha(): START_ID = START_ID[:-1] 
    with open(BASE_NAME+'.1', 'a') as fa:
        with open(BASE_NAME) as fr:
            last_part = fr.read()
            fa.write(last_part)
    print(f'Resume from {START_ID}')
except FileNotFoundError:
    START_ID = ''
SKIP_IDS = bool(START_ID)

with requests.Session() as popularyty_session:
    with requests.Session() as registry_session:
        db = []
        with open(BASE_NAME, 'w') as fw:
            for row in data['rows']:
                package_id = row['id']

                if SKIP_IDS:
                    if package_id == START_ID: SKIP_IDS = False
                    print(f'Skip {package_id} because loaded')
                    continue

                with open(LAST_PACKAGE_LOG, 'w') as flp: flp.write(package_id)

                try:
                    try:
                      package_popularity = int(json.loads(popularyty_session.get(POPULARITY_URL+package_id, timeout=TIMEOUT).text)['downloads'])
                    except KeyError:
                      print(f'Skip {package_id} because no popularity found')
                      continue
                    if package_popularity < MIN_POPULARITY_LEVEL:
                        print(f'Skip {package_id} by low popularity')
                        continue
                    package_data = json.loads(registry_session.get(REGISTRY_URL+package_id, timeout=TIMEOUT).text)
        
                    try:
                        latest_version = package_data['dist-tags']['latest']
                    except KeyError:
                        print(f'Don\'t know, how it may be, but no information about version. Skip {package_id}')
                        continue
        
                    try:
                        package_description = package_data['versions'][latest_version]['description']
                    except KeyError:
                        print('Description not found. Set to \'null\'')
                        package_description = 'null'
                except requests.exceptions.ReadTimeout:
                    print(f'Tooo long... Package {package_id} skiped by timeout')
                    continue
        
                res = json.dumps(json.loads('{' + f'"id": "{package_id}", "latest_version": "{latest_version}", "description": "{package_description}",  "downloads": {package_popularity}' + '}'))
                print(res)
                fw.write(f'{res}\n')

