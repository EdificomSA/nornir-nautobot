"""nornir dispatcher for Aruba AOSCX."""

from nornir_nautobot.plugins.tasks.dispatcher.default import NapalmDefault, NetmikoDefault


class NapalmArubaAoscx(NapalmDefault):
    """Collection of Napalm Nornir Tasks specific to Aruba AOSCX devices."""


class NetmikoArubaAoscx(NetmikoDefault):
    """Collection of Netmiko Nornir Tasks specific to Aruba AOSCX devices."""

    config_command = "show run"
