# checkmk-1-6-custom-active-checks

This repo explain how to write your custom Active Checks for CheckMK version 1.6
by presenting a working example.

# Installation

* Place the nagios plugin `check_validUntil.py` in `omd/sites/<site-id>/local/lib/nagios/plugins` and make it executable
* Place `check_validUntil` into `omd/sites/<site-id>/local/share/check_mk/checks/check_validUntil`
* Place `check_validUntil_params.py` into `omd/sites/<site-id>/local/share/check_mk/web/plugins/wato`

# Usage

* Explore to `WATO - CONFIGURATION` -> `Host & Service Parameters` -> `Active checks` -> `Check validUntil`.
* Click on "Check validUntil" and create a new rule in the folder of your preference.
* Fill the fields with your preference and click `Save`.

# Author

* Marco Malavolti - marco.malavolti[at]garr.it
