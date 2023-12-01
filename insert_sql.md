--Insert Values
INSERT into Employee(emp_fname, emp_Lname,emp_salary,emp_id)
VALUES ("Clark","Griswold",60000,48773625),
("Marty","Robbins",42000,78302971),
("John","Wayne",15000,44983012),
("Jack", "Daniels",20000,88929319),
("Dolly", "Parton", 30000, 48920132);

--SELECT * FROM Employee

INSERT into Games(Price, Console, Name, Game_ID, sold_by)
VALUES (60,	"Xbox One","Need for Speed Most Wanted", 100046, 48773625),
(50, "PS4", "Call of Duty Black Ops 3", 200101, 78302971),
(40, "Nintendo Switch", "Super Smash Bros Ultimate", 100201, 48773625),
(30, "PS3", "Fallout: New Vegas", 100582, 44983012),
(30, "Xbox 360", "Halo 3", 200489, 78302971);

--SELECT * FROM Games

INSERT into Customers(f_name, l_name, cust_id, game_bought)
VALUES ("john", "smith",46892, 000-046),
("ellie", "joel",20546, 000-101),
("billy", "joel",20547, 100-201),
("joe", "D",01348, 000-046),
("jack", "macdonald", 04589, 000-101);

-- SELECT * FROM Customers

INSERT into Payments(trans_id, trans_datetime, trans_price, customer)
VALUES (00001, '2023-01-01', 60, 46892),
(00002, '2023-01-02', 10, 20546),
(00003, '2023-01-03', 50, 20547),
(00004, '2023-01-04', 30, 01348),
(00005, '2023-01-10', 30, 04589);

--2023-27-11 1156CST: Updated to Include 5 entries for each table