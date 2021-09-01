from django.db import models

class ContactModel(models.Model):
    email = models.EmailField(max_length=250, blank=False, null=False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)


    class Meta:
        db_table = 'contact'
        verbose_name = 'Contact'
        verbose_name_plural='Contact'

    def __str__(self):
        return self.email