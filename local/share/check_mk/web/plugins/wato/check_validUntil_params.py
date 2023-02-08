#!/usr/bin/python3
# -*- encoding: utf-8; py-indent-offset: 4 -*-

# Check_MK check_validUntil_params.py
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
    "active_checks:validUntil",
    Dictionary(
        title = _("Check validUntil"),
        help = _("This check verify that the date and time provided by the validUntil XML argument in a metadata is at least X hours in the future."
                 "The check uses the active check <tt>check_validUntil</tt>."),
        elements = [
            ( "description",
              TextUnicode(title = _("Service Description"),
                 help = _("The name of this active service to be displayed."),
                 default_value = "Check validUntil",
                 allow_empty = False,
            )),
            ( "url",
                TextUnicode(
                    title = _("MD Entity URL"),
                    help = _('The URL provided the entity metadata to check'),
                    default_value = "https://mdx.idem.garr.it/idem/entities/https:%2F%2Fwiki.idem.garr.it%2Frp",
                    allow_empty = False,
                )
            ),
            ( "hours",
                Integer(
                    title = _("Hours to validate the date and time of the validUntil provided"),
                    minvalue = 1,
                    maxvalue = 100,
                    default_value = 3,
                    allow_empty = False,
                )
            ),
        ]
    ),
    match = 'all'
)
