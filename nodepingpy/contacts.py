# -*- coding: utf-8 -*-

""" Manage contacts on your NodePing account."""


from .nptypes import contacttypes
from . import _utils
from ._utils import API_URL


ROUTE = "contacts"


def get_all(
    token: str, customerid: str | None = None
) -> dict[str, contacttypes.ManyContacts]:
    """Get all contacts on the account or subaccount.

    https://nodeping.com/docs-api-contacts.html#get

    Args:
        token (str): NodePing API token
        customerid (str | None): subaccount ID

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
        customerid (str | None): subaccount ID

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
        customerid (str | None): subaccount ID

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
    custrole: str,
    name: str = "",
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


def update(token: str, cid: str, args: dict, customerid: str | None = None) -> dict:
    """Update an existing contact.

    NOTE: If you are using the addresses argument to update an existing
    address, you must supply the entire list of contacts. For example, if
    a contact has 2 addresses and you are only updating one, you must supply
    both addresses, one being with the revisions you are planning to make.

    Args:
        token (str): NodePing API token
        cid (str): The contact ID of the contact that is being changed
        customerid (str | None): subaccount ID

    Returns:
        dict: The contents of the updated contact
    """
    data = _utils.add_custid(args, customerid)
    data["token"] = token
    data["id"] = cid

    return _utils.put("{}/{}/{}".format(API_URL, ROUTE, cid), data)


def mute_contact(
    token: str,
    contact_dict: dict,
    duration: int | bool,
    customerid: str | None = None,
) -> dict:
    """Mute a contact.

    Mute or unmute a contact indefinitely, or mute it up until a set timestamp.
    Note that to update the contact, you must return the whole contact,
    otherwise you will lose contact methods in the update.

    Args:
        token (str): NodePing API token
        contact_dict (dict): The entire dict for the contact.
        duration (int|bool): true to mute infinitely, false to unmute, or a unix timestamp
        customerid (str | None): subaccount ID

    Returns:
        dict: The contents of the contact with the applied mute information
    """
    for _, address in contact_dict["addresses"].items():
        address["mute"] = duration

    addresses = contact_dict["addresses"]
    data = _utils.add_custid(
        {"token": token, "addresses": addresses}, customerid
    )

    return _utils.put("{}/{}/{}".format(API_URL, ROUTE, contact_dict["_id"]), data)


def mute_contact_method(
    token: str,
    contact_dict: dict,
    method_id: str,
    duration: int | bool,
    customerid: str | None = None,
):
    """Mute a contact method of a contact.

    Mute or unmute a single contact method indefinitely, or mute it up until a set timestamp.
    Note that to update the contact, you must return the whole contact,
    otherwise you will lose contact methods in the update.

    Args:
        token (str): NodePing API token
        contact_dict (dict): The entire dict for the contact, such as one fetched with get_one()
        method_id (str): the contact method id (e.g - K5SP9CQP found in the addresses object)
        duration (int|bool): true to mute infinitely, false to unmute, or a unix timestamp
        customerid (str | None): subaccount ID

    Returns:
        dict: The contents of the contact with the applied mute information
    """
    contact_dict["addresses"][method_id]["mute"] = duration 
    addresses = contact_dict["addresses"]
    data = _utils.add_custid({"token": token, "addresses": addresses}, customerid)

    return _utils.put("{}/{}/{}".format(API_URL, ROUTE, contact_dict["_id"]), data)


def delete_contact(token: str, cid: str, customerid: str | None = None) -> dict:
    """Delete a contact on a NodePing account.

     Args:
        token (str): NodePing API token
        cid (str): the contact id
        customerid (str | None): subaccount ID

    Returns:
        dict: Confirmation of a sucessful or failed deletion.
    """
    data = _utils.add_custid({"token": token}, customerid)

    return _utils.delete("{}/{}/{}".format(API_URL, ROUTE, cid), data)


def reset_password(token: str, cid: str, customerid: str | None = None) -> dict:
    """Reset the password for the specified contact.

    You can get the contact_id by querying the API with the get_all
    function. The ID would look something like this: "201205050153W2Q4C-OVDN7"

    Args:
        token (str): NodePing API token
        cid (str): the contact id
        customerid (str | None): subaccount ID

    Returns:
        dict: Confirmation of a successful or failed password reset.
    """
    data = _utils.add_custid({"token": token}, customerid)

    return _utils.get("{}/{}/{}?action=RESETPASSWORD".format(API_URL, ROUTE, cid), data)
