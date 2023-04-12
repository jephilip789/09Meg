Introduction
Online booking for airline tickets has been made possible through the SMJ Airline reservation system. The system offers a user-friendly interface that enables users to select their trip type (one-way or return), pick departure and return dates, specify the number of travelers, and calculate the total cost based on that number. Together with entering personal data like their first and last names and dates of birth, users can also make payments online with a credit or debit card. The system also stores all of the data entered by users in a MySQL database for the purpose of maintaining records and generating reports. For managing reservation data, the system offers the fundamental CRUD (Create, Read, Update, and Delete) functions of data entry, data retrieval, data update, and data deletion. In order to guarantee data accuracy and consistency, the system additionally includes validation and integrity checks. Overall, the SMJ Airline reservation system strives to offer users a simple and quick way to purchase airline tickets online while upholding the confidentiality and integrity of their personal information.
CREATE TABLE `reservations` (
  `id` int NOT NULL AUTO_INCREMENT,
  `trip_type` enum('one_way','return') DEFAULT NULL,
  `departure_date` date DEFAULT NULL,
  `return_date` date DEFAULT NULL,
  `num_travelers` int DEFAULT NULL,
  `total_amount` decimal(10,2) DEFAULT NULL,
  `first_name` varchar(50) DEFAULT NULL,
  `last_name` varchar(50) DEFAULT NULL,
  `date_of_birth` date DEFAULT NULL,
  `payment_card_number` varchar(16) DEFAULT NULL,
  `reservation_status` enum('success','pending','failed') DEFAULT NULL,
  PRIMARY KEY (`id`)
  The above code is showing the creation of the database which has been implemented in the MySQL Workbench. This is the very first step of the project first the database needs to create and the table and the rest of the GUI need to be implemented later.
  The above  represents an SQL query to create a table named “reservations” in a MySQL database. The table has several columns, including “id” which is an auto-incrementing primary key, “trip_type” which has “one_way” or “return”, values. “departure_date” and “return_date” which are of DATE data type. Besides this, all the entity has been created have unique IDs on the database.
