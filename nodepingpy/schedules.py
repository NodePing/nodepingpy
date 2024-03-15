# -*- coding: utf-8 -*-

"""
Get, create, update, and delete schedules for notifications.
"""

from . import _utils
from ._utils import API_URL

ROUTE = "schedules"


def get_all(token, customerid: str | None = None) -> dict:
    """ """
    data = _utils.add_custid({"token": token}, customerid)

    return _utils.get("{}/{}".format(API_URL, ROUTE), data)


def get(token: str, schedule: str, customerid: str | None = None) -> dict:
    """ """
    data = _utils.add_custid({"token": token}, customerid)

    return _utils.get("{}/{}/{}".format(API_URL, ROUTE, schedule), data)


def create(
    token: str, name: str, schedule: dict, customerid: str | None = None
) -> dict:
    """Create a new notification schedule for the specified NodePing account.

    Args:
        token (str): NodePing API token
        name (str): The name of the schedule
        schedule (dict): The schedules for each day for receiving notifications
        customerid (str | None): subaccount ID

    Returns:
        dict: Entry for newly created schedule

    Example:

    {'data': {'friday': {'disabled': True},
              'monday': {'allday': True},
              'saturday': {'exclude': False, 'time1': '6:00', 'time2': '18:00'},
              'sunday': {'exclude': False, 'time1': '6:00', 'time2': '18:00'},
              'thursday': {'exclude': False, 'time1': '6:00', 'time2': '18:00'},
              'tuesday': {'exclude': False, 'time1': '6:00', 'time2': '18:00'},
              'wednesday': {'exclude': False, 'time1': '6:00', 'time2': '18:00'}}}

    Days accept certain variables certain key/value pairs such as:
    time1: str - start of timespan (24-hour time)
    time2: str - end of timespan (24-hour time)
    exclude: True/False - inverts the time span so it is all day
    except for the time between time1 and time2
    disabled: True/False - disables notifications for this day.
    allday: True/False - enables notifications for the entire day.
    """
    schedule["token"] = token
    data = _utils.add_custid(schedule, customerid)

    return _utils.post("{}/{}/{}".format(API_URL, ROUTE, name), data)


def update(
    token: str, name: str, schedule: dict, customerid: str | None = None
) -> dict:
    """Update a new notification schedule for the specified NodePing account.

    Args:
        token (str): NodePing API token
        name (str): The name of the schedule
        schedule (dict): The schedules for each day for receiving notifications
        customerid (str | None): subaccount ID

    Returns:
        dict: Entry for updated schedule

    Example:

    {'data': {'friday': {'disabled': True},
              'monday': {'allday': True},
              'saturday': {'exclude': False, 'time1': '6:00', 'time2': '18:00'},
              'sunday': {'exclude': False, 'time1': '6:00', 'time2': '18:00'},
              'thursday': {'exclude': False, 'time1': '6:00', 'time2': '18:00'},
              'tuesday': {'exclude': False, 'time1': '6:00', 'time2': '18:00'},
              'wednesday': {'exclude': False, 'time1': '6:00', 'time2': '18:00'}}}

    Days accept certain variables certain key/value pairs such as:
    time1: str - start of timespan (24-hour time)
    time2: str - end of timespan (24-hour time)
    exclude: True/False - inverts the time span so it is all day
    except for the time between time1 and time2
    disabled: True/False - disables notifications for this day.
    allday: True/False - enables notifications for the entire day.
    """
    schedule["token"] = token
    data = _utils.add_custid(schedule, customerid)

    return _utils.put("{}/{}/{}".format(API_URL, ROUTE, name), data)


def delete(token: str, schedule: str, customerid: str | None = None) -> dict:
    """ """
    data = _utils.add_custid({"token": token}, customerid)

    return _utils.delete("{}/{}/{}".format(API_URL, ROUTE, schedule), data)
