# Полезные скрипты для редактирования информации в электронном дневнике


###  Использование
Все необходимые скрипты находятся в файле *scripts.py*

Поместите этот файл в ту же директорию, где находится файл *manage.py*

###  Содержание scripts.py

- **remove_chastisements(student_name)**

Функция позволяет удалить все замечания учителя для данного ученика.

Для использования имортируйте функцию:
```python
    from scripts import remove_chastisements
```
  
- **fix_marks(student_name)**

 Функция заменяет плохие(ниже 4) оценки ученика на 4 или 5.

Для использования имортируйте функцию:
 ```python
  from scripts import fix_marks

  ```

- **create_commendation(student_name, subject_title)**

 Функция заносит в дневник похвалу от учителя. Вам нужно передать в качестве аргументов
ФИО ученика и название предмета, например:
```python
  create_commendation('Фролов Иван', 'Музыка')

  ```

Для использования имортируйте функцию:
 ```python
  from scripts import create_commendation

  ```
