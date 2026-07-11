import voluptuous as vol

from homeassistant.config_entries import ConfigFlow
from homeassistant.helpers import selector

from .const import DOMAIN


class AromeWxTestConfigFlow(ConfigFlow, domain=DOMAIN):
    async def async_step_user(self, user_input=None):
        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema(
                {
                    vol.Required(
                        "latitude", default=self.hass.config.latitude
                    ): selector.NumberSelector(
                        selector.NumberSelectorConfig(
                            step=0.0001, mode=selector.NumberSelectorMode.BOX
                        )
                    ),
                }
            ),
        )
