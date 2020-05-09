import argparse
from .validators import *


def parse_cli() -> dict:
    """
    Parses the CLI arguments and returns a dictionary containing the data.

    :return dict: Dictionary containing the CLI arguments
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--token',
                        type=validate_token,
                        default="X" * 96,
                        help="Mist API token")
    parser.add_argument('--site_id',
                        type=validate_site_id,
                        required=False,
                        default="S" * 36,
                        help="Mist site ID")
    parser.add_argument('--ssid',
                        type=str,
                        required=True,
                        help="The wireless network name")
    parser.add_argument('--url',
                        type=str,
                        required=True,
                        metavar="URL",
                        dest="forward_url",
                        help="URL guests will be forwarded to after successful authentication")
    parser.add_argument('--emails',
                        action='append',
                        type=str,
                        required=True,
                        metavar="DOMAIN",
                        dest="sponsor_email_domains",
                        help="Valid domains for guest sponsor emails, for multiple domains repeat this argument")
    parser.add_argument('--expire',
                        type=int,
                        default=86400,
                        metavar="SECONDS",
                        help="Length of time guest accounts remain authorized in seconds (default: 86400)")
    arguments = vars(parser.parse_args())
    return arguments
