#!/usr/bin/env python


from __future__ import division, print_function
import pandas as pd
import numpy as np
import googlemaps
import os
import argparse
import sys


def get_args():
    '''Get the arguments passed via command line'''
    parser = argparse.ArgumentParser(description='Parse raw police data')
    required = parser.add_argument_group('required arguments')
    required.add_argument('--api-key', type=str, required=True,
                        help='API key for Google Maps API')
    required.add_argument('--filename', '-f', type=str, required=True,
                        help='Filename to parse')
    args = parser.parse_args()
    if not os.path.isfile(args.filename):
        print('Error: filename', args.filename, 'was not found.')
        sys.exit()
    return args


def get_gmaps_handle(api_key):
    '''Return the handle to the Google Maps API'''
    gmaps = googlemaps.Client(key=api_key)
    return gmaps


def geocode_address(address, gmaps):
    '''Geocode an address using the Google Maps API'''
    geocode = gmaps.geocode(address)
    try:
        location = geocode[0]['geometry']['location']
        return location['lat'],location['lng']
    except:
        print('Failed to geocode address:', address, flush=True)
        return np.nan, np.nan


def parse_reports(filename, api_key):
    '''Parse the reports'''
    df = pd.DataFrame(columns=['Case #', 'Date', 'Description', 'Victim', 'Address', 'Details', 'Latitude', 'Longitude'])
    gmaps = get_gmaps_handle(api_key)
    with open(filename, 'r') as f:
        info = {}
        for line in f:
            if '<td align=left>' in line:
                col_name = line.split('<b>', 1)[1].split(':', 1)[0]
                row_value = line.split('<td align=left>', 1)[1].split('<', 1)[0]
                info[col_name] = row_value
                if col_name == 'Address':
                    # Need to add city for Richmond reports but not for Wayne County Reports
                    if not 'sheriff' in filename:
                        info[col_name] += ', Richmond, IN  47374'
                    else:
                        info[col_name] +=', Wayne County, IN'
                    lat, lng = geocode_address(info[col_name], gmaps)
                    info['Latitude'] = lat
                    info['Longitude'] = lng
            elif '<td width=10></td><td align=left valign=top>' in line:
                col_name = 'Details'
                row_value = line.split('<td width=10></td><td align=left valign=top>', 1)[1].split('<', 1)[0]
                info[col_name] = row_value
                df = df.append(info, ignore_index=True)
                info = {}
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    df = df.sort_values('Case #')
    df.to_csv(filename.replace('.html', '.csv'), index=False)


if __name__ == '__main__':
    args = get_args()
    parse_reports(args.filename, args.api_key)

