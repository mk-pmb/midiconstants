#!/bin/bash
# -*- coding: utf-8, tab-width: 2 -*-


function build () {
  export LANG{,UAGE}=en_US.UTF-8  # make error messages search engine-friendly
  local SELFPATH="$(readlink -m "$BASH_SOURCE"/..)"
  cd "$SELFPATH" || return $?

  local NF_DIR='../dist/nonfree'
  mkdir -p "$NF_DIR" || return $?

  local CSV_FILES=(
    control_codes
    status_codes
    )
  local BFN=
  for BFN in "${CSV_FILES[@]}"; do
    echo -n "generate $BFN.csv: "
    </dev/null nodejs -- "$SELFPATH"/drybake.js \
      "../data/$BFN.dry.json" >"$NF_DIR"/"$BFN".csv || return $?
    echo 'done.'
  done

  local GH_USER='milasudril'
  local GH_REPO='midiconstants'
  local GH_COMMIT='c4b071e34acfd22f5bb6e96b6a2846704bd26737'
  local RAW_BASE="https://github.com/$GH_USER/$GH_REPO/raw/$GH_COMMIT/"
  CSV_FILES=(
    gm_drumkit
    gm_programs
    )
  for BFN in "${CSV_FILES[@]}"; do
    github_dl %.txt %.csv "$BFN" || return $?
  done

  return 0
}


function github_dl () {
  local ORIG_PTN="$1"; shift
  local SAVE_PTN="$1"; shift
  local BFN="$1"; shift
  local DL_URL="$RAW_BASE${ORIG_PTN//%/$BFN}"
  local SAVE_FN="$NF_DIR/${SAVE_PTN//%/$BFN}"
  echo -n "$FUNCNAME: $SAVE_FN"
  if [ -s "$SAVE_FN" ]; then
    echo ': already in cache.'
  else
    echo " <- $DL_URL :"; echo
    local UAGENT='Mozilla/5.0 (actually, wget) Gecko/19700101 Firefox/0.0'
    wget --user-agent="$UAGENT" -O "$SAVE_FN.part" -c "$DL_URL" || return $?
    mv --verbose --no-target-directory -- "$SAVE_FN"{.part,} || return $?
    echo
  fi
  return 0
}










[ "$1" == --lib ] && return 0; build "$@"; exit $?
