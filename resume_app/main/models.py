from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=1000)
    author_name = models.CharField(max_length=100)
    description = models.TextField()
    excerpt = models.TextField(max_length=300)
    num_lessons = models.PositiveIntegerField(default=0)
    picture = models.ImageField(upload_to="course_pictures")

    def __str__(self):
        return self.name