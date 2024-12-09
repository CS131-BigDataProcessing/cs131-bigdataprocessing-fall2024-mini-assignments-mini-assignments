#!/bin/bash -ue
echo $input_string | tr 'a-z' 'A-Z' > result.txt
echo $(cat result.txt)
