from django.db import models

# Create your models here.

class SenderEmail(models.Model):
	sender                   = models.CharField(max_length=200)

	created_at               = models.DateTimeField(auto_now_add=True)
	updated_at               = models.DateTimeField(auto_now=True)



class SendEmail(models.Model):
	EMAIL_STATUS        = [
		('Pending', 'Pending'),
		('Complete', 'Complete'),
	]

	users                    = models.TextField()
	subject                  = models.CharField(max_length=200, default='Email Subject')
	message                  = models.TextField()
	status                   = models.CharField(max_length=20, choices=EMAIL_STATUS, default='Complete',)

	created_at               = models.DateTimeField(auto_now_add=True)
	updated_at               = models.DateTimeField(auto_now=True)

	class Meta:
		db_table             = 'send_email'
		ordering = ['-id']