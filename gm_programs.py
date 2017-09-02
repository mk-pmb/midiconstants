#!/usr/bin/python3
# -*- coding: UTF-8, tab-width: 4 -*-
#
#   !!! !!! !!! !!! !!! !!! !!! !!! !!! !!! !!! !!! !!! !!! !!! !!!
#   !! AUTO-GENERATED FILE !! DON NOT EDIT DIRECTLY !!
#   !!! !!! !!! !!! !!! !!! !!! !!! !!! !!! !!! !!! !!! !!! !!! !!!
#
#   Instead, edit the template (build/maike.tpl.py)
#   and re-run the generator (build/maike.gen-py-files.sh)
#

MAIKE_META = """
#@  { "targets": [
#@      { "name": "gmprograms.hpp",
#@        "dependencies": [
#@          { "rel": "misc", "ref": "data/gm_programs.csv" },
#@          { "rel": "misc", "ref": "compile.py" }
#@          ]
#@        }
#@      ]
#@  }
"""

import compile
# Guess the CSV file name from the maike JSON instead from the Python file
# name, so you can rename the python file and it will still find its CSV:
(csv_file,) = [ ref for ref in compile.maike_dep_refs(MAIKE_META)
                    if ref.endswith('.csv') ]
compile.compile(csv_file)
