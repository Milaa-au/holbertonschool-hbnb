# 🏡 HBnB – System Design (Part 1)

This repository contains **Part 1 of the HBnB project**, developed as part of the **Holberton School Full Stack Software Engineering program**.

This stage focuses on **system design and architecture**, before implementing the backend.

The goal is to design a platform similar to **Airbnb**, allowing users to:

* create an account
* list places
* browse available places
* leave reviews
* manage amenities

---

# 🎯 Project Objectives

The purpose of this phase is to understand how to **design a complex backend system before coding it**.

Key objectives include:

* analyzing application requirements
* designing a scalable architecture
* modeling entities and relationships
* creating UML diagrams
* documenting system interactions

---

# 🏗 System Architecture

The application is built around four main entities.

### 👤 User

Represents a platform user.

Responsibilities:

* account creation
* authentication
* profile management

---

### 🏠 Place

Represents a property available for booking.

Each place contains:

* owner
* description
* location
* price
* amenities

---

### ⭐ Review

Allows users to leave feedback on a place.

A review contains:

* rating
* comment
* author
* associated place

---

### 🛠 Amenity

Represents features available in a place.

Examples include:

* Wi-Fi
* swimming pool
* parking
* air conditioning

---

# 📊 System Diagrams

## Class Diagram

This diagram represents the **relationships between the main entities** of the system.

![alt text](part1/Class_Diagram.png)

---

## Package Diagram

This diagram shows the **overall architecture of the application and module organization**.

![alt text](part1/UML-PackageDiagram.jpg)

---

# 🔄 Sequence Diagrams

These diagrams illustrate how the system components interact during API calls.

---

### Account Creation

![alt text](part1/Sequence-Diagrams_for_API_Calls_Account.jpg)

---

### Request List

![alt text](part1/Sequence-Diagrams_for_API_Calls_Criteria_RequestList.jpg)

---

### Place List

![alt text](part1/Sequence-Diagrams_for_API_Calls_PlaceList.jpg)

---

### Submit Review

![alt text](part1/Sequence-Diagrams_for_API_Calls_SubmitReview.jpg)

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

**Pawnee DEFIZE**
https://github.com/Pawnee33

**Milaa-au**

Holberton School – Bordeaux
