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

    https://nodeping.com/docs-api-maintenance.html#get

    Args:
        token (str): NodePing API token
        customerid (str): subaccount ID

    Returns:
        dict: All maintenance information
    """
    data = _utils.add_custid({"token": token}, customerid)

    return _utils.get("{}/{}".format(API_URL, ROUTE), data)


def get(token: str, maintenanceid: str, customerid: str | None = None) -> dict:
    """Get information about one maintenance.

    https://nodeping.com/docs-api-maintenance.html#get

    Args:
        token (str): NodePing API token
        maintenanceid (str): Maintenance ID
        customerid (str): subaccount ID

    Returns:
        dict: Maintenance ID's maintenance information
    """
    url = "{}/{}/{}".format(API_URL, ROUTE, maintenanceid)
    data = _utils.add_custid({"token": token}, customerid)

    return _utils.get(url, data)


def create(token: str, args, customerid: str | None = None) -> dict:
    """Create an new ad-hoc or scheduled maintenance.

    https://nodeping.com/docs-api-maintenance.html#post

    Args:
        token (str): NodePing API token
        args (dataclass): maintenancetypes.AdHocCreate or maintenancetypes.ScheduledCreate
        customerid (str): subaccount ID

    Returns:
        dict: Created maintenance's information
    """
    if isinstance(args, maintenancetypes.AdHocCreate):
        url = "{}/{}/ad-hoc".format(API_URL, ROUTE)
    elif isinstance(args, maintenancetypes.ScheduledCreate):
        url = "{}/{}".format(API_URL, ROUTE)
    else:
        return {"error": "Invalid maintenance class"}

    data = asdict(args)
    data["token"] = token
    senddata = _utils.add_custid(data, customerid)

    return _utils.post(url, senddata)


def update(token: str, id: str, args, customerid: str | None = None) -> dict:
    """Update an existing ad-hoc or scheduled maintenance.

    https://nodeping.com/docs-api-maintenance.html#put

    Args:
        token (str): NodePing API token
        id (str): Maintenance ID
        args (dataclass): maintenancetypes.AdHocUpdate or maintenancetypes.ScheduledUpdate
        customerid (str): subaccount ID

    Returns:
        dict: Updated maintenance's information
    """
    url = "{}/{}/{}".format(API_URL, ROUTE, id)

    data = asdict(args)
    data["token"] = token
    senddata = _utils.add_custid(data, customerid)

    return _utils.put(url, senddata)


def delete(token: str, maintenanceid: str, customerid: str | None = None) -> dict:
    """Delete one maintenance.

    https://nodeping.com/docs-api-maintenance.html#delete

    Args:
        token (str): NodePing API token
        maintenanceid (str): Maintenance ID
        customerid (str): subaccount ID

    Returns:
        dict: Confirmation of maintenance successfully being deleted or not.
    """
    url = "{}/{}/{}".format(API_URL, ROUTE, maintenanceid)
    data = _utils.add_custid({"token": token}, customerid)

    return _utils.delete(url, data)
