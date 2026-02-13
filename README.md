# holbertonschool-HBNB

## Description

HBNB is a web application designed to allow users to create, manage, and consult place listings. Users can register, publish places, add amenities, and submit reviews. The system is built using a layered architecture to ensure clear separation of responsibilities, maintainability, and scalability.

The application follows software engineering best practices and uses UML diagrams to model the system structure and interactions.

---

## Objectives

The main objectives of this project are:

* Manage user accounts (registration, update, deletion)
* Allow owners to create and manage place listings
* Allow administrators to manage amenities
* Allow users to leave reviews on places
* Store and retrieve data reliably from the database
* Apply clean architecture principles and design patterns

---

## Architecture

The project is based on a **3-layer architecture**:

### 1. Presentation Layer

* Handles interaction with the user
* Exposes API endpoints
* Sends requests to the Business Logic Layer
* Returns responses to the user

### 2. Business Logic Layer

* Contains the core logic of the application
* Manages the main entities:

  * User
  * Place
  * Review
  * Amenity
* Validates data and enforces business rules
* Uses the Facade pattern to simplify communication

### 3. Persistence Layer

* Handles data storage and retrieval
* Communicates directly with the database
* Ensures data consistency and persistence

---

## Main Entities

### User

Represents a user of the system.

Attributes:

* id
* firstName
* lastName
* email
* password
* isAdmin

### Place

Represents a place listing created by an owner.

Attributes:

* id
* title
* description
* price
* latitude
* longitude

### Review

Represents a review left by a user on a place.

Attributes:

* id
* rating
* comment

### Amenity

Represents an amenity that can be associated with a place.

Attributes:

* id
* name
* description

---

## API Features

The API allows the following operations:

* Create user account
* Update user profile
* Create place listing
* Update or delete place listing
* Add amenities
* Submit reviews
* Search places based on criteria
* Retrieve places list

---

## HTTP Status Codes

The API uses standard HTTP status codes:

* 200 OK – Request successful
* 201 Created – Resource created successfully
* 400 Bad Request – Invalid request data
* 401 Unauthorized – Authentication required
* 403 Forbidden – Permission denied
* 404 Not Found – Resource not found
* 409 Conflict – Resource conflict
* 500 Internal Server Error – Server error

---

## Design Patterns

The project uses the **Facade Pattern** to simplify communication between the Presentation Layer and the Business Logic Layer.

This improves:

* Code organization
* Maintainability
* Scalability

---

## UML Diagrams

The project includes:

* Package Diagram
* Class Diagram
* Sequence Diagrams

These diagrams help visualize:

* System structure
* Entity relationships
* Request flow

---
## Authors
Team:
* Mila AUDU: https://github.com/Milaa-au
* Pawnee DEFIZE: https://github.com/Pawnee33
