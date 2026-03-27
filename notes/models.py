from django.db import models
from django.contrib.auth.models import User

# Note model database mein notes store karne ke liye
class Note(models.Model):
    title = models.CharField(max_length=200)                    # Note ka title
    content = models.TextField()                                # Note ka content
    color = models.CharField(max_length=7, default="#FFFF99")   # Background color
    created_at = models.DateTimeField(auto_now_add=True)        # Banane ka time
    updated_at = models.DateTimeField(auto_now=True)            # Last update ka time
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notes')  # Note ka owner

    def __str__(self):
        return self.title

    # Latest notes pehlay dikhane ke liye
    class Meta:
        ordering = ['-updated_at']