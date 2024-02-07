"""nornir dispatcher for Aruba OS."""

from .default import NetmikoNautobotNornirDriver as DefaultNautobotNornirDriver


class NautobotNornirDriver(DefaultNautobotNornirDriver):
    """Driver for Aruba OS."""

    config_command = "show run"
