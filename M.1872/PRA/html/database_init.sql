CREATE DATABASE news;
USE news;
GRANT all privileges ON news.* TO user@localhost IDENTIFIED BY 'password';
flush privileges;
CREATE TABLE Users(Email VARCHAR(100) NOT NULL, Name VARCHAR (100), Password VARCHAR (100), AccountId INT,  PRIMARY KEY (Email));
CREATE TABLE News(Id INT NOT NULL, Title VARCHAR(100), Body TEXT, Datetime TIMESTAMP, PRIMARY KEY (Id));
INSERT INTO Users(Email, Password) VALUES('admin@admin.com', 'D917744DC087BDC494E961966E5EECE7');
INSERT INTO News(Id, Title, Body, Datetime) VALUES(3,'Boletin informativo','Buenos dias, actualizamos', '2014-10-05 12:12:12');