#@  {
#@  "targets":
#@      [
#@           {
#@			 "name":"statuscodes.hpp","dependencies":
#@				[{"ref":"data/status_codes.csv","rel":"misc"},{"ref":"compile.py","rel":"misc"}]
#@			 }
#@      ]
#@  }

import compile
compile.compile('data/status_codes.csv')
