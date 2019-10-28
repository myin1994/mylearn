"""
作业
"""

"""



"""

"""""
学生&班级：多对一
create table class(cid int primary key auto_increment,caption varchar(20) not null);

create table student(sid int primary key auto_increment,sname  varchar(20) not null,gender enum("男","女") not null,class_id int not null,foreign key(class_id) references class(cid) on delete cascade on update cascade )

insert into class(caption) values("三年二班"),("一年三班"),("三年一班");
insert into student(sname,gender,class_id) values("钢蛋","女",1),("铁锤","女",1),("山炮","男",2);

课程&老师：多对一
create table teacher(tid int primary key auto_increment,tname varchar(20) not null);
create table course(cid int primary key auto_increment,cname  varchar(20) not null,teacher_id int not null,foreign key(teacher_id) references teacher(tid) on delete cascade on update cascade );
insert into teacher(tname) values("波多"),("苍空"),("饭岛");
insert into course(cname,teacher_id) values("生物",1),("体育",1),("物理",2);

成绩表&学生&课程：多对多
create table score(sid int unique auto_increment,student_id int not null,course_id int not null,number int unsigned not null,constraint fk_student foreign key(student_id) references student(sid)  on delete cascade on update cascade,constraint fk_course foreign key(course_id) references course(cid)  on delete cascade on update cascade,primary key(student_id,course_id) );
insert into score(student_id,course_id,number) values(1,1,60),(1,2,59),(2,2,100);

"""""
