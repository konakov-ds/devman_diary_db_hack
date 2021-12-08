import random
from datacenter.models import Schoolkid, Chastisement,\
    Mark, Lesson, Subject, Commendation
from django.shortcuts import get_object_or_404


def remove_chastisements(student_name):
    schoolkid = get_object_or_404(
        Schoolkid,
        full_name__contains=student_name
    )
    if schoolkid:
        chastisements = Chastisement.objects.filter(schoolkid=schoolkid)
        chastisements.delete()
        print(f'{student_name} chastisements successfully deleted!')
    else:
        print('Student does not exist!')


def fix_marks(student_name):
    schoolkid = get_object_or_404(
        Schoolkid,
        full_name__contains=student_name
    )
    if not schoolkid:
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
    schoolkid = get_object_or_404(
        Schoolkid,
        full_name__contains=student_name
    )
    if not schoolkid:
        print('Student does not exist!')
    else:
        subject = get_object_or_404(
            Subject,
            title=subject_title,
            year_of_study=schoolkid.year_of_study
        )
        if not subject:
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
            print(f'{student_name} commendation successfully added!')
