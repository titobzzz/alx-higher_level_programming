-- If the database hbtn_0d_usa already exists, your script should not fail
-- If the table states already exists, your script should not fail

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
name VARCHAR(256) NOT NULL);
