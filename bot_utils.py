from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackQueryHandler, Filters
from telegram import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery, Update
import requests
import re
import logging
from advertisement_db import Advertisement, AdvertisementDB
from users_db import UserFlags, UsersDB

# Simple function that helps me get a debug message on the bots console
def basic_callback_debug(update: Update, context: CallbackQuery, command_name: str):
    print('command ' + command_name + ' received from chat with id ' +
          str(update.message.chat_id) + ' and name ' +
          str(update.message.from_user.username))

# Response for an unimplemented feature
def unimplemented_function(update):
    update.message.reply_text("This feature hasn't been implemented yet.")

# Helps build a menu with a list of buttons and a number of columns
def build_menu(buttons, n_cols, header_buttons=None, footer_buttons=None):
    menu = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]
    if header_buttons:
        menu.insert(0, [header_buttons])
    if footer_buttons:
        menu.append([footer_buttons])
    return menu