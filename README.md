# GWCreator

### Create a sponsored guest wireless network.

```bash
usage: gwcreator.py [-h] [--token TOKEN] [--site_id SITE_ID] --ssid SSID --url URL --emails DOMAIN [--expire SECONDS]

optional arguments:
  -h, --help         show this help message and exit
  --token TOKEN      Mist API token
  --site_id SITE_ID  Mist site ID
  --ssid SSID        The wireless network name
  --url URL          URL guests will be forwarded to after successful authentication
  --emails DOMAIN    Valid domains for guest sponsor emails, for multiple domains repeat this argument
  --expire SECONDS   Length of time guest accounts remain authorized in seconds (default: 86400)
```

Example:
```bash
$ cwcreator.py --token <API TOKEN> --site_id <MIST SITE ID> --ssid "NEW SSID" --psk "NEW PSK FOR WLAN" --vlan 100 --duration 3

2020-05-07 15:17:26 PDT [INFO   ][cwcreator]: Creating new wireless network 'NEW SSID' with the PSK 'NEW PSK FOR WLAN'.
2020-05-07 15:17:27 PDT [INFO   ][cwcreator]: New wireless network 'NEW SSID' created!
2020-05-07 15:17:27 PDT [INFO   ][cwcreator]: Created WLAN at 2020-05-07 15:17
2020-05-07 15:17:27 PDT [INFO   ][cwcreator]: WLAN to be destroyed at approx 2020-05-10 15:17
2020-05-07 15:17:27 PDT [INFO   ][cwcreator]: WLAN ID: 56ce01b6-fe4c-4186-97f2-1111d23c521c
```

Using the response from in the logs a secondary task to delete the newly created WLAN can easily be implemented.