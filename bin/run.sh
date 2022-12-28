#!/usr/bin/env bash

realpath() {
  OURPWD=$PWD
  cd "$(dirname "$1")"
  LINK=$(readlink "$(basename "$1")")
  while [ "$LINK" ]; do
    cd "$(dirname "$LINK")"
    LINK=$(readlink "$(basename "$1")")
  done
  REALPATH="$PWD/$(basename "$1")"
  cd "$OURPWD"
  echo "$REALPATH"
}
# realpath "$@"

if [ "$0" == "-bash" ]; then
    BASEDIR=$(realpath $(dirname ${BASH_SOURCE[0]})"/..");
else
    BASEDIR=$(realpath $(dirname "$0")"/..");
fi

"${BASEDIR}/"src/python/run.py $@;
