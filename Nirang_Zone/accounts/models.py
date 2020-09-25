from django.db import models

class Users(models.Model):

    user_id = models.CharField(max_length=10, unique=True) # Eg. 14MSE1007
    user_name = models.CharField(max_length=100) # MS Dhoni
    user_email = models.EmailField(max_length=100) # msd@bot.com
    user_password = models.CharField(max_length=100)
    user_age = models.IntegerField() # 39
    user_ranking = models.FloatField() # 7

    def upload_photo(self, filename):

        path = 'accounts/photos/{}',format(filename)

        return path

    user_photo = models.ImageField(
        upload_to=upload_photo,
        null=True,
        blank=True
    )

    def upload_resume(self, filename):

        path = 'accounts/resume/{}', format(filename)

        return path

    user_resume = models.ImageField(
        upload_to=upload_resume,
        null=True,
        blank=True
    )

    def __str__(self):

        return f"{self.user_id} - {self.user_name}"