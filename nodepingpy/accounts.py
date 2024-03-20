# -*- coding: utf-8 -*-

"""
Manage your account and subaccounts via the API, as referenced
in the NodePing documentation.

https://nodeping.com/docs-api-accounts.html
"""

from dataclasses import asdict, dataclass

from . import _utils
from ._utils import API_URL

ROUTE = "accounts"


@dataclass
class Account:
    """Account creation args.

    Args:
        name (str): Name for the subaccount
        contactname (str): name for the primary contact of the subaccount
        email (str): email address of the primary contact for the subaccount
        timezone (str): GMT offset for the subaccount ("-7", "+3", etc.)
        location (str): Default region for checks ('eur', 'nam', 'lam', 'eao', 'wlw')
        emailme (bool): True to opt-in the subaccount for service email notifications
        autodiagnotifications (bool): enable/disable account-wide emails for automated diagnostics
    """

    name: str
    contactname: str
    email: str
    timezone: str
    location: str
    emailme: bool
    autodiagnotifications: bool


@dataclass
class AccountUpdate:
    """Account update args.

    Args:
        name (str): Name for the subaccount
        timezone (str): GMT offset for the subaccount ("-7", "+3", etc.)
        location (str): Default region for checks ('eur', 'nam', 'lam', 'eao', 'wlw')
        emailme (bool): True to opt-in the subaccount for service email notifications
        status (str): "Active" or "Suspend", not supported for parent accounts
        autodiagnotifications (bool): enable/disable account-wide emails for automated diagnostics
    """

    name: str | None = None
    timezone: str | None = None
    location: str | None = None
    emailme: bool | None = None
    status: str | None = None
    autodiagnotifications: bool | None = None


def info(token: str, customerid: str | None = None) -> dict[str, str | int | bool]:
    """Returns the account information.

    Args:
        token (str): NodePing API token
        customerid (str): subaccount ID

    Returns:
        dict: Account information
    """
    data = _utils.add_custid({"token": token}, customerid)
    return _utils.get("{}/{}".format(API_URL, ROUTE), data)


def is_valid(token: str, customerid: str | None = None) -> bool:
    """Returns if you API key is valid or not.

    Args:
        token (str): NodePing API token
        customerid (str): subaccount ID

    Returns:
        bool: True if valid token, False if not
    """
    account_info = info(token, customerid)

    try:
        account_info["error"]
    except KeyError:
        return True
    else:
        return False


def create_subaccount(token: str, args: Account) -> dict[str, str | int | bool]:
    """Create a subaccount under your NodePing account.

    Args:
        token (str): NodePing API token
        args: (Account): Account class containing account information

    Returns:
        dict: Data returned from NodePing API
    """
    data = asdict(args)
    data["token"] = token

    return _utils.post("{}/{}".format(API_URL, ROUTE), data)


def update_account(
    token: str, args: AccountUpdate, customerid: str | None = None
) -> dict[str, str | int | bool]:
    """Update a NodePing account or subaccount.

    Args:
        token (str): NodePing API token
        args: (AccountUpdate): AccountUpdate class containing account information

    Returns:
        dict: Data returned from NodePing API
    """
    data = asdict(args)
    data["token"] = token
    put_data = _utils.add_custid(data, customerid)

    return _utils.put("{}/{}".format(API_URL, ROUTE), put_data)


def delete_subaccount(token: str, customerid: str):
    """Delete a NodePing subaccount.

    Args:
        token (str): NodePing API token
        customerid (str): subaccount ID

    Returns:
        dict: Confirmation of subaccount deletion success/failure
    """
    url = "{}/{}".format(API_URL, ROUTE)
    data = _utils.add_custid({"token": token}, customerid)

    return _utils.delete(url, data)


def disable_notifications(
    token: str, accountsupressall: bool, customerid: str | None = None
) -> dict[str, str | int | bool]:
    """Disable notifications on an account or subaccount.

    Args:
        token (str): NodePing API token
        accountsupressall (bool): True to disable notifcations, False to enable
        customerid (str): subaccount ID

    Returns:
        dict: Response from NodePing API
    """
    querystring = _utils.generate_querystring(
        {"accountsupressall": str(accountsupressall).lower()}
    )
    url = "{}/{}?{}".format(API_URL, ROUTE, querystring)
    data = _utils.add_custid({"token": token}, customerid)

    return _utils.put(url, data)
