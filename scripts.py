import random
from datacenter.models import Schoolkid, Chastisement,\
    Mark, Lesson, Subject, Commendation
from django.shortcuts import get_object_or_404


def get_schoolkid(student_name):
        schoolkid = Schoolkid.objects.filter(
            full_name__contains=student_name
        )
        if not schoolkid:
            raise ValueError(f'Student {student_name} does not exist!')
        elif len(schoolkid) > 1:
            raise ValueError(f'There are more than one student with name {student_name}')
        else:
            return schoolkid[0]


def remove_chastisements(student_name):
    schoolkid = get_schoolkid(student_name)
    chastisements = Chastisement.objects.filter(schoolkid=schoolkid)
    chastisements.delete()
    print(f'{student_name} chastisements successfully deleted!')


def fix_marks(student_name):
    schoolkid = get_schoolkid(student_name)
    schoolkid_bad_marks = Mark.objects.filter(schoolkid=schoolkid, points__lt=4)
    if schoolkid_bad_marks:
        for mark in schoolkid_bad_marks:
            mark.points = random.randint(4, 5)
            mark.save()
        print(f'{student_name} marks successfully changed!')
    else:
        print(f'Bad marks do not find!')


def create_commendation(student_name, subject_title):
    commendation_texts = ['Хвалю!', 'Отличная работа!',
                          'Предложил оригинальное решение!',
                          'Инициативный и ответственный!',
                          'Подготовка на выcшем уровне!']
    schoolkid = get_schoolkid(student_name)

    subject = get_object_or_404(
        Subject,
        title=subject_title,
        year_of_study=schoolkid.year_of_study
    )

    lessons = Lesson.objects.filter(subject=subject)
    lesson = random.choice(lessons)
    teacher = lesson.teacher
    lesson_date = lesson.date
    commendation_text = random.choice(commendation_texts)

    Commendation.objects.create(
        text=commendation_text,
        created=lesson_date,
        schoolkid=schoolkid,
        subject=subject,
        teacher=teacher
    )
    print(f'{student_name} commendation successfully added!')
