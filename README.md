# Publisher-Bot-Twitter-and-Instagram-
### Automation? Yes, please.

Este archivo template FUNCIONA y permite que una misma publicación se realice de manera simultánea tanto en tu cuenta de Instagram como de Twitter.  
Solamente se permite el envío de una imagen para Instagram y ninguna para Twitter (work in progress) acompañado por una descripción. En Instagram también se crea una Story con la imagen y enlace (si proporcionado).  
> Aspectos importantes a tener en cuenta:  
> - A la hora de proporcionar las rutas a los archivos, considerar el sistema operativo utilizado. Un ejemplo de válido ruta en Linux es "/tmp/dump.json" y la misma dirección en Windows es "\\\\tmp\\\\dump.json".
> - Si no queremos introducir ningún enlace, simplemente omitirmos dicha línea y eliminarmos las sucesivas apariciones.
> - Las líneas "cl.load_settings" y "get_timeline_feed()" siempre se ejecucarán excepto en la primera ejecución puesto que necesitan de "cl.dump_settings".
> - Para realizar las primeras comprobaciones, comentar las líneas de publicaciones (así nos evitamos tener que eliminarlas manualmente). Especialmente útil cuando estamos testeando el login.
> - Las claves de Twitter Developer deben ser de Read and Write.
### Instrucciones de uso.

#### Python instalation
- Acude [aqui](https://www.python.org/downloads/) para escoger tu version. Una vez instalado, introducir por consola los siguientes comandos.

#### Instagram API instalation
```python
pip install instagrapi
```
#### Twitter API instalation
```python
pip install tweepy
```
#### Aditional requirements
```python
pip install pillow
```
Finalmente, rellenar los datos necesarios en el codigo siguiendo los comentarios descriptivos.  
