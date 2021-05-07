SELECT max(salary) as max_salary,
min(salary) as min_salary,
round(avg(salary), 2) as average_salary,
sum(salary) as sum_salary,
count(salary) as count_salary
FROM users
WHERE first_name='Carly';