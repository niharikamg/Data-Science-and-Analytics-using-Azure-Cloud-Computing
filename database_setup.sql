CREATE TABLE Transactions (
    Hshd_num INT,
    Basket_num INT,
    Date DATE,
    Product_num INT,
    Department TEXT,
    Commodity TEXT,
    Spend FLOAT
);

CREATE TABLE Households (
    Hshd_num INT PRIMARY KEY,
    Income_Level TEXT,
    Loyalty_Member BOOLEAN
);

CREATE TABLE Products (
    Product_num INT PRIMARY KEY,
    Department TEXT,
    Commodity TEXT,
    Private_Brand BOOLEAN,
    Organic BOOLEAN
);
