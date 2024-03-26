# -*- coding: utf-8 -*-

"""Get notifications for checks on your NodePing account.

https://nodeping.com/docs-api-notifications.html
"""


from dataclasses import dataclass, asdict
from . import _utils
from ._utils import API_URL

ROUTE = "notifications"


@dataclass
class Notification:
    """
    Args:
        id (str): Check id of the check for which you want to list notifications.
        span (int): number of hours of notifications to retrieve.
        limit (int): default 300, max 43201 - number of records to retrieve.
        subaccounts (bool): if set, notifications sent to subaccounts will also be included.
    """
    id: str | None = None
    span: int | None = None
    limit: int | None = 300
    subaccounts: bool = False


def get(token: str, args: dict, customerid: str | None = None) -> dict:
    """Get notifications on your NodePing account.

    Get notifications according to a maximum limit (limit caps at 43201),
    or over a certain amount of hours, and whether or not to include
    subaccounts or not when fetching notifications.

    https://nodeping.com/docs-api-notifications.html

    Args:
        token (str): NodePing API token
        args (dict): Notifications class in this module.
        customerid (str): subaccount ID
    """
    data = asdict(args)
    data["token"] = token
    data["customerid"] = customerid

    if customerid:
        url = "{}/{}/{}".format(API_URL, ROUTE, customerid)
    else:
        url = "{}/{}".format(API_URL, ROUTE)

    return _utils.get(url, data)
