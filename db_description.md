IDs: Primaries
FK: sold_by->employee_id
FK: game_bought->game_id
FK customer -> cust_id

Games
Price		Name		Game_id 	Sold_by
60$		Xbox One	Need for Speed	000-046


Employees
emp_fname 	emp_Lname	emp_salary	employee_id
Clark		Griswold	60,000$		48773625

Customers			
f_name		l_name		cust_id		game_bought
john		smith		46892		000-046

Payments			
trans_id	trans_datetime	trans_price	customer
000-01		1/1/23		60		46892


primary keys: 	Game_id		employee_id	cust_id		trans_id