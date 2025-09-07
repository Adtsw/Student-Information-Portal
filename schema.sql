CREATE DATABASE IF NOT EXISTS StudentInfoPortal;
USE StudentInfoPortal;

CREATE TABLE IF NOT EXISTS Students(
    student_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    age INT NOT NULL,
    course VARCHAR(50) NOT NULL,
    email VARCHAR(50) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS Users(
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    role ENUM('admin', 'viewer') NOT NULL DEFAULT 'viewer'
);

-- CREATE INDEX idx_studet_name ON Students(name);
-- CREATE INDEX idx_user_username ON Users(username);