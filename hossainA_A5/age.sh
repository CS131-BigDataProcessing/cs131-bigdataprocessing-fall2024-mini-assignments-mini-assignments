#!/bin/bash

# Check if an argument is provided
if [ -z "$1" ]; then
    echo "Please provide an age as an argument."
    exit 1
fi

# Get the age from the first positional argument
age=$1

# Nested if statements to categorize the age
if [ "$age" -lt 13 ]; then
    echo "child"
elif [ "$age" -lt 20 ]; then
    echo "teen"
elif [ "$age" -lt 65 ]; then
    echo "adult"
else
    echo "elderly"
fi

