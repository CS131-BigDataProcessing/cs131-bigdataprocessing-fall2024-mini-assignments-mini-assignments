#!/usr/bin/env nextflow

nextflow.enable.dsl=2

params.input_string = params.input_string ?: 'Hello World'

workflow {
    toUpperCase(params.input_string)
        | printResult
}

process toUpperCase {
    input:
    val input_string

    output:
    val upper_case_string into result_channel

    script:
    """
    echo ${input_string^^}
    """
}

process printResult {
    input:
    val upper_case_string from result_channel

    script:
    """
    echo "Converted to uppercase: ${upper_case_string}"
    """
}

