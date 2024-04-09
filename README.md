📦 Cargo System README

    📝 Description 
        
    This Cargo System is designed to manage clients and parties efficiently.
    It offers functionalities to create, update, and retrieve information about clients and parties seamlessly.
    The system is built using Django, a high-level Python web framework, providing robustness and scalability.



🎗 Features

    Client Management: Easily add, update, and view client details including their full name, Telegram ID, and auto-generated keyword.
    Party Management: Create and manage parties with titles, allowing for seamless organization and tracking.



💻 Technologies used

| Technology | Use                       |
|------------|---------------------------|
| Python     | Main programming language |
| Django     | Web framework             |
| SQLite     | Database                  |



🚀 Getting Started

1.Clone the repository

    https://github.com/Abdullayev-Oxunjon/cargo_zed.git

2.Enter the Project

    cd your-repo

3.Run the migrations

    python manage.py migrate

4.Create a virtual environment

    python -m venv .venv

5.Install requirements

    pip install -r requirements.txt

6.Activate the virtual environment:

For Linux/MacOS:

    source .venv/bin/activate

For Windows:

    .venv\Scripts\activate

9.Run the server

    python manage.py runserver

10.Go to localhost http://localhost:8000/



📘 Additional information
    
1.The main parts of the project
    
    1. Login section (only for admin access).Pre-created login and password.

    2. User registration section.
        During user registration:
        1. It is enough to ask for name and surname and telegram ID.
        The keyword must be given by the backend part itself, starting from AAA1. The code date should also be saved automatically. 
        The rest information is not required.
        
    
    3. Available parties (departed flights)
       It is enough to save only party name and date
    
    4. Chinese Storage (shipments sent from China)
        Track code, product name, product number, product weight,
        customer ID number, box name and batch name are required.
    
    5. Uzbek storage (cargo arrived in Uzbekistan)
        Customer id number, track code, product weight and price per kg should be requested.
    
2.Admin credentials
    
    login: admincargo
<<<<<<< HEAD
    password: 2024
=======
    password: 2024
>>>>>>> origin/master
