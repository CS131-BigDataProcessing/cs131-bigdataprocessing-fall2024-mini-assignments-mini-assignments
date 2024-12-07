#!/bin/bash

# Check if the script receives an argument
if [ -z "$1" ]; then
    echo "Please provide a temperature as an argument."
    exit 1
fi

# Get the temperature from the first positional argument
temp=$1

# Check the temperature category using nested if statements
if [ "$temp" -lt 55 ]; then
    echo "freezing"
elif [ "$temp" -gt 55 ] && [ "$temp" -lt 67 ]; then
    echo "cold"
elif [ "$temp" -ge 67 ] && [ "$temp" -le 85 ]; then
    echo "nice"
else
    echo "hot"
fi
