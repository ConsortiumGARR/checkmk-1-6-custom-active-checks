# checkmk-1-6-custom-active-checks

This repo explain how to write your custom Active Checks for CheckMK version 1.6
by presenting several working examples.

## Index

1. [Installation](#installation)
   1. [check_validUntil installation](#check_validuntil-installation)
   2. [check_ssl_issuer installation](#check_ssl_issuer-installation)
2. [Usage](#usage)
   1. [check_validUntil usage](#check_validuntil-usage)
   2. [check_ssl_issuer usage](#check_ssl_issuer-usage) 
3. [Author](#author)

## Installation

### check_validUntil installation

* Place the nagios plugin `check_validUntil.py` in `omd/sites/<site-id>/local/lib/nagios/plugins` dir and make it executable
* Place `check_validUntil` into `omd/sites/<site-id>/local/share/check_mk/checks` dir
* Place `check_validUntil_params.py` into `omd/sites/<site-id>/local/share/check_mk/web/plugins/wato` dir

### check_ssl_issuer installation

* Place the nagios plugin `check_ssl_issuer` in `omd/sites/<site-id>/local/lib/nagios/plugins` dir and make it executable
* Place `check_ssl_issuer` into `omd/sites/<site-id>/local/share/check_mk/checks` dir
* Place `check_ssl_issuer_params.py` into `omd/sites/<site-id>/local/share/check_mk/web/plugins/wato` dir

## Usage

### check_validUntil usage

* Explore to `WATO - CONFIGURATION` -> `Host & Service Parameters` -> `Active checks`.
* Click on **Check validUntil** and create a new rule in the folder of your preference.
* Fill the fields with your preference and click `Save`.

### check_ssl_issuer usage

* Explore to `WATO - CONFIGURATION` -> `Host & Service Parameters` -> `Active checks`.
* Click on **Check SSL issuer** and create a new rule in the folder of your preference.
* Fill the fields with your preference and click `Save`.

## Author

* Marco Malavolti - marco.malavolti[at]garr.it
