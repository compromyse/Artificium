#!/usr/bin/env bash

shopt -s extglob

mkdir -p out

if [[ "$1" != '' ]]; then
  cd $1
fi

echo "Start build: $(date)"
echo

for d in $(ls -d !(build.sh|out|*.py)); do
  echo "Building $d"
  cd $d && zip -r "../../out/$d.zip" * > /dev/null && cd ..
done

echo
echo "End build: $(date)"
