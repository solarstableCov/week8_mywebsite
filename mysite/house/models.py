from django.db import models
# Create your models here.
class Activities(models.Model):
    activity_text = models.CharField(max_length=200,null=True)
    detail_text = models.TextField(max_length=1000,null=True)
    category_text = models.CharField(max_length=300,null=True)
    pub_date = models.DateTimeField('date published',null=True)
    #activity_text = "reading"
    def __str__(self):
        return self.activity_text
#class Details(models.Model):
    #detail_text = "You can pick up a book from your bookshelf or look up an ebook online" 
    def __str__(self):
        return self.detail_text
    
    #category_text = "leisure, alone, relaxing"
    def __str__(self):
        return self.category_text
    
    #pub_date = 05012023
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    class Meta:
        verbose_name = "The Activity"
        verbose_name_plural = "Activity"
