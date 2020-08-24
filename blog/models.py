from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.


class Post(models.Model):
    """
    Model that represents post data
    """

    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(
        User, related_name='posts', on_delete=models.CASCADE)
    slug = models.SlugField(max_length=255)

    def get_absolute_url(self):
        return reverse('blog:detail', args=[self.pk, self.slug])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.title}'
