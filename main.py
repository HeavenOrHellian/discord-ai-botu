import discord
from discord.ext import commands
from model import get_class

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def siniflandir(ctx):
    if ctx.message.attachments:
        #Sınıflandırma İşlemleri
        for attachment in ctx.message.attachments:
            name = attachment.filename
            url = attachment.url
            # ./ bulunduğun konum
            await attachment.save(f'./{attachment.filename}')
            await ctx.send(f'Resmi şuraya kaydettiniz. ./{attachment.filename}')

            await ctx.send('Sonucunuz yükleniyor.')
            #Sınıflandırma sonucunu göstermek
            await ctx.send (get_class(model_path ='./keras_model.h5' , labels_path = './labels.txt', image_path = f'./{attachment.filename}'))



    else:
        await ctx.send('Sınıflandırma için resim yükleyiniz...')




bot.run("")