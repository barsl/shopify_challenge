# models.py
from django.db import models
class Hero(models.Model):
    name = models.CharField(max_length=60)
    alias = models.CharField(max_length=60)
    def __str__(self):
        return self.name


class User(models.Model):
    name = models.CharField(max_length=60)
    email = models.CharField(max_length=60)
    balance = models.FloatField(default = 0, null = True ,blank = True)
    date_created = models.DateTimeField(null = True, auto_now_add=True)

    def __str__(self):
        return self.name


class Image(models.Model):
    owner = models.ForeignKey(User, on_delete = models.CASCADE, null = True)
    title = models.CharField(max_length=60)
    price = models.FloatField(default = 0, null = True ,blank = True)
    discount = models.FloatField(default = 0, null = True ,blank = True)
    image = models.ImageField(upload_to='images/' , null = True, blank = True)   
    date_created = models.DateTimeField(null = True, auto_now_add=True)     

    def __str__(self):
        return self.title                

    def html_for_img_gallery(self):
        result = f"""

            <div class="col-xl-3 col-lg-4 col-md-6 col-sm-6 col-12 mb-5">
                <figure class="effect-ming tm-video-item">
                    <img src="/frontend/img/{self.title}.jpg" alt="Image" class="img-fluid">
                    <figcaption class="d-flex align-items-center justify-content-center"> 
                        <h2>{self.title}</h2>
                        <a href="photo-detail.html">View more</a>
                    </figcaption>                    
                </figure>
                <div class="d-flex justify-content-between tm-text-gray">
                    <span class="tm-text-gray-light">{self.owner}</span>
                    <span>${self.price}</span>
                </div>
            </div> 

            """
        return result       


class Tag(models.Model):
    title = models.CharField(max_length=60)
    price = models.FloatField(default = 0, null = True ,blank = True)
    discount = models.FloatField(default = 0, null = True ,blank = True)
    image = models.ImageField(upload_to='images/' , null = True, blank = True)    
    date_created = models.DateTimeField(null = True, auto_now_add=True)    

    def __str__(self):
        return self.title 

class ImageHasTag(models.Model):
    image = models.ForeignKey(Image, on_delete = models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete = models.CASCADE)
    date_created = models.DateTimeField(null = True, auto_now_add=True)
    

    def __str__(self):
        return self.image.title + ': ' + self.tag.title