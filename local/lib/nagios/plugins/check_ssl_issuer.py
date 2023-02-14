#!/usr/bin/env python3
#-*- coding: utf-8 -*-; py-indent-offset: 4 -*-

# check_ssl_issuer.py
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

import argparse
import ssl, socket
import sys

# PARAMETERS

hostname  = "mdx.idem.garr.it"
issuer = "GEANT OV RSA CA 4"

# END PARAMETERS

parser = argparse.ArgumentParser(prog="check_ssl_issuer.py",description="Checks the presence of a specific Issuer on a web server", epilog="CHECK SSL ISSUER SCRIPT")
parser.add_argument("--debug", dest="debug", action="store_true", help="Print debug information", default=False)
parser.add_argument("--hostname", dest="hostname", help="Specify the hostname of the server to check", default=hostname)
parser.add_argument("--issuer", dest="issuer", help="Specify the valid issuer to find", default=issuer)
options = parser.parse_args()

if options.debug:
   print ("\nOptions passed to command: " + str(options))

ctx = ssl.create_default_context()
with ctx.wrap_socket(socket.socket(), server_hostname=hostname) as s:
    s.connect((hostname, 443))
    cert = s.getpeercert()

subject = dict(x[0] for x in cert['subject'])
issued_to = subject['commonName']
cert_issuer = dict(x[0] for x in cert['issuer'])
issued_by = cert_issuer['commonName']

if options.debug:
    print("\nHOSTNAME: "+ hostname +
          "\nISSUER: "+ issuer +
          "\nCHECKED_ISSUER: "+str(issued_by)+
          "\n")

if (issued_to == hostname) and (issued_by == issuer):
   print("SUCCESS - "+hostname+" has "+issued_by+" issuer")
   sys.exit(0)
else:
   print("CRITICAL - "+hostname+" has not "+issued_by+" issuer")
   sys.exit(2)
