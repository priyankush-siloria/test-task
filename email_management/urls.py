from django.urls import path


from .views import * 


urlpatterns = [

	# Party-Party business
	path('sender', DefineSenderDBView.as_view(),name="sender"),
	path('create', CreateEmailDBView.as_view(),name="create"),
	path('send', SendEmailDBView.as_view(),name="send"),
]