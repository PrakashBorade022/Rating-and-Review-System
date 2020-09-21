from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator
# Create your models here.
class Product(models.Model):
    productName = models.CharField(max_length=150,null=False)
    price = models.IntegerField()
    image = models.ImageField(upload_to='img/')
    isAvailable = models.BooleanField()
    seller = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    averageRating = models.FloatField(default=1.0)

    def __str__(self):
        return self.productName

class Rating(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='ratings')
    rating = models.IntegerField(
        default = 1,
        validators=[MaxValueValidator(5),MinValueValidator(1)]
    )

    def __str__(self):
        return self.product.productName
class Review(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='reviews')
    review = models.CharField(max_length=200)

    def __str__(self):
        
        return self.product.productName 
    