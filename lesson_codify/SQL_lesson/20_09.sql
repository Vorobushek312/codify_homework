INSERT INTO student VALUES('Anton','test@mail.tu', 'Krivosheev', 'Antonovich');
SELECT * FROM student;
--ALTER TABLE student.first_name RENAME TO
--DROP TABLE student;
--CREATE TABLE student
-- (
-- 	first_name character varying(100) NOT NULL,
-- 	email character varying(150) NOT NULL
-- );
ALTER TABLE student ALTER COLUMN first_name TYPE varchar (500);
ALTER TABLE student ADD COLUMN last_name varchar(150);
ALTER TABLE student ALTER COLUMN last_name SET NOT NULL;
ALTER TABLE student ADD COLUMN middle_name varchar(150);
ALTER TABLE student ALTER COLUMN middle_name SET NOT NULL;
DELETE FROM student;
