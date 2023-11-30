-- SQLite
SELECT Payments.trans_id, Customers.f_name
FROM Payments
Inner JOIN Customers
ON customerID = cust_id;