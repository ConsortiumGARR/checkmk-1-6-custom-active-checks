#!/usr/bin/env python3
#-*- coding: utf-8 -*-; py-indent-offset: 4 -*-

# check_validUntil.py
#
# Copyright 2023, Marco Malavolti <marco.malavolti[at]garr.it>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import xml.etree.cElementTree as ET

import sys
import argparse
import requests
from io import StringIO
from datetime import datetime

# PARAMETERS

mdx_url  = "https://mdx.idem.garr.it/idem/entities/https:%2F%2Fwiki.idem.garr.it%2Frp"
hours = 3

# END PARAMETERS

parser = argparse.ArgumentParser(prog="check_validUntil.py",description="Check the value of 'validUntil' XML argument for an entity provided by an MDX url", epilog="MDX VALIDUNTIL CHECK SCRIPT")
parser.add_argument("--debug", dest="debug", action="store_true", help="Print debug information", default=False)
parser.add_argument("--url", dest="mdx_url", help="Specify the URL of MDX entity", default=mdx_url)
parser.add_argument("--hours", dest="hours", help="Specify how many hours the validUntil found in the metadata must not be lower", default=hours)
options = parser.parse_args()

if options.debug:
   print ("\nOptions passed to command: " + str(options))

if options.mdx_url:
   mdx_url = options.mdx_url

if options.hours:
   hours = options.hours

md = requests.get(mdx_url) 
tree = ET.parse(StringIO(md.text))
root = tree.getroot()

now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
today = datetime.strptime(now, '%Y-%m-%d %H:%M:%S')
mdx_validUntil = datetime.strptime(root.attrib['validUntil'], '%Y-%m-%dT%H:%M:%SZ')

time_slice = mdx_validUntil - today
duration_in_sec = time_slice.total_seconds()

diff_hours = divmod(duration_in_sec, 3600)[0]

if options.debug:
    print("\nMDX_URL: "+ mdx_url +
          "\nTODAY: "+ str(today) +
          "\nMDX_VALIDUNTIL: "+str(mdx_validUntil)+
          "\nTIME_SLICE: "+str(time_slice)+
          "\nHOURS: "+str(hours)+
          "\nDIFF_HOURS: "+str(int(diff_hours))+
          "\n")

if int(diff_hours) >= int(hours):
   print("SUCCESS - MDX works well - Metadata's validUntil is "+ str(mdx_validUntil))
   sys.exit(0)
else:
   print("CRITICAL - MDX has a problem - Metadata's validUntil is "+ str(mdx_validUntil) +" hours")
   sys.exit(2)
