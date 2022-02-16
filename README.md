# Load popularity NPM packages

## Important!!!

It's sooooooooooo draft now (february, 2022). It's f#$@n fast add-hoc!

## Description

NPM registry is large. But yuo can load most popularity packages from it.

## How to use it???

1. Run `load_index.js`. It load last info about packages to `npm-all.json` file
2. Run `popularity.py`. It load information about packages to `base.json.1` file. You can watch progress if run `whereami.py`.
3. Run `refgen.sh` an pass to him `base.json.1` to generate download links fo all packages.
4. Run `ref_loader.sh` to load archives.
5. Run `json2db.py` with pass `base.json.1` if you want have data base in sqlite3 format.

`popularity.service` is template to make `popularity.py` deamon of linux system.

Use it if you want.
Author: Nikolay A. Merezhko (norn), 2022
