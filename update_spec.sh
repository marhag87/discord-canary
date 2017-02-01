#!/bin/bash
# Script for checking for new versions of atlassian products
# Written by Martin Hagström 2015-12-17

update=false
name=discord

function getlatestversion() {
  if [[ $name == discord-canary ]]; then
    ./latest.py -c
  else
    ./latest.py
  fi
}

function getcurrentversion() {
  awk '/^Version/ { print $2 }' ${name}.spec
}

function update() {
  datestring=$(date "+%a %b %d %Y Martin Hagstrom (API) <marhag87@gmail.com> $2-1")
  sed -i "s/\(^Version:\s*\)[[:digit:].]*/\1${2}/"   ${1}.spec
  sed -i "s/\(^Release:\s*\)[[:digit:].]*/\11/"      ${1}.spec
  sed -i "s/\%changelog/\%changelog\n\* ${datestring}\n- Update to $2/" ${1}.spec
}

function compareversions() {
  latestversion=$(getlatestversion)
  currentversion=$(getcurrentversion)
  if [[ $currentversion != $latestversion ]]; then
    if [[ $update == true ]]; then
      update $name $latestversion
    else
      echo "${name^} not up to date, latest version: ${latestversion}"
    fi
  fi
}

while getopts "uc" opt; do
  case $opt in
    u)
      update=true
      ;;
    c)
      name=discord-canary
      ;;
    \?)
      echo "Invalid option: -$OPTARG" >&2
      ;;
  esac
done

compareversions
