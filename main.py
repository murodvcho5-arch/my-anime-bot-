import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

# TOKENINGIZNI QUYING
TOKEN = "YANGI_TOKENINGIZNI_SHU_YERGA_QUYING"

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start_cmd(message: types.Message):
    await message.answer("Bot muvaffaqiyatli ishga tushdi!")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
