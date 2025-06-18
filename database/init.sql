CREATE DATABASE CafeDB;
GO

USE CafeDB;
GO

CREATE TABLE Orders (
    OrderID INT IDENTITY(1,1) PRIMARY KEY,
    Drink NVARCHAR(50),
    Qty INT,
    Price DECIMAL(5,2),
    Branch NVARCHAR(50),
    PaymentType NVARCHAR(50),
    OrderDateTime DATETIME
);
