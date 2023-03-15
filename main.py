from aiogram import Bot, Dispatcher, executor, types
from config import API_TOKEN

API_TOKEN = API_TOKEN

bot = Bot(API_TOKEN)
disp = Dispatcher(bot)

@disp.message_handler()
async def echo_message(message: types.Message):
    if message.text.count(' ') >= 1:  # if user > 1 word
        await message.answer(text=message.text)


if __name__ == '__main__':
    executor.start_polling(disp)
