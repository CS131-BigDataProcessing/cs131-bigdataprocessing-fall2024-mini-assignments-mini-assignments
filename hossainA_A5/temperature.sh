#!/bin/bash

# Positional argument for temperature
temp=$1

# Check if temperature is provided
if [ -z "$temp" ]; then
    echo "Please provide the temperature as an argument."
    exit 1
fi

# Nested if statements to check temperature conditions
if [ "$temp" -lt 55 ]; then
    echo "It's freezing."
else
    if [ "$temp" -ge 55 ] && [ "$temp" -lt 67 ]; then
        echo "It's cold."
    elif [ "$temp" -ge 67 ] && [ "$temp" -lt 85 ]; then
        echo "It's nice."
    elif [ "$temp" -ge 85 ]; then
        echo "It's hot."
    fi
fi

