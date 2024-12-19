import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.messages = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot connesso come {bot.user}')

@bot.command()
async def info(ctx):
    tips = [
        "Riduci l'uso della plastica.",
        "Usa i mezzi pubblici o vai in bicicletta.",
        "Risparmia energia spegnendo dispositivi non necessari.",
        "Ricicla i rifiuti correttamente."
    ]
    message = "L'inquinamento è un problema globale. Ecco alcune cose che puoi fare:\n\n" + "\n".join(f"- {tip}" for tip in tips)
    await ctx.send(message)

@bot.command()
async def saluto(ctx):
    await ctx.send("Ciao! Sono un bot che aiuta a sensibilizzare sull'inquinamento.")

# Inserisci il token del tuo bot Discord
bot.run('YOUR_DISCORD_BOT_TOKEN')
