# Shopify Challenge

Requirements:

Python3, pip Installer

To use this app. please:

1. clone the repository
2. open a terminal and run commands in the root directory of the project:


        $ pip install -r requirements.txt
  
  
        $ python manage.py runserver
  
3. Open a browser and visit: 

http://127.0.0.1:8000/index/
 

The app is initialized with 3 users:

User1: initialized with 3 images in their inventory: Dog, Cat and Mouse
User2: initialized with 1 image in their inventory: Car
User3: initialized with 1 image in their inventory: Flower

The user of the application starts the application as User1 and views their inventory as the home screen.

From there, the user can use the text field to search for images by keywords.

The user can also upload an image to search for similar images (powered by Google Vision API)
