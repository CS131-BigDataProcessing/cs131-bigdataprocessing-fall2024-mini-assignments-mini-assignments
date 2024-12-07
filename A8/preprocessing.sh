#!/bin/bash
INPUT_FILE="/home/dumpling/AB_NYC_2019.csv"
OUTPUT_FILE="/home/dumpling/cleaned_AB_NYC_2019.csv"

sed -i 's/[[:space:]]*$//' "$INPUT_FILE"

awk -F',' 'NF < 16 { print "Line", NR ":", $0 }' "$INPUT_FILE" > /home/dumpling/missing_values.csv

awk -F, '{
    has_missing=0
    for(i=1; i<=NF; i++) {
        if($i == "") {
            has_missing=1
            break
        }
    }
    if(has_missing==0) {
        print $0
    }
}' "$INPUT_FILE" > /home/dumpling/remove_missing.csv

awk -F, '{
    for(i=1; i<=NF; i++) {
        if($i == "") {
            $i="NA"
        }
    }
    print $0
}' OFS=',' "$INPUT_FILE" > /home/dumpling/replace_na.csv

awk '!seen[$0]++' /home/dumpling/remove_missing.csv > /home/dumpling/removed_duplicates.csv

awk -F',' '{print $10}' /home/dumpling/removed_duplicates.csv | sort -n > /home/dumpling/sorted_data.txt

total_lines=$(wc -l < /home/dumpling/sorted_data.txt)

q1_line=$(echo "$total_lines * 0.25" | bc | awk '{print int($1)}')
q1=$(sed "${q1_line}q;d" /home/dumpling/sorted_data.txt)

q3_line=$(echo "$total_lines * 0.75" | bc | awk '{print int($1)}')
q3=$(sed "${q3_line}q;d" /home/dumpling/sorted_data.txt)

iqr=$(echo "$q3 - $q1" | bc)

awk -F, -v Q1="$q1" -v Q3="$q3" -v IQR="$iqr" '{
    if ($10 < (Q1 - 1.5 * IQR) || $10 > (Q3 + 1.5 * IQR)) {
        print $10
    }
}' /home/dumpling/removed_duplicates.csv > /home/dumpling/price_outliers.txt

median=$(awk '{ a[NR] = $0 } END { if (NR % 2) { print a[(NR + 1) / 2] } else { print (a[(NR / 2)] + a[(NR / 2) + 1]) / 2 } }' /home/dumpling/sorted_data.txt)

awk -F',' -v med="$median" -v Q1="$q1" -v Q3="$q3" -v IQR="$iqr" '{
    if ($10 > (Q3 + 1.5 * IQR)) {
        $10 = med
    }
    print $0
}' OFS=',' /home/dumpling/removed_duplicates.csv > "$OUTPUT_FILE"

echo "Data cleaning complete. Cleaned dataset saved as $OUTPUT_FILE."
