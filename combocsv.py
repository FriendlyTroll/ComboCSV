#!/usr/bin/python3
#
# Combine multiple csvs into one xcel file with each csv file as separate sheet
#
# Tested on: Xubuntu 18.04.2
# Dependencies:
#
# sudo apt install python3-pandas
# pip3 install xlsxwriter

import pandas as pd
import glob
import os

path = r'/tmp' # use your path
col_names = ['Package', 'Version'] # define headers here e.g ['Package', 'Version'] if there are 2 columns


all_files = glob.glob(path + "/*.csv")


writer = pd.ExcelWriter('all_csvs.xlsx', engine='xlsxwriter')

for filename in all_files:
    # get the name of the file without the .csv part for use as sheet name below
    csv_name = os.path.splitext(os.path.basename(filename))[0]
    # if the names of columns are defined above write them in first row
    if col_names:
        df = pd.read_csv(filename, names=col_names, index_col=None, header=None)
        df.to_excel(writer, index=False, sheet_name=csv_name)
    # else write the date without any headers or indexes
    else:
        df = pd.read_csv(filename, index_col=None, header=None)
        df.to_excel(writer, index=False, header=None, sheet_name=csv_name)

writer.save()
