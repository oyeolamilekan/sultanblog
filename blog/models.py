from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.urlresolvers import reverse
from .utils import mentee_sender
from django.db.models.signals import pre_save

# Create your models here.
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')

class Profile(models.Model):
	OWNER_STATUS = (
	    ('owner', 'Owner'),
	    ('staff', 'Staff'),
	)
	owner = models.OneToOneField(User)
	background_pic = models.ImageField(upload_to="me/",null=True,blank=True)
	profile_pic = models.ImageField(upload_to='me/',null=True,blank=True)
	owner_status = models.CharField(max_length=300,choices=OWNER_STATUS,default='staff')

	def __str__(self):
		return str(self.owner)

class Post(models.Model):
	STATUS_CHOICES = (
	    ('draft', 'Draft'),
	    ('published', 'Published'),
	)
	title = models.CharField(max_length=250)
	slug = models.SlugField(max_length=250, unique_for_date='publish')
	author = models.ForeignKey(User, related_name='blog_posts')
	body = models.TextField()
	header_pic = models.ImageField(upload_to="",blank=True,null=True)
	heade_pic_descr = models.CharField(max_length=200,blank=True,null=True)
	topic_pic = models.ImageField(upload_to="users/%Y/%m/%d",blank=True,null=True)
	topic_pic_descr = models.CharField(max_length=200,blank=True,null=True)
	topic_pic_2 = models.ImageField(upload_to="users/%Y/%m/%d",blank=True,null=True)
	topic_pic_2_descr = models.CharField(max_length=200,blank=True,null=True)
	topic_pic_3 = models.ImageField(upload_to="users/%Y/%m/%d",blank=True,null=True)
	topic_pic_3_descr = models.CharField(max_length=200,blank=True,null=True,)
	topic_pic_4 = models.ImageField(upload_to="users/%Y/%m/%d",blank=True,null=True)
	topic_pic_4_descr = models.CharField(max_length=200,blank=True,null=True)
	publish = models.DateTimeField(default=timezone.now)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='published')
	page_views = models.IntegerField(default=0)
	objects = models.Manager() # The default manager.
	published = PublishedManager() # The Dahl-specific manager.

    #tags = TaggableManager()

	class Meta:
	    ordering = ('-publish',)

	def __str__(self):
	    return self.title

	def get_absolute_url(self):
	    return reverse('blog:post_detail', args=[self.publish.year,
	                                             self.publish.strftime('%m'),
	                                             self.publish.strftime('%d'),
	                                             self.slug])

class Mentee(models.Model):
	name = models.CharField(max_length=200)
	phone_number = models.IntegerField()
	email_field = models.EmailField()
	createdate = models.DateTimeField(auto_now_add=True,blank=True,null=True)

	def __str__(self):
		return self.name

class Ads(models.Model):
	url = models.CharField(max_length=200)
	banner = models.ImageField('ads/',blank=True,null=True)

	def __str__(self):
		return self.url

def pre_save_post_receiver(sender, instance, *args, **kwargs):
    mentee_sender(instance,Mentee.objects.all())



pre_save.connect(pre_save_post_receiver, sender=Post)

