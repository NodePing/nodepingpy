# -*- coding: utf-8 -*-

""" Manage scheduled or ad-hoc maintenance schedules.

Get, create, update, and delete maintenance schedules for your account.

https://nodeping.com/docs-api-maintenance.html
"""

from dataclasses import asdict
from .nptypes import maintenancetypes
from . import _utils
from ._utils import API_URL

ROUTE = "maintenance"

def get_all(token: str, customerid: str | None = None) -> dict:
    """Get information about all maintenances.

    """
    data = _utils.add_custid({"token": token}, customerid)

    return _utils.get("{}/{}".format(API_URL, ROUTE), data)


def get(token: str, maintenanceid: str, customerid: str | None = None) -> dict:
    """Get information about one maintenance.

    """
    url = "{}/{}/{}".format(API_URL, ROUTE, maintenanceid)
    data = _utils.add_custid({"token": token}, customerid)

    return _utils.get(url, data)


def create(token: str, args, customerid: str | None = None) -> dict:
    """Create an new ad-hoc or scheduled maintenance.

    """
    if isinstance(args, maintenancetypes.AdHoc):
        url = "{}/{}/ad-hoc".format(API_URL, ROUTE)
    elif isinstance(args, maintenancetypes.Scheduled):
        url = "{}/{}".format(API_URL, ROUTE)
    else:
        return {"error": "Invalid maintenance class"}

    data = asdict(args)
    data["token"] = token
    senddata = _utils.add_custid(data, customerid)

    return _utils.post(url, senddata)


def update(token: str, id : str, args, customerid: str | None = None) -> dict:
    """Update an existing ad-hoc or scheduled maintenance.

    """
    url = "{}/{}/{}".format(API_URL, ROUTE, id)

    data = asdict(args)
    data["token"] = token
    senddata = _utils.add_custid(data, customerid)

    return _utils.put(url, senddata)


def delete(token: str, maintenanceid: str, customerid: str | None = None) -> dict:
    """Delete one maintenance.

    """
    url = "{}/{}/{}".format(API_URL, ROUTE, maintenanceid)
    data = _utils.add_custid({"token": token}, customerid)

    return _utils.delete(url, data)



