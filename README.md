# Recruitment System
This project addresses the development of a candidate recruitment system for a given company. The data entered on the application page is processed, saved in a cloud SQL database and, at the end, a confirmation page is issued with the candidate's registration ID.

## Layout

### 1. Login Page
The login page requires the user's email and password. If the user doesn't have a registration, the user can go to the option "I don't have a register".

![FRONT1](https://github.com/CarlosFFilho/recruitment-register_system/blob/main/app/images/login_page_example.png)

### 2. Register Page
The registration page requires user name, email and password informations. After this, the user will be able to log in to the system.

![FRONT2](https://github.com/CarlosFFilho/recruitment-register_system/blob/main/app/images/register_page_example.png)

### 3. Recruitment Page
The recruitment page requires personal informations, address, educational informations and professional experiences of the person to be registered.

![FRONT3](https://github.com/CarlosFFilho/recruitment-register_system/blob/main/app/images/recruitment_page_example.png)

### 4. Confirmation Page
The confirmation page issues the ID and identity confirming the user's registration.

![FRONT4](https://github.com/CarlosFFilho/recruitment-register_system/blob/main/app/images/confirmation_page_example.png)

## Project Diagram
![LOGIC](https://github.com/CarlosFFilho/recruitment-register_system/blob/main/app/images/diagram_of_project.png)

## SQL database relationship (phpMyAdmin)
![SQL](https://github.com/CarlosFFilho/recruitment-register_system/blob/main/app/images/sql_database_relationship.png)

## Technologies used
### Back end
    Python
    MySQL (phpMyAdmin MySQL server)
    AWS instance (Amazon Web Services)
    
### Front end
    Figma
    Tkinter

## How to execute this project?
  1. Create a MySQL database locally or in the cloud, following the scheme previously explained. In this example, a MySQL database was created in the cloud via phpMyAdmin, which could also be controlled locally via MySQL workbench;
  
  2. Make sure the connection credentials between API and Database are correct;
    
  3. Instantiate the "api" directory in AWS, following the steps below;

         Step 1: place the "api" directory in a github repository;
     
         Step 2: Create profile and EC2 instance on AWS;
     
         Step 3: Download and install PUTTY to manage the AWS instance;

         Step 4: Generate a private key in the PUTTYgen and create session in the PUTTY;
     
         Step 5: Clone the Git repository in the instance using PUTTY;

             git clone <http link of repository>
     
         Step 6: Use Nginx and Gunicorn so that the AWS instance IP is used on the local server.

             sudo vim /etc/nginx/sites-enabled/flask_nginx

             server {
                    listen 80;   
                    server_name <INSTANCE_EC2_IP>;    
                    location / {        
                        proxy_pass http://127.0.0.1:8000;    
                    }
             }

             sudo service nginx restart

             gunicorn --bind 127.0.0.1:8000 controller:app_control
     
  
  5. Insert the AWS instance IP in the urls of the "front_connector.py" file ("app" directory);
  
  6. Run the "login_page.py" file in a Python IDE;
  
  7. Enter the information requested by the application;
  
  8. Wait for processing until the confirmation page appears.

OBS: The file "app.exe" can only be executed successfully with the IP logged in by the author. Therefore, it is advisable to follow the execution steps mentioned above or create a new executable, with the IP inserted appropriately, using the "PyInstaller" library.

## Author

      Carlos Aparecido Flor Filho
      www.linkedin.com/in/carlos-filho-5a0a1a1a7
      Email: engcarlosffilho@gmail.com

## Thanks

    Mario Henrique: Assistance and discussions during the preparation of this project.
