import reflex as rx
from reflex_admin.styles.tailwind_config import tw_config

config = rx.Config(
    app_name="reflex_admin",
    telemetry_enabled=False,
    tailwind=tw_config,
)
