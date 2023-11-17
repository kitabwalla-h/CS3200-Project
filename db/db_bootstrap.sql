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

CREATE TABLE Restaurant/Vendor (
  RestaurantID INTEGER PRIMARY KEY,
  RestaurantName varchar(128),
  CuisineType varchar(128),
  Phone varchar(128),
  Email varchar(128),
  OpeningTime INTEGER,
  ClosingTime INTEGER,
  Street varchar(128),
  City varchar(128),
  State varchar(128),
  ZipCode varchar(128)
);

CREATE TABLE Menu (
  MenuID INTEGER PRIMARY KEY,
  Name varchar(128),
  MenuStartTime INTEGER,
  MenuEndTime INTEGER,
  RestaurantID INTEGER,
);

CREATE TABLE MenuItems (
  MenuItemID INTEGER PRIMARY KEY,
  Name varchar(128),
  Ingredients varchar(500),
  Availibility BOOLEAN,
  Price INTEGER,
  Description varchar(128),
  AllergenInformation varchar(128),
  MenuID INTEGER,
);

-- CREATE TABLE OrderDeatils (
--   OrderId INTEGER PRIMARY KEY,
--   OrderTotal INTEGER,
--   OrderTime DATETIME,
-- );

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
);

CREATE TABLE Order (
  OrderID INTEGER PRIMARY KEY,
  TotalSale INTEGER,
  RestaurantID INTEGER,
  DeliveryDate varchar(128),
  CustomerID INTEGER
);




-- Add sample data. 
INSERT INTO fav_colors
  (name, color)
VALUES
  ('dev', 'blue'),
  ('pro', 'yellow'),
  ('junior', 'red');
