-- utworzenie db 
create database tm_db;
-- utworzenie użytkownika 
create user 'tm_user'@'localhost' identified by 'qwe123';
-- przypisanie uprawnień dla użytkownika dla bazy tm_db
-- SELECT, INSERT, DELETE, UPDATE -> DML
grant SELECT, INSERT, DELETE, UPDATE on tm_db.* to 'tm_user'@'localhost'; 