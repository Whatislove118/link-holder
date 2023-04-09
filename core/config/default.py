import json
import typing as t
from pathlib import Path
from typing import Any

from pydantic import BaseSettings

from core.config.providers.bot import BotSettings


def json_config_settings_source(settings: BaseSettings) -> dict[str, Any]:
    encoding = settings.__config__.env_file_encoding
    env_file = settings.__config__.env_file
    return json.loads(Path(env_file).read_text(encoding))


class Settings(BaseSettings):
    bot: BotSettings

    class Config:
        env_file_encoding = "utf-8"
        env_file = ".env.json"

        @classmethod
        @t.no_type_check
        def customise_sources(
            cls,
            init_settings,
            env_settings,
            file_secret_settings,
        ):
            return (
                init_settings,
                json_config_settings_source,
                env_settings,
                file_secret_settings,
            )


settings = Settings()
