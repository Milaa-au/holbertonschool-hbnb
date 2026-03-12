-- Script that creates the tables User
-- Create User if it does not already exist
CREATE TABLE IF NOT EXISTS User (
    id CHAR(36) PRIMARY KEY,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    is_admin BOOLEAN DEFAULT FALSE
);
-- Script that creates the tables Place
-- Create Place if it does not already exist
CREATE TABLE IF NOT EXISTS Place (
    id CHAR(36) PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description TEXT NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    latitude FLOAT NOT NULL,
    longitude FLOAT NOT NULL,
    owner_id CHAR(36),
    FOREIGN KEY (owner_id) REFERENCES User(id)
);
-- Script that creates the tables Review
-- Create Review if it does not already exist
CREATE TABLE IF NOT EXISTS Review (
    id CHAR(36) PRIMARY KEY,
    text TEXT NOT NULL,
    rating INT CHECK(rating >= 1 AND rating <= 5) NOT NULL,
    user_id CHAR(36) NOT NULL,
    FOREIGN KEY (user_id) REFERENCES User(id),
    place_id CHAR(36) NOT NULL,
    FOREIGN KEY (place_id) REFERENCES Place(id),
    UNIQUE(user_id, place_id)
);
-- Script that creates the tables Amenity
-- Create Amenity if it does not already exist
CREATE TABLE IF NOT EXISTS Amenity (
    id CHAR(36) PRIMARY KEY,
    name VARCHAR(255) UNIQUE NOT NULL
);
-- Script that creates the tables Place_Amenity
-- Create Place_Amenity if it does not already exist
CREATE TABLE IF NOT EXISTS Place_Amenity (
    place_id CHAR(36) NOT NULL,
    FOREIGN KEY (place_id) REFERENCES Place(id),
    amenity_id CHAR(36) NOT NULL,
    FOREIGN KEY (amenity_id) REFERENCES Amenity(id),
    PRIMARY KEY (place_id, amenity_id)
);
