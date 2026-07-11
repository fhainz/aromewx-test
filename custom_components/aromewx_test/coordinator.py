from __future__ import annotations

import datetime
import logging

from homeassistant.core import HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator

LOGGER = logging.getLogger(__name__)


class AromeWxTestCoordinator(DataUpdateCoordinator[dict]):
    def __init__(self, hass: HomeAssistant) -> None:
        super().__init__(
            hass,
            LOGGER,
            name="aromewx_test",
            update_interval=datetime.timedelta(minutes=15),
        )

    async def _async_update_data(self) -> dict:
        return {}
