import os
import json
import requests
from faker import Faker
from PIL import Image


fake = Faker()

# Configuration
num_categories = 5
num_products_per_category = 10
images_directory = 'media/products'

# Créez le répertoire des images s'il n'existe pas
os.makedirs(images_directory, exist_ok=True)

# Génération des données
categories = []
products = []

for category_id in range(1, num_categories + 1):
    categories.append({
        "model": "offers.category",
        "pk": category_id,
        "fields": {
            "name": fake.word()
        }
    })

    for product_id in range(1, num_products_per_category + 1):
        # Générez une URL d'image aléatoire
        image_url = "https://picsum.photos/350/300"

        # Téléchargez l'image
        response = requests.get(image_url)

        # Enregistrez temporairement l'image téléchargée
        temp_image_path = os.path.join(images_directory, 'temp_image')

        with open(temp_image_path, 'wb') as f:
            f.write(response.content)

        # Ouvrez l'image avec Pillow
        image = Image.open(temp_image_path)

        # Redimensionnez l'image (par exemple, en largeur maximale de 800 pixels)
        target_size = (800, 600)
        image.thumbnail(target_size)

        # Convertissez l'image en JPEG
        image = image.convert('RGB')

        # Enregistrez l'image traitée dans le répertoire des images
        image_filename = f"image{product_id}.jpg"
        image_path = os.path.join(images_directory, image_filename)
        image.save(image_path, 'JPEG', quality=90)

        # Supprimez l'image temporaire
        os.remove(temp_image_path)

        products.append({
            "model": "offers.product",
            "pk": (category_id - 1) * num_products_per_category + product_id,
            "fields": {
                "name": ' '.join(fake.words(nb=3)).title(),
                "description": fake.text(),
                "price": round(fake.random.uniform(1, 100), 2),
                "category": category_id,
                "image": os.path.join("products", image_filename)
            }
        })

# Écriture des fixtures dans un fichier JSON
with open('offers/fixtures/offers_data.json', 'w') as f:
    json.dump(categories + products, f, ensure_ascii=False, indent=2)
