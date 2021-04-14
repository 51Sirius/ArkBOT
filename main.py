from cfg import TOKEN
import discord
from discord.ext import commands
from discord import Webhook, RequestsWebhookAdapter, AsyncWebhookAdapter
import aiohttp


intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.members = True
client = commands.Bot(command_prefix="!", intents=intents)