# bot.py
import os
import random
import discord
from discord.ext import commands
from dotenv import load_dotenv

import matplotlib.pyplot as plt
import random
from PIL import Image, ImageDraw, ImageFont
import textwrap
import matplotlib.pyplot as plt
import json
import io

def text_in_image(path_img, text, path_font, width=40):
    image = Image.open(path_img)
    draw = ImageDraw.Draw(image)

    para = textwrap.wrap(text, width=width)
    n_lines = len(para)

    MAX_W, MAX_H = image.size
    font = ImageFont.truetype(path_font, 40)
    # f_h = font.getsize("Aa")[1]
    
    l_h = sum([font.getsize(line)[1] for line in para])
    pad=10
    text_h = (l_h+pad*(n_lines-1))
    
    current_h = (MAX_H - text_h)/2 #Debo revisar en el caso de jt el tamaño puede variar
    
    for line in para:
        w, h = draw.textsize(line, font=font)
        draw.text(((MAX_W - w) / 2, current_h), line, font=font)
        current_h += h + pad

    return image


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')


@bot.command(name='reto', help='Te entrega un reto de Tomanji')
async def reto_imagen(ctx):
    
    with open('retos.json') as f:
        data = json.load(f)
    text = random.choice(data["retos"])
    path_img = "test2.jpg"
    path_font = "Roboto/Roboto-BoldItalic.ttf"
    my_img = text_in_image(path_img, text, path_font, 38)
    
    #Using the response given in https://www.reddit.com/r/learnpython/comments/esmhxu/how_can_i_upload_a_pil_image_object_to_a_discord/
    with io.BytesIO() as image_binary:
        my_img.save(image_binary, 'PNG')
        image_binary.seek(0)
        await ctx.send(file=discord.File(fp=image_binary, filename='image.png'))


bot.run(TOKEN)