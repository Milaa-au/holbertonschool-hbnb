# HBNB-Project : Project Setup and Package Initialization:

## Description:
This part of the HBnB project focuses on setting up a modular and scalable architecture. 
Configuring the layer structure Presentation, business logic, and persistence of the Hbnb project.
Creating the necessary folders, packages, and files.
Initialization of the facade pattern for communication between layers. Implementation of in-memory storage to manage the storage and validation of objects.

---

## Structure Directory and file:
### Directory:
* hbnb/ : root directory
* app/ : directory contains the core application code.
* app/api/ : subdirectory houses the API endpoints, organized by version (v1/).
* app/models/ : subdirectory contains the business logic classes (e.g., user.py, place.py).
* app/services/ : subdirectory is where the Facade pattern is implemented, managing the interaction between layers.
* app/persistence/ : subdirectory is where the in-memory repository is implemented.

### File:
* run.py : is the entry point for running the Flask application.
* config.py : will be used for configuring environment variables and application settings.
* requirements.txt : will list all the Python packages needed for the project.

---
## Installation:
### Installing dependencies using:
* "pip install -r requirements.txt"
---
## Running the Application:
### Start the application with:
* "python run.py"

### The application will run on:
* http://127.0.0.1:5000/
---
## Authors
### Team:
* Mila AUDU: https://github.com/Milaa-au
* Pawnee DEFIZE: https://github.com/Pawnee33
