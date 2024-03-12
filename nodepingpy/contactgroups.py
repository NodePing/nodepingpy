# -*- coding: utf-8 -*-

""" Manage contact group information."""

from . import _utils
from ._utils import API_URL

ROUTE = "contactgroups"


def get_all(token: str, customerid : str | None = None) -> dict:
    """Get all contact groups on the account or subaccount.

    https://nodeping.com/docs-api-contactgroups.html#get

    Args:
        token (str): NodePing API token
        customerid (str | None): subaccount ID

    Returns:
        dict: All contact groups on the account or subaccount.
    """
    url = "{}/{}".format(API_URL, ROUTE)
    data = _utils.add_custid({"token": token}, customerid)

    return _utils.get(url, data)


def get(token: str, id, customerid : str | None = None) -> dict:
    """Get a contact group on the account or subaccount.

    https://nodeping.com/docs-api-contactgroups.html#get

    Args:
        token (str): NodePing API token
        id (str): The ID for the contact group
        customerid (str | None): subaccount ID

    Returns:
        dict: Information for the contact groups ID.
    """
    url = "{}/{}/{}".format(API_URL, ROUTE, id)
    data = _utils.add_custid({"token": token}, customerid)

    return _utils.get(url, data)


def create(token: str, name: str, members: list[str], customerid: str | None = None) -> dict:
    """Create a new contact group.

    https://nodeping.com/docs-api-contactgroups.html#post-put

    Args:
        token (str): NodePing API token
        name (str): Name for the contact group
        members (list): A list of contact IDs
        customerid (str | None): subaccount ID

    Returns:
        dict: Information about the newly created contact group.
    """
    url = "{}/{}".format(API_URL, ROUTE)
    data = _utils.add_custid({"token": token, "name": name, "members": members}, customerid)

    return _utils.post(url, data)


def update(token: str, id: str, args: dict, customerid: str | None = None) -> dict:
    """Update an existing contact group.

    https://nodeping.com/docs-api-contactgroups.html#post-put

    Args:
        token (str): NodePing API token
        name (str): Name for the contact group
        args (dict): `name` (str) or `members` (list)
        customerid (str | None): subaccount ID

    Returns:
        dict: Information about the updated contact group.
    """
    url = "{}/{}/{}".format(API_URL, ROUTE, id)
    args["token"] = token
    args = _utils.add_custid(args, customerid)

    return _utils.put(url, args)


def delete(token: str, id, customerid : str | None = None) -> dict:
    """Delete an existing contact group.

    https://nodeping.com/docs-api-contactgroups.html#delete

    Args:
        token (str): NodePing API token
        id (str): The ID for the contact group
        customerid (str | None): subaccount ID

    Returns:
        dict: success or failure message for deleting the contact group.
    """
    url = "{}/{}/{}".format(API_URL, ROUTE, id)
    data = _utils.add_custid({"token": token}, customerid)

    return _utils.delete(url, data)

