-- 1. Напишите запрос, чтобы получить название продукта и количество/единицу. 
SELECT product_name, quantity_per_unit FROM products;
select * from products;
-- 2. Напишите запрос для получения текущего списка продуктов (ID и название продукта). 
SELECT product_id, product_name FROM products;
-- 3. Напишите запрос для получения списка продуктов, со скидкой (ID и название продукта). 
SELECT product_id, product_name FROM products WHERE discontinued = 1;
-- 4. Напишите запрос, чтобы получить список самых дорогих и самых дешевых продуктов (название и цена за единицу). 
SELECT product_name, unit_price FROM products where unit_price = (SELECT MAX(unit_price) FROM products);
SELECT product_name, unit_price FROM products where unit_price = (SELECT MIN(unit_price) FROM products);
-- 5. Напишите запрос, чтобы получить список продуктов (идентификатор, название, цена за единицу), в котором текущие продукты стоят менее $20. 
SELECT product_name, unit_price FROM products where unit_price < 20;
-- 6. Выведите всех сотрудников которые старше 55 лет.
SELECT * FROM employees WHERE (current_date - birth_date) > 55;
-- 7. Выведите всех сотрудников которые младше 55 лет.
SELECT * FROM employees WHERE (current_date - birth_date) < 55;
-- 8. Выведите всех сотрудников, возраст которых между 55 и 60 годами.
SELECT * FROM employees WHERE (current_date - birth_date) > 55 AND (current_date - birth_date) < 60;