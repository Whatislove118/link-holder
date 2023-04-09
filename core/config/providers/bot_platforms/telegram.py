from pydantic import BaseModel

__all__ = ["TelegramBotSettings"]


class TelegramBotSettings(BaseModel):
    token: str
