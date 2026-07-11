from homeassistant.config_entries import ConfigFlow

from .const import DOMAIN


class AromeWxTestConfigFlow(ConfigFlow, domain=DOMAIN):
    async def async_step_user(self, user_input=None):
        return self.async_show_form(step_id="user")
