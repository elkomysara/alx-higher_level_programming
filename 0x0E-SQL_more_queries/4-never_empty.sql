-- Create the table id_not_null with id column having a default value of 1 and NOT NULL constraint
CREATE TABLE IF NOT EXISTS id_not_null (
  id INT DEFAULT 1 NOT NULL,
  name VARCHAR(256)
);
