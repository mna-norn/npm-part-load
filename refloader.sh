#!/usr/bin/bash

# Author: Nikolay A. Merezhko (norn), 2022
#
# Shell script fo load files with wget in parallel mode
# $1 - file with references

cat $1 | parallel --gnu "wget {}"
