# DiscordBot
Este es un bot realizado en base a las instrucciones de la página web:
[https://realpython.com/how-to-make-a-discord-bot-python/]

## Instalación
Para correr los programas se necesitan las librerias de:
- Pillow (pip install pillow)
- Discord-py (pip install -U discord.py)
- Jupyter (pip install jupyter)
- Matplotlib (pip install matplotlib)
- DotEnv (pip install -U python-dotenv)

En caso de usar Anaconda se puede crear un entorno de manera mas sencilla corriendo el siguiente comando:
```
conda env create -f discord_env.yml
```
Crear un archivo llamado .env en la carpeta raíz y colocar dentro de el lo siguiente:
```
DISCORD_TOKEN = PUT_YOUR_TOKEN_HERE
DISCORD_GUILD = PUT_YOUR_GUILD_OR_GROUP_NAME_HERE
```
## Programas
### text_image.ipynb
Este programa toma un texto y lo convierte a una imagen que contiene el texto, requiere de una imagen, una fuente y el texto.

### tomanji.py
Este programa te entrega retos de tomanji extraidos de retos.json. Para utilizarlo simplemente corre:
```
python tomanji.py
```
Una vez activo en terminal coloca en el grupo de discord en el que se encuentre el bot el mensaje:
```
!reto
```
para recibir un reto
