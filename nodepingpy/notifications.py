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
    id: str | None = None
    span: int | None = None
    limit: int | None = 300
    subaccounts: bool = False


def get(token: str, args: dict, customerid: str | None = None) -> dict:
    """ """
    data = asdict(args)
    data["token"] = token

    if customerid:
        url = "{}/{}/{}".format(API_URL, ROUTE, customerid)
    else:
        url = "{}/{}".format(API_URL, ROUTE)

    return _utils.get(url, data)
