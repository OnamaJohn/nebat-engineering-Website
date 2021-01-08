from django.contrib import admin

# Register your models here.
from . models import *



class HeaderAdmin(admin.ModelAdmin):
	list_display = ('market_statement','sub_statement',)
	filter_display = ('market_statement',)

class AboutAdmin(admin.ModelAdmin):
	list_display = ('core_values','description',)
	filter_display = ('core_values',)

class AboutStatementAdmin(admin.ModelAdmin):
	list_display = ('about_description',)

class AchievementAdmin(admin.ModelAdmin):
	list_display = ('satisified_clients','projects_worked_on','hours_of_support',)

class TeamAdmin(admin.ModelAdmin):
	list_display = ('name','position',)
	filter_display = ('name',)

class ServiceAdmin(admin.ModelAdmin):
	list_display = ('name','description',)
	filter_display = ('name','description',)

class ProjectAdmin(admin.ModelAdmin):
	list_display = ('name','location','description',)
	filter_display = ('name','location','description',)

class TestimonialAdmin(admin.ModelAdmin):
	list_display = ('name','intro','profession',)
	filter_display = ('name','profession',)
class PartnersAdmin(admin.ModelAdmin):
	list_display = ('partner_name',)

class FrequentlyAskedQuestionsAdmin(admin.ModelAdmin):
	list_display = ('question','answer',)
	filter_display = ('question',)

class ValuesAdmin(admin.ModelAdmin):
	list_display = ('mission','vision','values','descriptions','core_values')

class ContactAdmin(admin.ModelAdmin):
	list_display = ('email','name','subject','message',)
	filter_display = ('email','name',)	

admin.site.register(About, AboutAdmin)
admin.site.register(Achievement, AchievementAdmin)
admin.site.register(Team,TeamAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Project,ProjectAdmin)
admin.site.register(AboutStatement,AboutStatementAdmin)
admin.site.register(Testimonial,TestimonialAdmin)
admin.site.register(Partners,PartnersAdmin)
admin.site.register(FrequentlyAskedQuestions, FrequentlyAskedQuestionsAdmin)
admin.site.register(Values,ValuesAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Header,HeaderAdmin)