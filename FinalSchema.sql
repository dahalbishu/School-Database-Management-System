create database school_management;

use school_management;

create user teacher identified by 'teacher';
create user student identified by 'student';
select user from mysql.user;
create table entrance_form (
entrance_roll varchar(20) primary key,
fname varchar(30) NOT NULL,
lname varchar(30) not null,
dob date NOT NULL, /* Format '2057-9-11' */
gender set("M", "F", "O"), /* M,F or O */
address varchar(50) NOT NULL,
email varchar(50) NOT NULL,
faculty varchar(20) NOT NULL,
catagory varchar(1) NOT NULL,
gpa float Not NULL,
guardian_name varchar(50) NOT NULL,
guardian_number bigint(10) NOT NULL,
statuscheck set("Approved", "Rejected", "Waiting"), 
check (gpa between 0 and 4)
);


create table entrance_marks(
entrance_roll varchar(20) primary key,
marks int not null default 0,
check(marks between 0 and 100),
constraint temp_roll foreign key(entrance_roll) references entrance_form(entrance_roll)
);


create table registration(
s_roll varchar(20) primary key default "xxxxxx",
fname varchar(30) NOT NULL,
lname varchar(30) NOT NULL,
dob date, /* Format '2057-9-11' */
gender set("M", "F", "O"), /* M,F or O */
address varchar(50) NOT NULL,
email varchar(50) NOT NULL,
faculty varchar(20) NOT NULL,
catagory varchar(1) NOT NULL,
gpa float NOt NULL,
guardian_name varchar(50) NOT NULL,
guardian_number bigint(10) NOT NULL,
class int default 11,
section varchar(2) not null default "x"
);


create table Past_Student(
student_id varchar(20) primary key, 
fname varchar(30) NOT NULL,
lname varchar(30) NOT NULL,
dob date, /* Format '2057-9-11' */
gender set("M", "F", "O"), /* M,F or O */
address varchar(50) NOT NULL,
email varchar(50) NOT NULL,
faculty varchar(20) NOT NULL,
catagory varchar(1) NOT NULL,
aggregate_gpa float,
guardian_name varchar(50) NOT NULL,
guardian_number bigint(10) NOT NULL,
remarks_further_study varchar(50),
statuscheck set("Drop Out", "Passed Out", "Still Back") default "Passed out"
);


create table Teacher_details(
teacher_id varchar(30) primary key,
fname varchar(30) not null,
lname varchar(30) not null,
contact_number bigint not null,
email varchar(50) not null,
department varchar(50) not null
);


create table section_teacher(
teacher_id varchar(30),
class int not null,
faculty varchar(15) not null,
assigned_section varchar(2) not null,
foreign key(teacher_id) references Teacher_details(teacher_id)
);





create table security_table(
user_id varchar(20) primary key,
passwordhash varbinary(64) NOT NULL default "xxxxxxxx"
);


-- View is for only admins to see the real password
create view passwd_table as
select user_id, cast(passwordhash as char(8)) as normalized_password from security_table;

insert into security_table values(1000, "admin@12");


create table message_table(
message_id int primary key auto_increment,
sender_id varchar(20) not null,
receiver_id varchar(20) not null,
message_send_datetime datetime not null default now(),
message varchar(2000) not null,
msg_status varchar(1) not null default 'U',
foreign key(sender_id) references security_table(user_id),
foreign key(receiver_id) references security_table(user_id)
);



create table Catagory_Selection(
catagory varchar(1) primary key,
class int,
faculty varchar(20) NOT NULL,
subject1 varchar(20) NOT NULL,
subject2 varchar(20) NOT NULL,
subject3 varchar(20) NOT NULL,
subject4 varchar(20) NOT NULL,
subject5 varchar(20) NOT NULL,
subject6 varchar(20) default NULL
);

create table technical_data
(sn int primary key auto_increment,
entrance_appear_stu int,
approved_in_entrance_stu int,
max_marks_in_entrance int,
cutoff_marks_in_entrance int,
avg_marks_in_entrance_of_approved_stu float,
avg_marks_in_entrance float,
total_msg int,
total_msg_stuTotec int,
total_msg_tecTostu int,
total_msg_adminTotec int,
total_msg_tecToadmin int,
total_msg_adminTosec int,
total_msg_stuToadmin int,
Datetime_admin_declare_end_of_acedemic_year datetime default now() 
);

create table activity_record(
sn int primary key auto_increment,
activity_by varchar(20) not null,
activity varchar(255) not null,
activity_status varchar(15) not null,
activity_on datetime default now() 
);


create table Student_update_rec(
sn int primary key auto_increment,
student_id varchar(20) not null,
action_ varchar(10) not null, 
action_on varchar(20) not null,
address varchar(50) NOT NULL,
email varchar(50) NOT NULL,
catagory varchar(1),
aggregate_gpa float,
guardian_name varchar(50) NOT NULL,
guardian_number bigint(10) NOT NULL,
remarks_further_study varchar(50),
action_date datetime not null default now()
);


create table Teacher_details_update_rec(
sn int primary key auto_increment,
teacher_id varchar(30),
action_ varchar(10) not null,
contact_number bigint not null,
email varchar(50) not null,
action_date datetime not null default now()
);

create table marksheet_backup
(
year_of_exam int not null,
student_roll_number  varchar(20) not null,
terminal varchar(1) not null,
total_marks_obtained int not null,
percentage  decimal(21,4) not null,
remarks varchar(4) not null,
primary key (year_of_exam,student_roll_number,terminal)
);

create table old_teacher_details(
teacher_id varchar(30) primary key,
fname varchar(30) not null,
lname varchar(30) not null,
contact_number bigint not null,
email varchar(50) not null,
department varchar(50) not null
);


create view section_teacher_details as 
( select * from (select teacher_id,concat(fname,' ',lname) 
as full_name from teacher_details) as td natural join section_teacher);



delimiter $$
create function fn_gettotalpass(getyear_of_exam int,getterminal varchar(1),getfaculty varchar(20))
returns integer Deterministic
begin
Declare totalpass integer;
select count(*) into totalpass from marksheet_backup inner join 
(select s_roll roll,faculty from registration union select student_id roll,faculty from past_student)  D
 on  D.roll = marksheet_backup.student_roll_number
where remarks = 'pass' and year_of_exam =getyear_of_exam and terminal = getterminal and faculty = getfaculty;
return totalpass;
end;
$$
delimiter ;

create view  marksheet_backup_analysis as
select year_of_exam,faculty,case  when terminal = '1'   then 'First' 
when terminal = '2'   then 'Second'
when terminal = '3'   then 'Third'
when terminal = 'F'   then 'Final'
 end as terminal,max(percentage) as max_percent,avg(percentage) as avg_percent, count(*) as total_student,fn_gettotalpass(year_of_exam,terminal,faculty) as total_passed_student from 
marksheet_backup inner join 
(select s_roll roll,faculty from registration union select student_id roll,faculty from past_student)  D
 on  D.roll = marksheet_backup.student_roll_number 
 group by year_of_exam,terminal,faculty;







delimiter $$

create trigger before_update_in_registration
before update on registration
for each row 
begin 
insert into  student_update_rec
set 
student_id = old.s_roll,
action_ = 'update',
action_on = 'registration',
address = old.address,
email = old.email,
catagory = old.catagory,
guardian_name=old.guardian_name,
guardian_number  = old.guardian_number,
action_date = now();
end $$
delimiter ;


delimiter $$

create trigger before_update_in_past_student
before update  on past_student
for each row 
begin 
insert into  student_update_rec
set 
student_id = old.student_id ,
action_ = 'update',
action_on = 'past_student',
address = old.address,
email = old.email,
aggregate_gpa = old.aggregate_gpa,
guardian_name=old.guardian_name,
guardian_number  = old.guardian_number,
remarks_further_study = old.remarks_further_study,
action_date = now();
end $$
delimiter ;







delimiter $$

create trigger before_update_in_teacher_details
before update on teacher_details
for each row 
begin 
insert into  teacher_details_update_rec
set 
teacher_id = old.teacher_id ,
action_ = 'update',
contact_number  = old.contact_number,
email = old.email,
action_date = now();
end $$
delimiter ;



-- Permanent Grants For USERS 
grant select on school_management.registration TO 'student';
grant select on school_management.teacher_details TO 'student';
grant select,insert on school_management.entrance_form TO 'student';
grant insert,update,select on school_management.message_table TO 'student';
grant update,select on school_management.security_table TO 'student';
grant select on school_management.catagory_selection TO 'student';




grant select on school_management.registration TO 'teacher';
grant select on school_management.teacher_details TO 'teacher';
grant select on school_management.catagory_selection TO 'teacher';
grant insert,update,select on school_management.message_table TO 'teacher';
grant update,select on school_management.security_table TO 'teacher';