from aiogram import types

from bot.core import dp


class HandlerHolder:
    """Simply grouping handlers for import as one class."""

    @dp.message_handler(commands=["start", "help"])
    async def send_welcome(message: types.Message) -> None:
        """This handler will be called when user sends `/start` or `/help`
        command."""
        await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")

    @dp.message_handler()
    async def echo(message: types.Message) -> None:
        # old style:
        # await bot.send_message(message.chat.id, message.text)

        await message.answer(message.text)
