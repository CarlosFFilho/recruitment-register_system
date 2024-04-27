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
    MySQL (phpMyAdmin SQL server)
    
### Front end
    Figma
    Tkinter

## How to execute this project?
  1. Create a MySQL database locally or in the cloud, following the scheme previously explained. In this example, a MySQL database was created in the cloud via phpMyAdmin, which could also be controlled locally via MySQL workbench;
  
  2. Make sure the connection credentials between API and Database are correct;
  
  3. Open and run the "login_page.py" file in a python language IDE;
  
  4. If you have registered, enter your login and password. Otherwise, click "I don't have a register";
  
  5. Add candidate data to the registration page;
  
  6. Wait for processing until the confirmation page appears.

## Author

      Carlos Aparecido Flor Filho
      www.linkedin.com/in/carlos-filho-5a0a1a1a7
      Email: engcarlosffilho@gmail.com
