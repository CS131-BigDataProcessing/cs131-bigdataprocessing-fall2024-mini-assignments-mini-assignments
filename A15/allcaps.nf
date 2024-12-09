#!/usr/bin/env nextflow

// Define workflow
process ConvertToCaps {
    // Specify the input
    input:
    val input_string from params.input_string

    // Specify the output
    output:
    val result into uppercase_result

    // Process to convert input to uppercase
    script:
    result = input_string.toUpperCase()
}

// Print the result
uppercase_result.view { "Result: $it" }

