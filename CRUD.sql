--Create, ie insert new values into tables after creation
INSERT INTO Employee VALUES ("Chris", "Stapleton", 25000, 43982011);
--Read, ie select different data entries from table
SELECT * FROM Employee WHERE Employee.emp_salary > 25000;
--Update value from table
UPDATE Employee SET emp_salary = 30000 WHERE emp_id = 78302971;
--Delete entries from table
DELETE FROM Employee WHERE emp_fname = "Marty";

--Generalized forms for Employee below:
--INSERT INTO Employee VALUES ("emp_fname", "emp_lname", salary, emp_id)
--SELECT expr FROM Employee WHERE expr
--UPDATE Employee SET table_value = expr WHERE table_value = expr
--DELETE FROM Employee WHERE table_value = expr

INSERT INTO Games VALUES (60, "PS4", "Bloodborne", 300604);
SELECT * FROM Games WHERE Price = 60;
UPDATE Games SET Price = 50 WHERE Game_ID = 000046;
DELETE FROM Games WHERE Game_ID != 300604;
--SELECT * FROM Games

--Generalized forms for Games:
--INSERT INTO Games VALUES (Price, "Console", "Game Name", Game_ID)
--SELECT expr FROM Games WHERE expr
--UPDATE Games SET table_value = expr WHERE table_value = expr
--DELETE FROM Games WHERE table_value = expr

INSERT INTO Customers VALUES ("Jane", "Doe", 90823, "3296867321");
SELECT * FROM Customers WHERE cust_id = 20546;
UPDATE Customers SET cust_id = 44892 WHERE f_name = "Jane";
DELETE FROM Customers WHERE cust_id = 44892;

--Generalized forms for Customers:
--INSERT INTO Customers VALUES ("fname", "lname", cust_id, "phonenumber")
--SELECT expr FROM Customers WHERE expr
--UPDATE Customers SET table_value = expr WHERE table_value = expr
--DELETE FROM Customers WHERE table_value = expr

INSERT INTO Payments VALUES (00006, '2023-01-11', 60, 20546);
SELECT * FROM Payments WHERE cust_id = 20546;
UPDATE Payments SET trans_price = 50 WHERE trans_id = 6;
DELETE FROM Payments WHERE trans_price = 50;
SELECT * FROM Payments

--Generalized forms for Payments:
--INSERT INTO Payments VALUES ("fname", "lname", cust_id, "phonenumber")
--SELECT expr FROM Payments WHERE expr
--UPDATE Payments SET table_value = expr WHERE table_value = expr
--DELETE FROM Payments WHERE table_value = expr