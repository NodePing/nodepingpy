# -*- coding: utf-8 -*-

""" Get checks that were created on your NodePing account.

Allows you go get all checks, get passing, failing, by its ID,
disabled checks, and last results for a check.
"""

from dataclasses import asdict

from . import _utils
from ._utils import API_URL


ROUTE = "checks"


def get_all(token: str, customerid: str|None) -> dict[str, str|int|bool]:
    """Get all checks that exist for the account or subaccount.

    Args:
        token (str): NodePing API token
        customerid (str): subaccount ID

    Returns:
        dict: All checks on NodePing account or subaccount.
    """
    url = "{}/{}".format(API_URL, ROUTE)
    data = _utils.add_custid({"token": token}, customerid)

    return _utils.get(url, data)


def get_all_uptime(token: str, customerid: str|None) -> dict[str, str|int|bool]:
    """Get the uptime for all checks on the account or subaccount.

    Args:
        token (str): NodePing API token
        customerid (str): subaccount ID

    Returns:
        dict: All checks on NodePing account or subaccount.
    """
    url = "{}/{}".format(API_URL, ROUTE)
    data = _utils.add_custid({"token": token, "uptime": True}, customerid)

    return _utils.get(url, data)


def get_many(
    token: str,
    checkids: list[str],
    customerid: str|None,
    current: str|None,
) -> dict[str, str|int|bool]:
    """Get information for all specified checks.

    Args:
        token (str): NodePing API token
        checkids (list): List of NodePing check IDs
        customerid (str): subaccount ID
        current (bool): checks current events

    Additional information about `current` argument:
    https://nodeping.com/docs-api-checks.html

    Returns:
        dict: All specified checks on NodePing account or subaccount.
    """
    url = "{}/{}?{}".format(
        API_URL, ROUTE, _utils.generate_querystring({"id": ",".join(checkids)})
    )
    data = _utils.add_custid({"token": token, "current": current}, customerid)

    return _utils.get(url, data)


def get_passing(token: str, customerid: str|None) -> dict[str, str|int|bool]:
    """Get active passing NodePing checks.

     Args:
        token (str): NodePing API token
        checkids (list): List of NodePing check IDs
        customerid (str): subaccount ID

    Returns:
        dict: All passing checks on NodePing account or subaccount.
    """

    return _parse_pass_fail(get_all(token, customerid), 1)


def get_failing(token: str, customerid: str|None) -> dict[str, str|int|bool]:
    """Get active failing NodePing checks.

     Args:
        token (str): NodePing API token
        checkids (list): List of NodePing check IDs
        customerid (str): subaccount ID

    Returns:
        dict: All failing checks on NodePing account or subaccount.
    """

    return _parse_pass_fail(get_all(token, customerid), 0)


def get_uptime_passing(token: str, customerid: str|None) -> dict[str, str|int|bool]:
    """Get the uptime for passing and active checks on the account or subaccount.

    Args:
        token (str): NodePing API token
        customerid (str): subaccount ID

    Returns:
        dict: All passing checks and their uptime on NodePing account or subaccount.
    """
    url = "{}/{}".format(API_URL, ROUTE)
    data = _utils.add_custid({"token": token, "uptime": True}, customerid)

    return _parse_pass_fail(_utils.get(url, data), 1)


def get_uptime_failing(token: str, customerid: str|None) -> dict[str, str|int|bool]:
    """Get the uptime for failing and active checks on the account or subaccount.

    Args:
        token (str): NodePing API token
        customerid (str): subaccount ID

    Returns:
        dict: All failing checks and their uptime on NodePing account or subaccount.
    """
    url = "{}/{}".format(API_URL, ROUTE)
    data = _utils.add_custid({"token": token, "uptime": True}, customerid)

    return _parse_pass_fail(_utils.get(url, data), 0)


def get_by_id(
    token: str, checkid: str, customerid: str|None
) -> dict[str, str|int|bool]:
    """Get a single NodePing check by ID.

    Args:
        token (str): NodePing API token
        checkid (str): Check ID
        customerid (str): subaccount ID

    Returns:
        dict: Contents of a single check by check ID
    """
    url = "{}/{}/{}".format(API_URL, ROUTE, checkid)
    data = _utils.add_custid({"token": token}, customerid)

    return _utils.get(url, data)


def get_active(token: str, customerid: str|None) -> dict[str, str|int|bool]:
    """Get active (enabled) checks on the NodePing account or subaccount.

    Args:
        token (str): NodePing API token
        customerid (str): subaccount ID

    Returns:
        dict: All enabled checks.
    """

    checks = get_all(token, customerid)

    return {k: v for k, v in checks.items() if v["enable"] == "active"}


def get_inactive(token: str, customerid: str|None) -> dict[str, str|int|bool]:
    """Get inactive (disabled) checks on the NodePing account or subaccount.

    Args:
        token (str): NodePing API token
        customerid (str): subaccount ID

    Returns:
        dict: All disabled checks.
    """

    checks = get_all(token, customerid)

    return {k: v for k, v in checks.items() if v["enable"] == "inactive"}


def get_last_result(
    token: str, checkid: str, customerid: str|None
) -> dict[str, str|int|bool]:
    """Get the last result for the specified check.

    Args:
        token (str): NodePing API token
        checkid (str): Check ID
        customerid (str): subaccount ID

    Returns:
        dict: check information with lastresult in the response
    """
    querystring = _utils.generate_querystring({"uptime": "true"})
    url = "{}/{}/{}?{}".format(API_URL, ROUTE, checkid, querystring)
    data = _utils.add_custid({"token": token}, customerid)

    return _utils.get(url, data)


def create_check(token: str, args, customerid: str|None = None) -> dict[str,str|int|bool]:
    """Create a NodePing check with parameters from specific dataclass check type.

    Args:
        token (str): NodePing API token
        args (ClassVar): a dataclass such as AgentCheck, HttpCheck, PingCheck, etc.
        customerid (str): subaccount ID

    Returns:
        dict: Contents of successfully created check or error message
    """
    url = "{}/{}".format(API_URL, ROUTE)
    data = asdict(args)
    data["token"] = token
    data = _utils.add_custid(data, customerid)

    return _utils.post(url, data)


def _parse_pass_fail(checks: dict[str, str|int|bool], pass_or_fail: int) -> dict[str, str|int|bool]:
    """Get all passing or failing active checks in NodePing result.

    Args:
        pass_or_fail (int): 1 for passing, 0 for failing

    Returns:
        dict: Dictionary of all passing or failing checks
    """
    result = {}

    for checkid, contents in checks.items():
        try:
            state = contents["state"]

            if contents["enable"] == "active" and state == pass_or_fail:
                result.update({checkid: contents})
        except KeyError:
            continue

    return result
