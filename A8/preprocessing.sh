#1. identify missing values 
awk -F',' 'NF < 16 { print "Line", NR ":", $0 }' AB_NYC_2019.csv

#find number of rows that have missing values
awk -F',' 'NF < 16 {count++} END {print count " rows have missing values"}' AB_NYC_2019.csv

#Replace missing values with N/A
sed 's/,,/,N\/A,/g' AB_NYC_2019.csv > cleaned_AB_NYC_2019.csv

#2. Remove rows with missing values
sed 's/,,/,N\/A,/g' AB_NYC_2019.csv > cleaned_AB_NYC_2019.csv

#Alternative: Remove rows with missing values 
sed '/,,/d' AB_NYC_2019.csv > cleaned_AB_NYC_2019.csv

#3. Remove Duplicate Entries 
#Didn't see duplicates in dataset, so no need for this


#4. Identifying and Handling Outliers
awk -F',' 'NR > 1 && $10 ~ /^[0-9]+$/ { if ($10 > max || NR == 2) max = $10; if ($10 < min || NR == 2) min = $10; } END { print "Minimum Price:", min; print "Maximum Price:", max; }' AB_NYC_2019.csv

#Median for finding outliers
awk -F',' 'NR > 1 && $10 ~ /^[0-9]+$/ { prices[++count] = $10 }
END {
    asort(prices)
    median = (count % 2 == 1) ? prices[(count + 1) / 2] : (prices[count / 2] + prices[(count / 2) + 1]) / 2
    threshold_high = median * 2
    threshold_low = median / 2
    outliers = 0
    for (i = 1; i <= count; i++) {
        if (prices[i] > threshold_high || prices[i] < threshold_low) outliers++
    }
    print "Median:", median, "Number of Outliers:", outliers
}' AB_NYC_2019.csv

#Alternative method: Using IQR
awk -F',' 'NR > 1 && $10 ~ /^[0-9]+$/ { prices[++count] = $10 }
END {
    asort(prices)
    Q1 = prices[int(count * 0.25)]
    Q3 = prices[int(count * 0.75)]
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    outliers = 0
    for (i = 1; i <= count; i++) {
        if (prices[i] < lower_bound || prices[i] > upper_bound) outliers++
    }
    print "Q1:", Q1, "Q3:", Q3, "IQR:", IQR, "Number of Outliers:", outliers
}' AB_NYC_2019.csv


