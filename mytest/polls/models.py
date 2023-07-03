from django.db import models

<<<<<<< HEAD
# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
=======
# Modelo de preguntas, con texto y fecha
class Question(models.Model):
    question_text = models.CharField(max_length=200)    # Texto de la pregunta
    pub_date = models.DateTimeField("date published")   # Fecha de publicación
>>>>>>> new-things

    def __str__(self):
        return self.question_text

<<<<<<< HEAD
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
=======
# Modelo de elección, con pregunta, texto y votos
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)    # Nombre de la pregunta
    choice_text = models.CharField(max_length=200)                      # Nombre de la elección
    votes = models.IntegerField(default=0)                              # Cantidad de votos
>>>>>>> new-things

    def __str__(self):
        return self.choice_text
