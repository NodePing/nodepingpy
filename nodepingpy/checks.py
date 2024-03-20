# -*- coding: utf-8 -*-

""" Get checks that were created on your NodePing account.

Allows you go get all checks, get passing, failing, by its ID,
disabled checks, and last results for a check.
"""

from dataclasses import asdict

from .nptypes import checktypes
from . import _utils
from ._utils import API_URL


ROUTE = "checks"


def get_all(
    token: str, customerid: str | None = None
) -> dict[str, checktypes.GetCheck]:
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


def get_all_uptime(
    token: str, customerid: str | None = None
) -> dict[str, checktypes.GetCheckUptime]:
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
    customerid: str | None = None,
    current: str | None = None,
) -> dict[str, checktypes.GetCheck]:
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
    data = _utils.add_custid({"token": token}, customerid)

    if current:
        data["current"] = current

    return _utils.get(url, data)


def get_passing(
    token: str, customerid: str | None = None
) -> dict[str, checktypes.GetCheck]:
    """Get active passing NodePing checks.

     Args:
        token (str): NodePing API token
        checkids (list): List of NodePing check IDs
        customerid (str): subaccount ID

    Returns:
        dict: All passing checks on NodePing account or subaccount.
    """

    return _parse_pass_fail(get_all(token, customerid), 1)


def get_failing(
    token: str, customerid: str | None = None
) -> dict[str, checktypes.GetCheck]:
    """Get active failing NodePing checks.

     Args:
        token (str): NodePing API token
        checkids (list): List of NodePing check IDs
        customerid (str): subaccount ID

    Returns:
        dict: All failing checks on NodePing account or subaccount.
    """

    return _parse_pass_fail(get_all(token, customerid), 0)


def get_uptime(
    token: str,
    checks: str | list,
    customerid: str | None = None,
    start: str | None = None,
) -> dict[str, checktypes.GetCheckUptime]:
    """Get the uptime for passing and active checks on the account or subaccount.

    Args:
        token (str): NodePing API token
        checks (str|list): "all" for all checks or a list of checks to get
        customerid (str): subaccount ID
        start (str): an optional %Y-%m-%d timestamp of when to start getting uptime results

    Returns:
        dict: All passing checks and their uptime on NodePing account or subaccount.
    """
    if isinstance(checks, str) and checks.upper() == "ALL":
        url = "{}/{}".format(API_URL, ROUTE)
    else:
        url = "{}/{}?{}".format(
            API_URL, ROUTE, _utils.generate_querystring({"id": ",".join(checks)})
        )

    data = {"token": token, "uptime": True, "start": start}
    senddata = _utils.add_custid(data, customerid)

    return _utils.get(url, senddata)


def get_by_id(
    token: str, checkid: str, customerid: str | None = None
) -> checktypes.GetCheck:
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


def get_active(
    token: str, customerid: str | None = None
) -> dict[str, checktypes.GetCheck]:
    """Get active (enabled) checks on the NodePing account or subaccount.

    Args:
        token (str): NodePing API token
        customerid (str): subaccount ID

    Returns:
        dict: All enabled checks.
    """

    checks = get_all(token, customerid)

    return {k: v for k, v in checks.items() if v["enable"] == "active"}


def get_inactive(
    token: str, customerid: str | None = None
) -> dict[str, checktypes.GetCheck]:
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
    token: str, checkid: str, customerid: str | None = None
) -> checktypes.GetCheckUptime:
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


def create_check(
    token: str, args, customerid: str | None = None
) -> checktypes.ModifiedCheck:
    """Create a NodePing check with parameters from specific dataclass check type.

    Args:
        token (str): NodePing API token
        args: a dataclass such as AgentCheck, HttpCheck, PingCheck, etc.
        customerid (str): subaccount ID

    Returns:
        dict: Contents of successfully created check or error message
    """
    url = "{}/{}".format(API_URL, ROUTE)
    data = asdict(args)
    data.update({"token": token, "customerid": customerid})

    return _utils.post(url, data)


def update_check(
    token: str,
    checkid: str,
    checktype: str,
    args: dict[str, str | int | bool | None],
    customerid: str | None = None,
) -> checktypes.ModifiedCheck:
    """Update an existing check on your NodePing account

    Args:
        token (str): NodePing API token
        checkid (str): The check ID that is being updated
        checktype (str): HTTP, PING, MTR, DNS, etc. check type
        args (dict): fields being updated with their new values
        customerid (str|None): subaccount ID

    Returns:
        dict: Contents of check ID with updated fields or error message
    """
    url = "{}/{}/{}".format(API_URL, ROUTE, checkid)
    args.update({"type": checktype.upper(), "token": token, "customerid": customerid})

    return _utils.put(url, args)


def delete_check(
    token: str, checkid: str, customerid: str | None = None
) -> dict[str, str | bool]:
    """ """
    url = "{}/{}/{}".format(API_URL, ROUTE, checkid)
    senddata = _utils.add_custid({"token": token}, customerid)

    return _utils.delete(url, senddata)


def mute_check(
    token: str, checkid: str, duration: int | bool, customerid: str | None = None
) -> checktypes.ModifiedCheck:
    """Mute a NodePing check by check ID.

    Args:
        token (str): NodePing API token
        checkid (str): The check ID that is being updated
        duration (int|bool): True to mute infinitely, False to unmute, or a millisecond epoch timestamp in the future to specify when the check will be unmuted
        customerid (str|None): subaccount ID

    Returns:
        dict: check info
    """
    url = "{}/{}/{}".format(API_URL, ROUTE, checkid)
    senddata = _utils.add_custid({"token": token, "mute": duration}, customerid)

    return _utils.put(url, senddata)


def disable_by(
    token: str,
    disabletype: str,
    string: str,
    disable: bool,
    customerid: str | None = None,
) -> dict[str, int]:
    """Find matching checks and disable it/them.

    This will not re-enable checks that were previously disabled
    using the 'enabled' element.

    Returned data:
        `disableall` - number of checks disabled after command
        `disabled` - number of checks currently disabled
        `enabled` - number of checks currently enabled

    Args:
        token (str): NodePing API token
        disabletype (str): "type", "label", or "target"
            * type: regex that matches against the 'type' field of checks
            * label: regex that matches against the 'label' field of checks
            * target: regex that matches against the 'target' field of checks
        string (str): the regex string to match the type, label, or target
        disable (bool): re-enable check (False) or disable the check (True)
        customerid (str|None): subaccount ID

    Returns:
        dict: check information {'disableall': x, 'disabled': y, 'enabled': z}
    """
    querystring = _utils.generate_querystring(
        {disabletype: string, "disableall": disable}
    )
    url = "{}/{}?{}".format(API_URL, ROUTE, querystring)
    data = _utils.add_custid({"token": token}, customerid)

    return _utils.put(url, data)


def disable_all(
    token: str, disable: bool, customerid: str | None = None
) -> dict[str, int]:
    """Disable all checks on the account.

    This will not re-enable checks that were previously disabled
    using the 'enabled' element

    Returned data:
        `disableall` - number of checks disabled after command
        `disabled` - number of checks currently disabled
        `enabled` - number of checks currently enabled

    Args:
        token (str): NodePing API token
        disable (bool): re-enable check (False) or disable the check (True)
        customerid (str|None): subaccount ID

    Returns:
        dict: check information {'disableall': x, 'disabled': y, 'enabled': z}
    """
    querystring = _utils.generate_querystring({"disableall": disable})
    url = "{}/{}?{}".format(API_URL, ROUTE, querystring)
    data = _utils.add_custid({"token": token}, customerid)

    return _utils.put(url, data)


def _parse_pass_fail(
    checks: dict[str, checktypes.GetCheck | checktypes.GetCheckUptime],
    pass_or_fail: int,
) -> dict:
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
