import requests # parte del webscrapping
from bs4 import BeautifulSoup # hace el web scraping
import os # para guardar el resutlado en el disco

# URL de la búsqueda de imágenes
# url = 'https://unsplash.com/s/photos/ciberseguridad'
url = 'https://en.wikipedia.org/wiki/PC1512'

# Realizar una solicitud GET a la URL y obtener el contenido HTML de la página
response = requests.get(url)
html = response.content
# print(html)
# exit()

# Analizar el HTML utilizando BeautifulSoup
soup = BeautifulSoup(html, 'html.parser') # se parsea el codigo para poder hacer mejor las busquedas

# Encontrar todas las etiquetas 'img' en el HTML
p_tags = soup.find_all('p') 
print(p_tags)
exit()

# Crear un directorio para guardar las imágenes descargadas
# if not os.path.exists('parrafos_amstrad'):
#    os.makedirs('parrafos_amstrad')

# Iterar sobre todas las etiquetas 'img' encontradas y descargar las imágenes
# for img_tag in img_tags:
#    img_url = img_tag['src']
    if 'images.unsplash.com/photo' in img_url:
        response = requests.get(img_url)
        filename = img_url.split('/')[-1]
        with open(os.path.join('parrafos_amstrad', filename), 'wb') as f:
            f.write(response.content)
            print(f"Imagen descargada: {filename}")

