import requests
import json
from .logger import log


def create_wlan(ssid: str, expire: int, forward_url: str, sponsor_email_domains: [str], site_id: str, token: str) -> dict:
    """
    Creates a sponsored guest wireless network at a specified Mist site.

    :param str ssid: The name of the wireless network to be created.
    :param int expire: Guest account expiration in seconds.
    :param str forward_url: URL that authorized guests will be forwarded to after authentication succeeds.
    :param [str] sponsor_email_domains: Valid sponsor email address domains.
    :param str site_id: The unique site ID where the wireless network will be created.
    :param str token: Mist API token with network admin or super user rights.

    :return dict: A dictionary containing the JSON response from the Mist API.
    """
    url = f"https://api.mist.com/api/v1/sites/{site_id}/wlans"
    headers = {
        "Content-type": "application/json",
        "Authorization": f"Token {token}"
    }
    wlan = {
        "ssid": ssid,
        "enabled": True,
        "portal": {
            "enabled": True,
            "auth": "sponsor",
            "expire": expire,
            "forward": True,
            "forward_url": forward_url,
            "sponsor_enabled": True,
            "sponsor_email_domains": sponsor_email_domains,
            "sponsor_link_validity_duration": "60",
        }
    }
    res = requests.post(url=url, data=json.dumps(wlan), headers=headers)
    data = res.json()
    if res.status_code == 200:
        log.info(f"New sponsored guest wireless network '{ssid}' created!")
        return data
    else:
        log.error("Failed to create new sponsored guest wireless network!")
        log.error(f"Response: {res.content}")
        raise requests.exceptions.HTTPError(f"Failed with code: {res.status_code}, Response: {res.content}")
