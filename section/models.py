from django.db import models



class Category(models.Model):
    title = models.CharField(max_length=223)
    rating = models.DecimalField(max_digits=3, decimal_places=1, default=0.0)

    def __str__(self):
        return self.title


class Car(models.Model):
    title = models.CharField(max_length=123)
    model = models.CharField(max_length=123)
    category = models.ForeignKey(Category, on_delete=models.PROTECT,null=True)
    year = models.PositiveSmallIntegerField()
    image = models.ImageField(upload_to='media/car_images')
    price = models.DecimalField(decimal_places=2,max_digits=12)

    def __str__(self):
        return self.title
