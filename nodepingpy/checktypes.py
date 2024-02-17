# -*- coding: utf-8 -*-

"""NodePing check types."""

from dataclasses import dataclass, field


DEFAULTS = {
    "interval": 15,
    "enabled": False,
    "public": False,
    "runlocations": None,
    "homeloc": False,
    "ipv6": False,
    "threshold": 5,
    "sens": 2,
    "mute": False,
    "autodiag": False,
    "dep": "",
}


@dataclass
class AgentCheck:
    """NodePing AGENT check.

    AGENT checks allow you to install a NodePing probe,
    installed and maintained by you and available only to your account,
    inside your private network that you can assign other NodePing checks
    to run on.

    https://nodeping.com/agent_check.html

    Args:
        oldresultfail (bool): Fail the check if results are too old
        label (str): Name of the check that will be created
        autodiag (bool): Enable/disable auto diagnostics for this check
        interval (int): Interval in minutes to monitor target
        enabled (bool): If created check will be enabled or disabled
        public (bool): If the results for the created check will be public or not
        threshold (int): Time in seconds for an acceptable response
        sens (int): Rechecks to help avoid unecessary notifications
        dep (str): ID of the check used for the notification dependency
        notifications (list): list of objects containing contact ID, delay, and scheduling for notifications
        mute (bool|int): bool or millisecond timestamp (UTC) in the future. True to mute indefinitely
    """

    oldresultfail: bool = False
    label: str = ""
    autodiag: bool = DEFAULTS["autodiag"]
    interval: int = DEFAULTS["interval"]
    enabled: bool = DEFAULTS["enabled"]
    public: bool = DEFAULTS["enabled"]
    threshold: int = DEFAULTS["threshold"]
    sens: int = DEFAULTS["sens"]
    dep: str = DEFAULTS["dep"]
    notifications: list = field(default_factory=list)
    mute: bool = DEFAULTS["mute"]
    type: str = "AGENT"

    def __post_init__(self):
        self.type = "AGENT"


@dataclass
class AudioCheck:
    """NodePing AUDIO check.

    Monitor audio streaming services.

    https://nodeping.com/audio_check.html

    Args:
        target (str): URL to target host
        label (str): Name of the check that will be created
        verifyvolume (bool): enable/disable volume detection
        volumemin (int): The acceptable range for volume detection
        autodiag (bool): Enable/disable auto diagnostics for this check
        interval (int): Interval in minutes to monitor target
        enabled (bool): If created check will be enabled or disabled
        public (bool): If the results for the created check will be public or not
        runlocations (str|list): Which region to be originated from
        homeloc (str|bool): Which probe in the region to originate the check from
        threshold (int): Time in seconds for an acceptable response
        sens (int): Rechecks to help avoid unecessary notifications
        dep (str): ID of the check used for the notification dependency
        notifications (list): list of objects containing contact ID, delay, and scheduling for notifications
        mute (bool|int): bool or millisecond timestamp (UTC) in the future. True to mute indefinitely
    """

    target: str
    label: str = ""
    verifyvolume: bool = False
    volumemin: int = -45
    autodiag: bool = DEFAULTS["autodiag"]
    interval: int = DEFAULTS["interval"]
    enabled: bool = DEFAULTS["enabled"]
    public: bool = DEFAULTS["enabled"]
    runlocations: str | list = DEFAULTS["runlocations"]
    homeloc: str | bool = DEFAULTS["homeloc"]
    threshold: int = DEFAULTS["threshold"]
    sens: int = DEFAULTS["sens"]
    dep: str = DEFAULTS["dep"]
    notifications: list = field(default_factory=list)
    mute: bool = DEFAULTS["mute"]
    type: str = "AUDIO"

    def __post_init__(self):
        self.type = "AUDIO"


@dataclass
class ClusterCheck:
    """NodePing Cluster check.

    Group interdependent NodePing checks in order to get notifications and
    track availability of the group of checks as a whole, in addition to
    each component check individually.

    https://nodeping.com/cluster_check.html

    `data` example:
    checks = {
        "data": {
            "201205050153W2Q4C-0J2HSIRF": "1",
            "201205050153W2Q4C-4RZT8MLN": "1",
            "201205050153W2Q4C-IOPPFQOT": "1"
        }
    }

    Args:
        data (dict): List of checks associated with the cluster
        label (str): Name of the check that will be created
        autodiag (bool): Enable/disable auto diagnostics for this check
        interval (int): Interval in minutes to monitor target
        enabled (bool): If created check will be enabled or disabled
        public (bool): If the results for the created check will be public or not
        runlocations (str|list): Which region to be originated from
        homeloc (str|bool): Which probe in the region to originate the check from
        threshold (int): Time in seconds for an acceptable response
        sens (int): Rechecks to help avoid unecessary notifications
        dep (str): ID of the check used for the notification dependency
        notifications (list): list of objects containing contact ID, delay, and scheduling for notifications
        mute (bool|int): bool or millisecond timestamp (UTC) in the future. True to mute indefinitely
    """

    data: dict
    label: str = ""
    autodiag: bool = DEFAULTS["autodiag"]
    interval: int = DEFAULTS["interval"]
    enabled: bool = DEFAULTS["enabled"]
    public: bool = DEFAULTS["enabled"]
    runlocations: str | list = DEFAULTS["runlocations"]
    homeloc: str | bool = DEFAULTS["homeloc"]
    threshold: int = DEFAULTS["threshold"]
    sens: int = DEFAULTS["sens"]
    dep: str = DEFAULTS["dep"]
    notifications: list = field(default_factory=list)
    mute: bool = DEFAULTS["mute"]
    type: str = "CLUSTER"

    def __post_init__(self):
        self.type = "CLUSTER"


@dataclass
class DnsCheck:
    """NodePing DNS check.

    Args:
        target (str): URL of host to monitor
        port (int): Port for DNS server to query
        transport (str): UDP/TCP for DNS query
        dnstype (str): Type of DNS record to query
        dnsrd (int): Recursion desired. 1 for True, 0 for False
        dnssection (str): section of the DNS reply to look in for the `contentstring`
        contentstring (str): What you expect the response to be when resolved
        dnstoresolve (str): FQDN/IP you want to resolve
        verify (bool): If True will authenticate using DNSSEC
        label (str): Name of the check that will be created
        autodiag (bool): Enable/disable auto diagnostics for this check
        interval (int): Interval in minutes to monitor target
        enabled (bool): If created check will be enabled or disabled
        public (bool): If the results for the created check will be public or not
        runlocations (str|list): Which region to be originated from
        homeloc (str|bool): Which probe in the region to originate the check from
        threshold (int): Time in seconds for an acceptable response
        sens (int): Rechecks to help avoid unecessary notifications
        dep (str): ID of the check used for the notification dependency
        notifications (list): list of objects containing contact ID, delay, and scheduling for notifications
        mute (bool|int): bool or millisecond timestamp (UTC) in the future. True to mute indefinitely
    """

    target: str = ""
    port: int = 53
    transport: str = "udp"
    dnstype: str = "A"
    dnsrd: int = 1
    dnssection: str = "answer"
    contentstring: str = ""
    dnstoresolve: str = ""
    verify: bool = False
    label: str = ""
    autodiag: bool = DEFAULTS["autodiag"]
    interval: int = DEFAULTS["interval"]
    enabled: bool = DEFAULTS["enabled"]
    public: bool = DEFAULTS["enabled"]
    runlocations: str | list = DEFAULTS["runlocations"]
    homeloc: str | bool = DEFAULTS["homeloc"]
    threshold: int = DEFAULTS["threshold"]
    sens: int = DEFAULTS["sens"]
    dep: str = DEFAULTS["dep"]
    notifications: list = field(default_factory=list)
    mute: bool = DEFAULTS["mute"]
    type: str = "DNS"

    def __post_init__(self):
        self.type = "DNS"


@dataclass
class DohDotCheck:
    """NodePing DOHDOT check.

    Args:
        target (str): URL of host to monitor
        dnstoresolve (str): FQDN to query on target
        dohdot (str): DoH or DoT
        method (str): Select GET or POST
        statuscode (str): Expected Response HTTP status code (DoH only)
        sendheaders (dict): Request Headers (DoH only)
        clientcert (str): string to specify the ID of a client cert/key to be used
        verify (bool): Whether or not to verify the SSL cert
        dnstype (str): Type of DNS record to query
        contentstring (str): What you expect the response to be when resolved
        edns (dict): optional object used to send EDNS(0) OPT pseuedo-records in a DNS query
        ipv6 (bool): Whether to resolve IPv4 or IPv6
        label (str): Name of the check that will be created
        autodiag (bool): Enable/disable auto diagnostics for this check
        interval (int): Interval in minutes to monitor target
        enabled (bool): If created check will be enabled or disabled
        public (bool): If the results for the created check will be public or not
        runlocations (str|list): Which region to be originated from
        homeloc (str|bool): Which probe in the region to originate the check from
        threshold (int): Time in seconds for an acceptable response
        sens (int): Rechecks to help avoid unecessary notifications
        dep (str): ID of the check used for the notification dependency
        notifications (list): list of objects containing contact ID, delay, and scheduling for notifications
        mute (bool|int): bool or millisecond timestamp (UTC) in the future. True to mute indefinitely
    """

    target: str
    dnstoresolve: str
    dohdot: str = "doh"
    method: str = "GET"
    statuscode: str = "200"
    sendheaders: dict = field(default_factory=dict)
    clientcert: str = ""
    verify: bool = False
    dnstype: str = "A"
    contentstring: str = ""
    edns: dict = field(default_factory=dict)
    ipv6: bool = False
    label: str = ""
    autodiag: bool = DEFAULTS["autodiag"]
    interval: int = DEFAULTS["interval"]
    enabled: bool = DEFAULTS["enabled"]
    public: bool = DEFAULTS["enabled"]
    runlocations: str | list = DEFAULTS["runlocations"]
    homeloc: str | bool = DEFAULTS["homeloc"]
    threshold: int = DEFAULTS["threshold"]
    sens: int = DEFAULTS["sens"]
    dep: str = DEFAULTS["dep"]
    notifications: list = field(default_factory=list)
    mute: bool = DEFAULTS["mute"]
    type: str = "DOHDOT"

    def __post_init__(self):
        self.type = "DOHDOT"


@dataclass
class FtpCheck:
    """NodePing FTP check.

    Args:
        target (str): URL of host to monitor
        port (int): FTP server port
        username (str): Username to authenticate FTP connection
        password (str): Password for user authentication
        invert (bool): Whether you expect the content to exist or not (True == exists)
        contentstring (str): What you expect the response to be when resolved
        label (str): Name of the check that will be created
        autodiag (bool): Enable/disable auto diagnostics for this check
        interval (int): Interval in minutes to monitor target
        enabled (bool): If created check will be enabled or disabled
        public (bool): If the results for the created check will be public or not
        runlocations (str|list): Which region to be originated from
        homeloc (str|bool): Which probe in the region to originate the check from
        threshold (int): Time in seconds for an acceptable response
        sens (int): Rechecks to help avoid unecessary notifications
        dep (str): ID of the check used for the notification dependency
        notifications (list): list of objects containing contact ID, delay, and scheduling for notifications
        mute (bool|int): bool or millisecond timestamp (UTC) in the future. True to mute indefinitely
    """

    target: str
    port: int = 21
    username: str = ""
    password: str = ""
    invert: bool = False
    contentstring: str = ""
    label: str = ""
    autodiag: bool = DEFAULTS["autodiag"]
    interval: int = DEFAULTS["interval"]
    enabled: bool = DEFAULTS["enabled"]
    public: bool = DEFAULTS["enabled"]
    runlocations: str | list = DEFAULTS["runlocations"]
    homeloc: str | bool = DEFAULTS["homeloc"]
    threshold: int = DEFAULTS["threshold"]
    sens: int = DEFAULTS["sens"]
    dep: str = DEFAULTS["dep"]
    notifications: list = field(default_factory=list)
    mute: bool = DEFAULTS["mute"]
    type: str = "FTP"

    def __post_init__(self):
        self.type = "FTP"


@dataclass
class HttpCheck:
    """NodePing HTTP check.

    Args:
        target (str): URL to target host
        follow (bool): Whether to follow redirects or not
        ipv6 (bool): Whether to resolve IPv4 or IPv6
        label (str): Name of the check that will be created
        autodiag (bool): Enable/disable auto diagnostics for this check
        interval (int): Interval in minutes to monitor target
        enabled (bool): If created check will be enabled or disabled
        public (bool): If the results for the created check will be public or not
        runlocations (str|list): Which region to be originated from
        homeloc (str|bool): Which probe in the region to originate the check from
        threshold (int): Time in seconds for an acceptable response
        sens (int): Rechecks to help avoid unecessary notifications
        dep (str): ID of the check used for the notification dependency
        notifications (list): list of objects containing contact ID, delay, and scheduling for notifications
        mute (bool|int): bool or millisecond timestamp (UTC) in the future. True to mute indefinitely
    """

    target: str
    follow: bool = False
    ipv6: bool = False
    label: str = ""
    autodiag: bool = DEFAULTS["autodiag"]
    interval: int = DEFAULTS["interval"]
    enabled: bool = DEFAULTS["enabled"]
    public: bool = DEFAULTS["enabled"]
    runlocations: str | list = DEFAULTS["runlocations"]
    homeloc: str | bool = DEFAULTS["homeloc"]
    threshold: int = DEFAULTS["threshold"]
    sens: int = DEFAULTS["sens"]
    dep: str = DEFAULTS["dep"]
    notifications: list = field(default_factory=list)
    mute: bool = DEFAULTS["mute"]
    type: str = "HTTP"

    def __post_init__(self):
        self.type = "HTTP"


@dataclass
class HttpAdvCheck:
    """NodePing HTTPADV check.

    Args:
        target (str): URL to target host
        invert (bool): Used for "Does not contain" functionality
        contentstring (str): What you expect the response to be when resolved
        data (dict): key/value pair for POST fields
        clientcert (str): Specify the ID of a client certificate/key to be used
        method (str): HTTP method
        postdata (str): a single string to post instead of a data dictionary
        receiveheaders (dict): Headers that should be received
        sendheaders (dict): Headers to send in request
        statuscode (int): HTTP status code expected in return
        follow (bool): Whether to follow redirects or not
        ipv6 (bool): Whether to resolve IPv4 or IPv6
        label (str): Name of the check that will be created
        autodiag (bool): Enable/disable auto diagnostics for this check
        interval (int): Interval in minutes to monitor target
        enabled (bool): If created check will be enabled or disabled
        public (bool): If the results for the created check will be public or not
        runlocations (str|list): Which region to be originated from
        homeloc (str|bool): Which probe in the region to originate the check from
        threshold (int): Time in seconds for an acceptable response
        sens (int): Rechecks to help avoid unecessary notifications
        dep (str): ID of the check used for the notification dependency
        notifications (list): list of objects containing contact ID, delay, and scheduling for notifications
        mute (bool|int): bool or millisecond timestamp (UTC) in the future. True to mute indefinitely
    """

    target: str
    invert: bool = False
    contentstring: str = ""
    data: dict = field(default_factory=dict)
    clientcert: str = ""
    method: str = ""
    postdata: str = ""
    receiveheaders: str = ""
    sendheaders: str = ""
    statuscode: int = 200
    follow: bool = False
    ipv6: bool = False
    label: str = ""
    autodiag: bool = DEFAULTS["autodiag"]
    interval: int = DEFAULTS["interval"]
    enabled: bool = DEFAULTS["enabled"]
    public: bool = DEFAULTS["enabled"]
    runlocations: str | list = DEFAULTS["runlocations"]
    homeloc: str | bool = DEFAULTS["homeloc"]
    threshold: int = DEFAULTS["threshold"]
    sens: int = DEFAULTS["sens"]
    dep: str = DEFAULTS["dep"]
    notifications: list = field(default_factory=list)
    mute: bool = DEFAULTS["mute"]
    type: str = "HTTPADV"

    def __post_init__(self):
        self.type = "HTTPADV"


@dataclass
class HttpContentCheck:
    """NodePing HTTPCONTENT check.

    Args:
        target (str): URL to target host
        invert (bool): Used for "Does not contain" functionality
        contentstring (str): What you expect the response to be when resolved
        follow (bool): Whether to follow redirects or not
        ipv6 (bool): Whether to resolve IPv4 or IPv6
        label (str): Name of the check that will be created
        autodiag (bool): Enable/disable auto diagnostics for this check
        interval (int): Interval in minutes to monitor target
        enabled (bool): If created check will be enabled or disabled
        public (bool): If the results for the created check will be public or not
        runlocations (str|list): Which region to be originated from
        homeloc (str|bool): Which probe in the region to originate the check from
        threshold (int): Time in seconds for an acceptable response
        sens (int): Rechecks to help avoid unecessary notifications
        dep (str): ID of the check used for the notification dependency
        notifications (list): list of objects containing contact ID, delay, and scheduling for notifications
        mute (bool|int): bool or millisecond timestamp (UTC) in the future. True to mute indefinitely
    """

    target: str
    invert: bool = False
    contentstring: str = ""
    follow: bool = False
    ipv6: bool = False
    label: str = ""
    autodiag: bool = DEFAULTS["autodiag"]
    interval: int = DEFAULTS["interval"]
    enabled: bool = DEFAULTS["enabled"]
    public: bool = DEFAULTS["enabled"]
    runlocations: str | list = DEFAULTS["runlocations"]
    homeloc: str | bool = DEFAULTS["homeloc"]
    threshold: int = DEFAULTS["threshold"]
    sens: int = DEFAULTS["sens"]
    dep: str = DEFAULTS["dep"]
    notifications: list = field(default_factory=list)
    mute: bool = DEFAULTS["mute"]
    type: str = "HTTPCONTENT"

    def __post_init__(self):
        self.type = "HTTPCONTENT"


@dataclass
class HttpParseCheck:
    """NodePing HTTPPARSE check.


    `fields` expects a dictionary where each object should have a name, min, and max.

    Example dictionary:
    fields = {
        "processmem": {
            "name": "processmem",
            "min": 1000,
            "max": 5000
        },
        "cpuload": {
            "name": "cpuload",
            "min": 1,
            "max": 5
        }
    }

    Args:
        target (str): URL to target host
        fields (dict): Keyed list of fields, with an arbitrary string as the key.
        sendheaders (dict): Headers to send in request
        label (str): Name of the check that will be created
        autodiag (bool): Enable/disable auto diagnostics for this check
        interval (int): Interval in minutes to monitor target
        enabled (bool): If created check will be enabled or disabled
        public (bool): If the results for the created check will be public or not
        runlocations (str|list): Which region to be originated from
        homeloc (str|bool): Which probe in the region to originate the check from
        threshold (int): Time in seconds for an acceptable response
        sens (int): Rechecks to help avoid unecessary notifications
        dep (str): ID of the check used for the notification dependency
        notifications (list): list of objects containing contact ID, delay, and scheduling for notifications
        mute (bool|int): bool or millisecond timestamp (UTC) in the future. True to mute indefinitely
    """

    target: str
    fields: dict = field(default_factory=dict)
    sendheaders: dict = field(default_factory=dict)
    label: str = ""
    autodiag: bool = DEFAULTS["autodiag"]
    interval: int = DEFAULTS["interval"]
    enabled: bool = DEFAULTS["enabled"]
    public: bool = DEFAULTS["enabled"]
    runlocations: str | list = DEFAULTS["runlocations"]
    homeloc: str | bool = DEFAULTS["homeloc"]
    threshold: int = DEFAULTS["threshold"]
    sens: int = DEFAULTS["sens"]
    dep: str = DEFAULTS["dep"]
    notifications: list = field(default_factory=list)
    mute: bool = DEFAULTS["mute"]
    type: str = "HTTPPARSE"

    def __post_init__(self):
        self.type = "HTTPPARSE"


@dataclass
class Imap4Check:
    """NodePing IMAP4 check.

    Args:
        target (str): URL to target host
        port (int): port used to test IMAP4 communications
        verify (bool): The check should fail if the SSL/TLS certificate is invalid
        username (str): Email address for testing logins
        password (str): Password to authenticate email address
        secure (bool): Whether SSL/TLS should be used
        warningdays (int): Warning days befor certificate expiration
        label (str): Name of the check that will be created
        autodiag (bool): Enable/disable auto diagnostics for this check
        interval (int): Interval in minutes to monitor target
        enabled (bool): If created check will be enabled or disabled
        public (bool): If the results for the created check will be public or not
        runlocations (str|list): Which region to be originated from
        homeloc (str|bool): Which probe in the region to originate the check from
        threshold (int): Time in seconds for an acceptable response
        sens (int): Rechecks to help avoid unecessary notifications
        dep (str): ID of the check used for the notification dependency
        notifications (list): list of objects containing contact ID, delay, and scheduling for notifications
        mute (bool|int): bool or millisecond timestamp (UTC) in the future. True to mute indefinitely
    """

    target: str
    port: int = 143
    verify: bool = True
    username: str = ""
    password: str = ""
    secure: bool = False
    warningdays: int = 0
    label: str = ""
    autodiag: bool = DEFAULTS["autodiag"]
    interval: int = DEFAULTS["interval"]
    enabled: bool = DEFAULTS["enabled"]
    public: bool = DEFAULTS["enabled"]
    runlocations: str | list = DEFAULTS["runlocations"]
    homeloc: str | bool = DEFAULTS["homeloc"]
    threshold: int = DEFAULTS["threshold"]
    sens: int = DEFAULTS["sens"]
    dep: str = DEFAULTS["dep"]
    notifications: list = field(default_factory=list)
    mute: bool = DEFAULTS["mute"]
    type: str = "IMAP4"

    def __post_init__(self):
        self.type = "IMAP4"


@dataclass
class MongodbCheck:
    """NodePing MONGODB check.

    `fields` example:

    fields = {
        "processmem": {
            "name": "processmem",
            "min": 1000,
            "max": 5000
        },
        "cpuload": {
            "name": "cpuload",
            "min": 1,
            "max": 5
        }
    }

    Args:
        target (str): URL to target host
        query (str): JSON query to send to the database server (limit 25 results)
        fields (dict): Queries results to match.
        label (str): Name of the check that will be created
        autodiag (bool): Enable/disable auto diagnostics for this check
        interval (int): Interval in minutes to monitor target
        enabled (bool): If created check will be enabled or disabled
        public (bool): If the results for the created check will be public or not
        runlocations (str|list): Which region to be originated from
        homeloc (str|bool): Which probe in the region to originate the check from
        threshold (int): Time in seconds for an acceptable response
        sens (int): Rechecks to help avoid unecessary notifications
        dep (str): ID of the check used for the notification dependency
        notifications (list): list of objects containing contact ID, delay, and scheduling for notifications
        mute (bool|int): bool or millisecond timestamp (UTC) in the future. True to mute indefinitely
    """

    target: str
    query: str = ""
    fields: dict = field(default_factory=dict)
    database: str = ""
    namespace: str = ""
    label: str = ""
    autodiag: bool = DEFAULTS["autodiag"]
    interval: int = DEFAULTS["interval"]
    enabled: bool = DEFAULTS["enabled"]
    public: bool = DEFAULTS["enabled"]
    runlocations: str | list = DEFAULTS["runlocations"]
    homeloc: str | bool = DEFAULTS["homeloc"]
    threshold: int = DEFAULTS["threshold"]
    sens: int = DEFAULTS["sens"]
    dep: str = DEFAULTS["dep"]
    notifications: list = field(default_factory=list)
    mute: bool = DEFAULTS["mute"]
    type: str = "MONGODB"

    def __post_init__(self):
        self.type = "MONGODB"


@dataclass
class MtrCheck:
    """NodePing MTR check.

    Args:
        target (str): URL to target host
        ipv6 (bool): Whether to resolve IPv4 or IPv6
        label (str): Name of the check that will be created
        autodiag (bool): Enable/disable auto diagnostics for this check
        interval (int): Interval in minutes to monitor target
        enabled (bool): If created check will be enabled or disabled
        public (bool): If the results for the created check will be public or not
        runlocations (str|list): Which region to be originated from
        homeloc (str|bool): Which probe in the region to originate the check from
        threshold (int): Time in seconds for an acceptable response
        sens (int): Rechecks to help avoid unecessary notifications
        dep (str): ID of the check used for the notification dependency
        notifications (list): list of objects containing contact ID, delay, and scheduling for notifications
        mute (bool|int): bool or millisecond timestamp (UTC) in the future. True to mute indefinitely
    """

    target: str
    ipv6: bool = False
    label: str = ""
    autodiag: bool = DEFAULTS["autodiag"]
    interval: int = DEFAULTS["interval"]
    enabled: bool = DEFAULTS["enabled"]
    public: bool = DEFAULTS["enabled"]
    runlocations: str | list = DEFAULTS["runlocations"]
    homeloc: str | bool = DEFAULTS["homeloc"]
    threshold: int = DEFAULTS["threshold"]
    sens: int = DEFAULTS["sens"]
    dep: str = DEFAULTS["dep"]
    notifications: list = field(default_factory=list)
    mute: bool = DEFAULTS["mute"]
    type: str = "MTR"

    def __post_init__(self):
        self.type = "MTR"


@dataclass
class MySqlCheck:
    """NodePing MYSQL check.

    `fields` example:

    fields = {
        "checknum": {
            "name": "checknum",
            "min": 0,
            "max": 5
        },
        "checkstring": {
            "name": "checkstring",
            "match": "exactmatch"
        }
    }

    Args:
        target (str): URL to target host
        port (int): port used to test communications
        username (str): username for testing logins
        password (str): Password to authenticate to database
        secure (bool): Whether SSL/TLS should be used
        database (str): name of database to query
        query (str): SQL query to send to the database server
        fields (dict): Queries results to match.
        ipv6 (bool): Whether to resolve IPv4 or IPv6
        label (str): Name of the check that will be created
        autodiag (bool): Enable/disable auto diagnostics for this check
        interval (int): Interval in minutes to monitor target
        enabled (bool): If created check will be enabled or disabled
        public (bool): If the results for the created check will be public or not
        runlocations (str|list): Which region to be originated from
        homeloc (str|bool): Which probe in the region to originate the check from
        threshold (int): Time in seconds for an acceptable response
        sens (int): Rechecks to help avoid unecessary notifications
        dep (str): ID of the check used for the notification dependency
        notifications (list): list of objects containing contact ID, delay, and scheduling for notifications
        mute (bool|int): bool or millisecond timestamp (UTC) in the future. True to mute indefinitely
    """

    target: str
    port: int = 3306
    username: str = ""
    password: str = ""
    secure: bool = False
    database: str = ""
    query: str = ""
    fields: dict = field(default_factory=dict)
    ipv6: bool = False
    label: str = ""
    autodiag: bool = DEFAULTS["autodiag"]
    interval: int = DEFAULTS["interval"]
    enabled: bool = DEFAULTS["enabled"]
    public: bool = DEFAULTS["enabled"]
    runlocations: str | list = DEFAULTS["runlocations"]
    homeloc: str | bool = DEFAULTS["homeloc"]
    threshold: int = DEFAULTS["threshold"]
    sens: int = DEFAULTS["sens"]
    dep: str = DEFAULTS["dep"]
    notifications: list = field(default_factory=list)
    mute: bool = DEFAULTS["mute"]
    type: str = "MYSQL"

    def __post_init__(self):
        self.type = "MYSQL"


@dataclass
class NtpCheck:
    """NodePing NTP check.

    Args:
        target (str): URL to target host
        port (int): port used to test communications
        invert (bool): Pass if it responds (True) or not (False)
        label (str): Name of the check that will be created
        autodiag (bool): Enable/disable auto diagnostics for this check
        interval (int): Interval in minutes to monitor target
        enabled (bool): If created check will be enabled or disabled
        public (bool): If the results for the created check will be public or not
        runlocations (str|list): Which region to be originated from
        homeloc (str|bool): Which probe in the region to originate the check from
        threshold (int): Time in seconds for an acceptable response
        sens (int): Rechecks to help avoid unecessary notifications
        dep (str): ID of the check used for the notification dependency
        notifications (list): list of objects containing contact ID, delay, and scheduling for notifications
        mute (bool|int): bool or millisecond timestamp (UTC) in the future. True to mute indefinitely
    """

    target: str
    port: int = 123
    invert: bool = False
    label: str = ""
    autodiag: bool = DEFAULTS["autodiag"]
    interval: int = DEFAULTS["interval"]
    enabled: bool = DEFAULTS["enabled"]
    public: bool = DEFAULTS["enabled"]
    runlocations: str | list = DEFAULTS["runlocations"]
    homeloc: str | bool = DEFAULTS["homeloc"]
    threshold: int = DEFAULTS["threshold"]
    sens: int = DEFAULTS["sens"]
    dep: str = DEFAULTS["dep"]
    notifications: list = field(default_factory=list)
    mute: bool = DEFAULTS["mute"]
    type: str = "NTP"

    def __post_init__(self):
        self.type = "NTP"


@dataclass
class PingCheck:
    """NodePing PING check.

    Args:
        target (str): URL to target host
        ipv6 (bool): Whether to resolve IPv4 or IPv6
        label (str): Name of the check that will be created
        autodiag (bool): Enable/disable auto diagnostics for this check
        interval (int): Interval in minutes to monitor target
        enabled (bool): If created check will be enabled or disabled
        public (bool): If the results for the created check will be public or not
        runlocations (str|list): Which region to be originated from
        homeloc (str|bool): Which probe in the region to originate the check from
        threshold (int): Time in seconds for an acceptable response
        sens (int): Rechecks to help avoid unecessary notifications
        dep (str): ID of the check used for the notification dependency
        notifications (list): list of objects containing contact ID, delay, and scheduling for notifications
        mute (bool|int): bool or millisecond timestamp (UTC) in the future. True to mute indefinitely
    """

    target: str
    ipv6: bool = False
    label: str = ""
    autodiag: bool = DEFAULTS["autodiag"]
    interval: int = DEFAULTS["interval"]
    enabled: bool = DEFAULTS["enabled"]
    public: bool = DEFAULTS["enabled"]
    runlocations: str | list = DEFAULTS["runlocations"]
    homeloc: str | bool = DEFAULTS["homeloc"]
    threshold: int = DEFAULTS["threshold"]
    sens: int = DEFAULTS["sens"]
    dep: str = DEFAULTS["dep"]
    notifications: list = field(default_factory=list)
    mute: bool = DEFAULTS["mute"]
    type: str = "PING"

    def __post_init__(self):
        self.type = "PING"


@dataclass
class Pop3Check:
    """NodePing POP3 check.

    Args:
        target (str): URL to target host
        port (int): port used to test POP3 communications
        verify (bool): The check should fail if the SSL/TLS certificate is invalid
        username (str): Email address for testing logins
        password (str): Password to authenticate email address
        secure (bool): Whether SSL/TLS should be used
        warningdays (int): Warning days befor certificate expiration
        label (str): Name of the check that will be created
        autodiag (bool): Enable/disable auto diagnostics for this check
        interval (int): Interval in minutes to monitor target
        enabled (bool): If created check will be enabled or disabled
        public (bool): If the results for the created check will be public or not
        runlocations (str|list): Which region to be originated from
        homeloc (str|bool): Which probe in the region to originate the check from
        threshold (int): Time in seconds for an acceptable response
        sens (int): Rechecks to help avoid unecessary notifications
        dep (str): ID of the check used for the notification dependency
        notifications (list): list of objects containing contact ID, delay, and scheduling for notifications
        mute (bool|int): bool or millisecond timestamp (UTC) in the future. True to mute indefinitely
    """

    target: str
    port: int = 110
    verify: bool = True
    username: str = ""
    password: str = ""
    secure: bool = False
    warningdays: int = 0
    label: str = ""
    autodiag: bool = DEFAULTS["autodiag"]
    interval: int = DEFAULTS["interval"]
    enabled: bool = DEFAULTS["enabled"]
    public: bool = DEFAULTS["enabled"]
    runlocations: str | list = DEFAULTS["runlocations"]
    homeloc: str | bool = DEFAULTS["homeloc"]
    threshold: int = DEFAULTS["threshold"]
    sens: int = DEFAULTS["sens"]
    dep: str = DEFAULTS["dep"]
    notifications: list = field(default_factory=list)
    mute: bool = DEFAULTS["mute"]
    type: str = "POP3"

    def __post_init__(self):
        self.type = "POP3"


@dataclass
class PortCheck:
    """NodePing PORT check.

    Args:
        target (str): URL to target host
        port (int): Port to check
        invert (bool): True if accepts connection, False if does not accept connection to pass
        label (str): Name of the check that will be created
        autodiag (bool): Enable/disable auto diagnostics for this check
        interval (int): Interval in minutes to monitor target
        enabled (bool): If created check will be enabled or disabled
        public (bool): If the results for the created check will be public or not
        runlocations (str|list): Which region to be originated from
        homeloc (str|bool): Which probe in the region to originate the check from
        threshold (int): Time in seconds for an acceptable response
        sens (int): Rechecks to help avoid unecessary notifications
        dep (str): ID of the check used for the notification dependency
        notifications (list): list of objects containing contact ID, delay, and scheduling for notifications
        mute (bool|int): bool or millisecond timestamp (UTC) in the future. True to mute indefinitely
    """

    target: str
    port: int
    invert: bool = False
    label: str = ""
    autodiag: bool = DEFAULTS["autodiag"]
    interval: int = DEFAULTS["interval"]
    enabled: bool = DEFAULTS["enabled"]
    public: bool = DEFAULTS["enabled"]
    runlocations: str | list = DEFAULTS["runlocations"]
    homeloc: str | bool = DEFAULTS["homeloc"]
    threshold: int = DEFAULTS["threshold"]
    sens: int = DEFAULTS["sens"]
    dep: str = DEFAULTS["dep"]
    notifications: list = field(default_factory=list)
    mute: bool = DEFAULTS["mute"]
    type: str = "PORT"

    def __post_init__(self):
        self.type = "PORT"


@dataclass
class PostgreSqlCheck:
    """NodePing PGSQL check.

    `fields` example:

    fields = {
        "checknum": {
            "name": "checknum",
            "min": 0,
            "max": 5
        },
        "checkstring": {
            "name": "checkstring",
            "match": "exactmatch"
        }
    }

    Args:
        target (str): URL to target host
        query (str): SQL query to send to the database server
        fields (dict): Queries results to match.
        ipv6 (bool): Whether to resolve IPv4 or IPv6
        label (str): Name of the check that will be created
        autodiag (bool): Enable/disable auto diagnostics for this check
        interval (int): Interval in minutes to monitor target
        enabled (bool): If created check will be enabled or disabled
        public (bool): If the results for the created check will be public or not
        runlocations (str|list): Which region to be originated from
        homeloc (str|bool): Which probe in the region to originate the check from
        threshold (int): Time in seconds for an acceptable response
        sens (int): Rechecks to help avoid unecessary notifications
        dep (str): ID of the check used for the notification dependency
        notifications (list): list of objects containing contact ID, delay, and scheduling for notifications
        mute (bool|int): bool or millisecond timestamp (UTC) in the future. True to mute indefinitely
    """

    target: str
    query: str = ""
    fields: dict = field(default_factory=dict)
    ipv6: bool = False
    label: str = ""
    autodiag: bool = DEFAULTS["autodiag"]
    interval: int = DEFAULTS["interval"]
    enabled: bool = DEFAULTS["enabled"]
    public: bool = DEFAULTS["enabled"]
    runlocations: str | list = DEFAULTS["runlocations"]
    homeloc: str | bool = DEFAULTS["homeloc"]
    threshold: int = DEFAULTS["threshold"]
    sens: int = DEFAULTS["sens"]
    dep: str = DEFAULTS["dep"]
    notifications: list = field(default_factory=list)
    mute: bool = DEFAULTS["mute"]
    type: str = "PGSQL"

    def __post_init__(self):
        self.type = "PGSQL"


@dataclass
class PushCheck:
    """NodePing PUSH check.

    `fields` example:

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

    Args:
        checktoken (str): "reset" to regenerate the checktoken, or set to an empty string
        fields (dict): Contents of each metric collected with min/max values
        label (str): Name of the check that will be created
        autodiag (bool): Enable/disable auto diagnostics for this check
        interval (int): Interval in minutes to monitor target
        enabled (bool): If created check will be enabled or disabled
        public (bool): If the results for the created check will be public or not
        runlocations (str|list): Which region to be originated from
        homeloc (str|bool): Which probe in the region to originate the check from
        threshold (int): Time in seconds for an acceptable response
        sens (int): Rechecks to help avoid unecessary notifications
        dep (str): ID of the check used for the notification dependency
        notifications (list): list of objects containing contact ID, delay, and scheduling for notifications
        mute (bool|int): bool or millisecond timestamp (UTC) in the future. True to mute indefinitely
    """

    checktoken: str = "reset"
    fields: dict = field(default_factory=dict)
    label: str = ""
    autodiag: bool = DEFAULTS["autodiag"]
    interval: int = DEFAULTS["interval"]
    enabled: bool = DEFAULTS["enabled"]
    public: bool = DEFAULTS["enabled"]
    runlocations: str | list = DEFAULTS["runlocations"]
    homeloc: str | bool = DEFAULTS["homeloc"]
    threshold: int = DEFAULTS["threshold"]
    sens: int = DEFAULTS["sens"]
    dep: str = DEFAULTS["dep"]
    notifications: list = field(default_factory=list)
    mute: bool = DEFAULTS["mute"]
    type: str = "PUSH"

    def __post_init__(self):
        self.type = "PUSH"


@dataclass
class RedisCheck:
    """NodePing REDIS check.

    Args:
        target (str): URL to target host
        redistype (str): standalone, sentinel, cluster
        hosts (list): For sentinel or cluster. The hostname, port, and password to connect
        sentinelname (str): The master/primary name for the sentinel to query
        label (str): Name of the check that will be created
        autodiag (bool): Enable/disable auto diagnostics for this check
        interval (int): Interval in minutes to monitor target
        enabled (bool): If created check will be enabled or disabled
        public (bool): If the results for the created check will be public or not
        runlocations (str|list): Which region to be originated from
        homeloc (str|bool): Which probe in the region to originate the check from
        threshold (int): Time in seconds for an acceptable response
        sens (int): Rechecks to help avoid unecessary notifications
        dep (str): ID of the check used for the notification dependency
        notifications (list): list of objects containing contact ID, delay, and scheduling for notifications
        mute (bool|int): bool or millisecond timestamp (UTC) in the future. True to mute indefinitely
    """

    target: str
    redistype: str
    sentinelname: str = ""
    hosts: list = field(default_factory=list)
    label: str = ""
    autodiag: bool = DEFAULTS["autodiag"]
    interval: int = DEFAULTS["interval"]
    enabled: bool = DEFAULTS["enabled"]
    public: bool = DEFAULTS["enabled"]
    runlocations: str | list = DEFAULTS["runlocations"]
    homeloc: str | bool = DEFAULTS["homeloc"]
    threshold: int = DEFAULTS["threshold"]
    sens: int = DEFAULTS["sens"]
    dep: str = DEFAULTS["dep"]
    notifications: list = field(default_factory=list)
    mute: bool = DEFAULTS["mute"]
    type: str = "REDIS"

    def __post_init__(self):
        self.type = "REDIS"


@dataclass
class RblCheck:
    """NodePing RBL check.

    Args:
        target (str): URL to target host
        ignore (str): comma separated list of RBLs to ignore
        label (str): Name of the check that will be created
        autodiag (bool): Enable/disable auto diagnostics for this check
        interval (int): Interval in minutes to monitor target
        enabled (bool): If created check will be enabled or disabled
        public (bool): If the results for the created check will be public or not
        runlocations (str|list): Which region to be originated from
        homeloc (str|bool): Which probe in the region to originate the check from
        threshold (int): Time in seconds for an acceptable response
        sens (int): Rechecks to help avoid unecessary notifications
        dep (str): ID of the check used for the notification dependency
        notifications (list): list of objects containing contact ID, delay, and scheduling for notifications
        mute (bool|int): bool or millisecond timestamp (UTC) in the future. True to mute indefinitely
    """

    target: str
    ignore: str = ""
    label: str = ""
    autodiag: bool = DEFAULTS["autodiag"]
    interval: int = DEFAULTS["interval"]
    enabled: bool = DEFAULTS["enabled"]
    public: bool = DEFAULTS["enabled"]
    runlocations: str | list = DEFAULTS["runlocations"]
    homeloc: str | bool = DEFAULTS["homeloc"]
    threshold: int = DEFAULTS["threshold"]
    sens: int = DEFAULTS["sens"]
    dep: str = DEFAULTS["dep"]
    notifications: list = field(default_factory=list)
    mute: bool = DEFAULTS["mute"]
    type: str = "RBL"

    def __post_init__(self):
        self.type = "RBL"
