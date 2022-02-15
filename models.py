from django.db import models

# Create your models here.
class School(models.Model):
    GENDER_CHOICES = [
        ("F", "F"),
        ("M", "M")
    ]
    SECTION_CHOICES = [
        ("A", "A"),
        ("B", "B")
    ]

    gender = models.CharField(max_length = 1, choices = GENDER_CHOICES)
    _class = models.IntegerField()
    section = models.CharField(max_length = 1, choices = SECTION_CHOICES)
    height = models.FloatField()
    weight = models.FloatField()
    school = models.IntegerField()
    _timestamp = models.DateTimeField()
    year = models.IntegerField()
    month = models.IntegerField()
    week = models.IntegerField()
    day = models.IntegerField()
    hour = models.IntegerField()

    def __str__(self) -> str:
        return str(self.id)


# df = pd.read_excel("studentData.xlsx")
#for i in df.iloc():
#    ...:     sch = School.objects.create(gender = i['gender'], _class = i['_class'], section = i["section"], height = i['height'], weight = i['weight'], school = i['school'], _timestamp = i['_timestamp'], year = i['year'], month = i['mon
#    ...: th'], week = i['week'],day =  i['day'],hour =  i['hour'])
#    ...:     sch.save()