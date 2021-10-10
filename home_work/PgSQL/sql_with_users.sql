-- 1.1 пользователь с почтой mlutz2n@youtube.com не может зайти 
-- 1.2 пользователю под почтой styeodz@google.com не может зайти
UPDATE users SET is_active = true where email = 'satyeodz@google.com' or email = 'mlutz2n@youtube.com'
-- 1.3 Сколько человек с почтой из гугла
SELECT count(*) FROM users where email like '%@google.com'
-- 1.4 У каждого человека с почтой из гугла у которых ip адрес начинается на 11, заменить 11 на 19
SELECT *, replace(ip_address, '11', '19') FROM users where ip_address like '11.%'