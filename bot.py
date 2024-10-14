import discord
from discord.ext import commands
import os

# Définir les intents nécessaires pour le bot
intents = discord.Intents.default()
intents.messages = True  # Autoriser l'accès aux messages du serveur
intents.guilds = True    # Autoriser l'accès aux informations des serveurs
intents.reactions = True  # Autoriser l'accès aux réactions
intents.message_content = True  # Autoriser l'accès au contenu des messages (nécessaire si tu veux analyser les messages)


# Récupérer le token du bot depuis les variables d'environnement
TOKEN = os.getenv('DISCORD_TOKEN')

# Créer l'instance du bot avec les intents définis
bot = commands.Bot(command_prefix="!", intents=intents)

# Événement déclenché lorsque le bot est prêt
@bot.event
async def on_ready():
    print(f'{bot.user.name} est connecté et prêt à fonctionner.')

# Lancer le bot
bot.run(TOKEN)
