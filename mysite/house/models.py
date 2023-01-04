from django.db import models

# Create your models here.

class Activities(models.Model):
    activity_text = models.CharField(max_length=200)
    #def __str__(self):
        #return self.activity_text
class Details(models.Model):
    detail_text = models.CharField(max_length=1000)
    #def __str__(self):
        #return self.detail_text
    category_text = models.CharField(max_length=300)
    #def __str__(self):
        #return self.category_text
    pub_date = models.DateTimeField('date published')
    #def was_published_recently(self):
        #return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    
