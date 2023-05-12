import logging
from aiogram import Bot, Dispatcher, executor, types
from decouple import config

from googleLookup import make_translate

API_TOKEN = config('TOKEN', default="Your token")

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)




@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    
    await message.reply("Hi!\nI'm Goole translate bot\nPowered by aiogram.")


@dp.message_handler(commands=['help'])
async def send_welcome(message: types.Message):
    
    await message.reply("if you have any question, write to me, @orifov_islombek")


@dp.message_handler()
async def echo(message: types.Message):
    word = make_translate(message.text)
    if word.get('prononciation'):
        sending_message = f"So'z: {word['word']}\nTarjimasi: {word['translate']}"\
                           "\nTalaffuzi: {word['prononciation']}"
    else:
        sending_message = f"So'z: {word['word']}\nTarjimasi: {word['translate']}"
    await message.answer(sending_message)



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)