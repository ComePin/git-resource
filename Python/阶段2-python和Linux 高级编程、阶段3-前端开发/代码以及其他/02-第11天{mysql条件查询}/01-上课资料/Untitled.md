--登录数据库

--显示当前时间

--登出(退出)数据库

--查看所有数据库

--创建数据库

--使用数据库

--查看当前使用的数据库

--删除数据库-慎重

--查看当前数据库中所有表

--创建表

--修改表-添加birthday字段

--修改表-修改字段类型

--修改表-修改字段名和字段类型

--修改表-删除birthday字段

--查看表结构

--查看创表SQL语句

--查看创库SQL语句

--删除表

--查询所有列数据

--查询指定列数据

--添加数据--全列插入

主键列表插入数据的时候可以指定: 0、default、null
这里的default表示使用该字段默认值

--添加数据--部分列插入

insert into students values(0, '黄蓉', 28, '女'),(0,'黄老邪',50,default); 

--添加数据--部分列多行插入
insert into students(name, age) values('杨过', 20),('周伯通',55);

--修改数据
update students set age=18, gender = '女' where id = 3;

--删除数据
delete from students where id = 8;

--删除数据可以使用逻辑删除，添加一个标识字段

这里删除数据其实修改标识字段

--as关键字，用户给表的字段和表设置别名

提示: as 关键字可以省略，也表示设置别名

--distinct关键字， 用于去除重复的数据行

--查询编号大于3的学生


--查询编号不大于4的学生


--查询姓名不是“黄蓉”的学生

--查询没被删除的学生

--查询编号大于3的女同学

--查询编号小于4或没被删除的学生
--查询年龄不在10岁到15岁之间的学生

--查询姓黄的学生
--查询姓黄并且“名”是一个字的学生
%: 表示任意多个字符
_: 表示任意一个字符


--查询姓黄或叫靖的学生

--查询编号为3至8的学生

--查询编号不是3至8的男生

--查询编号是3、5、7的学生

--查询编号不是3、5、7的学生

--查询没有填写身高的学生

--查询填写身高的学生

--查询未删除男生信息，按学号降序
select * from students where is_del = 0 and gender = '男' order by id desc;

--显示所有的学生信息，先按照年龄从大-->小排序，当年龄相同时 按照身高从高-->矮排序
select * from students order by age desc, height desc;
默认是asc 不用指定。


--查询前3行男生信息
select * from students where gender='男' limit 0, 3;
简写方式，第一个参数是开始行索引，默认是0可以不指定， 第二个参数是查询条数
select * from students where gender='男' limit 3;

--查询学生表，获取第n页数据的SQL语句
select * from students limit (n-1) * m, m;





















