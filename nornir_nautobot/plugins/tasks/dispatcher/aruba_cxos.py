"""nornir dispatcher for Aruba CXOS."""

from nornir_nautobot.plugins.tasks.dispatcher.default import NapalmDefault, NetmikoDefault


class NapalmArubaCxos(NapalmDefault):
    """Collection of Napalm Nornir Tasks specific to Aruba CXOS devices."""


class NetmikoArubaCxos(NetmikoDefault):
    """Collection of Netmiko Nornir Tasks specific to Aruba CXOS devices."""

    config_command = "show run"
