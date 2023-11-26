-- SQLite
-- CREATE TABLE Employee(emp_fname TEXT NOT NULL, emp_Lname TEXT NOT NULL, 
-- emp_salary INTEGER NOT NULL, emp_id INTEGER NOT NULL);

-- INSERT into Employee(emp_fname, emp_Lname,emp_salary,emp_id)
-- VALUES ("Clark","Griswold",60000,48773625);
-- INSERT into Employee(emp_fname, emp_Lname,emp_salary,emp_id)
-- VALUES ("Marty","Robbins",42000,78302971);
-- INSERT into Employee(emp_fname, emp_Lname,emp_salary,emp_id)
-- VALUES ("John","Wayne",15000,44983012);

--SELECT * FROM Employee

-- CREATE TABLE Games(Price INTEGER NOT NULL,Console TEXT NOT NULL,
-- Name TEXT NOT NULL, Game_ID INTEGER NOT NULL PRIMARY KEY);

-- INSERT into Games(Price, Console, Name, Game_ID)
-- VALUES (60,	"Xbox One","Need for Speed Most Wanted", 000046);
-- INSERT into Games(Price, Console, Name, Game_ID)
-- VALUES (50, "PS4", "Call of Duty Black Ops 3", 000101);
-- INSERT into Games(Price, Console, Name, Game_ID)
-- VALUES (40, "Nintendo Switch", "Super Smash Bros Ultimate", 100201);

-- SELECT * FROM Games

-- CREATE TABLE Customers(f_name TEXT NOT NULL, l_name TEXT NOT NULL,
-- cust_id INTEGER NOT NULL PRIMARY KEY, phone varchar(15) NOT NULL);

-- INSERT into Customers(f_name, l_name, cust_id, phone)
-- VALUES ("john", "smith",46892, "3167894512");
-- INSERT into Customers(f_name, l_name, cust_id, phone)
-- VALUES ("ellie", "joel",20546, "2456293827");
-- INSERT into Customers(f_name, l_name, cust_id, phone)
-- VALUES ("billy", "joel",20547, "2456879041");
-- INSERT into Customers(f_name, l_name, cust_id, phone)
-- VALUES ("joe", "D",01348, "1453679587");

-- SELECT * FROM Customers

-- CREATE TABLE Payments(trans_id INTEGER NOT NULL PRIMARY KEY, trans_datetime DATE DEFAULT NULL, 
-- trans_price INT DEFAULT NULL, customerID NOT NULL);
-- INSERT into Payments(trans_id, trans_datetime, trans_price, customerID)
-- VALUES (00001, '2023-01-01', 60, 46892),
-- (00002, '2023-01-02', 10, 20546),
-- (00003, '2023-01-03', 50, 20547),
-- (00004, '2023-01-04', 30, 01348);
SELECT * FROM Payments