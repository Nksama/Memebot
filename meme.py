import requests
from pyrogram import filters , Client 
import os

api_id = os.environ.get('API_ID')
api_hash = os.environ.get('API_HASH')
token = os.environ.get('TOKEN')


bot = Client(
	"memebot",
	api_id=api_id,
	api_hash=api_hash,
	bot_token=token
	)



@bot.on_message(filters.command('start'))
def start(_,message):
	message.reply_text('.' , parse_mode='markdown')





@bot.on_message(filters.command('meme'))
def meme(_,message):
	r = requests.get('https://nksamamemeapi.pythonanywhere.com').json()
	pic = r['image']
	title = r['title']
	bot.send_photo(message.chat.id , pic , caption=title)




@bot.on_message(filters.command('hmeme') & filters.private)
def hmeme(_,message):
	r = requests.get('https://nksamamemeapi.pythonanywhere.com/get/hentaimemes').json()
	pic = r['image']
	title = r['title']
	bot.send_photo(message.chat.id , pic , caption=title)





bot.run()
