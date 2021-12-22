from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from mptt.models import MPTTModel, TreeForeignKey 
from mptt.fields import TreeForeignKey 
from django.contrib.auth.models import User
from django_resized import ResizedImageField




# Create your models here.
class Category(MPTTModel):
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    name = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.name

    class MPTTMeta:
        order_insertion_by = ['name']
    def __str__(self):
        full_path = [self.name]
        k = self.parent
        while k is not None:
            full_path.append(k.name)
            k = k.parent
        return ' / '.join(full_path[::-1])

class Product(models.Model):
    COLOR = (
        ('Black','Black'),
        ('Red', 'Red'),
        ('Blue','Blue'),
        ('Brown','Brown')
    )
    CATEGORY = (
        ('Electronics','Electronics'),
        ('Clothes','Clothes'),
        ('Food & Beverages','Food & Beverages'),
        ('Health & Beauty','Health & Beauty'),
        ('Sports & Leisure', 'Sports & Leisure'),
        ('Books & Entertainment', 'Books & Entertainment')
    )
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    prod_name = models.CharField(max_length=200,null=True, blank=True)
    prod_price = models.FloatField(blank=True, null=True)
    prod_discount = models.FloatField(blank=True, null=True, default=0)
    twenty_percent_discount = models.BooleanField(blank=True, null=True, default=False)
    prod_img1 = ResizedImageField(size=[520, 395],quality=100, blank=True,null=True) 
    prod_img2 = ResizedImageField(size=[520, 395],quality=100, blank=True,null=True)
    prod_img3 = ResizedImageField(size=[520, 395],quality=100, blank=True,null=True)
    prod_img4 = ResizedImageField(size=[520, 395],quality=100, blank=True,null=True)
    prod_img5 = ResizedImageField(size=[520, 395],quality=100, blank=True,null=True)
    prod_img6 = ResizedImageField(size=[520, 395],quality=100, blank=True,null=True)
    prod_img7 = ResizedImageField(size=[520, 395],quality=100, blank=True,null=True)
    prod_summary = models.TextField(blank=True,null=True)
    prod_information = RichTextField(blank=True, null=True)
    prod_cat = models.CharField(max_length=200, blank=True, null=True,choices=CATEGORY)
    category = models.ForeignKey(Category, on_delete=models.CASCADE )
    date = models.DateTimeField(auto_now_add=True, null=True)


    def __str__(self):
        return self.prod_name

    def snippet(self):
        return self.prod_summary[:20]+'...'
    
    class Meta:
        ordering = ['-date']

class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    product = models.ForeignKey(Product, default=None,on_delete=models.CASCADE)
    qnty = models.PositiveSmallIntegerField(default=1)
    unit_price = models.FloatField(blank=True, null=True) 
    price = models.FloatField(blank=True, null=True)
    discount = models.FloatField(blank=True, null=True)
    color = models.CharField(max_length=200,null=True, blank=True)
    tax = models.FloatField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.product.prod_name



    
    
