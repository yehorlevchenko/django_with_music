from django.db import models


class Contributor(models.Model):
    name = models.CharField(max_length=127, unique=True)


class Work(models.Model):
    iswc = models.CharField(max_length=14, unique=True)
    title = models.CharField(max_length=255, null=False)
    contributors = models.ManyToManyField(Contributor)

    @classmethod
    def create(cls, **kwargs):
        duplicate = Work.objects.filter(models.Q(iswc=kwargs['iswc']) |
                                        models.Q(title=kwargs['title'])).first()
        if duplicate:
            return duplicate

        work = cls(**kwargs)
        return work