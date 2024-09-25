# 0x0E. SQL - More Queries

## Description
This project focuses on more advanced SQL queries and database management techniques. You will learn how to manage MySQL users and their privileges, create databases and tables with constraints, and explore advanced querying techniques such as joins, unions, and subqueries. The project also dives into importing data into a MySQL database and retrieving meaningful information through complex SQL statements.

## Learning Objectives
By the end of this project, you should be able to explain the following concepts without external references:

- How to create a new MySQL user.
- How to manage privileges for a user to a database or table.
- What’s a PRIMARY KEY and FOREIGN KEY.
- How to use constraints like NOT NULL and UNIQUE.
- How to retrieve data from multiple tables in one query.
- What are subqueries and how to use them.
- Different types of joins (INNER JOIN, LEFT JOIN, etc.) and how to use them.
- How to use UNION and other SQL set operations.

## Requirements
- All files are executed on Ubuntu 20.04 LTS using MySQL 8.0 (version 8.0.25).
- All SQL queries include comments describing the task.
- All SQL keywords are written in uppercase.
- Each file ends with a new line.
- The length of each file is tested using `wc`.

## Project Structure
This project is organized into multiple tasks that progressively build your understanding of advanced SQL concepts. Each task requires creating a `.sql` script to solve a particular problem.

## Files

| Filename                  | Description                                                                                         |
|---------------------------|-----------------------------------------------------------------------------------------------------|
| `0-privileges.sql`         | Lists all privileges of the MySQL users `user_0d_1` and `user_0d_2`.                                |
| `1-create_user.sql`        | Creates the MySQL server user `user_0d_1` with all privileges.                                      |
| `2-create_read_user.sql`   | Creates the database `hbtn_0d_2` and the user `user_0d_2` with SELECT privileges.                   |
| `3-force_name.sql`         | Creates the table `force_name` with a `name` column that cannot be null.                            |
| `4-never_empty.sql`        | Creates the table `id_not_null` with an `id` column that cannot be null and defaults to 1.          |
| `5-unique_id.sql`          | Creates the table `unique_id` with a unique `id` column.                                            |
| `6-states.sql`             | Creates the database `hbtn_0d_usa` and the table `states` with a primary key `id`.                  |
| `7-cities.sql`             | Creates the table `cities` with a `state_id` as a foreign key referencing the `states` table.       |
| `8-cities_of_california_subquery.sql` | Lists all the cities in California, sorted by `cities.id`, without using JOIN.            |
| `9-cities_by_state_join.sql` | Lists all cities along with their states, sorted by `cities.id`.                                   |
| `10-genre_id_by_show.sql`  | Lists all shows with at least one genre linked.                                                     |
| `11-genre_id_all_shows.sql`| Lists all shows with their genres, or NULL if no genre is linked.                                   |
| `12-no_genre.sql`          | Lists all shows without any genre linked.                                                           |
| `13-count_shows_by_genre.sql` | Displays the number of shows linked to each genre.                                               |
| `14-my_genres.sql`         | Lists all genres of the show "Dexter".                                                              |
| `15-comedy_only.sql`       | Lists all Comedy shows.                                                                             |
| `16-shows_by_genre.sql`    | Lists all shows and their genres, or NULL if no genre is linked.                                    |
| `100-not_my_genres.sql`    | Lists all genres not linked to the show "Dexter".                                                   |
| `101-not_a_comedy.sql`     | Lists all shows without the Comedy genre.                                                           |
| `102-rating_shows.sql`     | Lists all shows from `hbtn_0d_tvshows_rate` by their rating.                                        |
| `103-rating_genres.sql`    | Lists all genres in `hbtn_0d_tvshows_rate` by their rating.                                         |

## How to Use

1. Install MySQL 8.0 on Ubuntu 20.04 LTS:
    ```bash
    sudo apt update
    sudo apt install mysql-server
    ```
    Check the version:
    ```bash
    mysql --version
    ```

2. Start the MySQL service:
    ```bash
    sudo service mysql start
    ```

3. Import databases or run scripts by executing:
    ```bash
    mysql -hlocalhost -uroot -p < script.sql
    ```

4. Make sure to replace `root` with the correct user and adjust the database names where needed.


