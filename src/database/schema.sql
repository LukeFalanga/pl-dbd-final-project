-- Table Creation statements for the e-commerce database
CREATE TABLE Customer (
    CustID INT AUTO_INCREMENT PRIMARY KEY,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    Email VARCHAR(100) UNIQUE
);

CREATE TABLE Product (
    ProductID INT AUTO_INCREMENT PRIMARY KEY,
    ProductName VARCHAR(100) NOT NULL,
    Price DECIMAL(10, 2) NOT NULL,
    Stock INT
);

CREATE TABLE Purchases (
    PurchaseID INT AUTO_INCREMENT PRIMARY KEY,
    CustID INT NOT NULL,
    PurchaseDate DATETIME NOT NULL,
    Total DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (CustID) REFERENCES Customer(CustID)
);

CREATE TABLE PurchaseItem (
    PurchaseID INT,
    ProductID INT,
    Quantity INT NOT NULL,
    PRIMARY KEY (PurchaseID, ProductID),
    FOREIGN KEY (PurchaseID) REFERENCES Purchases(PurchaseID),
    FOREIGN KEY (ProductID) REFERENCES Product(ProductID)
);

-- Table insertion commands for the e-commerce database, sample data
INSERT INTO Customer (FirstName, LastName, Email)
VALUES ('Luke', 'Falanga', 'falanglv@mail.uc.edu');

INSERT INTO Customer (FirstName, LastName, Email)
VALUES ('Alice', 'Smith', 'alicesmith@gmail.com');

INSERT INTO Customer (FirstName, LastName, Email)
VALUES ('Bob', 'Johnson', 'bobjohnson@gmail.com');

INSERT INTO Product (ProductName, Price, Stock)
VALUES ('Laptop', 999.99, 100);

INSERT INTO Product (ProductName, Price, Stock)
VALUES ('Phone', 899.99, 200);

INSERT INTO Product (ProductName, Price, Stock)
VALUES ('Backpack', 49.99, 500);

INSERT INTO Product (ProductName, Price, Stock)
VALUES ('Pencil', 0.99, 1000);

INSERT INTO Product (ProductName, Price, Stock)
VALUES ('Shoes', 79.99, 300);

INSERT INTO Purchases (CustID, PurchaseDate, Total)
Values (1, '2026-06-25 10:30:00', 999.99);

INSERT INTO Purchases (CustID, PurchaseDate, Total)
Values (2, '2026-07-22 12:30:00', 99.98);

INSERT INTO Purchases (CustID, PurchaseDate, Total)
Values (2, '2026-07-25 14:00:00', 4.95);

INSERT INTO PurchaseItem (PurchaseID, ProductID, Quantity)
Values (1, 1, 1);

INSERT INTO PurchaseItem (PurchaseID, ProductID, Quantity)
Values (1, 2, 1);

INSERT INTO PurchaseItem (PurchaseID, ProductID, Quantity)
Values (2, 3, 2);

INSERT INTO PurchaseItem (PurchaseID, ProductID, Quantity)
Values (3, 4, 5);