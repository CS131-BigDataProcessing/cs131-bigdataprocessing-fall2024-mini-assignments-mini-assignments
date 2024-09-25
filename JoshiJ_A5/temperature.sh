#!/usr/bin/env bash
# temperature.sh script - Categorizes temperature

if [ -z "$1" ]; then
  echo "Usage: ./temperature.sh <temperature>"
  exit 1
fi

temp=$1

echo "Debug: Received temperature $temp"

if [ "$temp" -lt 55 ]; then
  echo "Weather: Freezing"
elif [ "$temp" -gt 55 ] && [ "$temp" -lt 67 ]; then
  echo "Weather: Cold"
elif [ "$temp" -gt 67 ] && [ "$temp" -lt 85 ]; then
  echo "Weather: Nice"
else
  echo "Weather: Hot"
fi


