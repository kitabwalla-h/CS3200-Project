-- This file is to bootstrap a database for the CS3200 project. 

-- Create a new database.  You can change the name later.  You'll
-- need this name in the FLASK API file(s),  the AppSm3ith

-- data source creation.
drop database husky_eatz;
create database IF NOT EXISTS husky_eatz;

-- Via the Docker Compose file, a special user called webapp will 
-- be created in MySQL. We are going to grant that user 
-- all privilages to the new database we just created. 
-- TODO: If you changed the name of the database above, you need 
-- to change it here too.
grant all privileges on husky_eatz.* to 'webapp'@'%';
flush privileges;

-- Move into the database we just created.
-- TODO: If you changed the name of the database above, you need to
-- change it here too. 
use husky_eatz;

-- Put your DDL 
CREATE TABLE HuskyEatzEmployee (
  Role varchar(128) NOT NULL,
  EmployeeID INTEGER PRIMARY KEY AUTO_INCREMENT,
  FirstName varchar(128) NOT NULL,
  LastName varchar(128) NOT NULL
);


CREATE TABLE Vendor (
  VendorID INTEGER PRIMARY KEY AUTO_INCREMENT,
  VendorName varchar(128) NOT NULL,
  VendorType varchar(128) NOT NULL,
  CuisineType varchar(128) NOT NULL ,
  Phone varchar(128) NOT NULL UNIQUE,
  Email varchar(128) NOT NULL UNIQUE,
  EmployeeID INTEGER NOT NULL UNIQUE,
  FOREIGN KEY (EmployeeID) REFERENCES HuskyEatzEmployee(EmployeeID)
        ON UPDATE CASCADE ON DELETE RESTRICT
);

CREATE TABLE VendorLocations (
  VendorID INTEGER NOT NULL ,
  Street varchar(128) NOT NULL ,
  City varchar(128) NOT NULL ,
  `State` varchar(128) NOT NULL ,
  ZipCode varchar(128) NOT NULL ,
  PRIMARY KEY (VendorID, Street),
  FOREIGN KEY (VendorID) REFERENCES Vendor(VendorID)
       ON UPDATE CASCADE ON DELETE RESTRICT
);

CREATE TABLE Menu (
  MenuID INTEGER PRIMARY KEY AUTO_INCREMENT,
  Name varchar(128) NOT NULL ,
  VendorID INTEGER NOT NULL ,
  FOREIGN KEY (VendorID) REFERENCES Vendor(VendorID)
                  ON UPDATE CASCADE ON DELETE RESTRICT
);

CREATE TABLE Customer (
  CustomerID INTEGER PRIMARY KEY AUTO_INCREMENT,
  FirstName varchar(128) NOT NULL ,
  LastName varchar(128) NOT NULL ,
  Phone varchar(128) NOT NULL,
  Email varchar(128) NOT NULL
);


CREATE TABLE CustomerLocations (
  CustomerID INTEGER NOT NULL,
  Street varchar(128) NOT NULL,
  City varchar(128) NOT NULL,
  `State` varchar(128) NOT NULL,
  ZipCode varchar(128) NOT NULL,
  PRIMARY KEY (CustomerID, Street),
  FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID)
                               ON UPDATE CASCADE ON DELETE RESTRICT
);

CREATE TABLE DeliveryPeople (
  DeliveryPersonID INTEGER PRIMARY KEY AUTO_INCREMENT,
  FirstName varchar(128) NOT NULL ,
  LastName varchar(128) NOT NULL ,
  Email varchar(128) NOT NULL
);

CREATE TABLE DeliveryTransportation (
  TransportationID INTEGER PRIMARY KEY AUTO_INCREMENT,
  Color varchar(128) NOT NULL ,
  RegistrationNumber INTEGER,
  Type varchar(128) NOT NULL ,
  DeliveryPersonID INTEGER NOT NULL,
  FOREIGN KEY (DeliveryPersonID) REFERENCES DeliveryPeople(DeliveryPersonID)
                                    ON UPDATE CASCADE ON DELETE RESTRICT
);

CREATE TABLE `Order` (
  OrderID INTEGER PRIMARY KEY AUTO_INCREMENT,
  TotalSale DECIMAL(10,2) NOT NULL ,
  VendorID INTEGER NOT NULL ,
  DeliveryDate DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  CustomerID INTEGER NOT NULL ,
  DeliveryPersonID INTEGER NOT NULL ,
  FOREIGN KEY (DeliveryPersonID) REFERENCES DeliveryPeople(DeliveryPersonID)
                     ON UPDATE CASCADE ON DELETE RESTRICT,
  FOREIGN KEY (VendorID) REFERENCES Vendor(VendorID)
                     ON UPDATE CASCADE ON DELETE RESTRICT,
  FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID)
                     ON UPDATE CASCADE ON DELETE RESTRICT
);

CREATE TABLE OrderDetails (
  OrderID INTEGER NOT NULL ,
  OrderDetailsID INTEGER PRIMARY KEY AUTO_INCREMENT,
  OrderTotal DECIMAL(10,2) NOT NULL ,
  OrderTime DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (OrderID) REFERENCES `Order`(OrderID)
                          ON UPDATE CASCADE ON DELETE RESTRICT
);

CREATE TABLE OrderStatus (
  OrderDetailsID INTEGER NOT NULL,
  EstimatedDeliveryTime DATETIME NOT NULL,
  ActualDeliveryTime DATETIME,
  `Status` varchar(128) NOT NULL ,
  PRIMARY KEY (OrderDetailsID, EstimatedDeliveryTime),
  FOREIGN KEY (OrderDetailsID) REFERENCES OrderDetails(OrderDetailsID)
                         ON UPDATE CASCADE ON DELETE RESTRICT
);

CREATE TABLE MenuItems (
  `Name` varchar(128) PRIMARY KEY,
  Ingredients varchar(500) NOT NULL,
  Availability BOOLEAN NOT NULL,
  Price DECIMAL(10,2) NOT NULL,
  Description varchar(128) NOT NULL,
  AllergenInformation varchar(128) NOT NULL,
  MenuID INTEGER NOT NULL,
  FOREIGN KEY (MenuID) REFERENCES Menu(MenuID)
                       ON UPDATE CASCADE ON DELETE RESTRICT
);

CREATE TABLE MenuItemsInOrder (
    OrderDetailsID INTEGER NOT NULL,
    MenuItemName varchar(128) NOT NULL,
    PRIMARY KEY (OrderDetailsID, MenuItemName),
    FOREIGN KEY (OrderDetailsID) REFERENCES OrderDetails(OrderDetailsID)
                    ON UPDATE CASCADE ON DELETE RESTRICT,
    FOREIGN KEY (MenuItemName) REFERENCES MenuItems(`Name`)
                    ON UPDATE CASCADE ON DELETE RESTRICT
);

-- Add sample data. 

INSERT INTO HuskyEatzEmployee(Role, FirstName, LastName) VALUES ('Developer', 'Michelle', 'Velyunskiy');
INSERT INTO HuskyEatzEmployee(Role, FirstName, LastName) VALUES ('Developer', 'Elizabeth', 'Jamison');
INSERT INTO HuskyEatzEmployee(Role, FirstName, LastName) VALUES ('Data Scientist', 'Hani', 'K');
INSERT INTO HuskyEatzEmployee(Role, FirstName, LastName) VALUES ('Data Scientist', 'Eva', 'Balgoun');

INSERT INTO Vendor(VendorName, VendorType, CuisineType, Phone, Email, EmployeeID) VALUES ('El Jefes', 'Restaurant', 'Mexican', '123-456-7890', 'eljefes@example.com', 1);
INSERT INTO Vendor(VendorName, VendorType, CuisineType, Phone, Email, EmployeeID) VALUES ('Tatte', 'Restaurant', 'Cafe', '098-654-0321', 'tatte@example.com', 2);
INSERT INTO Vendor(VendorName, VendorType, CuisineType, Phone, Email, EmployeeID) VALUES ('Steast', 'Dining Hall', 'Dining Hall', '098-765-4321', 'steast@example.com', 3);
INSERT INTO Vendor(VendorName, VendorType, CuisineType, Phone, Email, EmployeeID) VALUES ('International Village', 'Dining Hall', 'Dining Hall', '123-987-7654', 'iv@example.com', 4);

INSERT INTO VendorLocations(VendorID, Street, City, State, ZipCode) VALUES (1, ' 123 Columbus Ave', 'Boston', 'MA', 02120);
INSERT INTO VendorLocations(VendorID, Street, City, State, ZipCode) VALUES (2, ' 123 Forsyth St', 'Boston', 'MA', 02120);
INSERT INTO VendorLocations(VendorID, Street, City, State, ZipCode) VALUES (3, ' 456 Huntington Ave', 'Boston', 'MA', 02120);
INSERT INTO VendorLocations(VendorID, Street, City, State, ZipCode) VALUES (4, ' 789 Ruggles St', 'Boston', 'MA', 02120);

INSERT INTO Menu (Name, VendorID) VALUES ('Jefes Menu', 1);
INSERT INTO Menu (Name, VendorID) VALUES ('Tatte Menu', 2);
INSERT INTO Menu (Name, VendorID) VALUES ('Steast Menu', 3);
INSERT INTO Menu (Name, VendorID) VALUES ('International Village Menu', 4);

INSERT INTO Customer(Email, FirstName, LastName, Phone) VALUES ('michelle.v@example.com', 'Michelle', 'V', '987-765-5432');
INSERT INTO Customer(Email, FirstName, LastName, Phone) VALUES ('elizabeth.j@example.com', 'Elizabeth', 'J', '123-345-5678');
INSERT INTO Customer(Email, FirstName, LastName, Phone) VALUES ('hani.k@example.com', 'Hani', 'K', '432-654-3456');
INSERT INTO Customer(Email, FirstName, LastName, Phone) VALUES ('eva.b@example.com', 'Eva', 'B', '654-432-4321');

INSERT INTO CustomerLocations(CustomerID, Street, City, State, ZipCode) VALUES (1, ' 123 Burke Ave', 'Boston', 'MA', 02115);
INSERT INTO CustomerLocations(CustomerID, Street, City, State, ZipCode) VALUES (2, ' 567 Hemingway St', 'Boston', 'MA', 02115);
INSERT INTO CustomerLocations(CustomerID, Street, City, State, ZipCode) VALUES (3, ' 789 Columbus Ave', 'Boston', 'MA', 02120);
INSERT INTO CustomerLocations(CustomerID, Street, City, State, ZipCode) VALUES (4, ' 329 Huntington St', 'Boston', 'MA', 02120);

INSERT INTO DeliveryPeople(FirstName, LastName, Email) VALUES ('Bob', 'Builder', 'bob.builder@example.com');
INSERT INTO DeliveryPeople(FirstName, LastName, Email) VALUES ('Alice', 'Smith', 'alice.s@example.com');
INSERT INTO DeliveryPeople(FirstName, LastName, Email) VALUES ('Dave', 'Jackson', 'dave.s@example.com');
INSERT INTO DeliveryPeople(FirstName, LastName, Email) VALUES ('Carol', 'Miller', 'c.miller@example.com');

INSERT INTO DeliveryTransportation(Color, Type, RegistrationNumber, DeliveryPersonID) VALUES ('Blue',  'Bike', 12345678, 1);
INSERT INTO DeliveryTransportation(Color, Type, RegistrationNumber, DeliveryPersonID) VALUES ('Red',  'Car', 87654321, 2);
INSERT INTO DeliveryTransportation(Color, Type, RegistrationNumber, DeliveryPersonID) VALUES ('Yellow', 'Skateboard',  78904321, 3);
INSERT INTO DeliveryTransportation(Color, Type, RegistrationNumber, DeliveryPersonID) VALUES ('Black', 'Limo', 76543098, 4);

INSERT INTO `Order`( TotalSale, VendorID, CustomerID, DeliveryPersonID) VALUES (20.36, 1, 1, 1);
INSERT INTO `Order`( TotalSale, VendorID, CustomerID, DeliveryPersonID) VALUES (100.78, 2, 2, 2);
INSERT INTO `Order`( TotalSale, VendorID, CustomerID, DeliveryPersonID) VALUES (74.28, 3, 3, 3);
INSERT INTO `Order`( TotalSale, VendorID, CustomerID, DeliveryPersonID) VALUES (52.95, 4, 4, 4);

INSERT INTO OrderDetails(OrderID, OrderTotal) VALUES (1, 1);
INSERT INTO OrderDetails(OrderID, OrderTotal) VALUES (2, 2);
INSERT INTO OrderDetails(OrderID, OrderTotal) VALUES (3, 3);
INSERT INTO OrderDetails(OrderID, OrderTotal) VALUES (4, 4);

INSERT INTO OrderStatus(OrderDetailsID, EstimatedDeliveryTime, ActualDeliveryTime, Status) VALUES (1, '2023-03-16 10:23:10', '2023-03-16 10:22:10', 'Delivered');
INSERT INTO OrderStatus(OrderDetailsID, EstimatedDeliveryTime, Status) VALUES (2, '2023-03-16 23:19:48', 'In Progress');
INSERT INTO OrderStatus(OrderDetailsID, EstimatedDeliveryTime, Status) VALUES (3, '2023-03-16 10:23:10',  'In Transit');
INSERT INTO OrderStatus(OrderDetailsID, EstimatedDeliveryTime, `Status`) VALUES (4, '2023-03-16 10:23:10','Canceled');

INSERT INTO MenuItems VALUES ('Pesto Pasta', 'Pesto, Pasta', TRUE, 15.99, 'Pesto Pasta', 'Vegan, Contains Nuts' , 1);
INSERT INTO MenuItems VALUES ('Greek Salad', 'Lettuce, Tomato, Onion, Feta, Greek Dressing', TRUE, 10.99, 'Greek Salad', 'Vegan, Dairy Free, Gluten Free, Nut Free' , 2);
INSERT INTO MenuItems VALUES ('Burrito', 'Tortilla, Beans. Cheese', TRUE, 12.99, 'Been and Cheese Burrito', 'Contains Gluten, Contains Dairy, Nut Free' , 3);
INSERT INTO MenuItems VALUES ('Grilled Cheese', 'Bread, Cheese, Butter', FALSE, 7.99, 'Grilled Cheese', 'Contains Gluten, Contains Dairy, Nut Free' , 4);

INSERT INTO MenuItemsInOrder VALUES (1, 'Pesto Pasta');
INSERT INTO MenuItemsInOrder VALUES (2, 'Burrito');
INSERT INTO MenuItemsInOrder VALUES (3, 'Greek Salad');
INSERT INTO MenuItemsInOrder VALUES (4, 'Greek Salad');