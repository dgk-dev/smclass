create table mem(
id varchar2(30) primary key,
pw varchar2(30) not null,
name varchar2(30) default '무명',
age number(3) default 0,
birth date default sysdate,
gender varchar2(6) check(gender in('Male','Female')),
hobby varchar2(50) default 'game',
mdate date default sysdate
);

insert into mem values(
'aaa','1111','홍길동','24','2000/05/05','Male','golf',sysdate
);

insert into mem values(
'bbb','1111','유관순','21','2003/07/27','Female','golf',sysdate
);

insert into mem values(
'ccc','1111','이순신','23','2001/07/27','Male','golf',sysdate
);

select * from mem;

commit;

select count(*) from employees where department_id=10;

SELECT 
    COUNT(*) AS total_employees,
    employees.department_id,
    departments.department_name 
    
FROM 
    employees
JOIN 
    departments 
ON 
    employees.department_id = departments.department_id
WHERE 
    employees.department_id = 50
GROUP BY 
    departments.department_name, employees.department_id;
    
commit;



