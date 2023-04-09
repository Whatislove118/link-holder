import asyncio
import sys

import uvloop

from core.config.default import settings

asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

print(settings)


if __name__ == "__main__":
    try:
        mode = sys.argv[1]
    except Exception:
        mode = "bot"

    if mode == "bot":
        from aiogram import executor

        from bot import dp

        executor.start_polling(dispatcher=dp, skip_updates=True)
