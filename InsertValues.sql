--Insert Values
INSERT into Employee(emp_fname, emp_Lname,emp_salary,emp_id)
VALUES ("Clark","Griswold",60000,48773625),
("Marty","Robbins",42000,78302971),
("John","Wayne",15000,44983012),
("Jack", "Daniels",20000,88929319),
("Dolly", "Parton", 30000, 48920132);

--SELECT * FROM Employee

INSERT into Games(Price, Console, Name, Game_ID, Sold_by)
VALUES (60,	"Xbox One","Need for Speed Most Wanted", 100046, 78302971),
(50, "PS4", "Call of Duty Black Ops 3", 200101, 44983012),
(40, "Nintendo Switch", "Super Smash Bros Ultimate", 100201, 48920132),
(30, "PS3", "Fallout: New Vegas", 100582, 48773625),
(30, "Xbox 360", "Halo 3", 200489, 44983012);

--SELECT * FROM Games

INSERT into Customers(f_name, l_name, cust_id, Game_bought)
VALUES ("john", "smith",46892, 100046),
("ellie", "joel",20546, 100201),
("billy", "joel",20547, 100582),
("joe", "D",01348, 00),
("jack", "macdonald", 04589, 100201);

-- SELECT * FROM Customers

INSERT into Payments(trans_id, trans_datetime, trans_price, customer)
VALUES (00001, '2023-01-01', 60, 46892),
(00002, '2023-01-02', 10, 20546),
(00003, '2023-01-03', 50, 20547),
(00004, '2023-01-04', 30, 01348),
(00005, '2023-01-10', 30, 04589);

--2023-27-11 1156CST: Updated to Include 5 entries for each table
--2023-30-11 1156CST: Updated to new table format
