#!/bin/bash

if [ "$#" -ne 2 ]
then
  echo "The following values need to be passed when calling this script:"
  echo "bash get_police_reports.sh <API_KEY> <YEAR>"
  exit 1
fi

API_KEY="$1"
YEAR="$2"

echo "Downloading Richmond Police Department Reports..."
f1="reports_richmond"
curl http://www.co.wayne.in.us/cgi-bin/rms/mediarpd.pl?sdate=$YEAR > $f1.html
echo "...done."
echo "Parsing the Richmond Police Department Reports..."
echo "    (Note: this may take some time.)"
python parse_reports.py --filename $f1 --api-key $API_KEY
echo "...done."

echo "Downloading the Wayne County Police Department Reports..."
f2="reports_sheriff"
curl http://co.wayne.in.us/cgi-bin/rms/media.pl?sdate=$YEAR > $f2.html
echo "...done."
echo "Parsing the Wayne County Sheriff Reports..."
echo "    (Note: this may take some time.)"
python parse_reports.py --filename $f --api-key $API_KEY
echo "...done."

echo "Combining the reports..."
python combine_reports.py $f1.csv $f2.csv $YEAR
echo "...done."
