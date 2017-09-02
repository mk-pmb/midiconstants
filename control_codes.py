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
import compile
# guessing the CSV filename from the maike JSON instead from the
# Python file name, so you can rename the python file and it will
# still find its CSV:
compile.compile_guess_data_file("""
#@  { "targets": [
#@      { "name": "controlcodes.hpp",
#@        "dependencies": [
#@          { "rel": "misc", "ref": "data/control_codes.csv" },
#@          { "rel": "misc", "ref": "compile.py" }
#@          ]
#@        }
#@      ]
#@  }
""")
