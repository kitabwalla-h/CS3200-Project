-- This file is to bootstrap a database for the CS3200 project. 

-- Create a new database.  You can change the name later.  You'll
-- need this name in the FLASK API file(s),  the AppSmith 
-- data source creation.
create database husky_eatz;

-- Via the Docker Compose file, a special user called webapp will 
-- be created in MySQL. We are going to grant that user 
-- all privilages to the new database we just created. 
-- TODO: If you changed the name of the database above, you need 
-- to change it here too.
grant all privileges on cool_db.* to 'webapp'@'%';
flush privileges;

-- Move into the database we just created.
-- TODO: If you changed the name of the database above, you need to
-- change it here too. 
use husky_eatz;

-- Put your DDL 
CREATE TABLE HuskyEatzEmployee (
  Role varchar(128),
  EmployeeID INTEGER PRIMARY KEY,
  FirstName varchar(128),
  LastName varchar(128)
);

CREATE TABLE Vendor (
  VendorID INTEGER PRIMARY KEY,
  VendorName varchar(128),
  VendorType varchar(128),
  CuisineType varchar(128),
  Phone varchar(128),
  Email varchar(128),
  Street varchar(128),
  City varchar(128),
  State varchar(128),
  ZipCode varchar(128)
  EmployeeID INTEGER,
  FOREIGN KEY (EmployeeID) REFERENCES HuskyEatzEmployee(EmployeeID)
);

CREATE TABLE Hours (
  VendorID INTEGER,
  OpeningTime TIME,
  ClosingTime TIME,
  FOREIGN KEY (VendorID) REFERENCES Vendor(VendorID)
);

CREATE TABLE Location (
  VendorID INTEGER,
  Street varchar(128),
  City varchar(128),
  `State` varchar(128),
  ZipCode varchar(128),
  FOREIGN KEY (VendorID) REFERENCES Vendor(VendorID)
);

CREATE TABLE Menu (
  MenuID INTEGER PRIMARY KEY,
  Name varchar(128),
  RestaurantID INTEGER,
  FOREIGN KEY (RestaurantID) REFERENCES Vendor(RestaurantID)
);

CREATE TABLE AvailibilityPeriod (
  MenuID INTEGER,
  MenuStartTime TIME,
  MenuEndTime TIME,
  FOREIGN KEY (MenuID) REFERENCES Menu(MenuID)
);


CREATE TABLE Customer (
  CustomerID INTEGER PRIMARY KEY,
  Email varchar(128),
  Ingredients varchar(500),
  Availibility BOOLEAN,
  Street varchar(128),
  City varchar(128),
  State varchar(128),
  ZipCode varchar(128)
);

CREATE TABLE DeliveryPeople (
  DeliveryPersonID INTEGER PRIMARY KEY,
  FirstName varchar(128),
  LastName varchar(128),
  Email varchar(128)
);

CREATE TABLE TransportationID (
  TransportationID INTEGER PRIMARY KEY,
  Color varchar(128),
  RegistrationNumber INTEGER,
  Type varchar(128),
  DeliveryPersonID INTEGER,
  FOREIGN KEY (DeliveryPersonID) REFERENCES DeliveryPeople(DeliveryPersonID)
);

CREATE TABLE Order (
  OrderID INTEGER PRIMARY KEY,
  TotalSale INTEGER,
  RestaurantID INTEGER,
  DeliveryDate DATETIME,
  CustomerID INTEGER
  DeliveryPeopleID INTEGER,
  FOREIGN KEY (RestaurantID) REFERENCES Restaurant(RestaurantID),
  FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID),
  FOREIGN KEY (DeliveryPeopleID) REFERENCES DeliveryPeople(DeliveryPeopleID)
);


CREATE TABLE OrderDeatils (
  OrderID INTEGER,
  OrderDetailsID INTEGER PRIMARY KEY,
  OrderTotal INTEGER,
  OrderTime DATETIME,
  FOREIGN KEY (OrderID) REFERENCES Order(OrderID)
);

CREATE TABLE OrderStatus (
  OrderID INTEGER,
  EstimatedDeliveryTime DATETIME,
  ActualDeliveryTime DATETIME,
  `Status` varchar(128),
  FOREIGN KEY (OrderID) REFERENCES Order(OrderID)
);

CREATE TABLE MenuItemsInOrder (
  MenuItemId INTEGER,
  OrderID INTEGER,
  FOREIGN KEY (MenuItemId) REFERENCES MenuItems(MenuItemId),
  FOREIGN KEY (OrderID) REFERENCES Order(OrderID)
);

CREATE TABLE MenuItems (
  `Name` varchar(128),
  Ingredients varchar(500),
  Availibility BOOLEAN,
  Price INTEGER,
  Description varchar(128),
  AllergenInformation varchar(128),
  MenuID INTEGER,
  FOREIGN KEY (MenuID) REFERENCES Menu(MenuID)
);



-- Add sample data. 
INSERT INTO fav_colors
  (name, color)
VALUES
  ('dev', 'blue'),
  ('pro', 'yellow'),
  ('junior', 'red');
