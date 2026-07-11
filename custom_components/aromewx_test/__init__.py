from __future__ import annotations

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant

PLATFORMS: list[str] = []

AromeWxTestConfigEntry = ConfigEntry[dict]


async def async_setup_entry(hass: HomeAssistant, entry: AromeWxTestConfigEntry) -> bool:
    return True


async def async_unload_entry(hass: HomeAssistant, entry: AromeWxTestConfigEntry) -> bool:
    return True
