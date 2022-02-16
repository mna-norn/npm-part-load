#!/usr/bin/env python3

# Author: Nikolay A. Merezhko (norn), 2022
#
# Script fo convert JSON base to sqlite3 DB

import json
import sqlite3

with open('normalize.json') as fr: src = fr.read().split('\n')[:-1]
data = [json.loads(string) for string in src]

db = sqlite3.connect('npmgt1000.sqlite')
c = db.cursor()
c.execute('''
CREATE TABLE main_info(
  id TEXT PRIMARY KEY,
  latest_version TEXT,
  description TEXT,
  downloads INTEGER)''')
c.execute('CREATE INDEX downloads_inx ON main_info(latest_version)')

for note in data:
  c.execute('INSERT INTO main_info VALUES(?,?,?,?)', list(note.values()))
db.commit()
c.close()
db.close()

