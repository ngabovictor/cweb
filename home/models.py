from django.db import models

# Create your models here.


class carousel(models.Model):
	image = models.FileField(upload_to='media/home/carousel')
	title = models.CharField(max_length=50)
	caption = models.TextField()
	bounceright = 'bounceInRight'
	bounceleft = 'bounceInLeft'
	bounceup = 'bounceInUp'
	bouncedown= 'bounceInDown'
	animations = {
	(bounceright, 'bounceInRight'),
	(bounceleft, 'bounceInLeft'),
	(bouncedown, 'bounceInDown'),
	(bounceup, 'bounceInUp'),
	}

	animation = models.CharField(max_length=50, choices=animations, default="bounceInLeft")

	def __str__(self):
		return self.title


class services(models.Model):
	image = models.FileField(upload_to='media/home/services')
	name = models.CharField(max_length=50)
	description = models.TextField()

	def __str__(self):
		return self.name


class portfolio(models.Model):
	image = models.FileField(upload_to='media/home/portfolio')
	title = models.CharField(max_length=200)
	caption = models.TextField()
	App = 'App'
	Web = 'Web'
	Designs = 'Design'
	Others = 'Others'
	categories = {
	(App, 'App'),
	(Web, 'Web'),
	(Designs, 'Design'),
	(Others, 'Others'),
	}
	category = models.CharField(max_length=200, choices=categories, default="App")
	
	def __str__(self):
		return self.caption


class toPricing(models.Model):
	title = models.ForeignKey(services, on_delete=models.CASCADE)
	coCounter = models.IntegerField(default=0)
	def __str__(self):
		return str(self.title)


class prices(models.Model):
	title = models.CharField(max_length=50)
	image = models.FileField(upload_to='media/home/pricings')
	category = models.ForeignKey(toPricing, on_delete=models.CASCADE)
	description = models.TextField()
	price = models.IntegerField()

	def __str__(self):
		return self.title



class staff(models.Model):
	name = models.CharField(max_length=50)
	post = models.CharField(max_length=20)
	image = models.FileField(upload_to='media/home/staff')
	statement = models.TextField()

	def __str__(self):
		return self.name
		
		
		
	
		
		
