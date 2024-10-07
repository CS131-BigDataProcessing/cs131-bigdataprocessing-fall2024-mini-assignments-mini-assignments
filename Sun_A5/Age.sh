#!/bin/bash

# Check if the script receives an argument
if [ -z "$1" ]; then
    echo "Please provide an age as an argument."
    exit 1
fi

# Get the age from the first positional argument
age=$1

# Check the age category using nested if statements
if [ "$age" -lt 13 ]; then
    echo "child"
elif [ "$age" -lt 20 ]; then
    echo "teen"
elif [ "$age" -lt 65 ]; then
    echo "adult"
else
    echo "elderly"
fi
