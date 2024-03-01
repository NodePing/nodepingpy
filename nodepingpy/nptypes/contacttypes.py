# -*- coding: utf-8 -*-

"""NodePing contact types"""


from typing import Optional, TypedDict


class GenericAddress(TypedDict):
    accountsuppressall: bool
    address: str
    status: str
    mute: Optional[bool | int]
    suppressdown: Optional[bool]
    suppresup: Optional[bool]
    suppressdiag: Optional[bool]


class EmailAddress(GenericAddress):
    type: str


class SmsAddress(GenericAddress):
    type: str


class VoiceAddress(GenericAddress):
    type: str


class WebhookAddress(GenericAddress):
    action: str
    data: dict[str, str]
    headers: dict[str, str]
    type: str


class PagerDutyAddress(GenericAddress):
    type: str


class PushoverAddress(GenericAddress):
    priority: int
    type: str


class SlackAddress(GenericAddress):
    type: str


class HipChatAddress(GenericAddress):
    type: str


class ManyContacts(TypedDict):
    addresses: dict[
        str,
        EmailAddress
        | SmsAddress
        | VoiceAddress
        | WebhookAddress
        | PagerDutyAddress
        | PushoverAddress
        | SlackAddress
        | HipChatAddress,
    ]
    customer_id: str
    custrole: str
    name: str
    type: str


class Contact(ManyContacts):
    _id: str
