from aiogram import F, Router, Bot

from aiogram.filters import CommandStart, Command, CommandObject
from aiogram.types import Message, LabeledPrice
from aiogram.utils.keyboard import InlineKeyboardBuilder

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message, ):
    await message.answer("Привет, введи /donate")


@router.message(Command("donate_1"))
@router.message(Command("donate_25"))
@router.message(Command("donate_50"))
@router.message(Command("donate"))
async def cmd_donate(message: Message, command: CommandObject):
    if command.command != "donate":
        amount = int(command.command.split("_")[1])
    else:
        if command.args is None or not command.args.isdigit() or not 1 <= int(command.args) <= 2500:
            await message.answer('Error')
            return
        amount = int(command.args)

    builder = InlineKeyboardBuilder()
    builder.button(
        text=f"pay {amount} XTR",
        pay=True
    )
    builder.button(
        text="Cancel",
        callback_data="cancel"
    )
    builder.adjust(1)

    prices = [LabeledPrice(label="XTR", amount=amount)]
    await message.answer_invoice(
        title="Free donate",
        description=f"Amount : {amount}",
        prices=prices,
        provider_token="",
        payload=f"{amount}_stars",
        currency="XTR",
        reply_markup=builder.as_markup()
        )