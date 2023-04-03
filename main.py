import sqlite3

import telebot

import time

# Initialize the bot using the API token

bot = telebot.TeleBot("<API_TOKEN>")

# Connect to the SQLite database

conn = sqlite3.connect('messages.db')

c = conn.cursor()

# Create a table to store the messages

c.execute('''CREATE TABLE IF NOT EXISTS messages

             (id INTEGER PRIMARY KEY, date TEXT, time TEXT, message TEXT, link TEXT)''')

# Define a function to handle new messages in the channel

@bot.channel_post_handler(func=lambda message: True)

def handle_channel_message(message):

    # Insert the message details into the database

    c.execute("INSERT INTO messages (date, time, message, link) VALUES (?, ?, ?, ?)", 

              (message.date.strftime("%Y-%m-%d"), message.date.strftime("%H:%M:%S"), 

               message.text, f"https://t.me/{message.chat.username}/{message.message_id}"))

    conn.commit()

# Start the bot and listen for new messages

bot.polling()

# Close the database connection

conn.close()

