#!/usr/bin/python3
# -*- encoding: utf-8; py-indent-offset: 4 -*-

# Check_MK check_ssl_issuer_params.py
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

group = "activechecks"

register_rule(group,
    "active_checks:ssl_issuer",
    Dictionary(
        title = _("Check SSL issuer"),
        help = _("This check verify that the right Issuer is contained by the server SSL certificate."
                 "The check uses the active check <tt>check_ssl_issuer</tt>."),
        elements = [
            ( "description",
              TextUnicode(title = _("Service Description"),
                 help = _("The name of this active service to be displayed."),
                 default_value = "Check SSL issuer",
                 allow_empty = False,
            )),
            ( "hostname",
                TextUnicode(
                    title = _("Server Hostname"),
                    help = _('The FQDN of the server to check'),
                    default_value = "mdx.idem.garr.it",
                    allow_empty = False,
                )
            ),
            ( "issuer",
                TextUnicode(
                    title = _("Certificate Issuer"),
                    help = _('The Issure to find on the server SSL certificate'),
                    default_value = "GEANT OV RSA CA 4",
                    allow_empty = False,
                )
            ),
        ]
    ),
    match = 'all'
)
