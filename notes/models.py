from django.db import models

# Create your models here.


class Tag(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self) -> str:
        return f"{self.title}"


class Note(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    tag = models.ForeignKey(Tag, null=True, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.id}. {self.title}"
