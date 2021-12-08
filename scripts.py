import random
from datacenter.models import Schoolkid, Chastisement,\
    Mark, Lesson, Subject, Commendation
from django.core.exceptions import ObjectDoesNotExist


def remove_chastisements(student_name):
    try:
        schoolkid = Schoolkid.objects.get(
            full_name__contains=student_name
        )
    except ObjectDoesNotExist:
        print('Student does not exist!')
    else:
        chastisements = Chastisement.objects.filter(schoolkid=schoolkid)
        chastisements.delete()
        print(f'{student_name} chastisements successfully deleted!')


def fix_marks(student_name):
    try:
        schoolkid = Schoolkid.objects.get(
            full_name__contains=student_name
        )
    except ObjectDoesNotExist:
        print('Student does not exist!')
    else:
        schoolkid_bad_marks = Mark.objects.filter(schoolkid=schoolkid, points__lt=4)
        if schoolkid_bad_marks:
            for mark in schoolkid_bad_marks:
                mark.points = random.randint(4, 5)
                mark.save()
                print(f'{student_name} marks successfully changed!')
        else:
            print(f'Bad marks do not find!')


def create_commendation(student_name, subject_title):
    commendation_text = 'Хвалю!'
    try:
        schoolkid = Schoolkid.objects.get(
            full_name__contains=student_name
        )
    except ObjectDoesNotExist:
        print('Student does not exist')
    else:
        try:
            subject = Subject.objects.get(
                title=subject_title,
                year_of_study=schoolkid.year_of_study
            )
        except ObjectDoesNotExist:
            print('Subject does not exist')
        else:
            lessons = Lesson.objects.filter(subject=subject)
            lesson = random.choice(lessons)
            teacher = lesson.teacher
            lesson_date = lesson.date

            Commendation.objects.create(
                text=commendation_text,
                created=lesson_date,
                schoolkid=schoolkid,
                subject=subject,
                teacher=teacher
            )
            print(f'{student_name} commendations successfully added!')
