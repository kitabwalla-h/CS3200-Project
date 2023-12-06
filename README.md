# Husky Eatz by Hungry Huskyz
Hungry Huskyz have developed an app called Husky Eatz in order to serve the students at Northeastern. This app is similar to DoorDash or UberEats, however, it gives students access to ordering Dining Hall food to their home so they cant take advantage of dining dollars without having to leave their home. The app will serve 4 main groups:
1. Customers - Students
2. Vendors - Restaurants and Dining Halls
3. Delivery Personnel
4. Husky Eatz Employees

# MySQL + Flask Boilerplate Project

This repo contains a boilerplate setup for spinning up 3 Docker containers: 
1. A MySQL 8 container for obvious reasons
1. A Python Flask container to implement a REST API
1. A Local AppSmith Server

## How to setup and start the containers
**Important** - you need Docker Desktop installed

1. Clone this repository.  
1. Create a file named `db_root_password.txt` in the `secrets/` folder and put inside of it the root password for MySQL. 
1. Create a file named `db_password.txt` in the `secrets/` folder and put inside of it the password you want to use for the a non-root user named webapp. 
1. In a terminal or command prompt, navigate to the folder with the `docker-compose.yml` file.  
1. Build the images with `docker compose build`
1. Start the containers with `docker compose up`.  To run in detached mode, run `docker compose up -d`. 

**Our Additions:** We also found that we needed to run the db_bootstrap.sql file in Datagrip while connected to localhost:3200 (user: root, password: from db_root_password.txt) to allow appsmith to find the husky_eatz database.


