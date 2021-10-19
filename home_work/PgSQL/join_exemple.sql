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
drop table pasport;
insert into person(first_name, last_name, number_pasport) values('Andrei', 'Voronov', 'AN332832');
insert into pasport(gender, date_rojdeniya, date_give, pasport_id) values('Man', '1995-02-22', '2010-07-14', 1);