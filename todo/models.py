from django.db import models

class Todo(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField(blank=True)
	complete = models.BooleanField(default=False)
	exp = models.PositiveIntegerField(default=0)
	completed_at = models.DateTimeField(null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	
	# 이미지 필드 추가
	image = models.ImageField(upload_to='todo_images/', blank=True, null=True)

	def __str__(self):
		return self.name