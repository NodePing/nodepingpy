# -*- coding: utf-8 -*-

"""
Manage notification profiles for NodePing Account.

https://nodeping.com/docs-api-notificationprofiles.html
"""

from . import _utils
from ._utils import API_URL

ROUTE = "notificationprofiles"


def get_all(token: str, customerid: str | None = None) -> dict:
    """Get all notification profiles on the account.

    https://nodeping.com/docs-api-notificationprofiles.html#get

    Args:
        token (str): NodePing API token
        customerid (str): subaccount ID

    Returns:
        dict: All notification profiles.
    """
    data = _utils.add_custid({"token": token}, customerid)
    url = "{}/{}".format(API_URL, ROUTE)

    return _utils.get(url, data)


def get(token: str, id: str, customerid: str | None = None) -> dict:
    """Get one notification profile on the account.

    https://nodeping.com/docs-api-notificationprofiles.html#get

    Args:
        token (str): NodePing API token
        id (str): The notification profile ID
        customerid (str): subaccount ID

    Returns:
        dict: Get the specified notification profile.
    """
    data = _utils.add_custid({"token": token, "id": id}, customerid)
    url = "{}/{}".format(API_URL, ROUTE)

    return _utils.get(url, data)


def create(
    token: str,
    name: str,
    notifications: list[dict[str, str | int]],
    customerid: str | None = None,
) -> dict:
    """Create a notification profile.

    https://nodeping.com/docs-api-notificationprofiles.html#post-put

    Args:
        token (str): NodePing API token
        name (str): Name of the notification profile.
        notifications (list): List of NodePing contacts and the notification schedules
        customerid (str): subaccount ID

    notifications argument example:
    [
        {"contactkey1":
            {"delay":0,
                "schedule":"schedule1"
            }
        },
        {"contactkey2":
            {"delay":5,
                "schedule":"schedule2"
            }
        }
    ]

    Returns:
        dict: New notification profile information.
    """
    data = _utils.add_custid(
        {"token": token, "name": name, "notifications": notifications}, customerid
    )
    url = "{}/{}".format(API_URL, ROUTE)

    return _utils.post(url, data)


def update(
    token: str,
    id: str,
    name: str,
    notifications: list[dict[str, str | int]],
    customerid: str | None = None,
) -> dict:
    """Update a notification profile.

    https://nodeping.com/docs-api-notificationprofiles.html#post-put

    Args:
        token (str): NodePing API token
        id (str): The notification profile ID
        name (str): Name of the notification profile.
        notifications (list): List of NodePing contacts and the notification schedules
        customerid (str): subaccount ID

    notifications argument example:
    [
        {"contactkey1":
            {"delay":0,
                "schedule":"schedule1"
            }
        },
        {"contactkey2":
            {"delay":5,
                "schedule":"schedule2"
            }
        }
    ]

    Returns:
        dict: Updated notification profile.
    """
    data = _utils.add_custid(
            {"token": token, "name": name, "notifications": notifications, "id": id}, customerid
    )
    url = "{}/{}".format(API_URL, ROUTE)

    return _utils.put(url, data)


def delete(token: str, id: str, customerid: str | None = None) -> dict:
    """Delete one notification profile on the account.

    https://nodeping.com/docs-api-notificationprofiles.html#get

    Args:
        token (str): NodePing API token
        id (str): The notification profile ID
        customerid (str): subaccount ID

    Returns:
        dict: Confirmation whether the deletion was successful or not.
    """
    data = _utils.add_custid({"token": token, "id": id}, customerid)
    url = "{}/{}".format(API_URL, ROUTE)

    return _utils.delete(url, data)


