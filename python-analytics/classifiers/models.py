from django.db import models

# schema for the database backing our django project

class Movie(models.Model):
    title = models.CharField(max_length=250)

    def __str__(self) -> str:
        return f'{self.title}'
    
class Sentiment(models.Model):
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )

    COUNTRY_CHOICES = (
		('Kenya', 'Kenya'),
		('Uganda', 'Uganda'),
		('Tanzania', 'Tanzania'),
		('Rwanda ', 'Rwanda'),
		('Congo', 'Congo'),
		('Somalia', 'Somalia'),
        ('South Africa', 'South Africa'),
        ('Nigeria', 'Nigeria')
	)

    movie = models.ForeignKey(Movie,on_delete=models.CASCADE)
    reviews = models.TextField()
    results = models.IntegerField()
    gender = models.CharField(max_length=6,choices=GENDER_CHOICES)
    age = models.IntegerField()
    country = models.CharField(max_length=24,choices=COUNTRY_CHOICES)
    timestamp = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.movie}'

    class Meta:
        ordering = ['-timestamp', '-updated']