# -*- coding: utf-8 -*-

""" Helper functions to reduce code reuse and misc other uses
"""

from typing import Any
from nodepingpy.nptypes.contacttypes import *

from time import time
from urllib.parse import urlencode
from urllib.error import HTTPError as httperror
from urllib.request import Request, urlopen

import json


API_URL = "https://api.nodeping.com/api/1"


def add_custid(
    data: dict[str, str | int | bool], customerid: str | None = None
) -> dict:
    """If the customerid isn't None, add it to data

    Args:
        data (dict): data dictionary
        customerid (str): NodePing customerid/subaccount id

    Returns:
        dict: data with customerid included if it isn't None
    """
    if customerid:
        data["customerid"] = customerid

    return data


def generate_querystring(args: dict) -> str:
    """Generates a querystring from a dict.

    Removes all `None` values and escaples invalid strings.

    Args:
        args (dict): key/value for querystring keys and values

    Returns:
        str: escaped querystring
    """

    return urlencode({k: v for k, v in args.items() if v != None})


def create_timestamp(duration):
    return int(time() * 1000) + (duration * 1000)


def get(url: str, data_dict: dict[str, str | int | bool | None]) -> dict:
    """Queries the URL with a GET request with JSON body.

    Does an HTTP GET request and returns an expected JSON payload
    as a Python dictionary.

    Args:
        url (str): URL for the GET request
        data_dict (dict): Dictionary to be submitted as the body

    Returns:
        dict: Data that was returned from NodePing from GET request
    """

    json_data = json.dumps(strip_none_values(data_dict)).encode("utf-8")

    req = Request(url)
    req.get_method = lambda: "GET"
    req.add_header("Content-Type", "application/json; charset=utf-8")
    req.add_header("Content-Length", str(len(json_data)))

    try:
        data = urlopen(req, json_data)
    except httperror as err:
        data = err

    json_bytes = data.read()

    return json.loads(json_bytes.decode("utf-8"))


def post(url: str, data_dict: dict[str, str | int | bool | None]) -> dict:
    """Queries the NodePing API via POST and creates a check

    Accepts a URL and data and POSTs the results to NodePing
    which then creates the check on the account with the user
    specified parameters

    Args:
        url (str): The URL to submit POST to
        data_dict (dict): Dictionary of data that is sent to NodePing

    Returns:
        dict: Response from API
    """

    json_data = json.dumps(strip_none_values(data_dict)).encode("utf-8")

    req = Request(url)
    req.add_header("Content-Type", "application/json; charset=utf-8")
    req.add_header("Content-Length", str(len(json_data)))

    try:
        data = urlopen(req, json_data)
    except httperror as err:
        data = err

    json_bytes = data.read()

    return json.loads(json_bytes.decode("utf-8"))


def put(url: str, data_dict: dict[str, str | int | bool | None]) -> dict:
    """Queries the NodePing API with a PUT request.

    Accepts a URL and data and PUTs the results to NodePing. The
    URL must have a checkid in the URL that will be updated. This
    updates the specified fields in the check.

    Args:
        url (str): The URL to submit POST to
        data_dict (dict): Dictionary of data that is sent to NodePing

    Returns:
        dict: Response from API
    """

    json_data = json.dumps(strip_none_values(data_dict)).encode("utf-8")

    req = Request(url)
    req.get_method = lambda: "PUT"
    req.add_header("Content-Type", "application/json; charset=utf-8")
    req.add_header("Content-Length", str(len(json_data)))

    try:
        data = urlopen(req, json_data)
    except httperror as err:
        data = err

    json_bytes = data.read()

    return json.loads(json_bytes.decode("utf-8"))


def delete(url: str, data_dict: dict[str, str | int | bool]) -> dict[str, Any]:
    """Queries the NodePing API via DELETE and returns its result

    Accepts a URL to the NodePing API to do a delete. A dictionary
    will be returned with "ok" == true meaning it was deleted, if
    false then the check wasn't deleted or an invalid ID was given

    Args:
        url (str): The URL to submit POST to
        data_dict (dict): Dictionary of data that is sent to NodePing

    Returns:
        dict: Response from API
    """

    json_data = json.dumps(strip_none_values(data_dict)).encode("utf-8")

    req = Request(url)
    req.get_method = lambda: "DELETE"
    req.add_header("Content-Type", "application/json; charset=utf-8")
    req.add_header("Content-Length", str(len(json_data)))

    try:
        data = urlopen(req, json_data)
    except httperror as err:
        data = err

    json_bytes = data.read()

    return json.loads(json_bytes.decode("utf-8"))


def strip_none_values(data: dict) -> dict:
    """Remove any keys with a value of None."""
    return {k: v for k, v in data.items() if bool(v) or isinstance(v, bool)}
