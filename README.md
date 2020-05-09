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
$ cwcreator.py --token <API TOKEN> --site_id <MIST SITE ID> --ssid "GUEST_TEST" --url <FORWARDING URL> --emails <SPONSOR EMAIL DOMAIN> --emails <SPONSOR EMAIL DOMAIN> --expire 172800

2020-05-08 17:11:57 PDT [INFO   ][gwcreator]: Creating new sponsored guest wireless network 'GUEST_TEST'...
2020-05-08 17:11:58 PDT [INFO   ][gwcreator]: New sponsored guest wireless network 'GUEST_TEST' created!
2020-05-08 17:11:58 PDT [INFO   ][gwcreator]: Successfully Created new guest wireless network...
2020-05-08 17:11:58 PDT [INFO   ][gwcreator]: New WLAN ID: 020feb56-9a58-4e17-8732-5bace02474e7
```

Using the response from in the logs a secondary task to delete the newly created WLAN can easily be implemented.