from django.urls import path


from personal.views import (
	home_screen_views,
	sendEmail,
)

app_name = "personal"


urlpatterns = [
    path('', home_screen_views, name='home'),
    path('send_email/',sendEmail, name="send_email"),
]