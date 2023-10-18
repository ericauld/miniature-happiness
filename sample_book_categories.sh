#!/bin/bash

n=$1
shift
for subject; do
    mkdir -p books/"${subject}"
    book_numbers=$(./csv_filter_column_regex.py <pg_catalog_en.csv Subjects $subject | \
	./csv_sample_rows.py $n | \
	./csv_only_columns.py 'Text#' | \
	tail -n +2)
    IFS=$'\n'
    for book_number in $book_numbers; do
	book_number=$(echo -n $book_number | tr -d '\r')
	./download.py $book_number >books/"${subject}"/pg${book_number}.txt
    done
    unset IFS
done
