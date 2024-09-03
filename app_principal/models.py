from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Movie(models.Model):
    title=models.CharField(max_length=200)
    description=models.CharField(max_length=5000)
    url=models.CharField(max_length=500)
    date_added=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class UserMovieList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='movie_list')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    # Adicione outros campos se necessário, por exemplo, para data de adição, notas, etc.

    class Meta:
        unique_together = ('user', 'movie')  # Garante que o mesmo filme não possa ser adicionado mais de uma vez para o mesmo usuário

    def __str__(self):
        return f'{self.user.username} - {self.movie.title}'