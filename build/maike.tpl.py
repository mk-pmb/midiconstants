#!/usr/bin/python3
# -*- coding: UTF-8, tab-width: 4 -*-
#
#   __GEN:warn-line__
#   __GEN:warn-edit__
#   __GEN:warn-line__
#
#   Instead, edit the template (__GEN:tplfn__)
#   and re-run the generator (__GEN:tplprog__)
#

MAIKE_META = """
__GEN:maike-meta__
"""

import compile
# Guess the CSV file name from the maike JSON instead from the Python file
# name, so you can rename the python file and it will still find its CSV:
(csv_file,) = [ ref for ref in compile.maike_dep_refs(MAIKE_META)
                    if ref.endswith('.csv') ]
compile.compile(csv_file)
