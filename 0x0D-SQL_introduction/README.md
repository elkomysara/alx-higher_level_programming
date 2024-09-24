# SQL - Introduction

This project introduces the basics of SQL and MySQL, covering core concepts and functionalities such as database creation, manipulation, querying, and handling data. The project includes practical exercises and scripts to perform various SQL operations.

## Concepts

For this project, we explore the following concepts:
- **Databases**: Structure and storage of data in relational databases.
- **SQL**: Structured Query Language used to manage and manipulate relational databases.

## Learning Objectives

By the end of this project, you will be able to:
- Understand what a database and a relational database are.
- Explain the meaning of SQL and MySQL.
- Create and manage databases using MySQL.
- Understand and use DDL (Data Definition Language) and DML (Data Manipulation Language).
- Perform basic SQL operations such as `SELECT`, `INSERT`, `UPDATE`, and `DELETE`.
- Use subqueries and MySQL functions effectively.

## Requirements

- **Editor**: `vi`, `vim`, or `emacs`
- **Operating System**: Ubuntu 20.04 LTS
- **MySQL Version**: 8.0 (version 8.0.25)
- All files must end with a new line and include a comment at the top describing the task.
- SQL keywords must be in uppercase.
- You are required to include a `README.md` file at the root of the project directory.
- Files will be tested for length using `wc`.

## Resources

To help you complete this project, refer to the following resources:
- [What is Database & SQL?](https://example.com)
- [A Basic MySQL Tutorial](https://example.com)
- [Basic SQL statements: DDL and DML](https://example.com)
- [Basic queries: SQL and RA](https://example.com)
- [MySQL Cheat Sheet](https://example.com)
- [Installing MySQL on Ubuntu 20.04](https://example.com)

## Project Tasks

### 0. List Databases
Write a script that lists all databases on your MySQL server.
- **File**: `0-list_databases.sql`

### 1. Create a Database
Write a script that creates the database `hbtn_0c_0`.
- **File**: `1-create_database_if_missing.sql`

### 2. Delete a Database
Write a script that deletes the database `hbtn_0c_0`.
- **File**: `2-remove_database.sql`

### 3. List Tables
Write a script that lists all tables of a database.
- **File**: `3-list_tables.sql`

### 4. First Table
Write a script that creates a table called `first_table` in the current database.
- **File**: `4-first_table.sql`

### 5. Full Description
Write a script that prints the full description of the table `first_table`.
- **File**: `5-full_table.sql`

### 6. List All in Table
Write a script that lists all rows of the table `first_table`.
- **File**: `6-list_values.sql`

### 7. First Add
Write a script that inserts a new row into the table `first_table`.
- **File**: `7-insert_value.sql`

### 8. Count 89
Write a script that displays the number of records with `id = 89` in `first_table`.
- **File**: `8-count_89.sql`

### 9. Full Creation
Write a script that creates the table `second_table` and adds multiple rows.
- **File**: `9-full_creation.sql`

### 10. List by Best
Write a script that lists all records of `second_table`, ordered by score (descending).
- **File**: `10-top_score.sql`

### 11. Select the Best
Write a script that lists all records with a score >= 10 in `second_table`.
- **File**: `11-best_score.sql`

### 12. Cheating is Bad
Write a script that updates Bob's score to 10 without using his `id`.
- **File**: `12-no_cheating.sql`

### 13. Score Too Low
Write a script that removes all records with a score <= 5 in `second_table`.
- **File**: `13-change_class.sql`

### 14. Average
Write a script that computes the average score of all records in `second_table`.
- **File**: `14-average.sql`

### 15. Number by Score
Write a script that lists the number of records with the same score in `second_table`.
- **File**: `15-groups.sql`

### 16. Say My Name
Write a script that lists all records in `second_table` where `name` is not empty.
- **File**: `16-no_link.sql`

### Advanced Tasks
- **Go to UTF8**: Convert the `hbtn_0c_0` database to UTF8 (utf8mb4). 
  - **File**: `100-move_to_utf8.sql`
- **Temperatures**: Import data and perform temperature-based queries.
  - **Files**: `101-avg_temperatures.sql`, `102-top_city.sql`, `103-max_state.sql`

## Installation and Setup

To install MySQL on Ubuntu 20.04, use the following commands:

```bash
$ sudo apt update
$ sudo apt install mysql-server
$ mysql --version
mysql Ver 8.0.25-0ubuntu0.20.04.1 for Linux on x86_64 ((Ubuntu))
```

To connect to MySQL, use:

```bash
$ sudo mysql
```

## Usage

Each SQL script can be executed using the following format:

```bash
$ cat script_name.sql | mysql -hlocalhost -uroot -p
```

For example:

```bash
$ cat 0-list_databases.sql | mysql -hlocalhost -uroot -p
```
