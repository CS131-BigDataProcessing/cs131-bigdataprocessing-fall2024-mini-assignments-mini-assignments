#!/bin/bash

###Activity 1: Displaying messages
#provide time and date
echo "The time and date are: $(date)"

#who's logged into the system
echo "Let's see who is logged into the system: $USER"

#check user home directory
echo "For $USER, the home directory is $HOME"

###Activity 2: Working with positional arguments
your_name=$1
amount_money=$2

echo "My name is $your_name and I have \$$amount_money in my wallet."

###Activity 3: Math Time
mathvar1=$((1+5))
mathvar2=$((mathvar1 * 20))
mathvar3=10

#calulating mathvar4
mathvar4=$((mathvar1 * (mathvar2 + mathvar3)))

echo "Variable 1 is $mathvar1. Variable 2 is $mathvar2. Using $mathvar3 for Variable3, our final Variable 4 is $mathvar4."


###Activity 4: Working with floating-point solution
floating=$(echo "scale=3; 4.5/1.7" | bc)

echo "Our floating variable is $floating"


