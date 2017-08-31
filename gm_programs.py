#@  {
#@  "targets":
#@      [
#@           {
#@			 "name":"gmprograms.hpp","dependencies":
#@				[{"ref":"data/gm_programs.csv","rel":"misc"},{"ref":"compile.py","rel":"misc"}]
#@			 }
#@      ]
#@  }

import compile
compile.compile('data/gm_programs.csv')
