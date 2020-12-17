from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    about_me_1 = models.TextField()
    about_me_2 = models.TextField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True)
    cv = models.URLField(blank=True, null=True)

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)



class Skill(models.Model):
    name = models.CharField(max_length=30)
    person = models.ForeignKey(Person, related_name='skills', blank=True, null=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name


class Portfolio(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField()
    description = models.TextField()
    person = models.ForeignKey(Person, blank=True, null=True, related_name='portfolios', on_delete=models.CASCADE)

    def __str__(self):
        return self.title