from django.db import models

# Create your models here.
class Test(models.Model):
    name=models.CharField(max_length=100)
    test_no=models.IntegerField()
    def __str__(self):
            return self.name


class Question(models.Model):
    subject_choice1 = (
    ('maths', 'maths'),
    ('physics', 'physics'),
    ('chemistry', 'chemistry'),)

    options_choice = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),('4','4'))
    question_text=models.TextField()
    question_text_image=models.ImageField(default="")
    option1=models.TextField()
    option1_image=models.ImageField(default="")

    option2=models.TextField()
    option2_image=models.ImageField(default="")

    option3=models.TextField()
    option3_image=models.ImageField(default="")

    option4=models.TextField()
    option4_image=models.ImageField(default="")

    answer=models.CharField(max_length=90,
                  choices=options_choice)

    subject=models.CharField(max_length=90,choices=subject_choice1)
    chapter=models.CharField(max_length=90,default="")
    subtopic=models.CharField(max_length=90,default="")
    exam= models.ForeignKey(Test, on_delete=models.CASCADE)
