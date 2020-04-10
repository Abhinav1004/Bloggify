from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class PublishedManager(models.Manager):
	def get_queryset(self):
		return super(PublishedManager,self).get_queryset().filter(status='published')
		

class Post(models.Model):
	STATUS_CHOICES = (
			('draft','Draft'),
			('published','Published')
		)
	title = models.CharField(max_length=250)
	slug = models.SlugField(max_length=250,unique_for_date='publish')  #short label containing only letters ,etc. for beautifl urls
	author = models.ForeignKey(User,related_name= 'blog_posts',on_delete=models.CASCADE)
	body = models.TextField()
	publish = models.DateTimeField(default = timezone.now)
	created = models.DateTimeField(auto_now_add = True)  #time for creation of object
	updated = models.DateTimeField(auto_now = True) #time for saving the object
	status = models.CharField(max_length=10,choices = STATUS_CHOICES,default = 'draft' )
	objects = models.Manager() 
	published = PublishedManager()



	def get_absolute_url(self):
		return reverse('blog:post_detail',args=[self.publish.year,
												self.publish.strftime('%m'),
												self.publish.strftime('%d'),
												self.slug])
	class Meta:  #this contains meta deta of the model
		ordering = ('-publish',) # ordering must be a tuple or a list

	def __str__(self):
		return self.title

