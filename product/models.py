from django.db import models

# Create your models here.

#ProductCaregory
class ProductCaregory(models.Model):
      category_name=models.CharField(null=True,blank=True,max_length=30)
      
      def __str__(self):
            return self.category_name
#Product
class Product(models.Model):
      category=models.ForeignKey(ProductCaregory,on_delete=models.CASCADE,null=True,blank=True)
      product_name=models.CharField(max_length=200)
      product_price=models.IntegerField()
      product_offer =models.IntegerField(null=True,blank=True)
      product_image = models.ImageField(upload_to='product image',null=True,blank=True)

      product_details =models.TextField()

      def __str__(self):
          return self.product_name
      