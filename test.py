import telebot
from telebot import types

import random
import requests
import json
import string

import threading
from datetime import datetime, timedelta
import time

from SimpleQIWI import *
import sqlite3

import others
from telebot.types import LabeledPrice
prices = [LabeledPrice(label='🌳Шишки АК-47 1г🐲',amount=23000)]
prices_1 = [LabeledPrice(label='🌿OG KUSH БШ 3г🌿',amount=18000)]
prices_2 = [LabeledPrice(label='🌳Шишки АК-47 2г🐲',amount=40000)]
prices_3 = [LabeledPrice(label='🤯Шишки Amnesia 1г🐉',amount=23000)]
prices_4 = [LabeledPrice(label='🤯Шишки Amnesia 2г🐉',amount=40000)]
prices_5 = [LabeledPrice(label='🧪Alfa PVP DeLuxe 0.5г💎',amount=25000)]
prices_6 = [LabeledPrice(label='💎Alfa PVP DeLuxe 1г💎',amount=40000)]
prices_7 = [LabeledPrice(label='💎Амфетамин Сульфат 0.5г💎',amount=25000)]
prices_8 = [LabeledPrice(label='💎Амфетамин Сульфат 1г💎',amount=37000)]
prices_9 = [LabeledPrice(label='🦠Мефедрон  0.5г🦠',amount=24000)]
prices_10 = [LabeledPrice(label='💊Экстези Etherium😻',amount=40000)]
prices_11 = [LabeledPrice(label='💊Экстези Batman🦇',amount=40000)]
prices_12 = [LabeledPrice(label='OG KUSH БШ 3г🌳',amount=18000)]
prices_13 = [LabeledPrice(label='План(Сыпуха) 3г🌱',amount=15000)]
prices_14 = [LabeledPrice(label='Шишки Mango Haze 1г🐍',amount=23000)]
prices_15 = [LabeledPrice(label='Амфетамин Розовый 0.5г💎',amount=25000)]
prices_16 = [LabeledPrice(label='Шишки OG-Kush 1г☘️',amount=23000)]
prices_17 = [LabeledPrice(label='Alfa PVP DeLuxe 0.5г💎',amount=25000)]
prices_18 = [LabeledPrice(label='Амфетамин Розовый 1г💎',amount=40000)]
prices_19 = [LabeledPrice(label='Экстези Barcelona💊',amount=40000)]
prices_20 = [LabeledPrice(label='Печеньки с ТГК🍪',amount=22000)]
prices_21 = [LabeledPrice(label='Битые шишки 3г🌱',amount=18000)]
prices_22 = [LabeledPrice(label='Шишки АК-47 1г🌳',amount=23000)]
prices_23 = [LabeledPrice(label='Шишки Pablo Escobar 1г🐍',amount=23000)]
prices_24 = [LabeledPrice(label='Alfa PVP DeLuxe 0.5г⚗🧬',amount=25000)]
prices_25 = [LabeledPrice(label='Амфетамин Сульфат 0.5г⚗️',amount=24000)]
prices_26 = [LabeledPrice(label='Амфетамин Сульфат 1г🧬',amount=40000)]
prices_27 = [LabeledPrice(label='Гаш Марроко 0.5🌳',amount=30000)]
prices_28 = [LabeledPrice(label='Экстези Batman💊',amount=40000)]
prices_29 = [LabeledPrice(label='Афганка БШ 3г🍃',amount=18000)]
prices_30 = [LabeledPrice(label='Шишки Lemon Haze 1г🐲',amount=23000)]
prices_31 = [LabeledPrice(label='Шишки Amnesia 1г🌳',amount=23000)]
prices_32 = [LabeledPrice(label='Alfa PVP DeLuxe 0.5г💎',amount=25000)]
prices_33 = [LabeledPrice(label='Амфетамин Сульфат 0.5г💎',amount=24000)]
prices_34 = [LabeledPrice(label='Мефедрон  0.5г💎',amount=25000)]
prices_35 = [LabeledPrice(label='Экстези TikTok💊',amount=40000)]
prices_36 = [LabeledPrice(label='LSD-25💿',amount=40000)]







bot = telebot.TeleBot(others.bot_token)
admin_user_id = others.admin_user_id
channel_id = others.channel_id

in_comment = []
threads = list()

# Главная клавиатура
markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
profile = types.KeyboardButton('🔱Мой профиль🔱')
catalog = types.KeyboardButton('💵Купить💵')
support = types.KeyboardButton('Поддержка')
rules = types.KeyboardButton('‼️Правила‼️')
markup.add(profile, catalog)
markup.add(rules)
# Главная клавиатура

# Каталог
product = types.ReplyKeyboardMarkup(resize_keyboard=True)
poltava = types.KeyboardButton('Полтава')
xar = types.KeyboardButton('Харьков')
dnepr = types.KeyboardButton('Ахтырка')
sumy = types.KeyboardButton('Сумы')
back = types.KeyboardButton('🔙Назад🔙')
product.add(dnepr, sumy, poltava)


product.add(back)
# Каталог

# Вкусы

# Вкусы

# Этап заказа 0 - товар 1 - вкус 2 - город 3 - количество HQD
user_dict = {}
class User:
    def __init__(self, city):
        self.city = city

        keys = ['name', 'taste', 'country', 
                'amount']
        
        for key in keys:
            self.key = None

def enterAmount(message):
	try:
		chat_id = message.chat.id
		chat_message = int(message.text)

		user = user_dict[chat_id]
		user.amount = message.text
		
		inline_keyboard = types.InlineKeyboardMarkup(row_width=1)
		inline = types.InlineKeyboardButton(text="Купить", callback_data='BUY')
		inline_keyboard.add(inline)
		if (user.id == '0'):
			bot.send_message(chat_id, "💁🏻‍♀️ Заказ *готов*!", parse_mode="Markdown", reply_markup=markup)
			Price = others.get_price_from_name(user.name)
			Price = Price * int(user.amount)
			bot.send_message(chat_id, f"*Товар:* {user.name}" +
				f"\n*Вкус:* {user.taste}\n*Цена:* {others.get_price_from_name(user.name)} ₽\n*Количество:* {user.amount}\n*К оплате:* {Price}\n"
				+ f"*Доставка в:* город {user.country}\n\nℹ️ После покупки данного товара с *Вами свяжется менеджер*", parse_mode="Markdown", reply_markup=inline_keyboard)
		elif (user.id == '1'):
			name = user.name.split(" ")
			Price = others.get_price_from_name(name[1])
			Price = Price * int(user.amount)
			bot.send_message(chat_id, "💁🏻‍♀️ Заказ *готов*!", parse_mode="Markdown", reply_markup=markup)
			bot.send_message(chat_id, f"*Товар:* картридж {name[0]}\n*Упаковка:* {name[1]} шт.\n*Цена:* {others.get_price_from_name(user.name)} ₽\n"
				+ f"*Количество:* {user.amount}\n*К оплате:* {Price}\n*Доставка в:* город {user.country}\n\nℹ️ После покупки данного товара с *Вами свяжется менеджер*",
				parse_mode="Markdown", reply_markup=inline_keyboard)
		else:
			bot.send_message(chat_id, "😟 Заказ не был *найден*.", parse_mode="Markdown")
	except:
		pass

def enterCountry(message):
	try:
		chat_id = message.chat.id
		chat_message = message.text

		tastes = types.ReplyKeyboardRemove(selective=False)

		user = user_dict[chat_id]
		user.country = message.text
		

		msg = bot.send_message(chat_id, "💁🏻‍♀️ Введите *количество* которое хотите приобрести", parse_mode="Markdown", reply_markup=tastes)
		bot.register_next_step_handler(msg, enterAmount)
	except:
		pass

def enterTastes(message):
	try:
		chat_id = message.chat.id
		chat_message = message.text

		tastes = types.ReplyKeyboardRemove(selective=False)

		user = user_dict[chat_id]
		user.taste = message.text

		msg = bot.send_message(chat_id, "💁🏻‍♀️ Напишите Ваш *город*", parse_mode="Markdown", reply_markup=tastes)
		bot.register_next_step_handler(msg, enterCountry)
	except:
		pass

def enterCount(message):
	chat_id = message.chat.id
	count = message.text

	user = user_dict[chat_id]

	tastes = types.ReplyKeyboardRemove(selective=False)

	if (count == '2'):
		user.name += ' 2'
		msg = bot.send_message(chat_id, "💁🏻‍♀️ Напишите Ваш *город*", parse_mode="Markdown", reply_markup=tastes)
		bot.register_next_step_handler(msg, enterCountry)
	elif (count == '4'):
		user.name += ' 4'
		msg = bot.send_message(chat_id, "💁🏻‍♀️ Напишите Ваш *город*", parse_mode="Markdown", reply_markup=tastes)
		bot.register_next_step_handler(msg, enterCountry)
	else:
		bot.send_message(chat_id, "😟 Данной упаковки *нет в наличии*", parse_mode="Markdown")
# Этап заказа

# Этап заказа 0 - товар 1 - вкус 2 - город 3 - количество Juul
def enterTastesJuul(message):
	try:
		chat_id = message.chat.id
		chat_message = message.text

		tastes = types.ReplyKeyboardRemove(selective=False)

		user = user_dict[chat_id]
		user.taste = message.text

		msg = bot.send_message(chat_id, "💁🏻‍♀️ Напишите Ваш *город*", parse_mode="Markdown", reply_markup=tastes)
		bot.register_next_step_handler(msg, enterCountry)
	except:
		pass
# Этап заказа 0 - товар 1 - вкус 2 - город 3 - количество Juul


#Xar

		
	

def pay2(message):
    if message.text=='Оформить':
        bot.send_invoice(message.chat.id, title='travf',
                         description='opisanie',
                         currency='uah',
                         # photo_url='http://res.cloudinary.com/muzicius/image/upload/v1493211949/foodservice-icecake/srrtvbiwv1wgfd8c8ppj.jpg',
                         is_flexible=False,  # True If you need to set up Shipping Fee
                         prices=prices_1,
                         start_parameter='test',
                         invoice_payload='plata za test',
                         provider_token="635983722:LIVE:i34056587473")
def pay3(message):
    if message.text=='Оформить':
        bot.send_invoice(message.chat.id, title='travf',
                         description='opisanie',
                         currency='uah',
                         # photo_url='http://res.cloudinary.com/muzicius/image/upload/v1493211949/foodservice-icecake/srrtvbiwv1wgfd8c8ppj.jpg',
                         is_flexible=False,  # True If you need to set up Shipping Fee
                         prices=prices_2,
                         start_parameter='test',
                         invoice_payload='plata za test',
                         provider_token="635983722:LIVE:i34056587473")
def pay4(message):
    if message.text=='Оформить':
        bot.send_invoice(message.chat.id, title='travf',
                         description='opisanie',
                         currency='uah',
                         # photo_url='http://res.cloudinary.com/muzicius/image/upload/v1493211949/foodservice-icecake/srrtvbiwv1wgfd8c8ppj.jpg',
                         is_flexible=False,  # True If you need to set up Shipping Fee
                         prices=prices_3,
                         start_parameter='test',
                         invoice_payload='plata za test',
                         provider_token="635983722:LIVE:i34056587473")
def pay5(message):
    if message.text=='Оформить':
        bot.send_invoice(message.chat.id, title='travf',
                         description='opisanie',
                         currency='uah',
                         # photo_url='http://res.cloudinary.com/muzicius/image/upload/v1493211949/foodservice-icecake/srrtvbiwv1wgfd8c8ppj.jpg',
                         is_flexible=False,  # True If you need to set up Shipping Fee
                         prices=prices_4,
                         start_parameter='test',
                         invoice_payload='plata za test',
                         provider_token="635983722:LIVE:i34056587473")
def pay6(message):
    if message.text=='Оформить':
        bot.send_invoice(message.chat.id, title='travf',
                         description='opisanie',
                         currency='uah',
                         # photo_url='http://res.cloudinary.com/muzicius/image/upload/v1493211949/foodservice-icecake/srrtvbiwv1wgfd8c8ppj.jpg',
                         is_flexible=False,  # True If you need to set up Shipping Fee
                         prices=prices_5,
                         start_parameter='test',
                         invoice_payload='plata za test',
                         provider_token="635983722:LIVE:i34056587473")
def pay7(message):
    if message.text=='Оформить':
        bot.send_invoice(message.chat.id, title='travf',
                         description='opisanie',
                         currency='uah',
                         # photo_url='http://res.cloudinary.com/muzicius/image/upload/v1493211949/foodservice-icecake/srrtvbiwv1wgfd8c8ppj.jpg',
                         is_flexible=False,  # True If you need to set up Shipping Fee
                         prices=prices_6,
                         start_parameter='test',
                         invoice_payload='plata za test',
                         provider_token="635983722:LIVE:i34056587473")
def pay8(message):
    if message.text=='Оформить':
        bot.send_invoice(message.chat.id, title='travf',
                         description='opisanie',
                         currency='uah',
                         # photo_url='http://res.cloudinary.com/muzicius/image/upload/v1493211949/foodservice-icecake/srrtvbiwv1wgfd8c8ppj.jpg',
                         is_flexible=False,  # True If you need to set up Shipping Fee
                         prices=prices_7,
                         start_parameter='test',
                         invoice_payload='plata za test',
                         provider_token="635983722:LIVE:i34056587473")
def pay9(message):
    if message.text=='Оформить':
        bot.send_invoice(message.chat.id, title='travf',
                         description='opisanie',
                         currency='uah',
                         # photo_url='http://res.cloudinary.com/muzicius/image/upload/v1493211949/foodservice-icecake/srrtvbiwv1wgfd8c8ppj.jpg',
                         is_flexible=False,  # True If you need to set up Shipping Fee
                         prices=prices_8,
                         start_parameter='test',
                         invoice_payload='plata za test',
                         provider_token="635983722:LIVE:i34056587473")
def pay10(message):
    if message.text=='Оформить':
        bot.send_invoice(message.chat.id, title='travf',
                         description='opisanie',
                         currency='uah',
                         # photo_url='http://res.cloudinary.com/muzicius/image/upload/v1493211949/foodservice-icecake/srrtvbiwv1wgfd8c8ppj.jpg',
                         is_flexible=False,  # True If you need to set up Shipping Fee
                         prices=prices_9,
                         start_parameter='test',
                         invoice_payload='plata za test',
                         provider_token="635983722:LIVE:i34056587473")
def pay11(message):
    if message.text=='Оформить':
        bot.send_invoice(message.chat.id, title='travf',
                         description='opisanie',
                         currency='uah',
                         # photo_url='http://res.cloudinary.com/muzicius/image/upload/v1493211949/foodservice-icecake/srrtvbiwv1wgfd8c8ppj.jpg',
                         is_flexible=False,  # True If you need to set up Shipping Fee
                         prices=prices_10,
                         start_parameter='test',
                         invoice_payload='plata za test',
                         provider_token="635983722:LIVE:i34056587473")
def pay12(message):
    if message.text=='Оформить':
        bot.send_invoice(message.chat.id, title='travf',
                         description='opisanie',
                         currency='uah',
                         # photo_url='http://res.cloudinary.com/muzicius/image/upload/v1493211949/foodservice-icecake/srrtvbiwv1wgfd8c8ppj.jpg',
                         is_flexible=False,  # True If you need to set up Shipping Fee
                         prices=prices_11,
                         start_parameter='test',
                         invoice_payload='plata za test',
                         provider_token="635983722:LIVE:i34056587473")
#Sumy
def pay13(message):
	if message.text=='OG-Kush БШ 3г':
		markup = telebot.types.InlineKeyboardMarkup()
		markup.add(telebot.types.InlineKeyboardButton(text='Курская💀', callback_data=3))
		markup.add(telebot.types.InlineKeyboardButton(text='Центр🌝', callback_data=4))
		markup.add(telebot.types.InlineKeyboardButton(text='Вокзал⛩', callback_data=5))
		markup.add(telebot.types.InlineKeyboardButton(text='🔙Назад🔙', callback_data="back"))
		bot.send_message(message.chat.id, text="\nВы выбрали:\n🌳 OG KUSH БШ 3г 🌳\n➖➖➖➖➖➖➖➖➖➖\nГород: Сумы\nТовар: 🌳 OG KUSH БШ 🌳\nФасовка: 3г⚖️\n➖➖➖➖➖➖➖➖➖➖\nВыберите район:", reply_markup=markup)
def pay14(message):
	if message.text=='План(Сыпуха) 3г':
		markup = telebot.types.InlineKeyboardMarkup()
		markup.add(telebot.types.InlineKeyboardButton(text='Курская💀', callback_data="kur2"))
		markup.add(telebot.types.InlineKeyboardButton(text='9-ка🌚', callback_data=91))
		markup.add(telebot.types.InlineKeyboardButton(text='Кирова❄️', callback_data="kir1"))
		markup.add(telebot.types.InlineKeyboardButton(text='🔙Назад🔙', callback_data="back"))
		bot.send_message(message.chat.id, text="\nВы выбрали:\n🌱 План(Сыпуха) 3г 🌱\n➖➖➖➖➖➖➖➖➖➖\nГород: Сумы\nТовар: 🌱 План(Сыпуха) 3г 🌱\nФасовка: 3г⚖️\n➖➖➖➖➖➖➖➖➖➖\nВыберите район:", reply_markup=markup)
def pay15(message):
	if message.text=='Шишки Mango Kush 1г':
		markup = telebot.types.InlineKeyboardMarkup()
		markup.add(telebot.types.InlineKeyboardButton(text='Роменская👽', callback_data="rom1"))
		markup.add(telebot.types.InlineKeyboardButton(text='9-ка🌚', callback_data=92))
		markup.add(telebot.types.InlineKeyboardButton(text='Центр🌝', callback_data="cen1"))
		markup.add(telebot.types.InlineKeyboardButton(text='🔙Назад🔙', callback_data="back"))
		bot.send_message(message.chat.id, text="\nВы выбрали:\n🐍 Шишки Mango Haze 🐍\n➖➖➖➖➖➖➖➖➖➖\nГород: Сумы\nТовар: 🐍 Шишки Mango Haze 🐍\nФасовка: 3г⚖️\n➖➖➖➖➖➖➖➖➖➖\nВыберите район:", reply_markup=markup)
def pay16(message):
	if message.text=='Амфетамин Розовый 0.5г':
		markup = telebot.types.InlineKeyboardMarkup()
		markup.add(telebot.types.InlineKeyboardButton(text='Химик💉', callback_data="xim1"))
		markup.add(telebot.types.InlineKeyboardButton(text='9-ка🌚', callback_data=93))
		markup.add(telebot.types.InlineKeyboardButton(text='🔙Назад🔙', callback_data="back"))
		bot.send_message(message.chat.id, text="\nВы выбрали:\n💎 Амфетамин Розовый 💎\n➖➖➖➖➖➖➖➖➖➖\nГород: Сумы\nТовар: 💎 Амфетамин Розовый 💎\nФасовка: 0,5г⚖️\n➖➖➖➖➖➖➖➖➖➖\nВыберите район:", reply_markup=markup)
def pay17(message):
	if message.text=='Шишки OG-Kush 1г':
		markup = telebot.types.InlineKeyboardMarkup()
		markup.add(telebot.types.InlineKeyboardButton(text='Центр🌝', callback_data="cen2"))
		markup.add(telebot.types.InlineKeyboardButton(text='9-ка🌚', callback_data=94))
		markup.add(telebot.types.InlineKeyboardButton(text='🔙Назад🔙', callback_data="back"))
		bot.send_message(message.chat.id, text="\nВы выбрали:\n🌳 Шишки OG-Kush 🌳\n➖➖➖➖➖➖➖➖➖➖\nГород: Сумы\nТовар: 🌳 Шишки OG-Kush 🌳\nФасовка: 1г⚖️\n➖➖➖➖➖➖➖➖➖➖\nВыберите район:", reply_markup=markup)
def pay18(message):
	if message.text=='Alfa PVP DeLuxe 0.5г':
		markup = telebot.types.InlineKeyboardMarkup()
		markup.add(telebot.types.InlineKeyboardButton(text='Химик💉', callback_data="xim2"))
		markup.add(telebot.types.InlineKeyboardButton(text='Центр🌝', callback_data="cen3"))
		markup.add(telebot.types.InlineKeyboardButton(text='🔙Назад🔙', callback_data="back"))
		bot.send_message(message.chat.id, text="\nВы выбрали:\n💎 Alfa PVP DeLuxe 💎\n➖➖➖➖➖➖➖➖➖➖\nГород: Сумы\nТовар: 💎 Alfa PVP DeLuxe 💎\nФасовка: 0,5г⚖️\n➖➖➖➖➖➖➖➖➖➖\nВыберите район:", reply_markup=markup)
def pay19(message):
	if message.text=='Амфетамин Розовый 1г':
		markup = telebot.types.InlineKeyboardMarkup()
		markup.add(telebot.types.InlineKeyboardButton(text='Химик💉', callback_data="xim3"))
		markup.add(telebot.types.InlineKeyboardButton(text='9-ка🌚', callback_data=95))
		markup.add(telebot.types.InlineKeyboardButton(text='🔙Назад🔙', callback_data="back"))
		bot.send_message(message.chat.id, text="\nВы выбрали:\n💎 Амфетамин Розовый 💎\n➖➖➖➖➖➖➖➖➖➖\nГород: Сумы\nТовар: 💎 Амфетамин Розовый 💎\nФасовка: 1г⚖️\n➖➖➖➖➖➖➖➖➖➖\nВыберите район:", reply_markup=markup)
def pay20(message):
	if message.text=='Экстези Barcelona 1шт':
		markup = telebot.types.InlineKeyboardMarkup()
		markup.add(telebot.types.InlineKeyboardButton(text='КРЗ⚽️', callback_data="vok1"))
		markup.add(telebot.types.InlineKeyboardButton(text='Барановка🕋', callback_data="bar1"))
		markup.add(telebot.types.InlineKeyboardButton(text='Басы🦚', callback_data="bas1"))
		markup.add(telebot.types.InlineKeyboardButton(text='🔙Назад🔙', callback_data="back"))
		bot.send_message(message.chat.id, text="\nВы выбрали:\n💊 XTC Barcelona 💊\n➖➖➖➖➖➖➖➖➖➖\nГород: Сумы\nТовар: 💊 XTC Barcelona 💊\nФасовка: 1 таблетка⚖️\n➖➖➖➖➖➖➖➖➖➖\nВыберите район:", reply_markup=markup)
def pay21(message):
	if message.text=='Печеньки с ТГК 1шт':
		markup = telebot.types.InlineKeyboardMarkup()
		markup.add(telebot.types.InlineKeyboardButton(text='Вокзал⛩', callback_data="vok2"))
		markup.add(telebot.types.InlineKeyboardButton(text='Металургов🚀', callback_data="met1"))
		markup.add(telebot.types.InlineKeyboardButton(text='Басы🦚', callback_data="bas2"))
		markup.add(telebot.types.InlineKeyboardButton(text='🔙Назад🔙', callback_data="back"))
		bot.send_message(message.chat.id, text="\nВы выбрали:\n🍪 Печеньки с ТГК 🍪\n➖➖➖➖➖➖➖➖➖➖\nГород: Сумы\nТовар: 🍪 Печеньки с ТГК 🍪\nФасовка: 1 шт⚖️\n➖➖➖➖➖➖➖➖➖➖\nВыберите район:", reply_markup=markup)
#ахтырка

def pay22(message):
	if message.text=='Битые шишки 3г':
		markup = telebot.types.InlineKeyboardMarkup()
		markup.add(telebot.types.InlineKeyboardButton(text='Петропавловская☣️', callback_data="pet1"))
		markup.add(telebot.types.InlineKeyboardButton(text='Центр🌝', callback_data="cen4"))
		markup.add(telebot.types.InlineKeyboardButton(text='Вокзал⛩', callback_data="vok3"))
		markup.add(telebot.types.InlineKeyboardButton(text='🔙Назад🔙', callback_data="back"))
		bot.send_message(message.chat.id, text="\nВы выбрали:\n🌳 Битые шишки 🌳\n➖➖➖➖➖➖➖➖➖➖\nГород: Ахтырка\nТовар: 🌳 Битые шишки 🌳\nФасовка: 3г⚖️\n➖➖➖➖➖➖➖➖➖➖\nВыберите район:", reply_markup=markup)
def pay24(message):
	if message.text=='Шишки Pablo Escobar 1г':
		markup = telebot.types.InlineKeyboardMarkup()
		markup.add(telebot.types.InlineKeyboardButton(text='Петропавловская☣️', callback_data="pet2"))
		markup.add(telebot.types.InlineKeyboardButton(text='Центр🌝', callback_data="cen5"))
		markup.add(telebot.types.InlineKeyboardButton(text='Вокзал⛩', callback_data="vok4"))
		markup.add(telebot.types.InlineKeyboardButton(text='🔙Назад🔙', callback_data="back"))
		bot.send_message(message.chat.id, text="\nВы выбрали:\n🐲 Шишки Pablo Escobar 🐉\n➖➖➖➖➖➖➖➖➖➖\nГород: Ахтырка\nТовар: 🐲 Шишки Pablo Escobar 🐉\nФасовка: 1г⚖️\n➖➖➖➖➖➖➖➖➖➖\nВыберите район:", reply_markup=markup)
def pay25(message):
	if message.text=='Alfa PVP DeLuxe 0.5г':
		markup = telebot.types.InlineKeyboardMarkup()
		markup.add(telebot.types.InlineKeyboardButton(text='Петропавловская☣️', callback_data="pet3"))
		markup.add(telebot.types.InlineKeyboardButton(text='Центр🌝', callback_data="cen6"))
		markup.add(telebot.types.InlineKeyboardButton(text='Вокзал⛩', callback_data="vok5"))
		markup.add(telebot.types.InlineKeyboardButton(text='🔙Назад🔙', callback_data="back"))
		bot.send_message(message.chat.id, text="\nВы выбрали:\n⚗ Alfa PVP DeLuxe 🧬\n➖➖➖➖➖➖➖➖➖➖\nГород: Ахтырка\nТовар: ⚗ Alfa PVP DeLuxe 🧬\nФасовка: 0,5г⚖️\n➖➖➖➖➖➖➖➖➖➖\nВыберите район:", reply_markup=markup)
def pay26(message):
	if message.text=='Амфетамин Сульфат 0.5г':
		markup = telebot.types.InlineKeyboardMarkup()
		markup.add(telebot.types.InlineKeyboardButton(text='Петропавловская☣️', callback_data="pet4"))
		markup.add(telebot.types.InlineKeyboardButton(text='Центр🌝', callback_data="cen7"))
		markup.add(telebot.types.InlineKeyboardButton(text='Вокзал⛩', callback_data="vok6"))
		markup.add(telebot.types.InlineKeyboardButton(text='🔙Назад🔙', callback_data="back"))
		bot.send_message(message.chat.id, text="\nВы выбрали:\n⚗️ Амфетамин Сульфат ⚗️\n➖➖➖➖➖➖➖➖➖➖\nГород: Ахтырка\nТовар: ⚗️ Амфетамин Сульфат ⚗️\nФасовка: 0,5г⚖️\n➖➖➖➖➖➖➖➖➖➖\nВыберите район:", reply_markup=markup)

#poltava 
def pay30(message):
	if message.text=='Афганка БШ 3г':
		markup = telebot.types.InlineKeyboardMarkup()
		markup.add(telebot.types.InlineKeyboardButton(text='Институт связи🤙🏽', callback_data="in1"))
		markup.add(telebot.types.InlineKeyboardButton(text='🔙Назад🔙', callback_data="back"))
		bot.send_message(message.chat.id, text="\nВы выбрали:\n🌳 Афганка БШ 🌳\n➖➖➖➖➖➖➖➖➖➖\nГород: Полтава\nТовар: 🌳 Афганка БШ 🌳\nФасовка: 3г⚖️\n➖➖➖➖➖➖➖➖➖➖\nВыберите район:", reply_markup=markup)
def pay32(message):
	if message.text=='Шишки Amnesia 1г':
		markup = telebot.types.InlineKeyboardMarkup()
		markup.add(telebot.types.InlineKeyboardButton(text='Дендропарк🚀', callback_data="den1"))
		markup.add(telebot.types.InlineKeyboardButton(text='Центр🌝', callback_data="cen8"))
		markup.add(telebot.types.InlineKeyboardButton(text='🔙Назад🔙', callback_data="back"))
		bot.send_message(message.chat.id, text="\nВы выбрали:\n🐉 Шишки Amnesia 🐉\n➖➖➖➖➖➖➖➖➖➖\nГород: Полтава\nТовар: 🐉 Шишки Amnesia 🐉\nФасовка: 1г⚖️\n➖➖➖➖➖➖➖➖➖➖\nВыберите район:", reply_markup=markup)
def pay33(message):
	if message.text=='Alfa PVP DeLuxe 0.5г':
		markup = telebot.types.InlineKeyboardMarkup()
		markup.add(telebot.types.InlineKeyboardButton(text='Пушкина🚀', callback_data="pus1"))
		markup.add(telebot.types.InlineKeyboardButton(text='Центр🌝', callback_data="cen9"))
		markup.add(telebot.types.InlineKeyboardButton(text='🔙Назад🔙', callback_data="back"))
		bot.send_message(message.chat.id, text="\nВы выбрали:\n💡 Alfa PVP DeLuxe 💡\n➖➖➖➖➖➖➖➖➖➖\nГород: Полтава\nТовар:  Alfa PVP DeLuxe 💡\nФасовка: 0,5г⚖️\n➖➖➖➖➖➖➖➖➖➖\nВыберите район:", reply_markup=markup)
def pay34(message):
	if message.text=='Амфетамин Сульфат 0.5г':
		markup = telebot.types.InlineKeyboardMarkup()
		markup.add(telebot.types.InlineKeyboardButton(text='Павленки🕋', callback_data="pav1"))
		markup.add(telebot.types.InlineKeyboardButton(text='Сады❄️', callback_data="cad1"))
		markup.add(telebot.types.InlineKeyboardButton(text='🔙Назад🔙', callback_data="back"))
		bot.send_message(message.chat.id, text="\nВы выбрали:\n💎 Амфетамин Сульфат 💎\n➖➖➖➖➖➖➖➖➖➖\nГород: Полтава\nТовар: 💎 Амфетамин Сульфат 💎\nФасовка: 0,5г⚖️\n➖➖➖➖➖➖➖➖➖➖\nВыберите район:", reply_markup=markup)
def pay35(message):
	if message.text=='Мефедрон  0.5г':
		markup = telebot.types.InlineKeyboardMarkup()
		markup.add(telebot.types.InlineKeyboardButton(text='Сады❄️', callback_data="cad2"))
		markup.add(telebot.types.InlineKeyboardButton(text='🔙Назад🔙', callback_data="back"))
		bot.send_message(message.chat.id, text="\nВы выбрали:\n💎 Мефедрон 💎\n➖➖➖➖➖➖➖➖➖➖\nГород: Полтава\nТовар: 💎 Мефедрон 💎\nФасовка: 0,5г⚖️\n➖➖➖➖➖➖➖➖➖➖\nВыберите район:", reply_markup=markup)
def pay36(message):
	if message.text=='Экстези TikTok 1шт':
		markup = telebot.types.InlineKeyboardMarkup()
		markup.add(telebot.types.InlineKeyboardButton(text='Центр🌝', callback_data="cen10"))
		markup.add(telebot.types.InlineKeyboardButton(text='🔙Назад🔙', callback_data="back"))
		bot.send_message(message.chat.id, text="\nВы выбрали:\n💊 XTC TikTok 💃🏼\n➖➖➖➖➖➖➖➖➖➖\nГород: Полтава\nТовар: 💊 XTC TikTok 💃🏼\nФасовка: 1 колесо⚖️\n➖➖➖➖➖➖➖➖➖➖\nВыберите район:", reply_markup=markup)
def pay37(message):
	if message.text=='LSD-25 1шт':
		markup = telebot.types.InlineKeyboardMarkup()
		markup.add(telebot.types.InlineKeyboardButton(text='Павленки🕋', callback_data="pav2"))
		markup.add(telebot.types.InlineKeyboardButton(text='Пушкина🚀', callback_data="pus2"))
		markup.add(telebot.types.InlineKeyboardButton(text='🔙Назад🔙', callback_data="back"))
		bot.send_message(message.chat.id, text="\nВы выбрали:\n🌈 LSD-25 🌈\n➖➖➖➖➖➖➖➖➖➖\nГород: Полтава\nТовар: 🌈 LSD-25 🌈\nФасовка: 1 марка⚖️\n➖➖➖➖➖➖➖➖➖➖\nВыберите район:", reply_markup=markup)




@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
	if call.data == '4':
		opl = types.InlineKeyboardMarkup(row_width=2)
		opl.add(types.InlineKeyboardButton(text='Купить товар✔️', callback_data=6))
		bot.send_message(call.message.chat.id, text="🦋Вы выбрали: *OG KUSH БШ 3г*🌳\nГород: *Сумы🚀*\nФасовка: *3г⚖️*\nРайон: *Центр🌝*\n➖➖➖➖➖➖➖➖➖➖\nКошелек: *51646449*\nЦена: *150грн*\n➖➖➖➖➖➖➖➖➖➖", parse_mode="Markdown", reply_markup=opl)
		
		answer = ''
	elif call.data == '3':
		opl = types.InlineKeyboardMarkup(row_width=2)
		opl.add(types.InlineKeyboardButton(text='Купить товар✔️', callback_data=6))
		bot.send_message(call.message.chat.id, text="🦋Вы выбрали: *OG KUSH БШ 3г*🌳\nГород: *Сумы*🚀\nФасовка: *3г⚖️*\nРайон: *Курская*💀\n➖➖➖➖➖➖➖➖➖➖\nКошелек: *51646449*\nЦена: *150грн*\n➖➖➖➖➖➖➖➖➖➖", parse_mode="Markdown", reply_markup=opl)
		
		answer = ''
	elif call.data == '5':
		opl = types.InlineKeyboardMarkup(row_width=2)
		opl.add(types.InlineKeyboardButton(text='Купить товар✔️', callback_data=6))
		bot.send_message(call.message.chat.id, text="🦋Вы выбрали: *OG KUSH БШ 3г*🌳\nГород: *Сумы🚀*\nФасовка: *3г⚖️*\nРайон: *Вокзал⛩*\n➖➖➖➖➖➖➖➖➖➖\nКошелек: *51646449*\nЦена: *150грн*\n➖➖➖➖➖➖➖➖➖➖", parse_mode="Markdown", reply_markup=opl)
		
		answer = ''
	elif call.data == 'kur2':
		opl = types.InlineKeyboardMarkup(row_width=2)
		opl.add(types.InlineKeyboardButton(text='Купить товар✔️', callback_data=6))
		bot.send_message(call.message.chat.id, text="🦋Вы выбрали: *План(Сыпуха) 3г🌱*\nГород: *Сумы🚀*\nФасовка: *3г⚖️*\nРайон: *Курская💀*\n➖➖➖➖➖➖➖➖➖➖\nКошелек: *51646449*\nЦена: *120грн*\n➖➖➖➖➖➖➖➖➖➖", parse_mode="Markdown", reply_markup=opl)
		
		answer = ''
	elif call.data == '91':
		opl = types.InlineKeyboardMarkup(row_width=2)
		opl.add(types.InlineKeyboardButton(text='Купить товар✔️', callback_data=6))
		bot.send_message(call.message.chat.id, text="🦋Вы выбрали: *План(Сыпуха) 3г🌱*\nГород: *Сумы🚀*\nФасовка: *3г⚖️*\nРайон: *9-ка🌚*\n➖➖➖➖➖➖➖➖➖➖\nКошелек: *51646449*\nЦена: *120грн*\n➖➖➖➖➖➖➖➖➖➖", parse_mode="Markdown", reply_markup=opl)
		
		answer = ''
	elif call.data == 'kir1':
		opl = types.InlineKeyboardMarkup(row_width=2)
		opl.add(types.InlineKeyboardButton(text='Купить товар✔️', callback_data=6))
		bot.send_message(call.message.chat.id, text="🦋Вы выбрали: *План(Сыпуха) 3г🌱*\nГород: *Сумы🚀*\nФасовка: *3г⚖️*\nРайон: *Кирова❄️*\n➖➖➖➖➖➖➖➖➖➖\nКошелек: *51646449*\nЦена: *120грн*\n➖➖➖➖➖➖➖➖➖➖", parse_mode="Markdown", reply_markup=opl)
		
		answer = ''
	elif call.data == 'rom1':
		opl = types.InlineKeyboardMarkup(row_width=2)
		opl.add(types.InlineKeyboardButton(text='Купить товар✔️', callback_data=6))
		bot.send_message(call.message.chat.id, text="🦋Вы выбрали: *Шишки Mango Kush 1г🐍*\nГород: *Сумы🚀*\nФасовка: *1г⚖️*\nРайон: *Роменская👽*\n➖➖➖➖➖➖➖➖➖➖\nКошелек: *51646449*\nЦена: *230грн*\n➖➖➖➖➖➖➖➖➖➖", parse_mode="Markdown", reply_markup=opl)
		
		answer = ''
	elif call.data == '92':
		opl = types.InlineKeyboardMarkup(row_width=2)
		opl.add(types.InlineKeyboardButton(text='Купить товар✔️', callback_data=6))
		bot.send_message(call.message.chat.id, text="🦋Вы выбрали: *Шишки Mango Kush 1г🐍*\nГород: *Сумы🚀*\nФасовка: *1г⚖️*\nРайон: *9-ка🌚*\n➖➖➖➖➖➖➖➖➖➖\nКошелек: *51646449*\nЦена: *230грн*\n➖➖➖➖➖➖➖➖➖➖", parse_mode="Markdown", reply_markup=opl)
		
		answer = ''
	elif call.data == 'cen1':
		opl = types.InlineKeyboardMarkup(row_width=2)
		opl.add(types.InlineKeyboardButton(text='Купить товар✔️', callback_data=6))
		bot.send_message(call.message.chat.id, text="🦋Вы выбрали: *Шишки Mango Kush 1г🐍*\nГород: *Сумы🚀*\nФасовка: *1г⚖️*\nРайон: *Центр🌝*\n➖➖➖➖➖➖➖➖➖➖\nКошелек: *51646449*\nЦена: *230грн*\n➖➖➖➖➖➖➖➖➖➖", parse_mode="Markdown", reply_markup=opl)
		
		answer = ''
	elif call.data == 'xim1':
		opl = types.InlineKeyboardMarkup(row_width=2)
		opl.add(types.InlineKeyboardButton(text='Купить товар✔️', callback_data=6))
		bot.send_message(call.message.chat.id, text="🦋Вы выбрали: *Амфетамин Розовый💎*\nГород: *Сумы🚀*\nФасовка: *0,5г⚖️*\nРайон: *Химик💉*\n➖➖➖➖➖➖➖➖➖➖\nКошелек: *51646449*\nЦена: *250грн*\n➖➖➖➖➖➖➖➖➖➖", parse_mode="Markdown", reply_markup=opl)
		
		answer = ''
	elif call.data == '93':
		opl = types.InlineKeyboardMarkup(row_width=2)
		opl.add(types.InlineKeyboardButton(text='Купить товар✔️', callback_data=6))
		bot.send_message(call.message.chat.id, text="🦋Вы выбрали: *Амфетамин Розовый💎*\nГород: *Сумы🚀*\nФасовка: *0,5г⚖️*\nРайон: *9-ка🌚*\n➖➖➖➖➖➖➖➖➖➖\nКошелек: *51646449*\nЦена: *250грн*\n➖➖➖➖➖➖➖➖➖➖", parse_mode="Markdown", reply_markup=opl)
		
		answer = ''
	elif call.data == 'cen2':
		opl = types.InlineKeyboardMarkup(row_width=2)
		opl.add(types.InlineKeyboardButton(text='Купить товар✔️', callback_data=6))
		bot.send_message(call.message.chat.id, text="🦋Вы выбрали: *Шишки OG-Kush 1г🐉*\nГород: *Сумы🚀*\nФасовка: *1г⚖️*\nРайон: *Центр🌝*\n➖➖➖➖➖➖➖➖➖➖\nКошелек: *51646449*\nЦена: *230грн*\n➖➖➖➖➖➖➖➖➖➖", parse_mode="Markdown", reply_markup=opl)
		
		answer = ''
	elif call.data == '94':
		opl = types.InlineKeyboardMarkup(row_width=2)
		opl.add(types.InlineKeyboardButton(text='Купить товар✔️', callback_data=6))
		bot.send_message(call.message.chat.id, text="🦋Вы выбрали: *Шишки OG-Kush 1г🐉*\nГород: *Сумы🚀*\nФасовка: *1г⚖️*\nРайон: *9-ка🌚*\n➖➖➖➖➖➖➖➖➖➖\nКошелек: *51646449*\nЦена: *230грн*\n➖➖➖➖➖➖➖➖➖➖", parse_mode="Markdown", reply_markup=opl)
		
		answer = ''
	elif call.data == 'xim2':
		opl = types.InlineKeyboardMarkup(row_width=2)
		opl.add(types.InlineKeyboardButton(text='Купить товар✔️', callback_data=6))
		bot.send_message(call.message.chat.id, text="🦋Вы выбрали: *Alfa PVP DeLuxe💎*\nГород: *Сумы🚀*\nФасовка: *0,5г⚖️*\nРайон: *Химик💉*\n➖➖➖➖➖➖➖➖➖➖\nКошелек: *51646449*\nЦена: *250грн*\n➖➖➖➖➖➖➖➖➖➖", parse_mode="Markdown", reply_markup=opl)
		
		answer = ''
	elif call.data == 'cen3':
		opl = types.InlineKeyboardMarkup(row_width=2)
		opl.add(types.InlineKeyboardButton(text='Купить товар✔️', callback_data=6))
		bot.send_message(call.message.chat.id, text="🦋Вы выбрали: *Alfa PVP DeLuxe💎*\nГород: *Сумы🚀*\nФасовка: *0,5г⚖️*\nРайон: *Центр🌝*\n➖➖➖➖➖➖➖➖➖➖\nКошелек: *51646449*\nЦена: *250грн*\n➖➖➖➖➖➖➖➖➖➖", parse_mode="Markdown", reply_markup=opl)
		
		answer = ''
	elif call.data == 'xim3':
		opl = types.InlineKeyboardMarkup(row_width=2)
		opl.add(types.InlineKeyboardButton(text='Купить товар✔️', callback_data=6))
		bot.send_message(call.message.chat.id, text="🦋Вы выбрали: *Амфетамин Розовый💎*\nГород: *Сумы🚀*\nФасовка: *0,5г⚖️*\nРайон: *Химик💉*\n➖➖➖➖➖➖➖➖➖➖\nКошелек: *51646449*\nЦена: *250грн*\n➖➖➖➖➖➖➖➖➖➖", parse_mode="Markdown", reply_markup=opl)
		
		answer = ''
	elif call.data == '95':
		opl = types.InlineKeyboardMarkup(row_width=2)
		opl.add(types.InlineKeyboardButton(text='Купить товар✔️', callback_data=6))
		bot.send_message(call.message.chat.id, text="🦋Вы выбрали: *Амфетамин Розовый💎*\nГород: *Сумы🚀*\nФасовка: *0,5г⚖️*\nРайон: *9-ка🌚*\n➖➖➖➖➖➖➖➖➖➖\nКошелек: *51646449*\nЦена: *250грн*\n➖➖➖➖➖➖➖➖➖➖", parse_mode="Markdown", reply_markup=opl)
		
		answer = ''
	elif call.data == 'vok1':
		opl = types.InlineKeyboardMarkup(row_width=2)
		opl.add(types.InlineKeyboardButton(text='Купить товар✔️', callback_data=6))
		bot.send_message(call.message.chat.id, text="🦋Вы выбрали: *XTC Barcelona💊*\nГород: *Сумы🚀*\nФасовка: *1 колесо💊*\nРайон: *Вокзал⛩*\n➖➖➖➖➖➖➖➖➖➖\nКошелек: *51646449*\nЦена: *380грн*\n➖➖➖➖➖➖➖➖➖➖", parse_mode="Markdown", reply_markup=opl)
		
		answer = ''
	elif call.data == 'bar1':
		opl = types.InlineKeyboardMarkup(row_width=2)
		opl.add(types.InlineKeyboardButton(text='Купить товар✔️', callback_data=6))
		bot.send_message(call.message.chat.id, text="🦋Вы выбрали: *XTC Barcelona💊*\nГород: *Сумы🚀*\nФасовка: *1 колесо💊*\nРайон: *КРЗ⚽️*\n➖➖➖➖➖➖➖➖➖➖\nКошелек: *51646449*\nЦена: *380грн*\n➖➖➖➖➖➖➖➖➖➖", parse_mode="Markdown", reply_markup=opl)
		
		answer = ''
	elif call.data == 'bas1':
		opl = types.InlineKeyboardMarkup(row_width=2)
		opl.add(types.InlineKeyboardButton(text='Купить товар✔️', callback_data=6))
		bot.send_message(call.message.chat.id, text="🦋Вы выбрали: *XTC Barcelona💊*\nГород: *Сумы🚀*\nФасовка: *1 колесо💊*\nРайон: *Басы🦚*\n➖➖➖➖➖➖➖➖➖➖\nКошелек: *51646449*\nЦена: *390грн*\n➖➖➖➖➖➖➖➖➖➖", parse_mode="Markdown", reply_markup=opl)
		
		answer = ''
	elif call.data == 'vok2':
		opl = types.InlineKeyboardMarkup(row_width=2)
		opl.add(types.InlineKeyboardButton(text='Купить товар✔️', callback_data=6))
		bot.send_message(call.message.chat.id, text="🦋Вы выбрали: *Печеньки с ТГК🍪*\nГород: *Сумы🚀*\nФасовка: *1 печенье🍪*\nРайон: *Вокзал⛩*\n➖➖➖➖➖➖➖➖➖➖\nКошелек: *51646449*\nЦена: *200грн*\n➖➖➖➖➖➖➖➖➖➖", parse_mode="Markdown", reply_markup=opl)
		
		answer = ''
	elif call.data == 'met1':
		opl = types.InlineKeyboardMarkup(row_width=2)
		opl.add(types.InlineKeyboardButton(text='Купить товар✔️', callback_data=6))
		bot.send_message(call.message.chat.id, text="🦋Вы выбрали: *Печеньки с ТГК🍪*\nГород: *Сумы🚀*\nФасовка: *1 печенье🍪*\nРайон: *Металургов🦋*\n➖➖➖➖➖➖➖➖➖➖\nКошелек: *51646449*\nЦена: *200грн*\n➖➖➖➖➖➖➖➖➖➖", parse_mode="Markdown", reply_markup=opl)
		
		answer = ''
	elif call.data == 'bas2':
		opl = types.InlineKeyboardMarkup(row_width=2)
		opl.add(types.InlineKeyboardButton(text='Купить товар✔️', callback_data=6))
		bot.send_message(call.message.chat.id, text="🦋Вы выбрали: *Печеньки с ТГК🍪*\nГород: *Сумы🚀*\nФасовка: *1 печенье🍪*\nРайон: *Басы🦚*\n➖➖➖➖➖➖➖➖➖➖\nКошелек: *51646449*\nЦена: *200грн*\n➖➖➖➖➖➖➖➖➖➖", parse_mode="Markdown", reply_markup=opl)
		
		answer = ''
	elif call.data == 'pet1':
		opl = types.InlineKeyboardMarkup(row_width=2)
		opl.add(types.InlineKeyboardButton(text='Купить товар✔️', callback_data=6))
		bot.send_message(call.message.chat.id, text="🦋Вы выбрали: *Битые шишки 3г🌱*\nГород: *Ахтырка🌪*\nФасовка: *3г⚖️*\nРайон: *Петропавловская🗽*\n➖➖➖➖➖➖➖➖➖➖\nКошелек: *51646449*\nЦена: *150грн*\n➖➖➖➖➖➖➖➖➖➖", parse_mode="Markdown", reply_markup=opl)
		
		answer = ''
	elif call.data == 'cen4':
		opl = types.InlineKeyboardMarkup(row_width=2)
		opl.add(types.InlineKeyboardButton(text='Купить товар✔️', callback_data=6))
		bot.send_message(call.message.chat.id, text="🦋Вы выбрали: *Битые шишки 3г🌱*\nГород: *Ахтырка🌪*\nФасовка: *3г⚖️*\nРайон: *Центр🌝*\n➖➖➖➖➖➖➖➖➖➖\nКошелек: *51646449*\nЦена: *150грн*\n➖➖➖➖➖➖➖➖➖➖", parse_mode="Markdown", reply_markup=opl)
		
		answer = ''
	elif call.data == 'vok3':
		opl = types.InlineKeyboardMarkup(row_width=2)
		opl.add(types.InlineKeyboardButton(text='Купить товар✔️', callback_data=6))
		bot.send_message(call.message.chat.id, text="🦋Вы выбрали: *Битые шишки 3г🌱*\nГород: *Ахтырка🌪*\nФасовка: *3г⚖️*\nРайон: *Вокзал⛩*\n➖➖➖➖➖➖➖➖➖➖\nКошелек: *51646449*\nЦена: *150грн*\n➖➖➖➖➖➖➖➖➖➖", parse_mode="Markdown", reply_markup=opl)
		
		answer = ''
	elif call.data == 'pet2':
		opl = types.InlineKeyboardMarkup(row_width=2)
		opl.add(types.InlineKeyboardButton(text='Купить товар✔️', callback_data=6))
		bot.send_message(call.message.chat.id, text="🦋Вы выбрали: *Шишки Pablo Escobar 1г🐍*\nГород: *Ахтырка🌪*\nФасовка: *1г⚖️*\nРайон: *Петропавловская🗽*\n➖➖➖➖➖➖➖➖➖➖\nКошелек: *51646449*\nЦена: *230грн*\n➖➖➖➖➖➖➖➖➖➖", parse_mode="Markdown", reply_markup=opl)
		
		answer = ''
	elif call.data == 'cen5':
		opl = types.InlineKeyboardMarkup(row_width=2)
		opl.add(types.InlineKeyboardButton(text='Купить товар✔️', callback_data=6))
		bot.send_message(call.message.chat.id, text="🦋Вы выбрали: *Шишки Pablo Escobar 1г🐍*\nГород: *Ахтырка🌪*\nФасовка: *1г⚖️*\nРайон: *Центр🌝*\n➖➖➖➖➖➖➖➖➖➖\nКошелек: *51646449*\nЦена: *230грн*\n➖➖➖➖➖➖➖➖➖➖", parse_mode="Markdown", reply_markup=opl)
		
		answer = ''
	elif call.data == 'vok4':
		opl = types.InlineKeyboardMarkup(row_width=2)
		opl.add(types.InlineKeyboardButton(text='Купить товар✔️', callback_data=6))
		bot.send_message(call.message.chat.id, text="🦋Вы выбрали: *Шишки Pablo Escobar 1г🐍*\nГород: *Ахтырка🌪*\nФасовка: *1г⚖️*\nРайон: *Вокзал⛩*\n➖➖➖➖➖➖➖➖➖➖\nКошелек: *51646449*\nЦена: *230грн*\n➖➖➖➖➖➖➖➖➖➖", parse_mode="Markdown", reply_markup=opl)
		
		answer = ''
	elif call.data == 'pet3':
		opl = types.InlineKeyboardMarkup(row_width=2)
		opl.add(types.InlineKeyboardButton(text='Купить товар✔️', callback_data=6))
		bot.send_message(call.message.chat.id, text="🦋Вы выбрали: *Alfa PVP DeLuxe⚗🧬*\nГород: *Ахтырка🌪*\nФасовка: *0,5г⚖️*\nРайон: *Петропавловская🗽*\n➖➖➖➖➖➖➖➖➖➖\nКошелек: *51646449*\nЦена: *250грн*\n➖➖➖➖➖➖➖➖➖➖", parse_mode="Markdown", reply_markup=opl)
		
		answer = ''
	elif call.data == 'cen6':
		opl = types.InlineKeyboardMarkup(row_width=2)
		opl.add(types.InlineKeyboardButton(text='Купить товар✔️', callback_data=6))
		bot.send_message(call.message.chat.id, text="🦋Вы выбрали: *Alfa PVP DeLuxe⚗🧬*\nГород: *Ахтырка🌪*\nФасовка: *0,5г⚖️*\nРайон: *Центр🌝*\n➖➖➖➖➖➖➖➖➖➖\nКошелек: *51646449*\nЦена: *250грн*\n➖➖➖➖➖➖➖➖➖➖", parse_mode="Markdown", reply_markup=opl)
		
		answer = ''
	elif call.data == 'vok5':
		opl = types.InlineKeyboardMarkup(row_width=2)
		opl.add(types.InlineKeyboardButton(text='Купить товар✔️', callback_data=6))
		bot.send_message(call.message.chat.id, text="🦋Вы выбрали: *Alfa PVP DeLuxe⚗🧬*\nГород: *Ахтырка🌪*\nФасовка: *0,5г⚖️*\nРайон: *Вокзал⛩*\n➖➖➖➖➖➖➖➖➖➖\nКошелек: *51646449*\nЦена: *250грн*\n➖➖➖➖➖➖➖➖➖➖", parse_mode="Markdown", reply_markup=opl)
		
		answer = ''
	elif call.data == 'pet4':
		opl = types.InlineKeyboardMarkup(row_width=2)
		opl.add(types.InlineKeyboardButton(text='Купить товар✔️', callback_data=6))
		bot.send_message(call.message.chat.id, text="🦋Вы выбрали: *Амфетамин Сульфат⚗️*\nГород: *Ахтырка🌪*\nФасовка: *0,5г⚖️*\nРайон: *Петропавловская🗽*\n➖➖➖➖➖➖➖➖➖➖\nКошелек: *51646449*\nЦена: *240грн*\n➖➖➖➖➖➖➖➖➖➖", parse_mode="Markdown", reply_markup=opl)
		
		answer = ''
	elif call.data == 'cen7':
		opl = types.InlineKeyboardMarkup(row_width=2)
		opl.add(types.InlineKeyboardButton(text='Купить товар✔️', callback_data=6))
		bot.send_message(call.message.chat.id, text="🦋Вы выбрали: *Амфетамин Сульфат⚗️*\nГород: *Ахтырка🌪*\nФасовка: *0,5г⚖️*\nРайон: *Центр🌝*\n➖➖➖➖➖➖➖➖➖➖\nКошелек: *51646449*\nЦена: *240грн*\n➖➖➖➖➖➖➖➖➖➖", parse_mode="Markdown", reply_markup=opl)
		
		answer = ''
	elif call.data == 'vok6':
		opl = types.InlineKeyboardMarkup(row_width=2)
		opl.add(types.InlineKeyboardButton(text='Купить товар✔️', callback_data=6))
		bot.send_message(call.message.chat.id, text="🦋Вы выбрали: *Амфетамин Сульфат⚗️*\nГород: *Ахтырка🌪*\nФасовка: *0,5г⚖️*\nРайон: *Вокзал⛩*\n➖➖➖➖➖➖➖➖➖➖\nКошелек: *51646449*\nЦена: *240грн*\n➖➖➖➖➖➖➖➖➖➖", parse_mode="Markdown", reply_markup=opl)
		
		answer = ''
	elif call.data == 'in1':
		opl = types.InlineKeyboardMarkup(row_width=2)
		opl.add(types.InlineKeyboardButton(text='Купить товар✔️', callback_data=6))
		bot.send_message(call.message.chat.id, text="🦋Вы выбрали: *Афганка БШ 3г🍃*\nГород: *Полтава🌚*\nФасовка: *3г⚖️*\nРайон: *Институт связи🤙🏽*\n➖➖➖➖➖➖➖➖➖➖\nКошелек: *51646449*\nЦена: *150грн*\n➖➖➖➖➖➖➖➖➖➖", parse_mode="Markdown", reply_markup=opl)
		
		answer = ''
	elif call.data == 'den1':
		opl = types.InlineKeyboardMarkup(row_width=2)
		opl.add(types.InlineKeyboardButton(text='Купить товар✔️', callback_data=6))
		bot.send_message(call.message.chat.id, text="🦋Вы выбрали: *Шишки Amnesia🌳*\nГород: *Полтава🌚*\nФасовка: *1г⚖️*\nРайон: *Дендропарк🦚*\n➖➖➖➖➖➖➖➖➖➖\nКошелек: *51646449*\nЦена: *230грн*\n➖➖➖➖➖➖➖➖➖➖", parse_mode="Markdown", reply_markup=opl)
		
		answer = ''
	elif call.data == 'cen8':
		opl = types.InlineKeyboardMarkup(row_width=2)
		opl.add(types.InlineKeyboardButton(text='Купить товар✔️', callback_data=6))
		bot.send_message(call.message.chat.id, text="🦋Вы выбрали: *Шишки Amnesia🌳*\nГород: *Полтава🌚*\nФасовка: *1г⚖️*\nРайон: *Центр🌝*\n➖➖➖➖➖➖➖➖➖➖\nКошелек: *51646449*\nЦена: *230грн*\n➖➖➖➖➖➖➖➖➖➖", parse_mode="Markdown", reply_markup=opl)
		
		answer = ''
	elif call.data == 'cen9':
		opl = types.InlineKeyboardMarkup(row_width=2)
		opl.add(types.InlineKeyboardButton(text='Купить товар✔️', callback_data=6))
		bot.send_message(call.message.chat.id, text="🦋Вы выбрали: *Alfa PVP DeLuxe💎*\nГород: *Полтава🌚*\nФасовка: *0,5г⚖️*\nРайон: *Центр🌝*\n➖➖➖➖➖➖➖➖➖➖\nКошелек: *51646449*\nЦена: *250грн*\n➖➖➖➖➖➖➖➖➖➖", parse_mode="Markdown", reply_markup=opl)
		
		answer = ''
	elif call.data == 'pus1':
		opl = types.InlineKeyboardMarkup(row_width=2)
		opl.add(types.InlineKeyboardButton(text='Купить товар✔️', callback_data=6))
		bot.send_message(call.message.chat.id, text="🦋Вы выбрали: *Alfa PVP DeLuxe💎*\nГород: *Полтава🌚*\nФасовка: *0,5г⚖️*\nРайон: *Пушкина🅿️*\n➖➖➖➖➖➖➖➖➖➖\nКошелек: *51646449*\nЦена: *250грн*\n➖➖➖➖➖➖➖➖➖➖", parse_mode="Markdown", reply_markup=opl)
		
		answer = ''
	elif call.data == 'cad1':
		opl = types.InlineKeyboardMarkup(row_width=2)
		opl.add(types.InlineKeyboardButton(text='Купить товар✔️', callback_data=6))
		bot.send_message(call.message.chat.id, text="🦋Вы выбрали: *Амфетамин Сульфат💎*\nГород: *Полтава🌚*\nФасовка: *0,5г⚖️*\nРайон: *Сады❇️*\n➖➖➖➖➖➖➖➖➖➖\nКошелек: *51646449*\nЦена: *240грн*\n➖➖➖➖➖➖➖➖➖➖", parse_mode="Markdown", reply_markup=opl)
		
		answer = ''
	elif call.data == 'pav1':
		opl = types.InlineKeyboardMarkup(row_width=2)
		opl.add(types.InlineKeyboardButton(text='Купить товар✔️', callback_data=6))
		bot.send_message(call.message.chat.id, text="🦋Вы выбрали: *Амфетамин Сульфат💎*\nГород: *Полтава🌚*\nФасовка: *0,5г⚖️*\nРайон: *Павленки🚀*\n➖➖➖➖➖➖➖➖➖➖\nКошелек: *51646449*\nЦена: *240грн*\n➖➖➖➖➖➖➖➖➖➖", parse_mode="Markdown", reply_markup=opl)
		
		answer = ''
	elif call.data == 'cad2':
		opl = types.InlineKeyboardMarkup(row_width=2)
		opl.add(types.InlineKeyboardButton(text='Купить товар✔️', callback_data=6))
		bot.send_message(call.message.chat.id, text="🦋Вы выбрали: *Мефедрон💎*\nГород: *Полтава🌚*\nФасовка: *0,5г⚖️*\nРайон: *Сады❇️*\n➖➖➖➖➖➖➖➖➖➖\nКошелек: *51646449*\nЦена: *280грн*\n➖➖➖➖➖➖➖➖➖➖", parse_mode="Markdown", reply_markup=opl)
		
		answer = ''
	elif call.data == 'cen10':
		opl = types.InlineKeyboardMarkup(row_width=2)
		opl.add(types.InlineKeyboardButton(text='Купить товар✔️', callback_data=6))
		bot.send_message(call.message.chat.id, text="🦋Вы выбрали: *XTC TikTok💃🏼*\nГород: *Полтава🌚*\nФасовка: *1 колесо💊*\nРайон: *Центр🌝*\n➖➖➖➖➖➖➖➖➖➖\nКошелек: *51646449*\nЦена: *380грн*\n➖➖➖➖➖➖➖➖➖➖", parse_mode="Markdown", reply_markup=opl)
		
		answer = ''
	elif call.data == 'pus2':
		opl = types.InlineKeyboardMarkup(row_width=2)
		opl.add(types.InlineKeyboardButton(text='Купить товар✔️', callback_data=6))
		bot.send_message(call.message.chat.id, text="🦋Вы выбрали: *LSD-25💿*\nГород: *Полтава🌚*\nФасовка: *1 марка🌈*\nРайон: *Пушкина🅿️*\n➖➖➖➖➖➖➖➖➖➖\nКошелек: *51646449*\nЦена: *390грн*\n➖➖➖➖➖➖➖➖➖➖", parse_mode="Markdown", reply_markup=opl)
		
		answer = ''
	elif call.data == 'pav2':
		opl = types.InlineKeyboardMarkup(row_width=2)
		opl.add(types.InlineKeyboardButton(text='Купить товар✔️', callback_data=6))
		bot.send_message(call.message.chat.id, "🦋Вы выбрали: *LSD-25💿*\nГород: *Полтава🌚*\nФасовка: *1 марка🌈*\nРайон: *Павленки🚀*\n➖➖➖➖➖➖➖➖➖➖\nКошелек: *51646449*\nЦена: *390грн*\n➖➖➖➖➖➖➖➖➖➖", parse_mode="Markdown", reply_markup=opl)
		
		answer = ''
	
	
	elif call.data == 'back':
		answer = '🔙Назад🔙'
	elif call.data == '6':
		answer = ''
		product_hqd = types.ReplyKeyboardMarkup(resize_keyboard=True)
		product_1 = types.KeyboardButton('Проверить оплату')
		product_hqd.add(product_1)
		print("Мейби оплата")
		bot.send_message(call.message.chat.id, "Метод оплаты EasyPay. Чтобы оплатить товар, переведите на кошелек  51646449 сумму указаную выше.. После оплаты: нажмите на кнопку *Проверить оплату*. Оплачивать можно частями с разных кошельков в течении действия брони на кошелек 51646449. *Если этого фото не будет выдано автоматически, обратитесь к саппорту*✅", parse_mode="Markdown", reply_markup=product_hqd)
		
		


	bot.send_message(call.message.chat.id, answer)
	bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
			 


# Пополние
def session_cp(chat_id):
	try:
		end = datetime.now() + timedelta(minutes = 30)
		api_start = True

		while (api_start == True):

			if (datetime.now() >= end):
				api_start = False
				bot.send_message(chat_id, "💁🏻‍♀️ Время на пополнение баланса *истекло.* Повторите попытку позже.", parse_mode="Markdown")
				others.user_delete_bill(chat_id)
	except:
		pass

def create_session_cp(chat_id):
	try:
		x = threading.Thread(target = session_cp, args=(chat_id,))
		x.start()
	except:
		pass

def notification(user_id, payment):
	try:
		worker = others.found_worker(user_id)
		username = ''

		if (worker != 0) and (worker != admin_user_id):
			bot.send_message(worker, f"💞 Успешное *пополнение*\nПоздравляю!\n\n🚀 *Пользователь:* {user_id} ([@{others.name_from_id(user_id)}])\n💸 *Сумма:* {payment} ₽", parse_mode="Markdown")
			username = f'{worker} (@[{others.name_from_id(worker)}])'
		elif (worker == 0):
			username = 'не найден'
			
		bot.send_message(admin_user_id, f"💞 Успешное *пополнение*\nПоздравляю!\n\n🚀 *Пользователь:* {user_id} ([@{others.name_from_id(user_id)}])\n💸 *Сумма:* {payment} ₽\n"
			+ f"👨‍💻 *Воркер:* {username}", parse_mode="Markdown")
		bot.send_message(channel_id, f"💞 Успешное *пополнение*\nПоздравляю!\n\n🚀 *Пользователь:* {user_id} ([@{others.name_from_id(user_id)}])\n💸 *Сумма:* {payment} ₽\n"
			+ f"👨‍💻 *Воркер:* {username}", parse_mode="Markdown")
	except:
		pass

def session(chat_id):
	try:
		api = QApi(token=others.token, phone=others.phone)
		price = 1

		code = f'{bill_create(5)}_{random.randint(0, 999999999)}'
		if (code in in_comment):
			code += f'{random.randint(0, 999)}'
		else:
			in_comment.append(code)

		others.create_bill_id(chat_id, code)
		comment = api.bill(price, code)

		inline_keyboard = types.InlineKeyboardMarkup(row_width=1)
		inline = types.InlineKeyboardButton(text="Перейти к оплате", url=f'https://qiwi.com/payment/form/99?extra[%27account%27]=+{others.phone}&amountInteger=1&amountFraction=0&currency=643&extra[%27comment%27]={others.user_bill_id(chat_id)}&blocked[0]=account&blocked[1]=comment')
		inline_keyboard.add(inline)
		bot.send_message(chat_id, f"  Пополнение *баланса* QIWI\n\nЛицевой счёт: `{others.phone}`\nПримечание: `{comment}`\nМинимальный перевод: *{price}* ₽\n\nℹ️ Вы можете воспользоваться ссылкой для быстрого пополнения кошелька", parse_mode="Markdown", reply_markup=inline_keyboard)
		api.start() 

		api_start = True
		end = datetime.now() + timedelta(minutes = 5)
		while (api_start == True):
			if (datetime.now() >= end):
				api_start = False
				bot.send_message(chat_id, " Время на пополнение баланса истекло. Повторите попытку позже.")
				others.user_delete_bill(chat_id)
				api.stop()

			if api.check(comment):
				json_data = api.payments['data']
				payment = ''
				for x in json_data:
					if (x['comment']) == comment:
						payment = x['sum']['amount']
						bot.send_message(chat_id, f" Пополнение баланса *завершено*\n\nПополнение счета на сумму *{payment}* ₽ успешно завершено.", parse_mode="Markdown")
						others.user_update_balance(chat_id, int(payment))
						
						notification(chat_id, payment)

						others.user_delete_bill(chat_id)
						api.stop()
						api_start = False
						break
	except:
		pass

def create_session(chat_id):
	if (others.user_exists_bill(chat_id) == False):
		x = threading.Thread(target=session, args=(chat_id,))
		x.start()
	else:
		bot.send_message(chat_id, " У вас есть *активная* сессия. Для создания новой, Вы должны завершить предыдущую сессию.", parse_mode="Markdown")

def is_digit(string):
    if string.isdigit():
       return True
    else:
        try:
            float(string)
            return True
        except ValueError:
            return False

def bill_create(length):
   letters = string.ascii_lowercase
   return ''.join(random.choice(letters) for i in range(length))

   

def enterDeposit(message):
	try:
		price = message.text
		chat_id = message.chat.id
		if (is_digit(price) == True):

			if (int(price) >= 2):
				request = requests.get(f'https://api.crystalpay.ru/api.php?s={others.secret}&n={others.login}&o=generate&amount={price}')
				js = request.json()

				url = js['url']
				code = js['id']

				others.create_bill_id(chat_id, code)
				create_session_cp(chat_id)

				inline_keyboard = types.InlineKeyboardMarkup(row_width=1)
				inline_1 = types.InlineKeyboardButton(text="Перейти к оплате", url=f'{url}')
				inline_2 = types.InlineKeyboardButton(text="Проверить", callback_data=f'CHECK-{code}')
				inline_keyboard.add(inline_1, inline_2)
				bot.send_message(chat_id, f"ℹ️ После *оплаты* нажмите кнопку «Проверить»", parse_mode="Markdown",
					reply_markup=inline_keyboard)
			else:
				bot.send_message(chat_id, " Пополнение баланса через этот метод начинается от *2 рублей*", parse_mode="Markdown")
		else:
			bot.send_message(chat_id, " Ошибка: укажите *сумму* пополнения", parse_mode="Markdown")
	except:
		pass
# Пополние платежной системой

def user_invite_code(message):
	try:
		code = message.text
		chat_id = message.chat.id
		if (is_digit(code) == True):
			if (others.user_exists(code) == True):
				others.user_update_referal(chat_id, code)
				bot.send_message(chat_id, "💁🏻‍♀️ Здорово! Вы получили бонус в размере *50* рублей!", parse_mode="Markdown")
				bot.send_message(code, f"❤️ /{chat_id} использовал твой *код-приглашение*", parse_mode="Markdown")
			else:
				bot.send_message(chat_id, "💁🏻‍♀️ Код-приглашение *не найден*", parse_mode="Markdown")
		else:
			bot.send_message(chat_id, "💁🏻‍♀️ Код-приглашение *не найден*", parse_mode="Markdown")
	except:
		pass

@bot.message_handler(commands=['start'])  
def start_command(message):
	chat_id = message.chat.id
	command = message.text
	user_name = message.from_user.username



@bot.message_handler(content_types=['text'])
def get_text_messages(message):
	chat_message = message.text
	chat_id = message.chat.id
	qqq=message.text

	if (chat_message == "🔱Мой профиль🔱"):
		inline_keyboard = types.InlineKeyboardMarkup(row_width=1)
		bot.send_message(chat_id, f"⚡️*Твой* профиль\n\n🚀Telegram ID: *{chat_id}*\n💸Баланс: {others.user_balance(chat_id)} " +
			f"\n✅*Количество покупок:* 0\n🤝*Приглашено*: {others.user_count_ref(chat_id)} пользователей", parse_mode="Markdown", reply_markup=inline_keyboard)
	elif (chat_message == "Отзывы"):
		bot.send_message(chat_id, f"💁🏻‍♀️ *Отзывы* о нас\n\nПосмотреть отзывы Вы можете в нашей группе: [{others.group}]",
			parse_mode="Markdown")
	elif (chat_message == "‼️Правила‼️"):
		bot.send_message(chat_id, f"*ПРАВИЛА*\n1.Перезаклад *50%*, если берешь в первые\n2.Все вопросы решаются через менеджера \n3.СПАМ МЕНЕДЖЕРУ В ЛС=*БАН*\n\nПолный список по ссылке:",
			parse_mode="Markdown")
	elif (chat_message == "💵Купить💵"):
		bot.send_message(chat_id, "Выберите город из списка: ", parse_mode="Markdown",
			reply_markup=product)
	elif (chat_message == "Харьков"):
		product_hd = types.ReplyKeyboardMarkup(resize_keyboard=True)
		product_1 = types.KeyboardButton('OG KUSH БШ 3г🌿')
		product_3 = types.KeyboardButton('Шишки АК-47 1г🐲')
		product_30 = types.KeyboardButton('Шишки АК-47 2г🐲')
		product_31 = types.KeyboardButton('Шишки Amnesia 1г🐉')
		product_32 = types.KeyboardButton('Шишки Amnesia 2г🐍')
		product_4 = types.KeyboardButton('Alfa PVP DeLuxe 0.5г💎')
		product_40 = types.KeyboardButton('Alfa PVP DeLuxe 1г🧿')
		product_5 = types.KeyboardButton('Амфетамин Сульфат 0.5г💎')
		product_50 = types.KeyboardButton('Амфетамин Сульфат 1г⚜💎')
		product_6 = types.KeyboardButton('Мефедрон  0.5г⚗️')
		product_7 = types.KeyboardButton('Экстези Etherium💊')
		product_8 = types.KeyboardButton('Экстези Batman🦇')
		back = types.KeyboardButton('🔙Назад🔙')
		product_hd.add(product_1)
		product_hd.add(product_3, product_30)
		product_hd.add(product_31, product_32)
		product_hd.add(product_4, product_40)
		product_hd.add(product_5, product_50)
		product_hd.add(product_7, product_8)
		product_hd.add(product_6)
		product_hd.add(back)

		bot.send_message(chat_id, "Ваш товар", parse_mode="Markdown",
			reply_markup=product_hd)
	elif (chat_message == "Сумы"):
		product_hd = types.ReplyKeyboardMarkup(resize_keyboard=True)
		product_1 = types.KeyboardButton('OG-Kush БШ 3г🌳')
		product_2 = types.KeyboardButton('План(Сыпуха) 3г🌱')
		product_3 = types.KeyboardButton('Шишки Mango Kush 1г🐍')
		product_30 = types.KeyboardButton('Амфетамин Розовый 0.5г💎')
		product_31 = types.KeyboardButton('Шишки OG-Kush 1г☘️')
		product_4 = types.KeyboardButton('Alfa PVP DeLuxe 0.5г⚡️')
		product_50 = types.KeyboardButton('Амфетамин Розовый 1г💎')
		product_7 = types.KeyboardButton('Экстези Barcelona💊')
		product_8 = types.KeyboardButton('Печеньки с ТГК🍪')
		back = types.KeyboardButton('🔙Назад🔙')
		product_hd.add(product_8)
		product_hd.add(product_2, product_1)
		product_hd.add(product_3, product_31)
		product_hd.add(product_50, product_30)
		product_hd.add(product_4)
		product_hd.add(product_7)
		product_hd.add(back)
		bot.send_message(chat_id, "Ваш товар", parse_mode="Markdown", reply_markup=product_hd)
	elif (chat_message == "Ахтырка"):
		product_hqd = types.ReplyKeyboardMarkup(resize_keyboard=True)
		product_1 = types.KeyboardButton('Битые шишки 3г🌱')
		product_31 = types.KeyboardButton('Шишки Pablo Escobar 1г🐍')
		product_4 = types.KeyboardButton('Alfa PVP DeLuxe 0.5г⚗🧬')
		product_5 = types.KeyboardButton('Амфетамин Сульфат 0.5г⚗️')
		back = types.KeyboardButton('🔙Назад🔙')
		product_hqd.add(product_1)
		product_hqd.add(product_31)
		product_hqd.add(product_4)
		product_hqd.add(product_5)
		product_hqd.add(back)
		bot.send_message(chat_id, "Ваш товар", parse_mode="Markdown", reply_markup=product_hqd)
	elif (chat_message == "Полтава"):
		product_hqd = types.ReplyKeyboardMarkup(resize_keyboard=True)
		product_1 = types.KeyboardButton('Афганка БШ 3г🍃')
		product_31 = types.KeyboardButton('Шишки Amnesia 1г🌳')
		product_4 = types.KeyboardButton('Alfa PVP DeLuxe 0.5г💎')
		product_5 = types.KeyboardButton('Амфетамин Сульфат 0.5г💎')
		product_6 = types.KeyboardButton('Мефедрон  0.5г💎')
		product_7 = types.KeyboardButton('Экстези TikTok💊')
		product_8 = types.KeyboardButton('LSD-25💿')
		back = types.KeyboardButton('🔙Назад🔙')
		product_hqd.add(product_1)
		product_hqd.add(product_31)
		product_hqd.add(product_4, product_5)
		product_hqd.add(product_7, product_8)
		product_hqd.add(product_6)
		product_hqd.add(back)
		bot.send_message(chat_id, "Ваш товар", parse_mode="Markdown", reply_markup=product_hqd)
	
	#Харьков
	elif (chat_message == "Шишки АК-47 1г🐲"):
		product_hqd = types.ReplyKeyboardMarkup(resize_keyboard=True)
		product_1 = types.KeyboardButton('ТРК')
		product_2 = types.KeyboardButton('Гагарина')	
		product_hqd.add(product_1, product_2)
		hh=bot.send_message(chat_id, "Выберите район:", parse_mode="Markdown")
		back = types.KeyboardButton('🔙Назад🔙')
		product_hqd.add(back)
		bot.send_message(chat_id, "Вы выбрали:\nШишки АК-47🐲\n\n➖➖➖➖➖➖➖➖➖➖➖\nГенотип:\n-Гибрид🐍\n65% сатива / 35% индика🌖\n\nТГК 24.5%🔥\n\nПоложительные эффекты:\n-креативность🧠\n\n-эйфория🤪\n\n-ощущение счастья🤤\n\n-улучшение настроения\n\nНеприхотливая, урожайная, быстро цветущая сатива, дающая мощный, но ласковый хай в голове и уют в теле. Несмотря на свое «металлическое» название, АК-47 наполняет тело мягким ощущением релакса, и способен приковать курильщика к дивану. C первой банки вы без пауз оказываетесь в приятной эйфории и постепенно расслабляетесь до неги и истомы🔥\n➖➖➖➖➖➖➖➖➖➖➖\nВыберите фасовку:", parse_mode="Markdown", reply_markup=product_hqd)
		bot.register_next_step_handler(hh, pay1)
	elif (chat_message == "Шишки АК-47 2г🐲"):
		product_hqd = types.ReplyKeyboardMarkup(resize_keyboard=True)
		product_1 = types.KeyboardButton('ТРК')
		product_2 = types.KeyboardButton('Гагарина')	
		product_hqd.add(product_1, product_2)
		hh=bot.send_message(chat_id, "Выберите район:", parse_mode="Markdown")
		product_hqd = types.ReplyKeyboardMarkup(resize_keyboard=True)
		back = types.KeyboardButton('🔙Назад🔙')
		product_hqd.add(back)
		bot.send_message(chat_id, "ФОто иВы выбрали:\nШишки АК-47🐲\n\n➖➖➖➖➖➖➖➖➖➖➖\nГенотип:\n-Гибрид🐍\n65% сатива / 35% индика🌖\n\nТГК 24.5%🔥\n\nПоложительные эффекты:\n-креативность🧠\n\n-эйфория🤪\n\n-ощущение счастья🤤\n\n-улучшение настроения\n\nНеприхотливая, урожайная, быстро цветущая сатива, дающая мощный, но ласковый хай в голове и уют в теле. Несмотря на свое «металлическое» название, АК-47 наполняет тело мягким ощущением релакса, и способен приковать курильщика к дивану. C первой банки вы без пауз оказываетесь в приятной эйфории и постепенно расслабляетесь до неги и истомы🔥\n➖➖➖➖➖➖➖➖➖➖➖\nВыберите фасовку:", parse_mode="Markdown", reply_markup=product_hqd)
		bot.register_next_step_handler(hh, pay3)
	elif (chat_message == "Шишки Amnesia 1г🐉"):
		product_hqd = types.ReplyKeyboardMarkup(resize_keyboard=True)
		product_1 = types.KeyboardButton('Киевский')
		product_2 = types.KeyboardButton('Майдан')
		hh=bot.send_message(chat_id, "Выберите район:", parse_mode="Markdown")	
		product_hqd.add(product_1, product_2)
		back = types.KeyboardButton('🔙Назад🔙')
		product_hqd.add(back)
		bot.send_message(chat_id, "ФОто\n➖➖➖➖➖➖➖➖➖➖➖\nГенотип:\n-гибрид🐍\nВ основном Сатива (Сатива 80%, Индика 20%)🌖\nПоложительные эффекты:\n-креативность🧠\n-эйфория🤪\n-чувство благополучия и счастья🤤\n\nПосле 1-го джойнта или бонга вы будете более чем удовлетворены дымом💨\nКаждый хит приходит с поистине психоделическим эффектом с ясной головой, вероятно, чтобы отправить любого пользователя прямо в дали небесные.\n\nВкус свежий и фруктовый, что и стоило ожидать от дымки.\nКурильщики предупреждают, что это сильная джумба и, как следует из названия, пользователи могут впасть в действительно полный транс🔥\n➖➖➖➖➖➖➖➖➖➖➖\nВыбирете фасовку:", parse_mode="Markdown", reply_markup=product_hqd)
		bot.register_next_step_handler(pay4, hh)
	elif (chat_message == "Шишки Amnesia 2г🐍"):
		product_hqd = types.ReplyKeyboardMarkup(resize_keyboard=True)
		product_1 = types.KeyboardButton('Киевский')
		product_2 = types.KeyboardButton('Майдан')
		hh=bot.send_message(chat_id, "Выберите район:", parse_mode="Markdown")	
		product_hqd.add(product_1, product_2)
		back = types.KeyboardButton('🔙Назад🔙')
		product_hqd.add(back)
		bot.send_message(chat_id, "ФОто\nВы выбрали:\nШишки Amnesia Haze🐉\n\n➖➖➖➖➖➖➖➖➖➖➖\nГенотип:\n-гибрид🐍\nВ основном Сатива (Сатива 80%, Индика 20%)🌖\n\nПоложительные эффекты:\n-креативность🧠\n\n-эйфория🤪\n\n-чувство благополучия и счастья🤤\n\nПосле 1-го джойнта или бонга вы будете более чем удовлетворены дымом💨\n\nКаждый хит приходит с поистине психоделическим эффектом с ясной головой, вероятно, чтобы отправить любого пользователя прямо в дали небесные.\n\nВкус свежий и фруктовый, что и стоило ожидать от дымки.\nКурильщики предупреждают, что это сильная джумба и, как следует из названия, пользователи могут впасть в действительно полный транс🔥\n➖➖➖➖➖➖➖➖➖➖➖\nВыбирете фасовку:", parse_mode="Markdown", reply_markup=product_hqd)
		bot.register_next_step_handler(hh, pay5)
	elif (chat_message == "Alfa PVP DeLuxe 0.5г🌪"):
		product_hqd = types.ReplyKeyboardMarkup(resize_keyboard=True)
		product_1 = types.KeyboardButton('ТГК')
		product_2 = types.KeyboardButton('Майдан')	
		hh=bot.send_message(chat_id, "Выберите район:", parse_mode="Markdown")	
		product_hqd.add(product_1, product_2)
		back = types.KeyboardButton('🔙Назад🔙')
		product_hqd.add(back)
		bot.send_message(chat_id, "ФОто и описание", parse_mode="Markdown", reply_markup=product_hqd)
		bot.register_next_step_handler(hh, pay6)
	elif (chat_message == "Alfa PVP DeLuxe 1г🧿"):
		product_hqd = types.ReplyKeyboardMarkup(resize_keyboard=True)
		product_1 = types.KeyboardButton('ТГК')
		product_2 = types.KeyboardButton('Майдан')	
		hh=bot.send_message(chat_id, "Выберите район:", parse_mode="Markdown")
		back = types.KeyboardButton('🔙Назад🔙')
		product_hqd.add(back)
		bot.send_message(chat_id, "ФОто и описание", parse_mode="Markdown", reply_markup=product_hqd)
		bot.register_next_step_handler(hh, pay7)
	elif (chat_message == "Амфетамин Сульфат 0.5г"):
		product_hqd = types.ReplyKeyboardMarkup(resize_keyboard=True)
		product_1 = types.KeyboardButton('ТГК')
		product_2 = types.KeyboardButton('Майдан')	
		hh=bot.send_message(chat_id, "Выберите район:", parse_mode="Markdown")
		back = types.KeyboardButton('🔙Назад🔙')
		product_hqd.add(back)
		bot.send_message(chat_id, "ФОто и описание", parse_mode="Markdown", reply_markup=product_hqd)
		bot.register_next_step_handler(hh, pay8)
	elif (chat_message == "Амфетамин Сульфат 1г"):
		product_hqd = types.ReplyKeyboardMarkup(resize_keyboard=True)
		product_1 = types.KeyboardButton('ТГК')
		product_2 = types.KeyboardButton('Майдан')	
		hh=bot.send_message(chat_id, "Выберите район:", parse_mode="Markdown")
		back = types.KeyboardButton('🔙Назад🔙')
		product_hqd.add(back)
		bot.send_message(chat_id, "ФОто и описание", parse_mode="Markdown", reply_markup=product_hqd)
		bot.register_next_step_handler(hh, pay9)
	elif (chat_message == "Мефедрон  0.5г🦠"):
		product_hqd = types.ReplyKeyboardMarkup(resize_keyboard=True)
		product_1 = types.KeyboardButton('ТГК')
		product_2 = types.KeyboardButton('Майдан')	
		hh=bot.send_message(chat_id, "Выберите район:", parse_mode="Markdown")
		back = types.KeyboardButton('🔙Назад🔙')
		product_hqd.add(back)
		bot.send_message(chat_id, "ФОто и описание", parse_mode="Markdown", reply_markup=product_hqd)
		bot.register_next_step_handler(hh, pay10)
	elif (chat_message == "Экстези Etherium"):
		product_hqd = types.ReplyKeyboardMarkup(resize_keyboard=True)
		product_1 = types.KeyboardButton('ТГК')
		product_2 = types.KeyboardButton('Майдан')	
		hh=bot.send_message(chat_id, "Выберите район:", parse_mode="Markdown")
		back = types.KeyboardButton('🔙Назад🔙')
		product_hqd.add(back)
		bot.send_message(chat_id, "ФОто и\nВы выбрали:\nEcstasy Etheruim💊\n\n➖➖➖➖➖➖➖➖➖➖➖\nДозировка: 300 мг🤏\nСпособ употребления: пероральный☝🏿\nВес: около 1г⚖️\nВид: качественно спресованная таблетка экстази аккуратной формы известной криптовалюты Эфир. Очень твердая💊\nЦвет: Фиолетовый⚛️\nВкус: горькая. Менее горькая, чем чистый мдма✅\n➖➖➖➖➖➖➖➖➖➖➖\nВыбирете фасовку:", parse_mode="Markdown", reply_markup=product_hqd)
		bot.register_next_step_handler(hh, pay11)
	elif (chat_message == "Экстези Batman🦇"):
		product_hqd = types.ReplyKeyboardMarkup(resize_keyboard=True)
		product_1 = types.KeyboardButton('ТГК')
		product_2 = types.KeyboardButton('Майдан')	
		hh=bot.send_message(chat_id, "Выберите район:", parse_mode="Markdown")
		back = types.KeyboardButton('🔙Назад🔙')
		product_hqd.add(back)
		bot.send_message(chat_id, "ФОто и\nВы выбрали:\nEcstasy Batman💊\n\n➖➖➖➖➖➖➖➖➖➖➖\nДозировка: 300 мг🤏\nСпособ употребления: пероральный☝🏿\nВес: около 1г⚖️\nВид: качественно спресованная таблетка экстази формы летучей мыши🦇 Очень твердая💊\nВкус: горькая✅\n➖➖➖➖➖➖➖➖➖➖➖\nВыбирете фасовку:", parse_mode="Markdown", reply_markup=product_hqd)
		bot.register_next_step_handler(hh, pay12)
	
	#Sumy
	elif (chat_message == "OG-Kush БШ 3г🌳"):
		product_hqd = types.ReplyKeyboardMarkup(resize_keyboard=True)
		of = types.KeyboardButton('OG-Kush БШ 3г')
		back = types.KeyboardButton('🔙Назад🔙')
		product_hqd.add(of)
		product_hqd.add(back)
		h=bot.send_message(chat_id, "*Цена: 150грн*" , parse_mode="Markdown")
		bot.send_message(chat_id, "➖➖➖➖➖➖➖➖➖➖➖\nБитое шишло OG🌿\nХорошая однобаночная джумба с перетёртых шишек🌳\n➖➖➖➖➖➖➖➖➖➖➖\nВыбирете фасовку:", parse_mode="Markdown", reply_markup=product_hqd)
		bot.register_next_step_handler(h, pay13)
	elif (chat_message == "План(Сыпуха) 3г🌱"):
		product_hqd = types.ReplyKeyboardMarkup(resize_keyboard=True)
		product_1 = types.KeyboardButton('План(Сыпуха) 3г')
		product_hqd.add(product_1)
		h=bot.send_message(chat_id, "*Цена: 120грн*" , parse_mode="Markdown")
		back = types.KeyboardButton('🔙Назад🔙')
		product_hqd.add(back)
		bot.send_message(chat_id, "Вы выбрали:\nПлан🌿\n➖➖➖➖➖➖➖➖➖➖➖\n\nОтличный двухбаночный стаффчик🌿\n\n➖➖➖➖➖➖➖➖➖➖➖\nВыбирете фасовку:", parse_mode="Markdown", reply_markup=product_hqd)
		bot.register_next_step_handler(h,pay14)
	elif (chat_message == "Шишки Mango Kush 1г🐍"):
		product_hqd = types.ReplyKeyboardMarkup(resize_keyboard=True)
		product_1 = types.KeyboardButton('Шишки Mango Kush 1г')
		product_hqd.add(product_1)
		h=bot.send_message(chat_id, "*Цена: 230грн*" , parse_mode="Markdown")
		back = types.KeyboardButton('🔙Назад🔙')
		product_hqd.add(back)
		bot.send_message(chat_id, "Вы выбрали:\nШишки Mango Kush🥭\n\n➖➖➖➖➖➖➖➖➖➖➖\nГенотип:\n-Гибрид🐍\n75% сатива / 25% индика🌖\n\nТГК 27%🔥\n\nВкус, аромат: Манго🥭\n\nЭффект: сбалансированный, эйфория переходящая в релакс🤤\n\nАроматическая палитра пролеченных шишек наполнена ароматами тропического манго и апельсина. Сбалансированное воздействие культуры придется по нраву ценителям релакса в сопровождении легкой эйфории🔥\n➖➖➖➖➖➖➖➖➖➖➖\nВыберите фасовку:", parse_mode="Markdown", reply_markup=product_hqd)
		bot.register_next_step_handler(h, pay15)
	elif (chat_message == "Амфетамин Розовый 0.5г💎"):
		product_hqd = types.ReplyKeyboardMarkup(resize_keyboard=True)
		product_1 = types.KeyboardButton('Амфетамин Розовый 0.5г')
		product_hqd.add(product_1)
		back = types.KeyboardButton('🔙Назад🔙')
		h=bot.send_message(chat_id, "*Цена: 250грн*" , parse_mode="Markdown")
		product_hqd.add(back)
		bot.send_message(chat_id, '\nВы выбрали:\Амфетамин розовый💎\n\n➖➖➖➖➖➖➖➖➖➖➖\nДозировка для однократного употребления:  0,1г🤏\nСпособ употребления: пернозальный☝🏿\nВес: около 0,5/1 г⚖️\nВкус: горький✅\n➖➖➖➖➖➖➖➖➖➖➖\nВыберите фасовку:', parse_mode="Markdown", reply_markup=product_hqd)
		bot.register_next_step_handler(h, pay16)
	elif (chat_message == "Шишки OG-Kush 1г☘️"):
		product_hqd = types.ReplyKeyboardMarkup(resize_keyboard=True)
		product_1 = types.KeyboardButton('Шишки OG-Kush 1г')
		product_hqd.add(product_1)
		back = types.KeyboardButton('🔙Назад🔙')
		product_hqd.add(back)
		h=bot.send_message(chat_id, "*Цена: 230грн*" , parse_mode="Markdown")
		bot.send_message(chat_id, "Вы выбрали:\nШишки  OG-Kush🐍\n\\n➖➖➖➖➖➖➖➖➖➖➖\nГенотип:\n-Гибрид🐍\n25% сатива / 75% индика🌒\n\nТГК 25%🔥\n\nВысушенные соцветия издают цитрусово-хвойный запах. Stone-эффект присутствует — все биоритмы организма на момент действия несколько замедляются, но с точки зрения курильщика незаметен. Преобладает мощный cerebral high, сподвигающий людей на весёлые и отважные поступки, а также придающий бесстрашие — именно эта черта сорта Pablo Escobar и снискала ему столь мужское имя. Подходит для ежедневного употребления, утром тонизирует эффективнее, чем напитки на основе кофеина и танина🔥\n➖➖➖➖➖➖➖➖➖➖➖\nВыберите фасовку:", parse_mode="Markdown", reply_markup=product_hqd)
		bot.register_next_step_handler(h, pay17)
	elif (chat_message == "Alfa PVP DeLuxe 0.5г⚡️"):
		product_hqd = types.ReplyKeyboardMarkup(resize_keyboard=True)
		product_1 = types.KeyboardButton('Alfa PVP DeLuxe 0.5г')
		product_hqd.add(product_1)
		back = types.KeyboardButton('🔙Назад🔙')
		h=bot.send_message(chat_id, "*Цена: 250грн*" , parse_mode="Markdown")
		product_hqd.add(back)
		bot.send_message(chat_id, "\nВы выбрали:\Alfa PVP DeLuxe 💎\n\n➖➖➖➖➖➖➖➖➖➖➖\nДозировка для однократного употребления:  0,1г-0,2🤏\nСпособ употребления: пернозальный/лампа☝🏿\nВес: около 0,5/1 г⚖️\nВкус: горькая✅\n➖➖➖➖➖➖➖➖➖➖➖\nВыберите фасовку:", parse_mode="Markdown", reply_markup=product_hqd)
		bot.register_next_step_handler(h, pay18)
	elif (chat_message == "Амфетамин Розовый 1г💎"):
		product_hqd = types.ReplyKeyboardMarkup(resize_keyboard=True)
		product_1 = types.KeyboardButton('Амфетамин Розовый 1г')
		product_hqd.add(product_1)
		back = types.KeyboardButton('🔙Назад🔙')
		product_hqd.add(back)
		h=bot.send_message(chat_id, "*Цена: 400грн*" , parse_mode="Markdown")
		bot.send_message(chat_id, '\nВы выбрали:\Амфетамин розовый💎\n\n➖➖➖➖➖➖➖➖➖➖➖\nДозировка для однократного употребления:  0,1г🤏\nСпособ употребления: пернозальный☝🏿\nВес: около 0,5/1 г⚖️\nВкус: горький✅\n➖➖➖➖➖➖➖➖➖➖➖\nВыберите фасовку:', parse_mode="Markdown", reply_markup=product_hqd)
		bot.register_next_step_handler(h, pay19)
	elif (chat_message == "Экстези Barcelona💊"):
		product_hqd = types.ReplyKeyboardMarkup(resize_keyboard=True)
		product_1 = types.KeyboardButton('Экстези Barcelona 1шт')
		product_hqd.add(product_1)
		back = types.KeyboardButton('🔙Назад🔙')
		product_hqd.add(back)
		h=bot.send_message(chat_id, "*Цена: 380грн*" , parse_mode="Markdown")
		bot.send_message(chat_id, "Вы выбрали:\nEcstasy Barcelona💊\n\n➖➖➖➖➖➖➖➖➖➖➖\nДозировка: 300 мг🤏\nСпособ употребления: пероральный☝🏿\nВес: около 1г⚖️\nВид: качественно спресованная таблетка экстази аккуратной формы известной футбольной команды. Очень твердая💊\nВкус: горькая. Менее горькая, чем чистый мдма✅\n➖➖➖➖➖➖➖➖➖➖➖\nВыбирете фасовку:", parse_mode="Markdown", reply_markup=product_hqd)
		bot.register_next_step_handler(h,pay20)
	elif (chat_message == "Печеньки с ТГК🍪"):
		product_hqd = types.ReplyKeyboardMarkup(resize_keyboard=True)
		product_1 = types.KeyboardButton('Печеньки с ТГК 1шт')
		product_hqd.add(product_1)
		back = types.KeyboardButton('🔙Назад🔙')
		product_hqd.add(back)
		hh=bot.send_message(chat_id, "*Цена: 200грн*", parse_mode="Markdown")
		bot.send_message(chat_id, '\nВы выбрали:\Печенье с ТГК🍪\n\n➖➖➖➖➖➖➖➖➖➖➖\nСъеденная марихуана работает по-другому\n\nКурение марихуаны и поедание ее по-разному влияют на тело и сознание человека. Когда вы курите марихуану, ваше тело превращает непсихоактивный ТГК, главный психотропный компонент марихуаны, в ТГК дельта-9.\nИменно эта форма ТГК вызывает те самые качества, которыми знамениты курильщики – тяжелые веки, апатию и расслабленность, хихиканье, зажоры.\nСъеденная марихуана приводит к другому эффекту, так как тело, фактически, превращает непсихоактивную форму ТГК не в ТГК дельта-9, а в ТГК дельта-11.\nЭто, в свою очередь, вызывает другой эффект в сознании и теле человека: его последствия более приятны, чем эффект от выкуренной самокрутки с марихуаной.\n➖➖➖➖➖➖➖➖➖➖➖\nВыбирете район:', parse_mode="Markdown", reply_markup=product_hqd)
		bot.register_next_step_handler(hh, pay21)
		#do kazdogo postav "hh" vazno suka ne zabud!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!)

#ахтырка
	elif (chat_message == "Битые шишки 3г🌱"):
		product_hqd = types.ReplyKeyboardMarkup(resize_keyboard=True)
		product_1 = types.KeyboardButton('Битые шишки 3г')
		product_hqd.add(product_1)
		hh=bot.send_message(chat_id, "*Цена: 150грн*", parse_mode="Markdown")
		bot.send_message(chat_id, "Вы выбрали:\nБитые шишки🌳\n\n➖➖➖➖➖➖➖➖➖➖➖\nБитое шишло🌿\nХорошая однобаночная жбумба с перетёртых шишек🌳\n➖➖➖➖➖➖➖➖➖➖➖\nВыбирете фасовку:", parse_mode="Markdown", reply_markup=product_hqd)
		bot.register_next_step_handler(hh, pay22)
	elif (chat_message == "Шишки Pablo Escobar 1г🐍"):
		product_hqd = types.ReplyKeyboardMarkup(resize_keyboard=True)
		product_1 = types.KeyboardButton('Шишки Pablo Escobar 1г')
		product_hqd.add(product_1)
		hh=bot.send_message(chat_id, "*Цена: 230грн*", parse_mode="Markdown")
		bot.send_message(chat_id, "Вы выбрали:\nШишки Pablo Eskobar🐍\n\n➖➖➖➖➖➖➖➖➖➖➖\nГенотип:\n-Гибрид🐍\n25% сатива / 75% индика🌒\n\nТГК 24%🔥\n\nВкус, аромат:\n\n-Сладкий\n\nЭфект:\n\n-Мощный, церебральный, расслабляющий\n\nНЭто настоящий гангстерский стаффчик, ходят слухи, что все Американские знаменитости просто обожают этот сорт, в особенности рэперы. Этот гибрид разрывает твоё понимание о каннабисе просто в клочья, до того как попробовал его, я и представить не мог, что так бывает.\nДым заходит не очень легко, если ты не прикурен, но моментально накрывает волной, словно ты попал в океан посреди штрома, через 10 минут этот шок проходит и ты понимаешь, за что его так любят рэперы. Дело в том, что в голове ты чувстуешь поток мыслей, радость и желание творить, чистый хай, а тело находится под воздействием жесткого стоуна и от этого диссонанса мозг начинает вырабатывать просто гениальные мысли, правда которые потом очень сложно вспомнить.\nСорт отноcим к категории — на выходные, заниматься какими-либо важными делами невозможно. Крайне легко «перебрать» поэтому новичкам относиться к этому сорту с осторожностью🔥\n➖➖➖➖➖➖➖➖➖➖➖\nВыберите фасовку:", parse_mode="Markdown", reply_markup=product_hqd)
		bot.register_next_step_handler(hh, pay24)
	elif (chat_message == "Alfa PVP DeLuxe 0.5г⚗🧬"):
		product_hqd = types.ReplyKeyboardMarkup(resize_keyboard=True)
		product_1 = types.KeyboardButton('Alfa PVP DeLuxe 0.5г')
		product_hqd.add(product_1)
		hh=bot.send_message(chat_id, "*Цена: 250грн*", parse_mode="Markdown")
		bot.send_message(chat_id, "\nВы выбрали:\Alfa PVP DeLuxe 💎\n\n➖➖➖➖➖➖➖➖➖➖➖\nДозировка для однократного употребления:  0,1г-0,2🤏\nСпособ употребления: пернозальный/лампа☝🏿\nВес: около 0,5/1 г⚖️\nВкус: горькая✅\n➖➖➖➖➖➖➖➖➖➖➖\nВыбирете фасовку:", parse_mode="Markdown", reply_markup=product_hqd)
		bot.register_next_step_handler(hh, pay25)
	elif (chat_message == "Амфетамин Сульфат 0.5г⚗️"):
		product_hqd = types.ReplyKeyboardMarkup(resize_keyboard=True)
		product_1 = types.KeyboardButton('Амфетамин Сульфат 0.5г')
		product_hqd.add(product_1)
		hh=bot.send_message(chat_id, "*Цена: 250грн*", parse_mode="Markdown")
		bot.send_message(chat_id, "\nВы выбрали:\Амфетамин Сульфат💎\n\n➖➖➖➖➖➖➖➖➖➖➖\nДозировка для однократного употребления:  0,1г🤏\nСпособ употребления: пернозальный☝🏿\nВес: около 0,5/1 г⚖️\nВкус: горький✅\n➖➖➖➖➖➖➖➖➖➖➖\nВыбирете фасовку:", parse_mode="Markdown", reply_markup=product_hqd)
		bot.register_next_step_handler(hh, pay26)

	
#poltava

	elif (chat_message == "Афганка БШ 3г🍃"):
		product_hqd = types.ReplyKeyboardMarkup(resize_keyboard=True)
		product_1 = types.KeyboardButton('Афганка БШ 3г')
		product_hqd.add(product_1)
		hh=bot.send_message(chat_id, "*Цена: 150грн*", parse_mode="Markdown")
		bot.send_message(chat_id, "Вы выбрали:\nБитое шишло Afgan Kush🌿\n\n➖➖➖➖➖➖➖➖➖➖➖\nХорошая однобаночная джумба с перетёртых шишек🌳\n➖➖➖➖➖➖➖➖➖➖➖\nВыбирете фасовку:", parse_mode="Markdown", reply_markup=product_hqd)
		bot.register_next_step_handler(hh, pay30)
	elif (chat_message == "Шишки Amnesia 1г🌳"):
		product_hqd = types.ReplyKeyboardMarkup(resize_keyboard=True)
		product_1 = types.KeyboardButton('Шишки Amnesia 1г')
		product_hqd.add(product_1)
		hh=bot.send_message(chat_id, "*Цена: 230грн*", parse_mode="Markdown")
		bot.send_message(chat_id, "Вы выбрали:\nШишки Amnesia Haze🐉\n\n➖➖➖➖➖➖➖➖➖➖➖\nГенотип:\n-гибрид🐍\nВ основном Сатива (Сатива 80%, Индика 20%)🌖\n\nПоложительные эффекты:\n-креативность🧠\n\n-эйфория🤪\n\n-чувство благополучия и счастья🤤\n\nПосле 1-го джойнта или бонга вы будете более чем удовлетворены дымом💨\n\nКаждый хит приходит с поистине психоделическим эффектом с ясной головой, вероятно, чтобы отправить любого пользователя прямо в дали небесные.\n\nВкус свежий и фруктовый, что и стоило ожидать от дымки.\nКурильщики предупреждают, что это сильная джумба и, как следует из названия, пользователи могут впасть в действительно полный транс🔥\n➖➖➖➖➖➖➖➖➖➖➖\nВыбирете фасовку:", parse_mode="Markdown", reply_markup=product_hqd)
		bot.register_next_step_handler(hh, pay32)
	elif (chat_message == "Alfa PVP DeLuxe 0.5г💎"):
		product_hqd = types.ReplyKeyboardMarkup(resize_keyboard=True)
		product_1 = types.KeyboardButton('Alfa PVP DeLuxe 0.5г')
		product_hqd.add(product_1)
		hh=bot.send_message(chat_id, "*Цена: 250грн*", parse_mode="Markdown")
		bot.send_message(chat_id, "\nВы выбрали:\Alfa PVP DeLuxe 💎\n\n➖➖➖➖➖➖➖➖➖➖➖\nДозировка для однократного употребления:  0,1г-0,2🤏\nСпособ употребления: пернозальный/лампа☝🏿\nВес: около 0,5/1 г⚖️\nВкус: горькая✅\n➖➖➖➖➖➖➖➖➖➖➖\nВыбирете фасовку:", parse_mode="Markdown", reply_markup=product_hqd)
		bot.register_next_step_handler(hh, pay33)
	elif (chat_message == "Амфетамин Сульфат 0.5г💎"):
		product_hqd = types.ReplyKeyboardMarkup(resize_keyboard=True)
		product_1 = types.KeyboardButton('Амфетамин Сульфат 0.5г')
		product_hqd.add(product_1)
		hh=bot.send_message(chat_id, "*Цена: 240грн*", parse_mode="Markdown")
		bot.send_message(chat_id, "\nВы выбрали:\Амфетамин Сульфат💎\n\n➖➖➖➖➖➖➖➖➖➖➖\nДозировка для однократного употребления:  0,1г🤏\nСпособ употребления: пернозальный☝🏿\nВес: около 0,5/1 г⚖️\nВкус: горький✅\n➖➖➖➖➖➖➖➖➖➖➖\nВыбирете фасовку:", parse_mode="Markdown", reply_markup=product_hqd)
		bot.register_next_step_handler(hh, pay34)
	elif (chat_message == "Мефедрон  0.5г💎"):
		product_hqd = types.ReplyKeyboardMarkup(resize_keyboard=True)
		product_1 = types.KeyboardButton('Мефедрон  0.5г')
		product_hqd.add(product_1)
		hh=bot.send_message(chat_id, "*Цена: 280грн*", parse_mode="Markdown")
		bot.send_message(chat_id, "\nВы выбрали:\Мефедрон💎\n\n➖➖➖➖➖➖➖➖➖➖➖\nМефедро́н, также известный как 4-метилметкатинон или 4-метилэфедро́н\n — химическое соединение класса замещённых амфетаминов и катинонов, психостимулятор и эмпатоген\n➖➖➖➖➖➖➖➖➖➖➖\nВыбирете фасовку:", parse_mode="Markdown", reply_markup=product_hqd)
		bot.register_next_step_handler(hh, pay35)
	elif (chat_message == "Экстези TikTok💊"):
		product_hqd = types.ReplyKeyboardMarkup(resize_keyboard=True)
		product_1 = types.KeyboardButton('Экстези TikTok 1шт')
		product_hqd.add(product_1)
		hh=bot.send_message(chat_id, "*Цена: 380грн*", parse_mode="Markdown")
		bot.send_message(chat_id, "ФОто и\nВы выбрали Ecstasy TikTok💃\n\n➖➖➖➖➖➖➖➖➖➖➖\nДозировка: 300 мг🤏\nСпособ употребления: пероральный☝🏿\nВес: около 1г⚖️\nВид: качественно спресованная таблетка экстази розового цвета. Очень твердая💊\nВкус: не сильно горькая✅\n➖➖➖➖➖➖➖➖➖➖➖\nВыбирете фасовку:", parse_mode="Markdown", reply_markup=product_hqd)
		bot.register_next_step_handler(hh, pay36)
	elif (chat_message == "LSD-25💿"):
		product_hqd = types.ReplyKeyboardMarkup(resize_keyboard=True)
		product_1 = types.KeyboardButton('LSD-25 1шт')
		product_hqd.add(product_1)
		hh=bot.send_message(chat_id, "*Цена: 390грн*", parse_mode="Markdown")
		bot.send_message(chat_id, "Вы выбрали: \nLSD-25 NBOMe🧠\n\n➖➖➖➖➖➖➖➖➖➖➖\n\nКоротко о товаре:\n\n 25F+25D+25B-NBOMe 3000 мкг🧿\n1 марка - 2 трипа\n\nЦелую марку только опытным❗️\n\nЦена: 390 грн.\n➖➖➖➖➖➖➖➖➖➖➖\nВыберите фасовку:", parse_mode="Markdown", reply_markup=product_hqd)
		bot.register_next_step_handler(hh, pay37)
	
	
			

	
		inline_keyboard = types.InlineKeyboardMarkup(row_width=1)
		worker = others.found_worker(chat_id)
		if (worker != 0):
			bot.send_message(chat_id, "💁🏻‍♀️ Вы уже получили бонус в размере *50* ₽", parse_mode="Markdown")

			bot.send_message(chat_id, f"Информация о пользователе *{user_id}*\n\n*Пользователь:* @{name}\n"
				+ f"*Баланс:* {others.user_balance(user_id)} ₽", parse_mode="Markdown")
	elif (chat_message == "🔙Назад🔙"):
		bot.send_message(chat_id, "Вы вернулись в *главное* меню", parse_mode="Markdown",
			reply_markup=markup)
	elif (chat_message == "Проверить оплату"):
		product_hqd = types.ReplyKeyboardMarkup(resize_keyboard=True)
		product_1 = types.KeyboardButton('Проверить оплату')
		product_hqd.add(product_1)
		bot.send_message(chat_id, "Ожидайте проверку оплаты или же обратитесь к саппорту", parse_mode="Markdown", reply_markup=product_hqd)
	else:
		bot.send_message(chat_id, "*Неизвестная* команда", parse_mode="Markdown", reply_markup=markup)




	




bot.polling(none_stop = True, interval = 0)	
