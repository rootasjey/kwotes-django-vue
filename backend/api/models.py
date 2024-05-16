from django.db import models

# Create your models here.
class Quote(models.Model):
  id = models.CharField(max_length=100, primary_key=True)
  author = models.ForeignKey('SimpleAuthor', on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)
  language = models.CharField(max_length=100)
  name = models.TextField(max_length=1000)
  reference = models.ForeignKey('SimpleReference', on_delete=models.CASCADE)
  updated_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.name

class SimpleAuthor(models.Model):
  id = models.CharField(max_length=100, primary_key=True)
  name = models.CharField(max_length=100)

  def __str__(self):
    return self.name

class SimpleReference(models.Model):
  id = models.CharField(max_length=100, primary_key=True)
  name = models.CharField(max_length=100)

  def __str__(self):
    return self.name
