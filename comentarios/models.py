from django.contrib.auth.models import User
from django.db import models

class Comentario(models.Model):
    #se deletar usuario, todos comentários irá ser deletado tbm
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    comentario = models.TextField()
    #auto_now_add cadastrar automatico data atual
    data = models.DateTimeField(auto_now_add=True)
    aprovado = models.BooleanField(default=True)

    def __str__(self):
        return self.usuario.username
