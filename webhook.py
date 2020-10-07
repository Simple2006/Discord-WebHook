from discord_webhook import DiscordWebhook
import sys

def webhook():
    while True:
        x = input("What message? ")
        webhook = DiscordWebhook(url='INSERT URL', content=x)
        response = webhook.execute()
webhook()