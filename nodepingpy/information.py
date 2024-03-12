# -*- coding: utf-8 -*-

""" Get checks that were created on your NodePing account.

Allows you go get all checks, get passing, failing, by its ID,
disabled checks, and last results for a check.
"""

from . import _utils
from ._utils import API_URL


def get_all_probes(token: str) -> dict:
    """Get information on all NodePing probes


    The list of probes can be found at our FAQ:
    https://nodeping.com/faq.html

    Args:
        token (str): NodePing API token

    Returns:
        dict: Dictionary of NodePing probe information
    """
    url = "{}/info/probe".format(API_URL)

    return _utils.get(url, {"token": token})


def get_probe(token: str, location: str) -> dict:
    """Get information for a single NodePing probe

    The list of probes can be found at our FAQ:
    https://nodeping.com/faq.html

    Args:
        token (str): NodePing API token
        location (str): 2-letter abbreviation for the probe

    Returns:
        dict: Dictionary of single NodePing probe information
    """
    url = "{}/info/probe/{}".format(API_URL, location)

    return _utils.get(url, {"token": token})


def get_all_locations(token: str) -> dict:
    """Get information on all NodePing regions/locations


    The list of locations can be found at our FAQ:
    https://nodeping.com/faq.html

    Args:
        token (str): NodePing API token

    Returns:
        dict: Dictionary of NodePing location information
    """
    url = "{}/info/location".format(API_URL)

    return _utils.get(url, {"token": token})


def get_location(token: str, location: str) -> dict:
    """Get information for a single NodePing region/location

    The list of locations can be found at our FAQ:
    https://nodeping.com/faq.html

    Args:
        token (str): NodePing API token
        location (str): 3-letter abbreviation for the location

    Returns:
        dict: Dictionary of single NodePing location information
    """
    url = "{}/info/location/{}".format(API_URL, location)

    return _utils.get(url, {"token": token})
