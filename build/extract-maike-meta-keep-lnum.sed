#!/bin/sed -nurf
# -*- coding: UTF-8, tab-width: 2 -*-

1s~^~:~
: wait_for_maike_meta
  s~^(\n*:)\s*(//|#)@~\1\n~
  s~^(\n*:)([^\n].*|\s+)$~\1~
  /^\n*:\n/{
    s~:\n~~p
    b found_maike_meta
  }
  N;s~^(\n*:)\n~\n\1~
b wait_for_maike_meta

: found_maike_meta
  n;s~^\s*(//|#)@~~p
b found_maike_meta
