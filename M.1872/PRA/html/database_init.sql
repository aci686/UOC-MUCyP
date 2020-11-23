CREATE DATABASE news;
USE news;
GRANT all privileges ON news.* TO user@localhost IDENTIFIED BY 'password';
flush privileges;
CREATE TABLE Users (Email VARCHAR (100) NOT NULL, Name VARCHAR (100), Password VARCHAR (100), AccountId INT,  PRIMARY KEY (Email));
CREATE TABLE News (Id INT NOT NULL, Title VARCHAR (100), Body TEXT, Datetime TIMESTAMP, PRIMARY KEY (Id));
INSERT INTO Users (Email, Password) VALUES ('admin@admin.com', 'D917744DC087BDC494E961966E5EECE7');
INSERT INTO News (Id, Title, Body, Datetime) VALUES (3, 'Boletin informativo', 'Buenos días, actualizamos la información del evento. Los premios de los torneos y concuersos de NetWired! están actualizados, cada uno en su respectiva página. FutureWorks comunicará próximamente los premios de sus actividades. Asimismo, hemos habilitado en la intranet la inscripción en todaslas actividades. El horario de las actividades del eventio está disponible en la intranet. Durante el transcurso de NetWired pueden suceder imprevistos que nos haga modificarlo.', '2014-10-05 12:12:12');