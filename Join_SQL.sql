-- SQLite
SELECT Payments.trans_id, Customers.f_name as Customer
FROM Payments
Inner JOIN Customers
ON customerID = cust_id;

SELECT Employee.emp_fname as Employee_Name, Games.Name as Game_Sold
FROM Games
Inner JOIN Employee
ON Sold_by = emp_id;

SELECT Customers.f_name as CustomerName, Games.Name as Purchased_Game 
FROM Games
Inner JOIN Customers
ON Game_bought = Game_ID;

SELECT Customers.f_name as CustomerName, Games.Name as Purchased_Game 
FROM Games
LEFT JOIN Customers
ON Game_bought = Game_ID;