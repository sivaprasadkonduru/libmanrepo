from django.db import models
# Create your models here.
BOOK_CATEGORY = (('Electronics', 'ECE'),
                 ('Computers', 'CSE'),
                 ('Civil', 'CIVIL'),
                 ('Human Resources', 'HR'),
                 ('Finance', 'FIN'),
                 ('Marketing', 'MKT')
                )

AVAILABLE = (('Yes', 'Y'),
             ('No', 'N')
             )


class Book(models.Model):

    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    edition = models.IntegerField()
    category = models.CharField(max_length=20, choices=BOOK_CATEGORY)
    publisher = models.CharField(max_length=50)
    reviews = models.FloatField()
    available = models.CharField(max_length=5, choices=AVAILABLE)
    issued_date = models.DateTimeField(auto_now=True)
    return_date = models.DateTimeField()

    def __str__(self):
        return '{} -  {}'.format(self.name, self.edition)





