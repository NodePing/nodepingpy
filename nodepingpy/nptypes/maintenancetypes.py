# -*- coding: utf-8 -*-

"""NodePing maintenance dataclass."""

from dataclasses import dataclass


@dataclass
class AdHocCreate:
    """Args for creating an ad-hoc maintenance.

    https://nodeping.com/docs-api-maintenance.html

    Args:
        duration (int): duration in minutes to keep the checks disabled
        checklist (list): List of check IDs to disable
        enabled (bool): whether or not to enable or disable this maintenance
        name (str): name for the ad-hoc maintenance
    """
    duration: int
    checklist: list
    enabled: bool
    name: str
    id: str = "ad-hoc"

    def __post_init__(self):
        self.id = "ad-hoc"


@dataclass
class AdHocUpdate:
    """Args for updating an ad-hoc maintenance.

    https://nodeping.com/docs-api-maintenance.html

    Args:
        duration (int): duration in minutes to keep the checks disabled
        checklist (list): List of check IDs to disable
        enabled (bool): optional - whether or not to enable or disable this maintenance
        name (str): optional - new name for the ad-hoc maintenance
    """
    duration: int
    checklist: list
    enabled: bool | None = None
    name: str | None = None
    id: str = "ad-hoc"

    def __post_init__(self):
        self.id = "ad-hoc"


@dataclass
class ScheduledCreate:
    """Args for creating a scheduled maintenance.

    https://nodeping.com/docs-api-maintenance.html

    Args:
        duration (int): duration in minutes to keep the checks disabled
        checklist (list): List of check IDs to disable
        enabled (bool): whether or not to enable or disable this maintenance
        name (str): name for the scheduled maintenance
        cron (str): cron line for scheduled maintenance start
    """
    duration: int
    checklist: list
    enabled: bool
    name: str
    cron: str


@dataclass
class ScheduledUpdate:
    """Args for updating a scheduled maintenance.

    https://nodeping.com/docs-api-maintenance.html

    Args:
        duration (int): duration in minutes to keep the checks disabled
        checklist (list): List of check IDs to disable
        enabled (bool): optional - whether or not to enable or disable this maintenance
        name (str): optional - new name for the scheduled maintenance
        cron (str): optional - new cron line for scheduled maintenance start
    """
    duration: int
    checklist: list
    enabled: bool | None = None
    name: str | None = None
    cron: str | None = None
