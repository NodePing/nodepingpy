# nodepingpy

A new Python 3 library for managing NodePing checks, schedules, contacts, etc.

## General Usage

To use the NodePing API with Python3, you are required to use your
provided API token. You can find your API key on your NodePing account
under `Account Settings → API`.

You can also optionally provide a Sub Account ID which can be found
under `Account Settings → SubAccounts` and you will see the ID by its
name.

You can set these variables, for example, like so:

``` python
token = (my-api-token"
customerid = "your-subaccount-id"
```

An example use of specifically managing an account/subaccount via the
ID might look like this:

``` py
>>> from nodepingpy import accounts
>>> token = "api-token-here"
>>> customerid = "your-subaccount-id"
>>> accounts.info(token, customerid)
```

## Installation

To install this package, run:

```
pip install nodepingpy
```

## Accounts Module

This module returns account information, including getting and updating
accounts/subaccounts, creating subaccounts, and deleting subaccounts.

Can be imported with

``` py
from nodepingpy import accounts
```

### Check API Token Validity

Returns `True` if API token is valid or `False` if not.

``` py
>>> from nodepingpy import accounts
>>> token = "api-token-here"
>>> accounts.is_valid(token)
True
```

### Get Account Info

Use `accounts.info` to get details about the parent account

``` py
>>> accounts.info(token)
{
    "201205050153W2Q4C": {
        "parent": 5,
        "name": "Peter Provider",
        "status": "Active",
        "count": 120
    },
    "201204251942S197J": {
        "name": "Courageous Charlie",
        "status": "Active",
        "count": 31
    }
}
```

Or when specifying an account/subaccount

``` py
>>> accounts.info(token, customerid)
{
    "_id": "201205102227VZ6XU",
    "type": "customer",
    "customer_name": "My Company Name",
    "creation_date": 1336626000000,
    "status": "Active",
    "timezone": "-7.0",
    "nextBillingDate": "2012-05-15",
    "defaultlocations": [ "nam" ]
}
```

### Creating Accounts

This will only create subaccounts, not a new account. A dataclass is
used for simple templating of arguments to pass to the API.

``` py
token = "my-token"
args = accounts.Account(name="My Company Name", contactname="Courageous Charlie", email="charlie@example.com", timezone="-5", location="nam", emailme=True, autodiagnotifications=True)
accounts.create_subaccount(token, args)
```

### Updating Accounts

Uses the `accounts.AccountUpdate` dataclass, which has all optional values,
including an additional `status` key to allow activating or suspending subaccounts.

``` py
token = "my-token"
customerid = "201205102227VZ6XU"
args = accounts.AccountUpdate(name="ChangedTheName", status="Suspend")
accounts.update_account(token, args, customerid=customerid)
```

### Deleting Subaccounts

``` py
token = "my-token"
customerid = "201205102227VZ6XU"
accounts.delete_subaccount(token, customerid)
```

### Disabling Notifications

You can disable or enable notifications on your account or subaccount. Doing
this on a parent account will not disable notifications on subaccounts.

``` py
token = "my-token"
accounts.disable_notifications(token, customerid)
```

## Checks Module

This module manages checks on your account and subaccount.

``` py
from nodepingpy import checks
```

If you are going to create checks, also import the `checktypes` module to
use the dataclasses for creating different check types.

``` py
from nodepingpy.nptypes import checktypes
```

### Get All Checks

``` py
token = "my-token"
checks.get_all(token)
```

You can also get all checks with their uptime

``` py
token = "my-token"
checks.get_all_uptime(token)
```

### Get Single or Many Checks

Use this method to get one check on your account or subaccount.

``` py
token = "my-token"
checkid = "201205050153W2Q4C-0J2HSIRF"
checks.get_by_id(token, checkid)
```

Or many

``` py
token = "my-token"
checkids = ["201205050153W2Q4C-0J2HSIRF", "201205050153W2Q4C-4RZT8MLN"]
checks.get_many(token, checkids)
```

You can also get current events ("down" or "disabled") by setting `current`
to True

``` py
token = "my-token"
checkids = ["201205050153W2Q4C-0J2HSIRF", "201205050153W2Q4C-4RZT8MLN"]
checks.get_many(token, checkids, current=True)
```

### Get Uptime

You can get uptime for checks. There is a combination of getting all one,
many, or all checks, with all uptime, and with uptime stats back to a
certain date.

Get all uptime

``` py
token = "my-token"
checks.get_uptime(token, "all")
```

Get uptime for a list of checks

``` py
token = "my-token"
checkids = ["201205050153W2Q4C-0J2HSIRF", "201205050153W2Q4C-4RZT8MLN"]
checks.get_uptime(token, checkids)
```

Uptime back to a certain date

``` py
token = "my-token"
checks.get_uptime(token, "all", "2024-01-01)
```

### Get lastresult

This gets the last result for a single check

``` py
token = "my-token"
checkid = "201205050153W2Q4C-0J2HSIRF"
checks.get_last_result(token, checkid)
```

### Other GET Methods

Get passing checks

``` py
token = "my-token"
checks.get_passing(token)
```

Get failing checks

``` py
token = "my-token"
checks.get_failing(token)
```

Get active checks

``` py
token = "my-token"
checks.get_active(token)
```

Get inactive checks

``` py
token = "my-token"
checks.get_inactive(token)
```

### Create a Check

To create a check, checktype dataclasses were created to have more convenient
access to the different fields for each TYPE. For example, creating a PING check

``` py
from nodepingpy import checks
from nodepingpy.nptypes import checktypes
token = "my-token"
args = checktypes.PingCheck("example.com", ipv4=False, label="ping example.com", interval=1, autodiag=True, sens=5, runlocations="nam")
checks.create_check(token, args)
```

If you do not want to import all check types, you can import only the
check types you want:

``` py
from nodepingpy.nptypes import PingCheck, HttpCheck, MtrCheck
```

### Update a Check

Updating a check requires passing in a dictionary of keys to update in
the check being updated. For example, replacing the `label` and `fields`
key in a PUSH check:

``` py
from nodepingpy import checks
token = "my-token"
checkid = "201205050153W2Q4C-0J2HSIRF"
newlabel = "PUSH checking stuff"
fields = {
        "checknum": {
            "name": "checknum",
            "min": 0,
            "max": 5
        },
        "check2": {
            "name": "check2.item",
            "min": 0,
            "max": 0
        }
    }
args = {"label": newlabel, "fields": fields}
checks.update_check(token, checkid, "PUSH", args)
```

### Delete a Check

``` py
from nodepingpy import checks
token = "my-token"
checkid = "201205050153W2Q4C-0J2HSIRF"
checks.delete_check(token, checkid)
```

### Mute a Check

Mute for 10 minutes

``` py
from time import time
from nodepingpy import checks
token = "my-token"
checkid = "201205050153W2Q4C-0J2HSIRF"
ts_later = round((time() + 600) * 1000)
checks.mute_check(token, checkid, duration)
```

You can also set duration to `True` or `False` to indefinitely
mute or unmute the check.

``` py
from nodepingpy import checks
token = "my-token"
checkid = "201205050153W2Q4C-0J2HSIRF"
checks.mute_check(token, True, duration)
```

### Disable All

Disable all checks on the account. True will disable all checks,
but not affect subaccounts. False to re-enable. This will not re-enable
checks that were previously disabled using the "enabled" element in a check.

``` py
from nodepingpy import checks
token = "my-token"
checks.disable_all(token, True)
```

### Disable By

There are a few ways to disable checks:

1. By type: (PING, HTTP, DNS, etc.)
2. By label: the label provided for the check
3. By target: the FQDN, IP, URL in the target field

These are matched with regex. Like with disable_all, re-enabling
checks will only work with checks that weren't previously disabled
by using the 'enabled' element.

In this example, checks with the label including "example.com" will be disabled.

``` py
from nodepingpy import checks
token = "my-token"
disabletype = "label"
string = "example.com"
checks.disable_by(token, disabletype, string, True)
```

## Contacts Module

To use this module, import it into your project

``` py
from nodepingpy import contacts
```

### Get All Contacts

``` py
from nodepingpy import contacts
token = "my-token"
contacts.get_all(token)
```

### Get One Contact

NodePing contacts contain your account ID as well as a 5-character value after it,
like "201205050153W2Q4C-BKPGH".

``` py
from nodepingpy import contacts
token = "my-token"
contactid = "201205050153W2Q4C-BKPGH"
contacts.get_one(token, contactid)
```

### Get by Type

Get contacts by type, such as email, sms, webhook.

``` py
from nodepingpy import contacts
token = "my-token"
contacttype = "email"
contacts.get_by_type(token, contacttype)
```

### Create a Contact

``` py
from nodepingpy import contacts
token = "my-token"
customerid = "201205050153W2Q4C"
name = "Bob Alice"
custrole = "edit"
newaddresses = [{'address': 'me@email.com'}, {'address': '5551238888'}]
contacts.create(token, customerid, custrole, name, newaddresses)
```

### Update Existing Addresses

Updating existing addresses requires getting the current addresses, modifying their
contents, and then PUT them back. To add addresses to the contact, you will use the
`newaddresses` key with the additional info.

``` py
>>> from nodepingpy import contacts
>>> from pprint import pprint
>>> token = "my-token"
>>> contactid = "201205050153W2Q4C-BKPGH"
>>> result = contacts.get_one(token, contactid)
>>> addresses = result["addresses"]
>>> pprint(addresses)
{'JMMARFHQ': {'accountsupressall': False, 'address': 'newme@example.com'},
 'NMYW1XC1': {'accountsupressall': False, 'address': 'newme2@example.com'},
 'P080YGYO': {'accountsuppressall': False, 'address': '321444777'}}
>>> addresses["JMMARFHQ"]["address"] = "ichangedthis@example.com"
>>> newaddresses = [{'accountsupressall': True, 'address': 'addinganother@example.com'}]}
>>> contacts.update(token, contactid, {"addresses": addresses, "newaddresses": newaddresses})
```

### Muting a Contact Method

Muting a contact method involves muting not a whole contact, but just one of the contact methods.
In the above example, it could involve muting only the SMS number 321444777 with key `P080YGYO` only
in the contact.

``` py
from nodepingpy import contacts
token = "my-token"
contactid = "201205050153W2Q4C-BKPGH"
method_id = "P080YGYO"
contact = contacts.get_one(token, contactid)
duration = True # this will mute it forever, or until set back to False
contacts.mute_contact_method(token, contact, method_id, duration)
```

### Muting a Contact

Compared to the last example, this mutes the entire contact. The contact ID `201205050153W2Q4C-BKPGH`

``` py
from nodepingpy import contacts
token = "my-token"
contactid = "201205050153W2Q4C-BKPGH"
contact = contacts.get_one(token, contactid)
duration = True # this will mute it forever, or until set back to False
contacts.mute_contact(token, contact, duration)
```

### Delete a Contact

``` py
from nodepingpy import contacts
token = "my-token"
contactid = "201205050153W2Q4C-BKPGH"
contacts.delete_contact(token, contactid)
```

### Reset a Password

Reset password for a contact. A new password will be emailed to the contact.

``` py
from nodepingpy import contacts
token = "my-token"
contactid = "201205050153W2Q4C-BKPGH"
contacts.reset_password(token, contactid)
```


