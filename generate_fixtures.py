import os
import json
import requests
from faker import Faker
from PIL import Image


fake = Faker()

# Nombre de produits et categories
num_categories = 5
num_products_per_category = 10
images_directory = 'media/products'

# Crée le répertoire des images s'il n'existe pas
os.makedirs(images_directory, exist_ok=True)

# créations des fixtures catégories et produits
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
        # Va chercher les images aléatoires sur picsum
        image_url = "https://picsum.photos/350/300"
        response = requests.get(image_url)

        # Enregistre temporairement l'image téléchargée
        temp_image_path = os.path.join(images_directory, 'temp_image')

        with open(temp_image_path, 'wb') as f:
            f.write(response.content)

        # Redimenssionne l'image avec pillow et la converti en jpg
        image = Image.open(temp_image_path)
        target_size = (800, 600)
        image.thumbnail(target_size)
        image = image.convert('RGB')

        # Enregistre l'image sus media/products
        image_filename = f"image{product_id}.jpg"
        image_path = os.path.join(images_directory, image_filename)
        image.save(image_path, 'JPEG', quality=90)

        # Supprime l'image temporaire
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
