# -*- coding: utf-8 -*-

"""NodePing maintenance dataclass."""

from dataclasses import dataclass


@dataclass
class AdHoc:
    """
    """
    duration: int
    checklist: list
    enabled: bool
    name: str | None = None
    id: str = "ad-hoc"

    def __post_init__(self):
        self.id = "ad-hoc"


@dataclass
class Scheduled:
    """
    """
    duration: int
    checklist: list
    enabled: bool
    name: str | None = None
    cron: str | None = None
