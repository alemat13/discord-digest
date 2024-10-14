import logging
import os
import json
import discord
from discord.ext import commands, tasks
import openai
import azure.functions as func
from datetime import datetime, timedelta

TOKEN = os.getenv('DISCORD_TOKEN')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
OPENAI_ENDPOINT_URL = os.getenv('OPENAI_ENDPOINT_URL')

if TOKEN is None or OPENAI_API_KEY is None or OPENAI_ENDPOINT_URL is None:
    raise ValueError("Les informations d'authentification ne sont pas correctement définies dans les variables d'environnement.")

openai.api_key = OPENAI_API_KEY
openai.api_base = OPENAI_ENDPOINT_URL

intents = discord.Intents.default()
intents.messages = True  # Autoriser l'accès aux messages du serveur
intents.guilds = True    # Autoriser l'accès aux informations des serveurs
intents.reactions = True  # Autoriser l'accès aux réactions
intents.message_content = True  # Autoriser l'accès au contenu des messages (nécessaire si tu veux analyser les messages)

bot = commands.Bot(command_prefix="!", intents=intents)

def generate_summary(messages):
    prompt = "Rédige un résumé des messages suivants : " + "\n".join(messages)
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

@bot.event
async def on_ready():
    logging.info(f'{bot.user.name} est connecté et prêt à fonctionner.')
    publish_summary.start()

@tasks.loop(time=datetime.now().replace(hour=21, minute=0, second=0, microsecond=0))
async def publish_summary():
    summary_channel = discord.utils.get(bot.get_all_channels(), name="daily-digest")
    if summary_channel is None:
        logging.error("Le salon #daily-digest n'a pas été trouvé.")
        return

    all_messages = []
    for guild in bot.guilds:
        for channel in guild.text_channels:
            if channel.name == "bienvenue":
                continue
            try:
                yesterday = datetime.utcnow() - timedelta(days=1)
                async for message in channel.history(after=yesterday):
                    all_messages.append(f"[{message.author.display_name}] {message.content}")
            except Exception as e:
                logging.error(f"Erreur lors de la récupération des messages du salon {channel.name}: {e}")

    if all_messages:
        summary = generate_summary(all_messages)
        await summary_channel.send(f"**Résumé du jour** :\n{summary}")
    else:
        await summary_channel.send("Aucun message notable aujourd'hui.")

async def main(req: func.HttpRequest) -> func.HttpResponse:
    bot.run(TOKEN)
    return func.HttpResponse("Bot lancé", status_code=200)
