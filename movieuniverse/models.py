from django.db import models

AGE_OPTIONS = [
    ('7+', '7+'),
    ('13+', '13+'),
    ('16+', '16+'),
    ('18+', '18+'),
    ('all', 'all')
]

class Movie(models.Model):
    title = models.CharField(max_length=200)
    year = models.CharField(max_length=4)
    age = models.CharField(max_length=4, choices=AGE_OPTIONS)
    IMDb_rating = models.FloatField()
    Rotten_Tomatoes_rating = models.CharField(max_length=3)
    netflix = models.IntegerField(help_text='1 for available, 0 for not available')
    hulu = models.IntegerField(help_text='1 for available, 0 for not available')
    prime = models.IntegerField(help_text='1 for available, 0 for not available')
    disney = models.IntegerField(help_text='1 for available, 0 for not available')
    directors = models.CharField(max_length=50, help_text='Separate each director with commas')
    genres = models.CharField(max_length=50, help_text='Separate each genre with commas')
    country = models.CharField(max_length=50, help_text='Separate each country with commas')
    language = models.CharField(max_length=50, help_text='Separate each language with commas')
    runtime = models.IntegerField(name='runtime')

    def __str__(self) -> str:
        return self.title



