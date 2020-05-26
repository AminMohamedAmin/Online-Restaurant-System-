from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta: #used when we send table to admin
        ordering = ('name',)
        verbose_name = "Category"  # the singular form of the object of the database table #تظهر كأسم للفورم بعد ما ادخل للجدول
        verbose_name_plural = "Categorys" #the plural form of the database table # تظهر كاسم للجدول

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    components = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',) # - تعني ترتيب عكسي
        index_together = (('id', 'slug'),) # when we use query #هيستخدم الاتنين مع بعض عشان يرجع المنتج
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return self.name


class Table(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.IntegerField(default=0)
    many = models.IntegerField(default=1)
    date = models.DateField()
    time = models.TimeField()
    message = models.TextField()
    attendance = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, db_index=True, null=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',) # - تعني ترتيب عكسي
        verbose_name = "Reservation"
        verbose_name_plural = "Reservations"


class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    date = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ('-created',) # - تعني ترتيب عكسي
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"


class Careers(models.Model):
    """Model containing file field"""
    name = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.IntegerField(default=0)
    role = models.CharField(max_length=150)
    work = models.CharField(max_length=150)
    experience = models.CharField(max_length=150)
    cv = models.FileField(upload_to="media")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    date = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ('-created',) # - تعني ترتيب عكسي
        verbose_name = "Career"
        verbose_name_plural = "Careers"