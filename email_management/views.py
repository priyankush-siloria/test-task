from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework.renderers import TemplateHTMLRenderer

from .serializers import *

from django.conf import settings 
from django.core.mail import send_mail 

class DefineSenderDBView(APIView):
	def get(self,request):
		
		context={}
		try:
			db_obj = SenderEmail.objects.all()
			serializer = SenderEmailSerializer(db_obj, many=True)
			if serializer.data:
				context['status'] = True
				context['data'] = serializer.data
			else:
				context['status'] = True
				context['data'] = []
				context['message'] = 'No data found.'
				return Response(context)
		except Exception as e :
			context['status'] = False
			context['message'] = 'Something went wrong.'+str(e)
		return Response(context)

	def post(self,request):
		context={}
		try:
			serializer_obj = SenderEmailSerializer(data = request.data)
			if serializer_obj.is_valid():
				SenderEmail.objects.all().delete()
				serializer_obj.save()
				context['status'] = True
				context['message'] = 'Data is saved.'
				context['data'] = serializer_obj.data
			else:
				context['status'] = False
				context['message'] = 'Data is not saved.'
				context['error'] = serializer_obj.errors
		except Exception as e:
			context['status'] = False
			context['message'] = 'Something went wrong '+str(e)		
		return Response(context)

class CreateEmailDBView(APIView):
	def get(self,request):
		
		context={}
		try:
			id = request.GET.get('id')
			if id :
				try:
					db_obj = SendEmail.objects.get(id=id)
					serializer = SendEmailSerializer(db_obj)
				except Exception as e:
					context['status'] = False
					context['data'] = []
					context['message'] = 'No data found.'
					return Response(context)
			else:
				db_obj = SendEmail.objects.all()
				serializer = SendEmailSerializer(db_obj, many=True)
			if serializer.data:
				context['status'] = True
				context['data'] = serializer.data
			else:
				context['status'] = False
				context['data'] = []
				context['message'] = 'No data found.'
				return Response(context)
		except Exception as e :
			context['status'] = False
			context['message'] = 'Something went wrong.'+str(e)
		return Response(context)

	def post(self,request):
		context={}
		try:
			serializer_obj = SendEmailSerializer(data = request.data)
			if serializer_obj.is_valid():
				serializer_obj.save()
				context['status'] = True
				context['message'] = 'Email is saved.'
				context['data'] = serializer_obj.data
			else:
				context['status'] = False
				context['message'] = 'Data is not saved.'
				context['error'] = serializer_obj.errors
		except Exception as e:
			context['status'] = False
			context['message'] = 'Something went wrong '+str(e)		
		return Response(context)

class SendEmailDBView(APIView):
	def post(self,request):
		context={}
		try:
			try:
				obj = SendEmail.objects.get(id=request.data.get('id'), status='Pending')
				receiver = obj.users.split(',')

				# function to send email need to write functioan
				sender_obj = SenderEmail.objects.last()
				if not sender_obj:
					context['status'] = False
					context['message'] = 'Sender is not defined'
					return Response(context)
				else:
					if settings.EMAIL_HOST_USER !=sender_obj.sender:
						context['status'] = False
						context['message'] = 'Sender details not matched with SMTP credentials.'
						return Response(context)	

				subject = obj.subject
				message = obj.message
				email_from = settings.EMAIL_HOST_USER 
				recipient_list = obj.users.split(',')

				try:
					send_mail( subject, message, email_from, recipient_list ) 
				except Exception as e:
					context['status'] = False
					context['message'] = 'Unable to send email. '+str(e)	
					return Response(context)					
				


				obj.status='Complete'
				obj.save()

				context['status'] = True
				context['message'] = 'Email is Sent.'
			except Exception as e:
				context['status'] = False
				context['message'] = 'Data not found with passed ID and pending status.'
		except Exception as e:
			context['status'] = False
			context['message'] = 'Something went wrong '+str(e)		
		return Response(context)

