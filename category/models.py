from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=200)
    slug =  models.SlugField(max_length=100, unique=True) #unique=True means that it is unique
    description =  models.CharField(max_length=255, blank=True)
    cat_image = models.ImageField(upload_to='photos/categories', blank=True) # blank=True means that it is optional

    class Meta: # if the plural name in django admin page is wron like this u change it
        verbose_name = 'category'
        verbose_name_plural = 'categories'



    # 'products_by_category' is the name of category store items url (urls.py in store) so this function returns the slug 
            # in tepmlates 
    def get_url(self):
        return reverse('products_by_category', args=[self.slug])


    def __str__(self):
        return self.category_name