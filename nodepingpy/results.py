# -*- coding: utf-8 -*-

from dataclasses import asdict
from . import _utils
from .nptypes import resulttypes
from ._utils import API_URL


def get(token: str, id: str, args, customerid: str | None = None) -> dict:
    """ 
    https://nodeping.com/docs-api-results.html#get

    Args:
        token (str): NodePing API token
        id (str): ID of the check for which you are retrieving events
        args (dict): nptypes.resulttypes dataclass for Results, Uptime, or Events
        customerid (str | None): subaccount ID

    Returns:
        dict: API return data
    """
    data = asdict(args)
    data["token"] = token
    senddata = _utils.add_custid(data, customerid)

    if isinstance(args, resulttypes.Results):
        route = "results"
    elif isinstance(args, resulttypes.Uptime):
        route = "results/uptime"
    elif isinstance(args, resulttypes.Events):
        route = "results/events"
    else:
        return {"error": "args not a valid data type"}

    return _utils.get("{}/{}/{}".format(API_URL, route, id), senddata)


def get_current(token: str, customerid: str | None = None) -> dict:
    """ 
    https://nodeping.com/docs-api-results.html#uptime

    Args:
        token (str): NodePing API token
        customerid (str | None): subaccount ID

    Returns:
        dict: Current events for checks
    """
    route = "results/current"
    data = _utils.add_custid({"token": token}, customerid)

    return _utils.get("{}/{}".format(API_URL, route), data)


def get_summary(token: str, id: str, customerid: str | None = None) -> dict:
    """ 
    https://nodeping.com/docs-api-results.html#events

    Args:
        token (str): NodePing API token
        customerid (str | None): subaccount ID

    Returns:
        dict: Hourly summary information about the results for a check
    """
    route = "results/summary"
    data = _utils.add_custid({"token": token}, customerid)

    return _utils.get("{}/{}/{}".format(API_URL, route, id), data)
