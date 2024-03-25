# -*- coding: utf-8 -*-

"""Request diagnostic information from a probe or AGENT."""

from . import _utils
from ._utils import API_URL

from dataclasses import asdict


ROUTE = "diagnostics"


def get(token: str, checkid: str, args, customerid: str | None = None) -> dict:
    """Get diagnostic information from a probe or AGENT.

    Args:
        token (str): NodePing API token
        checkid (str): check id associated with the diagnostic request
        args (dataclass): nptypes.checktypes.{Mtr,Ping,Traceroute,Dig,Pageload,Screenshot}
        customerid (str): subaccount ID

    Return:
        dict: Diagnostic information
    """

    querystring = _utils.generate_querystring(asdict(args))
    url = "{}/{}/{}?{}".format(API_URL, ROUTE, checkid, querystring)
    data = _utils.add_custid({"token": token}, customerid)

    return _utils.get(url, data)
