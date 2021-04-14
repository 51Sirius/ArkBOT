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


@client.event
async def on_member_join(member):
    print(f'{member} has joined to server')
    async with aiohttp.ClientSession() as session:
        webhook = Webhook.from_url(cfg.WEBHOOK_URL, adapter=AsyncWebhookAdapter(session))
        image = member.avatar
        await webhook.send(f'Hello {member} and welcome to our server', username='Welcome')