# -*- coding: utf-8 -*-

""" Get contacts on your NodePing account."""


from nptypes import contacttypes
from . import _utils
from ._utils import API_URL


ROUTE = "contacts"


def get_all(token: str, customerid: str | None = None) -> dict[str, contacttypes.ManyContacts]:
    """Get all contacts on the account or subaccount.

    https://nodeping.com/docs-api-contacts.html#get

    Args:
        token (str): NodePing API token
        customerid (str): subaccount ID

    Returns:
        dict: All contacts on NodePing account or subaccount.
    """
    data = _utils.add_custid({"token": token}, customerid)

    return _utils.get("{}/{}".format(API_URL, ROUTE), data)


def get_one(
    token: str, contactid: str, customerid: str | None = None
) -> dict[str, contacttypes.Contact]:
    """Get one contact on the account or subaccount.

    https://nodeping.com/docs-api-contacts.html#get

    Args:
        token (str): NodePing API token
        contactid (str): The `_id` for the contact
        customerid (str): subaccount ID

    Returns:
        dict: All contacts on NodePing account or subaccount.
    """
    url = "{}/{}?{}".format(
        API_URL, ROUTE, _utils.generate_querystring({"id": contactid})
    )
    data = _utils.add_custid({"token": token}, customerid)

    return _utils.get(url, data)


def get_by_type(
    token: str, contacttype: str, customerid: str | None = None
) -> dict[str, contacttypes.Contact]:
    """Get one contact on the account or subaccount.

    https://nodeping.com/docs-api-contacts.html#get

    Args:
        token (str): NodePing API token
        contacttype (str): sms, email, webhook, etc.
        customerid (str): subaccount ID

    Returns:
        dict: All contacts on NodePing account or subaccount of type `contacttype`
    """
    contacts_dict = {}
    contacts = get_all(token, customerid)

    for key, value in contacts.items():
        contact = value["addresses"]

        contacts_dict.update(
            {
                key: value
                for _cid, contents in contact.items()
                if contents["type"] == contacttype
            }
        )

    return contacts_dict


def create(
    token: str,
    customerid: str,
    name: str = "",
    custrole: str = "view",
    newaddresses: list | None = None,
) -> dict:
    """Create a new contact on your account or subaccount.

    https://nodeping.com/docs-api-contacts.html#post-put

    newaddresses example:
    [{'address': 'me@email.com'}, {'address': '5551238888'}]

    newaddresses webhook example

    [{'action': 'post',
        'address': 'https://webhook.example.com',
        'data': {'event': '{event}',
            'id': '{_id}',
            'label': '{label}',
            'runtime': '{runtime}',
            'target': '{target}'},
        'headers': {'Content-Type': 'application/json'},
        'type': 'webhook'}
    ]

    Args:
        token (str): NodePing API token
        customerid (str): subaccount ID
        contacttype (str): sms, email, webhook, etc.
        name (str): The name of your contact
        custrole (str): permissions for this contact. Default: view
        newaddresses (str): list of dictionaries containing address info

    Returns:
        dict: API result about created contact
    """
    data = {
        "name": name,
        "newaddresses": newaddresses,
        "custrole": custrole,
        "token": token,
        "customerid": customerid,
    }

    return _utils.post("{}/{}/{}".format(API_URL, ROUTE, customerid), data)


def update(
    token: str, cid: str, args: dict, customerid: str
) -> dict:
    """Update an existing contact.

    NOTE: If you are using the addresses argument to update an existing
    address, you must supply the entire list of contacts. For example, if
    a contact has 2 addresses and you are only updating one, you must supply
    both addresses, one being with the revisions you are planning to make.

    Args:
        token (str): NodePing API token
        cid (str): The contact ID of the contact that is being changed
        customerid (str): subaccount ID

    Returns:
        dict: The contents of the updated contact
    """
    data = _utils.add_custid(args, customerid)
    data["token"] = token
    data["id"] = cid

    return _utils.put("{}/{}/{}".format(API_URL, ROUTE, cid), data)


def mute_contact(
    token: str,
    contact_dict: dict[str, str | bool],
    duration: int | bool,
    customerid: str | None = None,
) -> dict:
    """ """
    addresses_muted = {}
    cid = next(iter(contact_dict.keys()))
    value = next(iter(contact_dict.values()))
    for contact_method, address in value["addresses"].items():
        address["mute"] = duration
        addresses_muted.update({contact_method: address})

    data = _utils.add_custid(
        {"token": token, "id": cid, "addresses": addresses_muted}, customerid
    )

    return _utils.put("{}/{}/{}".format(API_URL, ROUTE, cid), data)


def mute_contact_method(
    token: str,
    contact_dict: dict[str, list],
    duration: int | bool,
    customerid: str | None = None,
):
    """ """
    addresses_muted = {}
    cid = next(iter(contact_dict.keys()))
    value = next(iter(contact_dict.values()))
    for contact_method, address in value["addresses"].items():
        address["mute"] = duration
        addresses_muted.update({contact_method: address})

    data = _utils.add_custid(
        {"token": token, "id": cid, "addresses": addresses_muted}, customerid
    )

    return _utils.put("{}/{}/{}".format(API_URL, ROUTE, cid), data)
