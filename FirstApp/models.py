from django.db import models


class Profile(models.Model):
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others'),
    )

    RELIGION = (
        ('Islam', 'Islam'),
        ('Hindu', 'Hindu'),
        ('Bodho', 'Bodho'),
        ('Kristian', 'Kristian'),
    )

    image = models.ImageField(upload_to='prof_pic/', default='def.png', null=True, blank=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, null=True, blank=True)
    address = models.TextField(max_length=100)
    number = models.TextField(max_length=15)
    age = models.FloatField()
    gender = models.CharField(max_length=8, choices=GENDER, default='Male')
    religion = models.CharField(max_length=10, choices=RELIGION, default='Islam')
    division = models.CharField(max_length=10)
    post_code = models.IntegerField()

    def __str__(self):
        return str(self.name)

