import os
import json
import discord
from discord.ext import commands

# Récupérer le token du bot depuis les variables d'environnement
TOKEN = os.getenv('DISCORD_TOKEN')

# Si la variable d'environnement n'est pas définie, récupérer depuis un fichier de configuration secret
if TOKEN is None:
    try:
        with open('secrets.json') as f:
            secrets = json.load(f)
            TOKEN = secrets.get('DISCORD_TOKEN')
            if TOKEN is None:
                raise ValueError("Le token Discord n'est pas défini dans secrets.json.")
    except FileNotFoundError:
        raise FileNotFoundError("Le fichier secrets.json est introuvable. Assurez-vous de l'avoir créé.")

# Vérifier que le token est bien récupéré
if TOKEN is None:
    raise ValueError("Le token Discord n'a pas été trouvé. Assurez-vous que la variable d'environnement DISCORD_TOKEN est définie ou que le fichier secrets.json est correct.")

# Définir les intents nécessaires pour le bot
intents = discord.Intents.default()
intents.messages = True  # Autoriser l'accès aux messages du serveur
intents.guilds = True    # Autoriser l'accès aux informations des serveurs
intents.reactions = True  # Autoriser l'accès aux réactions
intents.message_content = True  # Autoriser l'accès au contenu des messages (nécessaire si tu veux analyser les messages)

# Créer l'instance du bot avec les intents définis
bot = commands.Bot(command_prefix="!", intents=intents)

# Événement déclenché lorsque le bot est prêt
@bot.event
async def on_ready():
    print(f'{bot.user.name} est connecté et prêt à fonctionner.')

# Lancer le bot
bot.run(TOKEN)
