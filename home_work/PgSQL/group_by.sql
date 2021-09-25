-- 1. Напишите запрос, чтобы получить список продуктов (id, название, цена за единицу), в котором продукты стоят от $15 до $25. 
SELECT * FROM products;
SELECT product_id, product_name, unit_price FROM products WHERE unit_price >= 15 AND unit_price <= 25;
-- 2. Напишите запрос, чтобы получить список продуктов (название, цена за единицу) по цене выше средней.
SELECT AVG(unit_price) FROM products;
SELECT product_name, unit_price FROM products WHERE unit_price > (SELECT AVG(unit_price) FROM products);
-- 3. Напишите запрос, чтобы получить список продуктов (название, цена за единицу) из десяти самых дорогих продуктов. 
SELECT product_name, unit_price FROM products ORDER BY unit_price DESC LIMIT 10;
-- 4. Напишите запрос для подсчета текущих и со скидкой продуктов. 
SELECT COUNT(product_name) FROM products;
SELECT COUNT(product_name) FROM products WHERE discontinued = 1;
-- 5. Напишите запрос, чтобы получить список продуктов (название, единицы в заказе , единицы на складе), количество которых на складе меньше, чем количество в заказе. 
SELECT product_name, units_on_order, units_in_stock FROM products WHERE units_in_stock < units_on_order;
-- 6. Получить количество заказов по дате заказа из таблицы orders, где дата заказа от 1 апреля 1996 года(включительно), 
-- при этом исключить из выборки заказы с сентября каждого года по ноябрь (включительно),
-- всё с сортировкой по дате заказа в порядке убыванию.
-- Для получения месяца из даты используйте EXTRACT.
-- В результирующей выборке должно быть 350 записей.
SELECT * FROM orders WHERE order_date > '1996-04-01' 
AND extract(month from order_date) NOT IN (9,10,11)
LIMIT 350;
-- 7. Получить все товары у которых цена в между 10(не включительно) и 43.9(включительно) и содержит 'ea' в названии продукта, сортировка по product_id в убывающем порядке
SELECT product_name, unit_price FROM 
products 
WHERE unit_price > 10 
AND unit_price <= 43.9 
AND product_name LIKE '%ea%' 
ORDER BY unit_price DESC;