# -*- coding: utf-8 -*-

from dataclasses import dataclass

@dataclass
class Notification:
    id: str | None = None
    span: int | None = None
    limit: int | None = 300
    subaccounts: bool = False
