# 🏡 HBnB – System Design (Part 1)

This repository contains **Part 1 of the HBnB project**, developed as part of the **Holberton School Full Stack Software Engineering program**.

This first stage focuses on **system design and architecture**, before implementing the application.

The goal of the project is to design a platform similar to **Airbnb**, allowing users to:

* create an account
* list places for rent
* browse available places
* leave reviews
* manage amenities

---

# 🎯 Project Objectives

The main goal of this part is to understand how to **design a complex backend application before coding it**.

Key learning objectives include:

* analyzing application requirements
* designing system architecture
* modeling entities and relationships
* creating UML diagrams
* documenting API interactions

---

# 🏗 System Architecture

The HBnB platform is structured around several core entities.

### 👤 User

Represents a platform user.

Responsibilities:

* account creation
* authentication
* profile management

---

### 🏠 Place

Represents a property available for rent.

Each place includes:

* an owner
* description
* price
* location
* associated amenities

---

### ⭐ Review

Allows users to leave feedback on a place.

A review contains:

* a rating
* a comment
* the author
* the associated place

---

### 🛠 Amenity

Represents an amenity available in a place.

Examples include:

* Wi-Fi
* swimming pool
* air conditioning
* parking

---

# 📊 Diagrams Included

This folder contains several diagrams used to design the system architecture.

---

## Class Diagram

Defines the relationships between the main entities of the system:

* User
* Place
* Review
* Amenity

File:

Class Diagram.png

---

## Sequence Diagrams

These diagrams illustrate how different components interact during API calls.

### Account Creation

Describes the process of creating a new user account.

### Request List

Shows how the system retrieves available places.

### Place List

Displays the flow for listing places.

### Submit Review

Illustrates how a user submits a review.

Files:

* Sequence-Diagrams_for_API Calls_Account.jpg
* Sequence-Diagrams_for_API Calls_RequestList.jpg
* Sequence-Diagrams_for_API Calls_PlaceList.jpg
* Sequence-Diagrams_for_API Calls_SubmitReview.jpg

---

## Package Diagram

The package diagram shows the **overall structure of the project** and how the modules are organized.

File:

UML-PackageDiagram.jpg

---

# 📂 Project Structure

```
part1
│
├── Class Diagram.png
├── UML-PackageDiagram.jpg
├── Documentation Compilation.pdf
│
├── Sequence-Diagrams_for_API Calls_Account.jpg
├── Sequence-Diagrams_for_API Calls_RequestList.jpg
├── Sequence-Diagrams_for_API Calls_PlaceList.jpg
└── Sequence-Diagrams_for_API Calls_SubmitReview.jpg
```

---

# 🛠 Technologies Used

* UML
* System Design
* Software Architecture
* Technical Documentation

---

# 👨‍💻 Authors

Project developed by:

**Pawnee DEFIZE**
GitHub: https://github.com/Pawnee33

**Milaa-au**

As part of the **Holberton School Bordeaux program**.

---

# 📚 Context

This project represents the **design phase of the HBnB application**.

Later stages of the project include:

* backend implementation
* REST API development
* database integration
* full platform development

