#!/usr/bin/env python

# Import relevant packages.
import csv

# Open file to read.
with open("brca_cnvs_tcga-1.csv", newline="") as my_csv:
    csv_content = csv.reader(my_csv)
    # Open file to write.
    with open("brca_cnvs_tcga-1-seq-length.csv", "w") as output_csv:
        new_csv_content = csv.writer(output_csv)
        # Handle this line-by-line.
        for cnv in csv_content:
            # Handle the header separately.
            if cnv[0] == "ID":
                cnv.append("seq_length")
                new_csv_content.writerow(cnv)
            else:
                # Calculate the 0-based distance.
                cnv.append(int(cnv[3]) - int(cnv[2]))
                new_csv_content.writerow(cnv)