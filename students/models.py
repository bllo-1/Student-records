from django.db import models
# from ckeditor.fields import RichTexField
# Create your models here.
class student(models.Model):
    classes = [
        ('5th','class 5th'),
        ('6th','class 6th'),
        ('7th','class 7th'),
        ('8th','class 8th'),
        ('9th','class 9th'),
        ('10th','class 10th'),
    ]


    name = models.CharField(max_length=500, verbose_name='Student Name')
    fname = models.CharField(max_length=500, verbose_name='Father Name')
    dob = models.DateField(auto_now_add=False, verbose_name='Date of Birth')
    address = models.CharField(max_length=500)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pin = models.CharField(max_length=500)
    phone = models.IntegerField()
    email = models.EmailField(max_length=254)
    classes = models.CharField(max_length=50, choices=classes)
    marks = models.IntegerField(verbose_name='Percentage')
    enrolled = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name