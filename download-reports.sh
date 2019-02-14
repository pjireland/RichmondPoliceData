#!/bin/bash

# Download Richmond PD Reports
curl http://www.co.wayne.in.us/cgi-bin/rms/mediarpd.pl?sdate=2018 > reports2018-richmond.html

# Download Wayne County Sheriff Reports
curl http://co.wayne.in.us/cgi-bin/rms/media.pl?sdate=2018 > reports2018-sheriff.html
