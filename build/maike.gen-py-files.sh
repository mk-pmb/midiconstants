#!/bin/bash
# -*- coding: utf-8, tab-width: 2 -*-


function make_maike_files () {
  export LANG{,UAGE}=en_US.UTF-8  # make error messages search engine-friendly
  local SELFFILE="$(readlink -m "$BASH_SOURCE")"
  local SELFPATH="$(readlink -m "$SELFFILE"/..)"
  cd "$SELFPATH"/.. || return $?

  local BUILD_SUBDIR="${SELFPATH#$PWD/}"
  local GEN_TPLPROG="${SELFFILE#$PWD/}"
  local GEN_TPLFN="$BUILD_SUBDIR/maike.tpl.py"
  local WARN_BAR='!!!:::::::::::::::'
  WARN_BAR="${WARN_BAR//:/ ${WARN_BAR%%:*}}"

  local CSV=
  local BFN=
  for CSV in data/*.csv; do
    BFN="$(basename "$CSV" .csv)"
    gen_maike_py "$BFN" >"$BFN".py || return $?
    grep -HnPe '\a' -C 3 -- "$BFN".py && return 3
    chmod a+x -- "$BFN".py || return $?
  done

  return 0
}


function quotemeta () {
  sed -re 's~[^A-Za-z0-9_-]~\\&~g'
}


function gen_maike_py () {
  local BFN="$1"

  local CLSN_LC="$BFN"
  CLSN_LC="${CLSN_LC//_/}"
  CLSN_LC="${CLSN_LC,,}"

  LANG=C sed -re '/^__GEN:maike-meta__/r '"$BUILD_SUBDIR/maike.meta.json
    " -- "$GEN_TPLFN" | LANG=C sed -re '
    /^__GEN:maike-meta__/{
      s~^__~~;s~__~ ~;N
      s~^\S+\s*[^ -~]*~~
      : more_maike_meta
      /\n\S/!{N;b more_maike_meta}
      s~^|\n~&#@  ~g
    }
    ' | LANG=C sed -re "
    s~__GEN:warn-edit__~!! AUTO-GENERATED FILE !! DON NOT EDIT DIRECTLY !!~g
    s~__GEN:warn-line__~$WARN_BAR~g
    s~__GEN:tplfn__~$GEN_TPLFN~g
    s~__GEN:tplprog__~$GEN_TPLPROG~g
    s~__GEN:tablename__~$BFN~g
    s~__GEN:classname-lower__~$CLSN_LC~g
    " | LANG=C sed -re "/__GEN:/{i
      i #>>$WARN_BAR>>#
      i #>>$WARN_BAR>>#\a
      a #<<$WARN_BAR<<#\a
      a #<<$WARN_BAR<<#
      a
    }"
}
















[ "$1" == --lib ] && return 0; make_maike_files "$@"; exit $?
