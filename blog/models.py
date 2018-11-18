from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')


    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:200]

    def pub_preety_date(self):
        return self.pub_date.strftime('%b %e %Y')

    def pub_preety_time(self):
        return self.pub_date.strftime('%I:%M:%S %p')
