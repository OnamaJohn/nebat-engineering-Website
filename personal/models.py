from django.db import models


class Header(models.Model):
	background_image = models.ImageField(upload_to='images', null=True, blank=True)
	market_statement = models.CharField(max_length=255, null=True,blank=True)
	sub_statement = models.CharField(max_length=250,null=True,blank=True)

	def __str__(self):
		return self.market_statement


class About(models.Model):
	core_values = models.CharField(max_length=225,null=True, blank=True)
	description = models.CharField(max_length=255, null=True, blank=True)

	class Meta:
		verbose_name_plural = 'About'

	def __str__(self):
		return self.core_values

class AboutStatement(models.Model):
	about_description = models.TextField()

	class Meta:
		verbose_name_plural = 'About Statement'

		def __str__(self):
			return self.about_description

class Achievement(models.Model):
	satisified_clients = models.IntegerField(null=True, blank=True)
	projects_worked_on = models.IntegerField(null=True, blank=True)
	hours_of_support = models.IntegerField(null=True, blank=True)
	number_of_employees = models.IntegerField(null=True, blank=True)

	class Meta:
		verbose_name_plural = 'Achievement'

	def __str__(self):
		return str(self.satisified_clients)


class Team(models.Model):
	name = models.CharField(max_length=255,null=True,blank=True)
	position = models.CharField(max_length=255,null=True,blank=True)
	photo = models.ImageField(upload_to='images', null=True, blank=True)
	twitter = models.CharField(max_length=300,null=True, blank=True)
	facebook = models.CharField(max_length=300,null=True, blank=True)
	linked = models.CharField(max_length=300,null=True, blank=True)

	class Meta:
		verbose_name_plural = 'Team'

	def __str__(self):
		return self.name

class Service(models.Model):
	name = models.CharField(max_length=255,null=True, blank=True)
	description = models.TextField(max_length=200,null=True, blank=True)

	class Meta:
		verbose_name_plural = 'Service'

	def __str__(self):
		return self.name

class Project(models.Model):
	name = models.CharField(max_length=200,null=True, blank=True)
	location = models.CharField(max_length=200,null=True, blank=True)
	description = models.TextField(null=True, blank=True)
	image = models.ImageField(upload_to='images', null=True, blank=True)

	class Meta:
		verbose_name_plural = 'Project'

	def __str__(self):
		return self.name


class Testimonial(models.Model):
	intro = models.TextField(null=True, blank=True)
	name = models.CharField(max_length=255,null=True, blank=True)
	profession = models.CharField(max_length=255, null=True, blank=True)
	image = models.ImageField(upload_to='images', null=True)

	class Meta:
		verbose_name_plural = 'Testimonial'

	def __str__(self):
		return self.name

class Partners(models.Model):
	partner_logo = models.ImageField(upload_to='images', null=True, blank=True)
	partner_name = models.CharField(max_length=255, null=True, blank=True)

	class Meta:
		verbose_name_plural = 'Partners'

	def __str__(self):
		return self.partner_name

class FrequentlyAskedQuestions(models.Model):
	question = models.CharField(max_length=400, null=True, blank=True)
	answer = models.TextField(null=True, blank=True)

	class Meta:
		verbose_name_plural = 'FrequentlyAskedQuestions'

	def __str__(self):
		return self.question


class Values(models.Model):
	values = models.CharField(max_length=200, null=True, blank=True)
	vision = models.CharField(max_length=300, null=True, blank=True)
	mission = models.CharField(max_length=300, null=True, blank=True)
	descriptions = models.CharField(max_length=500, null=True,blank=True)
	core_values = models.CharField(max_length=200, null=True, blank=True)


	class Meta:
		verbose_name_plural = 'Values'

	def __str__(self):
		return self.values

class Contact(models.Model):
	name = models.CharField(max_length=255, null=True, blank=True)
	email = models.EmailField(max_length=255, null=True, blank=True)
	subject = models.CharField(max_length=255, null=True, blank=True)
	message = models.TextField(max_length=300,null=True, blank=True)


	class Meta:
		verbose_name_plural = 'Contact'

	def __str__(self):
		return self.email