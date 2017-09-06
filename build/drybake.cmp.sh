#!/bin/bash
# -*- coding: utf-8, tab-width: 2 -*-


function drybake_cmp () {
  export LANG{,UAGE}=en_US.UTF-8  # make error messages search engine-friendly
  local SELFPATH="$(readlink -m "$BASH_SOURCE"/..)"
  cd "$SELFPATH"/../data || return $?

  local BFN="$1"
  BFN="${BFN%.json}"
  BFN="${BFN%.csv}"
  BFN="${BFN%.dry}"
  BFN="${BFN%.}"

  local JSLINT="$(which \
    jsl \
    jslint \
    2>/dev/null | grep -Pe '^/' -m 1)"
  local JSONLINT="$JSLINT"
  [ -n "$JSONLINT" ] || JSONLINT="$(which \
    jsonlint \
    2>/dev/null | grep -Pe '^/' -m 1)"
  [ ! -x "$JSONLINT" ] || "$JSONLINT" "$BFN".dry.json || return $?

  export CSV_SEP=';'

  # "$FUNCNAME"_edition py python3
  "$FUNCNAME"_edition js nodejs
  return 0
}


function drybake_cmp_edition () {
  local FXT="$1"
  local INTPR="$2"
  local BAKE="$SELFPATH"/drybake."$FXT"

  case "$FX" in
    js )    [ ! -x "$JSLINT" ] || "$JSLINT" "$BAKE" || return $?;;
  esac

  local DRIED="$("$INTPR" "$BAKE" "$BFN".dry.json 2>&1)"
  local MAXLN="$(<<<"$DRIED" grep -Fe ';' | wc -l)"
  let MAXLN="${MAXLN:-0}+2"
  colordiff -sU 2 --label want --label "$FXT" <(head -n "$MAXLN" -- "$BFN.csv"
    ) <(echo "$DRIED") | sed -re '/^(\x1B\[[0-9;]*m)(\-{3}|@@)/d'
  return 0
}










[ "$1" == --lib ] && return 0; drybake_cmp "$@"; exit $?
