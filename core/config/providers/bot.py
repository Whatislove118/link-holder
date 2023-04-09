from pydantic import BaseModel

from core.config.providers.bot_platforms import TelegramBotSettings


class BotSettings(BaseModel):
    telegram: TelegramBotSettings
