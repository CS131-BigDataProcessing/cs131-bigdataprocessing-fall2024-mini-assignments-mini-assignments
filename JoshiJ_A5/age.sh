#!/usr/bin/env bash
# age.sh script - Categorizes age

if [ -z "$1" ]; then
  echo "Usage: ./age.sh <age>"
  exit 1
fi

age=$1

echo "Debug: Received age $age"

if [ "$age" -lt 13 ]; then
  echo "Category: Child"
elif [ "$age" -lt 20 ]; then
  echo "Category: Teen"
elif [ "$age" -lt 65 ]; then
  echo "Category: Adult"
else
  echo "Category: Elderly"
fi



