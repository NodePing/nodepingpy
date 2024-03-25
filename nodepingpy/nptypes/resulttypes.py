# -*- coding: utf-8 -*-

from dataclasses import dataclass


@dataclass
class Results:
    """
    https://nodeping.com/docs-api-results.html#get

    Args:
        span (int): number of hours of results to retrieve. Cannot be used with start/end.
        limit (int): number of records to retrieve
        start (int | str): date/time for results to start. Millisecond, RFC2822, or ISO 8601. Times are assumed to be GMT unless the time includes the timezone
        end (int | str): use in conjunction with start. End time to get results
        clean (bool): whether to use the older format for results. True is recommended.
    """
    span: int | None = None
    limit: int = 300
    start: int | str | None = None
    end: int | str | None = None
    clean: bool = True


@dataclass
class Uptime:
    """
    https://nodeping.com/docs-api-results.html#uptime

    Args:
        interval (str): "days" or "months"
        start (str): start date of days or months (e.g. 2024-03-10). None starts at beginning of available data
        end (str): end date of days or months. None meands the end date is "now"
        offset (int): records are stored using UTC. Use this to offset the information for a different time zone. e.g. -24 to 24 hours offset.
    """
    offset: int | None = None
    interval: str = "months"
    start: str | None = None
    end: str | None = None


@dataclass
class Events:
    """
    https://nodeping.com/docs-api-results.html#events

    Records are sorted by the start time of event in descending order.

    Args:
        start (str): start date to retrieve events from a specific range of time
        end (str): end date to retrieve events from a specific range of time
        limit (int): limit for number of records to retrieve
    """
    start: int | str | None = None
    end: int | str | None = None
    limit: int | None = None
