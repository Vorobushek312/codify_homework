--- ONE TO ONE
-- Person-Passport (Each person has only one passport from a particular country and each passport is intended for only one person.)
create table person (
id serial PRIMARY KEY,
first_name varchar(100) NOT NULL,
last_name varchar(100) NOT NULL,
number_pasport varchar(10) UNIQUE
);
create table pasport (
id serial PRIMARY KEY,
gender varchar(10) NOT NULL,
date_rojdeniya date,
date_give date check(date_rojdeniya < date_give),
pasport_id integer UNIQUE REFERENCES person(id) ON DELETE SET NULL
);
drop table person;
drop table pasport;
drop table bad;
-- Person-Bed
select * from person;
insert into person(first_name, last_name, number_pasport) values('Andrei', 'Voronov', 'AN332832');
insert into person(first_name, last_name, number_pasport) values('Anton', 'Kulik', 'AN332978');
insert into pasport(gender, date_rojdeniya, date_give, pasport_id) values('Man', '1995-02-22', '2010-07-14', (select id from person where number_pasport = 'AN332832'));
create table bad (
	id serial PRIMARY KEY,
	type_bad varchar(100) NOT NULL,
	number_bad integer UNIQUE REFERENCES person(id) ON DELETE SET NULL
);
insert into bad(type_bad, number_bad) values('iron-bad', 1);
insert into bad(type_bad, number_bad) values('wood-bad', 2);
-- Country-Flag (Each country has only one flag and each flag belongs to only one country.)
create table country (
	id serial PRIMARY KEY,
	name_country varchar(100) NOT NULL,
	capital varchar(100) NOT NULL,
	square real NOT NULL
);
create table flag_country (
	id serial PRIMARY KEY,
	color_flag varchar(20) NOT NULL,
	country_id integer UNIQUE REFERENCES country(id) ON DELETE SET NULL
);
insert into country(name_country, capital, square) values('Kyrgizistan', 'Bishkek', 199900);
insert into country(name_country, capital, square) values('Kazahstan', 'Nut-Sultan', 2725000);
insert into flag_country(color_flag, country_id) values('Red', (select id from country where name_country = 'Kyrgizistan'));
insert into flag_country(color_flag, country_id) values('Blue', (select id from country where name_country = 'Kazahstan'));
drop table country;
drop table flag_country;
-- Spousal Relationships (Each person has only one spouse.) Wife-Husband
CREATE TABLE men (
	id serial PRIMARY KEY,
	first_name varchar(100) NOT NULL,
	last_name varchar(100) NOT NULL,
	number_pasport varchar(10) UNIQUE
);
CREATE TABLE women (
	id serial PRIMARY KEY,
	first_name varchar(100) NOT NULL,
	last_name varchar(100) NOT NULL,
	number_pasport varchar(10) UNIQUE,
	man_id integer UNIQUE REFERENCES men(id) ON DELETE SET NULL
);
-- Order-OrderDetails
CREATE TABLE orders(
	id serial PRIMARY KEY,
	weight real,
	date_order date,
	name_order varchar(100),
);
CREATE TABLE order_detail (
	id serial PRIMARY KEY,
	place integer,
	customer varchar(),
	employee varchar(),
	order_id UNIQUE REFERENCES orders(id) ON DELETE SET NULL
);
-- ONE TO MANY
-- Doctor - Patient
create table doctor (
	id serial PRIMARY KEY,
	first_name varchar(100) NOT NULL,
	last_name varchar(100) NOT NULL,
	specialization varchar(100) CHECK (specialization !='')
);
create table patient (
	id serial PRIMARY KEY,
	first_name varchar(100) NOT NULL,
	last_name varchar(100) NOT NULL,
	symptoms varchar(100) NOT NULL,
	doctor_id integer REFERENCES doctor(id) ON DELETE SET NULL
);
insert into doctor(first_name, last_name, specialization) values('Nekita', 'Griboedov', 'Urolog'),
('Kolyan', 'Hlebov', 'Stomotolog'),
('Misha', 'Rechnoi', 'Hirurg');
insert into patient(first_name, last_name, symptoms, doctor_id) 
values('Andrei', 'Petrov', 'toothache', (select id from doctor where specialization = 'Stomotolog')),
('Kiril', 'Myasnov', 'wound', (select id from doctor where specialization = 'Hirurg')),
('Maks', 'Pushkin', 'loss of a finger', (select id from doctor where specialization = 'Hirurg'));
-- Museums-Works
create table museum (
	id serial PRIMARY KEY,
	title varchar(100) NOT NULL,
	address varchar(100) NOT NULL,
	special varchar(100) NOT NULL
);
create table worker (
	id serial PRIMARY KEY,
	first_name varchar(100) NOT NULL,
	last_name varchar(100) NOT NULL,
	price integer NOT NULL,
	specialization varchar(100) NOT NULL,
	museum_id integer REFERENCES museum(id) ON DELETE SET NULL
);
insert into museum(title, address, special) values('Gogo Plane', '4 mkr', 'Airplane'),
('ZZZombiEEE', '5 mkr', 'Big Zombie'),
('Old Books', '6 mkr', 'Book');
insert into worker(first_name, last_name, price, specialization, museum_id) 
values('Inna', 'Ignatieva', 15000, 'clining_manger', (select id from museum where title ='Old Books')),
('Donya', 'Pigeev', 20000, 'security guard', (select id from museum where title ='Old Books'));
-- People-Addresses (Each person can live at one address, but each address can house one or more people.)
CREATE TABLE address (
	id serial PRIMARY KEY,
	addres varchar(100) NOT NULL,
	type_house varchar(100) NOT NULL
);
CREATE TABLE peoples(
	id serial PRIMARY KEY,
	first_name varchar(100) NOT NULL,
	last_name varchar(100) NOT NULL,
	address_id integer REFERENCES address(id) ON DELETE SET NULL
);
INSERT INTO address(addres, type_house) VALUES('4 mkr', 'Hrushovka'),
('5 mkr', 'Hrushovka'),
('6 mkr', 'Hrushovka');
INSERT INTO peoples(first_name, last_name, address_id) 
VALUES('Nekita', 'Griboedov', (SELECT id FROM address WHERE addres = '5 mkr')),
('Kolyan', 'Hlebov', (SELECT id FROM address WHERE addres = '5 mkr')),
('Misha', 'Rechnoi', (SELECT id FROM address WHERE addres = '5 mkr'));
-- Owners-Pets (Each pet has one owner, but each owner can have one or more pets.)
CREATE TABLE owners (
	id serial PRIMARY KEY,
	first_name varchar(100) NOT NULL,
	last_name varchar(100) NOT NULL,
	pasport_number varchar(10) UNIQUE
);
CREATE TABLE pets (
	id serial PRIMARY KEY,
	type_pet varchar(100),
	weight real,
	old_pet integer,
	owner_id integer REFERENCES owners(id) ON DELETE SET NULL
);
-- Farmer-Equipment (Each piece of farming equipment is owned by one farmer, but each farmer can own many pieces of equipment.)
CREATE TABLE farmers (
	id serial PRIMARY KEY,
	first_name varchar(100) NOT NULL,
	last_name varchar(100) NOT NULL,
	pasport_number varchar(10) UNIQUE
);
CREATE TABLE eqiipment (
	id serial PRIMARY KEY,
	brand varchar(50),
	type_equipment varchar(100),
	date_create date,
	farmer_id integer REFERENCES farmers(id) ON DELETE SET NULL
);
-- Employee-Order
CREATE TABLE employees (
	id serial PRIMARY KEY,
	first_name varchar(100) NOT NULL,
	last_name varchar(100) NOT NULL,
	pasport_number varchar(10) UNIQUE
);
CREATE TABLE orders(
	id serial PRIMARY KEY,
	weight real,
	date_order date,
	name_order varchar(100),
	employee_id integer REFERENCES emloyees(id) ON DELETE SET NULL
);
-- Customer-Order
CREATE TABLE customers(
	id serial PRIMARY KEY,
	first_name varchar(100) NOT NULL,
	last_name varchar(100) NOT NULL,
	pasport_number varchar(10) UNIQUE
);
CREATE TABLE orders(
	id serial PRIMARY KEY,
	weight real,
	date_order date,
	name_order varchar(100),
	customers_id integer REFERENCES customers(id) ON DELETE SET NULL
);


--- MANY TO MANY
-- Books-Authors
create table books(
	id serial PRIMARY KEY,
	title varchar(100) NOT NULL,
	price integer NOT NULL
);
create table authors(
	id serial PRIMARY KEY,
	first_name varchar(100) NOT NULL,
	last_name varchar(100) NOT NULL,
	address varchar(100) NOT NULL
);
create table BooksAuthors(
	books_id integer REFERENCES books(id) ON DELETE CASCADE,
	author_id integer REFERENCES authors(id) ON DELETE CASCADE
);
insert into books(title, price) values('Garry Potter', 690),
('CSS and HTML', 850),
('Python 2020', 750);
insert into authors(first_name, last_name, address) values('Anna', 'Darck', '9 mkr'),
('Dasha', 'Kostko', 'Yg-2'),
('Misha', 'Mihailov', 'Panarama');
insert into BooksAuthors(books_id, author_id) 
values((select id from books where title = 'Garry Potter'), (select id from authors where first_name = 'Anna')),
((select id from books where title = 'Python 2020'), (select id from authors where first_name = 'Anna'));
-- Ingredients-Recipes (Each food item can be used in multiple recipes and each recipe requires multiple ingredients.)
create table ingredients(
	id serial PRIMARY KEY,
	title varchar(100) NOT NULL,
	callories real NOT NULL
);
create table recepts(
	id serial PRIMARY KEY,
	name_recet varchar(100) NOT NULL,
	time_cock time NOT NULL
);
create table IngredientsRecepts(
	ingredients_id integer REFERENCES ingredients(id) ON DELETE CASCADE,
	recepts_id integer REFERENCES recepts(id) ON DELETE CASCADE
);
insert into ingredients(title, callories) values('potete', 26.4),
('suger', 359), ('paper', 77), ('milk', 88), ('oil', 785);
insert into recepts(name_recet, time_cock) values('fried pot', '00:30:00'),
('ais_creem', '00:45:30');

insert into IngredientsRecepts(ingredients_id, recepts_id) 
values((select id from ingredients where title = 'potete'), (select id from recepts where name_recet = 'fire pot')),
((select id from ingredients where title = 'oil'), (select id from recepts where name_recet = 'fire pot')),
((select id from ingredients where title = 'paper'), (select id from recepts where name_recet = 'fire pot')),
((select id from ingredients where title = 'milk'), (select id from recepts where name_recet = 'ais_cream')),
((select id from ingredients where title = 'suger'), (select id from recepts where name_recet = 'ais_cream'));
select * from ingredients
-- Doctors-Patients (Each doctor sees many patients and each patient sees many doctors.)
create table doctors (
	id serial PRIMARY KEY,
	first_name varchar(100) NOT NULL,
	last_name varchar(100) NOT NULL,
	specialization varchar(100) CHECK (specialization !='')
);
create table patients (
	id serial PRIMARY KEY,
	first_name varchar(100) NOT NULL,
	last_name varchar(100) NOT NULL,
	symptoms varchar(100) NOT NULL
);
create table DoctorsPatients (
	doctor_id integer REFERENCES doctors(id) ON DELETE CASCADE,
	patient_id integer REFERENCES patients(id) ON DELETE CASCADE
);
INSERT INTO doctors(first_name, last_name, specialization) VALUES('Misha', 'Gorlov', 'hirurg'),
('Arsenii', 'Levchug', 'Okulist'),
('Anna', 'Orlova', 'Teropevt');
INSERT INTO patients(first_name, last_name, symptoms) VALUES('Andrei', 'Petrov', 'toothache'),
('Kiril', 'Myasnov', 'wound'),
('Maks', 'Pushkin', 'loss of a finger');
INSERT INTO DoctorsPatients(doctor_id, patient_id) 
VALUES ((SELECT id FROM doctors WHERE specialization = 'hirurg'), (SELECT id FROM patients WHERE symptoms = 'wound')),
((SELECT id FROM doctors WHERE specialization = 'hirurg'), (SELECT id FROM patients WHERE symptoms = 'loss of a finger')),
((SELECT id FROM doctors WHERE specialization = 'Teropevt'), (SELECT id FROM patients WHERE symptoms = 'loss of a finger')),
((SELECT id FROM doctors WHERE specialization = 'Okulist'), (SELECT id FROM patients WHERE symptoms = 'loss of a finger'));
SELECT * FROM patients;
SELECT * FROM DoctorsPatients;
-- Employees-Tasks (Each employee works on many tasks at a time while each task is being worked on by one or more employees.)
CREATE TABLE employyes(
	id serial PRIMARY KEY,
	first_name varchar(100) NOT NULL,
	last_name varchar(100) NOT NULL,
	position varchar(100) NOT NULL
);
CREATE TABLE tasks(
	id serial PRIMARY KEY,
	descriptin varchar(100) NOT NULL,
	time_to_finish time NOT NULL
);
CREATE TABLE EmployyesTasks(
	employye_id integer REFERENCES employyes(id) ON DELETE CASCADE,
	task_id integer REFERENCES tasks(id) ON DELETE CASCADE
);
INSERT INTO employyes(first_name, last_name, position) VALUES('Misha', 'Gorlov', 'Python'),
('Arsenii', 'Levchug', 'HTML&CSS'),
('Anna', 'Orlova', 'Java');
INSERT INTO tasks(descriptin, time_to_finish) VALUES('Make backend site', '12:00:00'),
('Make front site', '15:00:00'),
('Make java site', '14:00:00'),
('Make full site', '24:00:00');
INSERT INTO EmployyesTasks(employye_id, task_id) 
VALUES((SELECT id FROM employyes WHERE position = 'Python'), (SELECT id FROM tasks WHERE descriptin = 'Make backend site')),
((SELECT id FROM employyes WHERE position = 'Python'), (SELECT id FROM tasks WHERE descriptin = 'Make full site')),
((SELECT id FROM employyes WHERE position = 'Python'), (SELECT id FROM tasks WHERE descriptin = 'Make front site')),
((SELECT id FROM employyes WHERE position = 'HTML&CSS'), (SELECT id FROM tasks WHERE descriptin = 'Make front site'));
-- Customers-Products (Each customer can purchase many products, and each of those products can be purchased by many different customers.)
CREATE TABLE customers (
	id serial PRIMARY KEY,
	first_name varchar(100) NOT NULL,
	last_name varchar(100) NOT NULL,
	pasport varchar(100) UNIQUE
);
CREATE TABLE products(
	id serial PRIMARY KEY,
	product_name varchar(100) NOT NULL,
	price real NOT NULL
);
CREATE TABLE CustomersProducts(
	customer_id integer REFERENCES customers(id) ON DELETE CASCADE,
	product_id integer REFERENCES products(id) ON DELETE CASCADE
);
INSERT INTO customers(first_name, last_name, pasport) VALUES('Andrei', 'Voronov', 'AN332832'),
('Anton', 'Kulik', 'AN332978'),
('Dasha', 'Kim', 'AN332944');
INSERT INTO products(product_name, price) VALUES('milk', 44),
('bread', 20), ('meat', 500), ('chees', 250);
INSERT INTO CustomersProducts(customer_id, product_id)
VALUES((SELECT id FROM customers WHERE pasport = 'AN332832'), (SELECT id FROM products WHERE product_name = 'milk')),
((SELECT id FROM customers WHERE pasport = 'AN332832'), (SELECT id FROM products WHERE product_name = 'bread')),
((SELECT id FROM customers WHERE pasport = 'AN332832'), (SELECT id FROM products WHERE product_name = 'chees')),
((SELECT id FROM customers WHERE pasport = 'AN332944'), (SELECT id FROM products WHERE product_name = 'milk')),
((SELECT id FROM customers WHERE pasport = 'AN332944'), (SELECT id FROM products WHERE product_name = 'chees'));



