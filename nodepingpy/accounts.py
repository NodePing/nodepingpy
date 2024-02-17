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
    name: str
    contactname: str
    email: str
    timezone: str
    location: str
    emailme: bool
    autodiagnotifications: bool


@dataclass
class AccountUpdate:
    customerid: str
    name: str
    timezone: str
    location: str
    emailme: bool
    status: str
    autodiagnotifications: bool


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


def populate_account(token: str, customerid: str) -> AccountUpdate:
    """Get account information and add it to an AccountUpdate class.

    Args:
        token (str): NodePing API token
        customerid (str): subaccount ID

    Returns:
        AccountUpdate: Populated with account information for easy modification
    """
    account_info = info(token, customerid)
    name = account_info["customer_name"]
    timezone = account_info["timezone"]
    location = account_info["defaultlocations"][0]
    emailme = account_info["emailme"]
    status = account_info["status"]
    autodiagnotifications = account_info["autodiagnotifications"]

    return AccountUpdate(
        customerid, name, timezone, location, emailme, status, autodiagnotifications
    )


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
    post_data = _utils.add_custid(data, customerid)

    return _utils.put("{}/{}".format(API_URL, ROUTE), post_data)


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
