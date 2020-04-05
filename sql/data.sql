-- utworzenie db 
create database tm_db;
-- utworzenie użytkownika 
create user 'tm_user'@'localhost' identified by 'qwe123';
-- przypisanie uprawnień dla użytkownika dla bazy tm_db
-- SELECT, INSERT, DELETE, UPDATE -> DML
grant SELECT, INSERT, DELETE, UPDATE on tm_db.* to 'tm_user'@'localhost';

-- struktura tabel
use tm_db;
create table user(
	user_id int primary key auto_increment,
    name varchar(255) not null,
    lastname varchar(255) not null,
    email varchar(255) not null,
    password varchar(255) not null,
    registraton_date datetime default now(),
	enable bool default 1
);
create table task(
	task_id int primary key auto_increment,
    task_name varchar(255) not null,
    task_description text not null,
    task_category enum('SQL', 'Git', 'Python', 'PythonLib', 'ML') not null,
    user_id int,
    foreign key (user_id) references user (user_id)
);
create table subtask(
	subtask_id int primary key auto_increment,
    subtask_name varchar(255) not null,
    subtask_date_start date,
    subtask_date_stop date,
    task_id int,
    foreign key (task_id) references task (task_id)
);