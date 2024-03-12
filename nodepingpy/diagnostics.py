# -*- coding: utf-8 -*-

"""Request diagnostic information from a profe or AGENT."""

from . import _utils
from ._utils import API_URL

from dataclasses import asdict


ROUTE = "diagnostics"


def get(token: str, checkid: str, args) -> dict:
    """Get diagnostic information from a probe or AGENT.

    Args:
        token (str): NodePing API token
        checkid (str): check id associated with the diagnostic request
        args (dataclass): nptypes.checktypes.{Mtr,Ping,Traceroute,Dig,Pageload,Screenshot}

    Return:
        dict: Diagnostic information
    """

    querystring = _utils.generate_querystring(asdict(args))
    url = "{}/{}/{}?{}".format(API_URL, ROUTE, checkid, querystring)
    data = {"token": token}

    return _utils.get(url, data)
