#@  {
#@  "targets":
#@      [
#@           {
#@			 "name":"gmdrumkit.hpp","dependencies":
#@				[{"ref":"data/gm_drumkit.csv","rel":"misc"},{"ref":"compile.py","rel":"misc"}]
#@			 }
#@      ]
#@  }

import compile
compile.compile('data/gm_drumkit.csv')
