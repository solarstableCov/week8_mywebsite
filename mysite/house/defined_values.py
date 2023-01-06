# importing the model
# from house app
from house.models import Activities
  
# importing datetime module
import datetime
  
# creating an instance of 
# datetime.date
d = datetime(2015, 10, 9, 23, 55, 59, 342380)
  
# creating an instance of 
# Activities
pub_date = Activities.objects.create(pub_date = d)
pub_date.save()
