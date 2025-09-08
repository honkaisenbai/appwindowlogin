CREATE TABLE users (
    id INT PRIMARY KEY AUTOINCREMENT,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(255) NOT NULL,
    gmail VARCHAR(100) NOT NULL,
    phone VARCHAR(20) LENGTH(phone) = 10
);

-- Example insert
INSERT INTO users (username, password, gmail, phone) VALUES
('john_doe', 'password123', 'john.doe@gmail.com', '1234567890'),
('jane_smith', 'securepass', 'jane.smith@gmail.com', '0987654321');

ROLLBACK