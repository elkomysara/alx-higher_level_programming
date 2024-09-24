-- Create the table unique_id with id column unique and default value of 1
CREATE TABLE IF NOT EXISTS unique_id (
  id INT DEFAULT 1 UNIQUE NOT NULL,
  name VARCHAR(256)
);
