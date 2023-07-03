from django.db import models

# Modelo de preguntas, con texto y fecha
class Question(models.Model):
    question_text = models.CharField(max_length=200)    # Texto de la pregunta
    pub_date = models.DateTimeField("date published")   # Fecha de publicación
    
    def __str__(self):
        return self.question_text

# Modelo de elección, con pregunta, texto y votos
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)    # Nombre de la pregunta
    choice_text = models.CharField(max_length=200)                      # Nombre de la elección
    votes = models.IntegerField(default=0)                              # Cantidad de votos
    
    def __str__(self):
        return self.choice_text
