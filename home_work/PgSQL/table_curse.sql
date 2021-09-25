-- CREATE
-- 1. Создать таблицу СТУДЕНТ(id,имя, фамилия, отчество(необязательное поле), email, год рождения) и заполнить её данными(минимум 10).
-- 2. Создать таблицу КУРС(id,название, дата начала, дата конца) и заполнить данными(минимум 3).
-- 3. Создать таблицу УРОК(id,название, дата начала(дата со временем), дата конца(дата со временем)) и заполнить данными(минимум 3).
-- 4. Создать таблицу ДОМАШНЕЕ ЗАДАНИЕ(id,название, описание, дата начала(дата со временем), дата конца(дата со временем)) и заполнить данными(минимум 3).

-- ALTER
-- 1. Измените таблицу СТУДЕНТ, добавив в неё поле "дата регистрации" и "группа" с помощью ALTER, 
-- сначала добавьте эти поля с возможностью NULL, заполните недостающие данные и измените тип колонок на NOT NULL.
-- 2. Измените таблицу КУРС, добавив в неё поле "стоимость(числовой тип с плавающей запятой)" с помощью ALTER,
-- сначала добавьте это поле с возможностью NULL, заполните недостающие данные и измените тип колонок на NOT NULL.

-- SELECT
-- 1. Для каждой таблицы после всех преобразований напишите SELECT.

-- ТИПЫ ДАННЫХ СМОТРИТЕ ПО ТАБЛИЦЕ:
-- https://www.postgresql.org/docs/9.5/datatype.html
DROP TABLE IF EXISTS student;
CREATE TABLE student
(
id serial PRIMARY KEY,
first_name varchar(100) NOT NULL,
last_name varchar(100) NOT NULL,
middlename varchar(100),
email varchar(50) NOT NULL,
date_of_birth date NOT NULL
);
INSERT INTO student VALUES(1, 'Andrei', 'Voronov', 'Andreevich', 'Voronov_95@list.ru', to_date('22 Feb 1995', 'DD Mon YYYY')),
(2, 'Darya', 'Kostko', 'Evginivna', 'Darya@gmail.com', to_date('13 Sep 1985', 'DD Mon YYYY')),
(3, 'Sasha', 'Miheec', 'Dmitriev', 'Miheec@gmail.com', to_date('01 Nov 1999', 'DD Mon YYYY')),
(4, 'Petr', 'Pexhenyg', 'Olegovich', 'Olegovich@gmail.com', to_date('16 Dec 2003', 'DD Mon YYYY')),
(5, 'Max', 'Korj', null, 'Max@list.ru', to_date('23 Oct 1991', 'DD Mon YYYY')),
(6, 'Den', 'Pechkin', 'Mihailov', 'Den@gmail.com', to_date('26 Aug 1988', 'DD Mon YYYY')),
(7, 'Sam', 'Krang', null, 'Krang@list.ru', to_date('21 May 1976', 'DD Mon YYYY')),
(8, 'Anna', 'Korelina', 'Shedkovich', 'Anna@gmail.com', to_date('08 Apr 1966', 'DD Mon YYYY')),
(9, 'Kate', 'Morozova', 'Semenova', 'Semenova@list.ru', to_date('01 Feb 1974', 'DD Mon YYYY')),
(10, 'Luisa', 'Kim', 'Ivanova', 'Ivanova@gmail.com', to_date('24 Sep 1201', 'DD Mon YYYY'));
SELECT * FROM student;
ALTER TABLE student ADD COLUMN date_regist timestamp;
UPDATE student SET date_regist = to_timestamp('2021 09 21 19:00:00', 'yyyymmdd hh24:mi:ss');
ALTER TABLE student ALTER COLUMN date_regist SET NOT NULL;
SELECT * FROM student;
ALTER TABLE student ADD COLUMN group_student varchar(100);
UPDATE student SET group_student = 'Python';
ALTER TABLE student ALTER COLUMN date_regist SET NOT NULL;
SELECT * FROM student;


DROP TABLE IF EXISTS course;
CREATE TABLE course
(
id serial PRIMARY KEY,
course_name varchar(100) NOT NULL,
date_start date NOT NULL,
date_finish date NOT NULL
);
INSERT INTO course VALUES(1, 'Python', to_date('01 Feb 2021', 'DD Mon YYYY'), to_date('01 Aug 2021', 'DD Mon YYYY')),
(2, 'Java', to_date('01 Sep 2021', 'DD Mon YYYY'), to_date('01 Mar 2022', 'DD Mon YYYY')),
(3, 'C#', to_date('01 Oct 2021', 'DD Mon YYYY'), to_date('01 May 2022', 'DD Mon YYYY'));
SELECT * FROM course;


DROP TABLE IF EXISTS lesson;
CREATE TABLE lesson
(
id serial PRIMARY KEY,
lesson_name varchar(100) NOT NULL,
date_start timestamp NOT NULL,
date_finish timestamp NOT NULL
);
INSERT INTO lesson VALUES(1, 'Python', to_timestamp('2021 09 21 19:00:00', 'yyyymmdd hh24:mi:ss'), to_timestamp('2021 09 21 21:00:00', 'yyyymmdd hh24:mi:ss')),
(2, 'Java', to_timestamp('2021 10 21 19:00:00', 'yyyymmdd hh24:mi:ss'), to_timestamp('2021 10 21 21:00:00', 'yyyymmdd hh24:mi:ss')),
(3, 'C#', to_timestamp('2021 09 21 19:00:00', 'yyyymmdd hh24:mi:ss'), to_timestamp('2021 09 21 21:00:00', 'yyyymmdd hh24:mi:ss'));
SELECT * FROM lesson;


DROP TABLE IF EXISTS home_work;
CREATE TABLE home_work
(
id serial PRIMARY KEY,
homework_name varchar(100) NOT NULL,
description varchar(500) NOT NULL,
date_start timestamp NOT NULL,
date_finish timestamp NOT NULL
);
INSERT INTO home_work VALUES(1, 'Data type bool','поставьте логический операторы(and,or) вместо *** так чтобы выражение дало значение True. True *** False *** True ', to_timestamp('2021 09 21 19:00:00', 'yyyymmdd hh24:mi:ss'), to_timestamp('2021 09 21 21:00:00', 'yyyymmdd hh24:mi:ss')),
(2, 'Прямоугольник','Пользователь вводит длины сторон прямоугольника, найдите и выведите периметр и площадь этого прямоугольника', to_timestamp('2021 10 21 19:00:00', 'yyyymmdd hh24:mi:ss'), to_timestamp('2021 10 21 21:00:00', 'yyyymmdd hh24:mi:ss')),
(3, 'Круг','Пользователь вводит радиус, надо найти и вывести площадь круга и длину окружности:', to_timestamp('2021 09 21 19:00:00', 'yyyymmdd hh24:mi:ss'), to_timestamp('2021 09 21 21:00:00', 'yyyymmdd hh24:mi:ss'));
SELECT * FROM home_work;
