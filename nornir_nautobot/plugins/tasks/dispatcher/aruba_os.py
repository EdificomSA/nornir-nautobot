"""nornir dispatcher for Aruba OS."""

from nornir_nautobot.plugins.tasks.dispatcher.default import NapalmDefault, NetmikoDefault


class NapalmArubaOs(NapalmDefault):
    """Collection of Napalm Nornir Tasks specific to Aruba OS devices."""


class NetmikoArubaOs(NetmikoDefault):
    """Collection of Netmiko Nornir Tasks specific to Aruba OS devices."""

    config_command = "show run"
