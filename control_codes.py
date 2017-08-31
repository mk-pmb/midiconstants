#@  {
#@  "targets":
#@      [
#@           {
#@			 "name":"controlcodes.hpp","dependencies":
#@				[{"ref":"data/control_codes.csv","rel":"misc"},{"ref":"compile.py","rel":"misc"}]
#@			 }
#@      ]
#@  }

import compile
compile.compile('data/control_codes.csv')
