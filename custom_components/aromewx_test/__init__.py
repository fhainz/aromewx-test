from __future__ import annotations

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant

from .coordinator import AromeWxTestCoordinator

PLATFORMS: list[str] = []

AromeWxTestConfigEntry = ConfigEntry[AromeWxTestCoordinator]


async def async_setup_entry(hass: HomeAssistant, entry: AromeWxTestConfigEntry) -> bool:
    coordinator = AromeWxTestCoordinator(hass)
    await coordinator.async_config_entry_first_refresh()
    entry.runtime_data = coordinator
    return True


async def async_unload_entry(hass: HomeAssistant, entry: AromeWxTestConfigEntry) -> bool:
    return True
