#!/usr/bin/env python


from __future__ import division, print_function
import pandas as pd
import os
import argparse
import sys
import datetime as dt


def get_args():
    '''Get the arguments passed via command line'''
    parser = argparse.ArgumentParser(description='Combine parsed police data')
    parser.add_argument('Richmond', type=str,
                        help='Parsed data from Richmond Police Department')
    parser.add_argument('WayneCounty', type=str,
                        help='Parsed data from Wayne County Sheriff')
    parser.add_argument('year', type=int, help='Year to analyze')
                        
    args = parser.parse_args()
    for arg in [args.Richmond, args.WayneCounty]:
        if not os.path.isfile(arg):
            print('Error: filename', arg, 'was not found.')
            sys.exit()
    return args


def read_report(filename):
    '''Read the report from file'''
    df = pd.read_csv(filename)
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    if 'sheriff' in filename:
        df['department'] = 'sheriff'
    else:
        df['department'] = 'richmond'
    return df


def combine_and_filter_reports(df1, df2, year):
    '''Combine the reports together and filter by year'''
    df = df1.append(df2)
    return df[df['Date'].dt.year == year]


def write_combined_report(df):
    '''Write the combined report to a file'''
    df.to_csv('reports_all.csv', index=False)


if __name__ == '__main__':
    args = get_args()
    df1 = read_report(args.Richmond)
    df2 = read_report(args.WayneCounty)
    df = combine_and_filter_reports(df1, df2, args.year)
    write_combined_report(df)

