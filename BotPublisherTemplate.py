#Instagram api
from instagrapi import Client
from instagrapi.types import StoryLink
from pathlib import Path
from PIL import Image
# Twitter api
import tweepy


# Detalles de la publicacion comun
IMAGE = "AQUI TU IMAGEN"    # Solo para Instagram
ENLACE = "AQUI TU ENLACE"   # Opcional (quitar de abajo)
DESCRIPCION = "AQUI TU TEXTO"

# Informacion de la cuenta de Instagram
ACCOUNT = "AQUI TU @"   
PSWD = "AQUI TU CONTRASENIA"   

# ----------------------------------- #
# --------- Instagram Stuff --------- #
# ----------------------------------- #

image = Image.open(IMAGE)
image = image.convert("RGB")
# Es necesario reajustar la imagen
new_image = image.resize((1080, 1080))
new_image.save("imagen_reajustada.jpg")
phot_path = "imagen_reajustada.jpg"
phot_path = Path(phot_path)

cl = Client()
# Los settings permiten evitar el reiterado envio al email del codigo de confirmacion
cl.load_settings('/tmp/dump.json') # Descomentado EXCEPTO en la primera ejecucion
cl.login(ACCOUNT, PSWD)
cl.get_timeline_feed()  # Descomentado EXCEPTO en la primera ejecucion
#cl.dump_settings('/tmp/dump.json') # Descomentado SOLO en la primera ejecucion

print("Comenzando a publicar en Instagram...")

cl.photo_upload(phot_path, DESCRIPCION)
cl.photo_upload_to_story(phot_path, links=[StoryLink(webUri=ENLACE)])
# Consulta el objeto cl para mas acciones...

print("¡Publicacion en Instagram completada!")

# ----------------------------------- #
# ---------- Twitter Stuff ---------- #
# ----------------------------------- #

# Necesita registro en https://developer.twitter.com/en
# Recuerda que las claves deben ser de Read and Write
consumerKey = ""
consumerSecret = ""
accessToken = ""
accessTokenSecret = ""
BearerToken = ""

# Autenticacion en Twitter
client = tweepy.Client(
    bearer_token=BearerToken,
    consumer_key=consumerKey, 
    consumer_secret=consumerSecret,
    access_token=accessToken,
    access_token_secret=accessTokenSecret
)

print("Comenzando a publicar en Twitter...")

client.create_tweet(text=DESCRIPCION)
# Consulta el objeto client para mas acciones...

print("¡Publicacion en Twitter completada!")