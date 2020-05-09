#!/usr/bin/env python
#
# GWCreator - Create a simple guest wireless network.
#
# usage: gwcreator.py [-h] [--token TOKEN] [--site_id SITE_ID] --ssid SSID --url URL --emails DOMAIN [--expire SECONDS]
#
# optional arguments:
#   -h, --help         show this help message and exit
#   --token TOKEN      Mist API token
#   --site_id SITE_ID  Mist site ID
#   --ssid SSID        The wireless network name
#   --url URL          URL guests will be forwarded to after successful authentication
#   --emails DOMAIN    Valid domains for guest sponsor emails, for multiple domains repeat this argument
#   --expire SECONDS   Length of time guest accounts remain authorized in seconds (default: 86400)
#

from gwc import *
import sys

if __name__ == '__main__':
    args = parse_cli()
    print(args)
    log.info(f"Creating new sponsored guest wireless network {args['ssid']}...")
    try:
        new_wlan = create_wlan(**args)
    except Exception as e:
        sys.exit(e)
    log.info(f"Successfully Created new guest wireless network...")
    log.info(f"New WLAN ID: {new_wlan['id']}")
