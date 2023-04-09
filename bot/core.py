import asyncio

from aiogram import Bot, Dispatcher

from core.config.default import settings

tg_bot = Bot(token=settings.bot.telegram.token, loop=asyncio.get_event_loop())
dp = Dispatcher(tg_bot)
