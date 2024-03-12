# -*- coding: utf-8 -*-

"""NodePing diagnostic dataclass."""

from dataclasses import dataclass


@dataclass
class Mtr:
    """Args for diagnostics.

    https://nodeping.com/docs-api-diagnostics.html

    Args:
        location (str): probe 2-character indicater or AGENT check ID
        target (str | None): URL, FQDN, IP address to get diagnostics about. Taken from check data if not specified
        count (int): number of pings to send
    """

    location: str
    target: str | None = None
    count: int = 10
    tool: str = "mtr"

    def __post_init__(self):
        self.tool = "mtr"


@dataclass
class Ping:
    """Args for diagnostics.

    https://nodeping.com/docs-api-diagnostics.html

    Args:
        location (str): probe 2-character indicater or AGENT check ID
        target (str | None): URL, FQDN, IP address to get diagnostics about. Taken from check data if not specified
        count (int): number of pings to send
    """

    location: str
    target: str | None = None
    count: int = 10
    tool: str = "ping"

    def __post_init__(self):
        self.tool = "ping"


@dataclass
class Traceroute:
    """Args for diagnostics.

    https://nodeping.com/docs-api-diagnostics.html

    Args:
        location (str): probe 2-character indicater or AGENT check ID
        target (str | None): URL, FQDN, IP address to get diagnostics about. Taken from check data if not specified
    """

    location: str
    target: str | None = None
    tool: str = "traceroute"

    def __post_init__(self):
        self.tool = "traceroute"


@dataclass
class Dig:
    """Args for diagnostics.

    https://nodeping.com/docs-api-diagnostics.html

    Args:
        location (str): probe 2-character indicater or AGENT check ID
        target (str | None): URL, FQDN, IP address to get diagnostics about. Taken from check data if not specified
        dnsserver (str): FQDN or IP of the DNS server to query
        dnstype (str): DNS record type for the query
        transport (str): udp or tcp
    """

    location: str
    target: str | None = None
    dnsserver: str | None = None
    dnstype: str = "A"
    transport: str = "udp"
    tool: str = "dig"

    def __post_init__(self):
        self.tool = "dig"


@dataclass
class Pageload:
    """Args for diagnostics.

    https://nodeping.com/docs-api-diagnostics.html

    Args:
        location (str): probe 2-character indicater or AGENT check ID
        target (str | None): URL, FQDN, IP address to get diagnostics about. Taken from check data if not specified
    """

    location: str
    target: str | None = None
    tool: str = "pageload"

    def __post_init__(self):
        self.tool = "pageload"


@dataclass
class Screenshot:
    """Args for diagnostics.

    https://nodeping.com/docs-api-diagnostics.html

    Args:
        location (str): probe 2-character indicater or AGENT check ID
        target (str | None): URL, FQDN, IP address to get diagnostics about. Taken from check data if not specified
    """

    location: str
    target: str | None = None
    tool: str = "screenshot"

    def __post_init__(self):
        self.tool = "screenshot"
