#!/usr/bin/env nextflow

nextflow.enable.dsl=2

process convertToUppercase {
    input:
    val input_string 

    output:
    stdout

    script:
    """
    echo \$input_string | tr 'a-z' 'A-Z'
    """
}

workflow {
    input_string = params.str ?: "Hello World"  
    result = convertToUppercase(input_string)
    result.view()
}

