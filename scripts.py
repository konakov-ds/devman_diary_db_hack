import random
from datacenter.models import Schoolkid, Chastisement, \
    Mark, Lesson, Subject, Commendation


def get_schoolkid(schoolkid_name):
    try:
        schoolkid = Schoolkid.objects.get(
            full_name__contains=schoolkid_name
        )
        return schoolkid
    except Schoolkid.MultipleObjectsReturned:
        print(f'There are more than one student with name {schoolkid_name}')

    except Schoolkid.DoesNotExist:
        print(f'Student {schoolkid_name} does not exist!')


def remove_chastisements(schoolkid_name):
    schoolkid = get_schoolkid(schoolkid_name)
    if schoolkid:
        chastisements = Chastisement.objects.filter(schoolkid=schoolkid)
        chastisements.delete()
        print(f'{schoolkid_name} chastisements successfully deleted!')


def fix_marks(schoolkid_name):
    schoolkid = get_schoolkid(schoolkid_name)
    if schoolkid:
        schoolkid_bad_marks = Mark.objects.filter(schoolkid=schoolkid, points__lt=4)
        if schoolkid_bad_marks:
            for mark in schoolkid_bad_marks:
                mark.points = random.randint(4, 5)
                mark.save()
            print(f'{schoolkid_name} marks successfully changed!')
        else:
            print(f'Bad marks do not find!')


def create_commendation(schoolkid_name, subject_title):
    commendation_texts = ['Хвалю!', 'Отличная работа!',
                          'Предложил оригинальное решение!',
                          'Инициативный и ответственный!',
                          'Подготовка на выcшем уровне!']
    schoolkid = get_schoolkid(schoolkid_name)
    if schoolkid:
        try:
            subject = Subject.objects.get(
                title=subject_title,
                year_of_study=schoolkid.year_of_study
            )
            lesson = Lesson.objects.filter(subject=subject).order_by('-date').first()
            if lesson:
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
                print(f'{schoolkid_name} commendation successfully added!')
            else:
                print(f'There is no lesson at this subject: {subject_title}')

        except Subject.DoesNotExist:
            print(f'Subject {subject_title} does not exist!')
