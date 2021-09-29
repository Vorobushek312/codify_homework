-- 1. Выбрать из таблицы products(product_name,unit_price),categories(description,category_name), suppliers(company_name,city,region)
SELECT products.product_name, products.unit_price, 
categories.description, categories.category_name,
suppliers.company_name, suppliers.city, suppliers.region
FROM products
JOIN categories ON categories.category_id = products.category_id
JOIN suppliers ON suppliers.supplier_id = products.supplier_id
-- 2. Выбрать из таблицы customers(company_name,phone), orders(order_date,ship_city,ship_name), shippers(company_name,phone), employees(first_name,last_name)
SELECT customers.company_name, customers.phone, 
orders.order_date, orders.ship_city, orders.ship_name,
shippers.company_name, shippers.phone,
employees.first_name, employees.last_name
FROM customers
JOIN orders on orders.customer_id = customers.customer_id
JOIN shippers on shippers.shipper_id = orders.ship_via
JOIN employees on employees.employee_id = orders.employee_id;