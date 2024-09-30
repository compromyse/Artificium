#!/usr/bin/env bash

shopt -s extglob

if [[ "$1" != '' ]]; then
  cd $1
fi

echo "Start upload: $(date)"
echo

for i in *.zip; do
  echo "Uploading $i"
  curl 'http://cmp.compromyse.xyz/jury/import-export' \
    -X POST \
    -H "Cookie: PHPSESSID=$2" \
    -F 'problem_upload[contest]=' \
    -F "problem_upload[archive]=@$i" \
    -F 'problem_upload[upload]='
done

echo
echo "End upload: $(date)"
