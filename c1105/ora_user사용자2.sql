-- join
-- inner join - equi join, non-equi-join, self join, outer join

-- employees 사원번호 - employees, 사원명, 부서번호, 부서명, -departments 을 출력하시오.
-- 현대식 문법
SELECT a.employee_id, a.emp_name, a.department_id, b.department_name
FROM employees a
INNER JOIN departments b
ON a.department_id = b.department_id;

select * from stu_grade;
select * from students;

-- 두테이블간 동일한 컬럼없이 데이터를 가져오는 방법 : non-equi join
-- avg값을 가지고 다른 컬럼을 다른 테이블에서 가져와 출력
select name,avg,grade from students,stu_grade
where avg between loavg and hiavg;

-- 현대식 문법
SELECT s.name, s.avg, g.grade
FROM students s
CROSS JOIN stu_grade g
WHERE s.avg BETWEEN g.loavg AND g.hiavg;



select employee_id,emp_name,manager_id from employees;

-- self join 자신의 테이블을 2번 호출
--

select a.employee_id,a.emp_name,a.manager_id,b.emp_name
from employees a, employees b
where a.manager_id = b.employee_id;

-- 현대식 문법
SELECT a.employee_id, a.emp_name, a.manager_id, b.emp_name AS manager_name
FROM employees a
INNER JOIN employees b ON a.manager_id = b.employee_id;

select * from stu;

-- 컬럼 삭제
alter table stu drop column result;

-- 컬럼 추가
alter table stu add result varchar2(10);

-- avg의 컬럼을 가지고, stu_grade 활용해서 이 값을 result에 입력하시오.
SELECT s.name, s.avg, g.grade
FROM stu s
JOIN stu_grade g
ON s.avg BETWEEN g.loavg AND g.hiavg;

UPDATE stu s
SET s.result = (
    SELECT g.grade
    FROM stu_grade g
    WHERE s.avg BETWEEN g.loavg AND g.hiavg
)
WHERE EXISTS (
    SELECT 1
    FROM stu_grade g
    WHERE s.avg BETWEEN g.loavg AND g.hiavg
);

select * from stu;

select s.no 번호,s.name 이름,s.avg 평균 ,s.result 등급
from stu s
join stu_grade g
on s.avg between g.loavg and g.hiavg
order by s.avg desc;


-- self join
SELECT e1.employee_id AS 직원_ID,
       e1.emp_name AS 직원_이름,
       e1.salary AS 직원_연봉,
       e2.employee_id AS 매니저_ID,
       e2.emp_name AS 매니저_이름,
       e2.salary AS 매니저_연봉
FROM employees e1
JOIN employees e2
ON e1.manager_id = e2.employee_id
AND e1.salary BETWEEN (e2.salary * 0.8) AND (e2.salary * 1.2)
ORDER BY e1.salary DESC;

select * from stu;
update stu set rank=0;

select no, name, rank() over(order by avg desc) as ranks from stu;

-- rank()의 결과값을 rank 컬럼에 모두 입력하시오.

MERGE INTO stu s
USING (
    SELECT no, rank() OVER (ORDER BY avg DESC) AS ranks
    FROM stu
) Ranked
ON (s.no = Ranked.no)
WHEN MATCHED THEN
    UPDATE SET s.rank = Ranked.ranks;
    
select employee_id, emp_name, manager_id from employees;

select count(manager_id) from employees
where manager_id is not null;

select manager_id from employees;

select nvl(manager_id,0) from employees;
select nvl(to_char(manager_id),'CEO') from employees;

-- self join manager_id, 매니저의 이름을 출력하시오.

SELECT e1.employee_id AS 직원_ID,
       e1.emp_name AS 직원_이름,
       e2.employee_id AS 매니저_ID,
       e2.emp_name AS 매니저_이름
FROM employees e1
JOIN employees e2
ON e1.manager_id = e2.employee_id;


SELECT e.employee_id, e.emp_name, d.department_name
FROM employees e
LEFT JOIN departments d ON e.department_id = d.department_id;

-- 사원번호, 사원명, 부서번호, 부서명
select e.employee_id,e.emp_name,e.department_id,d.department_name
from employees e
left join departments d
on e.department_id = d.department_id;

SELECT d.department_id, d.department_name, e.employee_id, e.emp_name
FROM departments d
LEFT JOIN employees e ON d.department_id = e.department_id;

select * from departments;
select d.department_name, e.department_id, e.emp_name
from employees e
left join departments d
on d.department_id = e.department_id
where d.department_id is null;

-- ansi cross join
select a.department_id, b.department_name
from employees a
inner join departments b
on a.department_id = b.department_id;

-- 실무에서는 잘 사용 안함
select department_id, department_name
from employees
inner join departments
using (department_id);

-- ansi join: natural join 거의 사용되지 않음
select department_id, department_name
from employees natural join departments;

-- 거의 사용되지 않음. natural join 사용하지 말 것
select *
from employees natural inner join departments;

-- left outer join 
SELECT *
FROM employees
LEFT JOIN departments
ON employees.department_id = departments.department_id;

-- right outer join
select *
from employees e
right join departments d
on e.department_id = d.department_id;

-- full outer join
select *
from employees e
full outer join departments d
on e.department_id = d.department_id;

-- 부서가 없는 직원이거나, 직원이 없는 부서거나
select *
from employees e
full outer join departments d
on e.department_id = d.department_id
where e.emp_name is null or d.department_name is null;

-- 직원 수가 0명인 부서와 해당 부서명 출력하기
select d.department_id, d.department_name
from employees e
right join departments d
on e.department_id = d.department_id
where e.emp_name is null;

-- union
select * from students
where total >= 250
union
select * from students
where name like '%a%';

-- union
select employee_id, emp_name from employees;
select no, name from students;

select employee_id,emp_name from employees
union
select no,name from students;

-- 50인 사원 부서번호, 부서이름
-- 부서번호, 부서이름

select * from employees;



select department_id, department_name from departments;

select distinct department_id from employees;

select * from member;
 
select * from board;


create table board2 (
	bno number(4),
	btitle VARCHAR2(50),
	bcontent VARCHAR2(50),
	id VARCHAR2(50),
	bgroup number(4),
	bstep number(4),
	bindent number(4),
	bhit number(4),
	bfile VARCHAR2(50)
);

insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (1, 'Netaji Subhash Chandra Bose International Airport', 'Staff Scientist', 'aaa', 1, 0, 0, 0, 'Dimanche');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (2, 'Pala Airport', 'Human Resources Assistant III', 'bbb', 2, 0, 0, 0, 'Doleman');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (3, 'Barriles Airport', 'Marketing Assistant', 'ccc', 3, 0, 0, 0, 'Tatum');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (4, 'Kristiansund Airport (Kvernberget)', 'Senior Editor', 'ddd', 4, 0, 0, 0, 'Himpson');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (5, 'Hawke''s Bay Airport', 'Statistician III', 'eee', 5, 0, 0, 0, 'Fennelly');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (6, 'Bozoum Airport', 'Web Designer I', 'abc', 6, 0, 0, 0, 'Velde');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (7, 'Baitadi Airport', 'Engineer II', 'Faustina', 7, 0, 0, 0, 'Scimone');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (8, 'Rurenabaque Airport', 'Safety Technician I', 'Gilly', 8, 0, 0, 0, 'Greystoke');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (9, 'Industrial Airpark', 'Editor', 'Godart', 9, 0, 0, 0, 'Springthorpe');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (10, 'Barreirinhas Airport', 'Account Coordinator', 'Cole', 10, 0, 0, 0, 'Jerram');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (11, 'Toledo Airport', 'Safety Technician IV', 'Mannie', 11, 0, 0, 0, 'Longden');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (12, 'Tamale Airport', 'Occupational Therapist', 'Sofie', 12, 0, 0, 0, 'Cheeld');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (13, 'Budapest Liszt Ferenc International Airport', 'Dental Hygienist', 'Danyette', 13, 0, 0, 0, 'Grigolli');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (14, 'Juan Pablo Pérez Alfonso Airport', 'Systems Administrator I', 'Irv', 14, 0, 0, 0, 'Lyster');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (15, 'Kangaatsiaq Heliport', 'Product Engineer', 'Maggi', 15, 0, 0, 0, 'O''Ferris');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (16, 'Dabo Airport', 'Environmental Specialist', 'Theo', 16, 0, 0, 0, 'Sothcott');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (17, 'Rivers Airport', 'Mechanical Systems Engineer', 'Svend', 17, 0, 0, 0, 'Lidgley');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (18, 'Fitzroy Crossing Airport', 'Project Manager', 'Harp', 18, 0, 0, 0, 'Wallworke');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (19, 'Minnipa Airport', 'Environmental Specialist', 'Dorelle', 19, 0, 0, 0, 'Farmar');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (20, 'Arboletes Airport', 'General Manager', 'Caresse', 20, 0, 0, 0, 'Camacke');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (21, 'Yakutat Airport', 'Teacher', 'Bibby', 21, 0, 0, 0, 'Gai');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (22, 'Zahedan International Airport', 'Actuary', 'Viv', 22, 0, 0, 0, 'Penrice');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (23, 'Xingyi Airport', 'VP Marketing', 'Gris', 23, 0, 0, 0, 'Liddicoat');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (24, 'La Chorrera Airport', 'Assistant Manager', 'Rouvin', 24, 0, 0, 0, 'Brassington');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (25, 'Peretola Airport', 'Research Assistant III', 'Thane', 25, 0, 0, 0, 'Pittel');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (26, 'Flughafen München-Riem', 'Account Representative II', 'Dore', 26, 0, 0, 0, 'Newcom');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (27, 'Merritt Island Airport', 'Analyst Programmer', 'Jacobo', 27, 0, 0, 0, 'Bragginton');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (28, 'Anaco Airport', 'Electrical Engineer', 'Stanislaus', 28, 0, 0, 0, 'Eppson');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (29, 'Barinas Airport', 'Operator', 'Ariana', 29, 0, 0, 0, 'Duchart');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (30, 'Araxos Airport', 'Senior Editor', 'Delphinia', 30, 0, 0, 0, 'Wheway');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (31, 'Kamloops Airport', 'Research Associate', 'Gannon', 31, 0, 0, 0, 'Matches');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (32, 'Tzaneen Airport', 'Quality Control Specialist', 'Dorree', 32, 0, 0, 0, 'Frondt');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (33, 'Mayajigua Airport', 'VP Accounting', 'Kellia', 33, 0, 0, 0, 'Miettinen');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (34, 'Kadugli Airport', 'Help Desk Technician', 'Magdaia', 34, 0, 0, 0, 'MacTeague');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (35, 'Miyazaki Airport', 'Software Consultant', 'Brenda', 35, 0, 0, 0, 'Pentony');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (36, 'Escuela Mariscal Sucre Airport', 'Data Coordinator', 'Arman', 36, 0, 0, 0, 'Jarvie');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (37, 'Arua Airport', 'Research Associate', 'Alexandro', 37, 0, 0, 0, 'Lecointe');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (38, 'Lagunillas Airport', 'Account Representative I', 'Christye', 38, 0, 0, 0, 'Smitham');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (39, 'Buzzards Point Seaplane Base', 'Operator', 'Nedda', 39, 0, 0, 0, 'Cardoe');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (40, 'Paraparaumu Airport', 'Assistant Professor', 'Linnet', 40, 0, 0, 0, 'Swane');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (41, 'Wudalianchi Dedu Airport', 'Analog Circuit Design manager', 'Guenna', 41, 0, 0, 0, 'Pillinger');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (42, 'D. Casimiro Szlapelis Airport', 'Payment Adjustment Coordinator', 'Ozzy', 42, 0, 0, 0, 'Ogbourne');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (43, 'Pondicherry Airport', 'Media Manager III', 'Lev', 43, 0, 0, 0, 'Marritt');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (44, 'Tonghua Sanyuanpu Airport', 'Statistician IV', 'Franni', 44, 0, 0, 0, 'Saldler');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (45, 'Fort Albany Airport', 'Professor', 'Katerina', 45, 0, 0, 0, 'Golland');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (46, 'Žilina Airport', 'Accounting Assistant I', 'Whittaker', 46, 0, 0, 0, 'Owbridge');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (47, 'Soekarno-Hatta International Airport', 'Project Manager', 'Rosemaria', 47, 0, 0, 0, 'Pohl');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (48, 'Sebba Airport', 'Actuary', 'Keelby', 48, 0, 0, 0, 'Palatini');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (49, 'Rundu Airport', 'Health Coach I', 'Bonni', 49, 0, 0, 0, 'Boniface');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (50, 'London Stansted Airport', 'Paralegal', 'Martin', 50, 0, 0, 0, 'Pentlow');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (51, 'Rustaq Airport', 'Chemical Engineer', 'Karlen', 51, 0, 0, 0, 'Dell Casa');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (52, 'Ratnagiri Airport', 'Pharmacist', 'Constantin', 52, 0, 0, 0, 'Trees');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (53, 'Cooinda Airport', 'Database Administrator III', 'Lauretta', 53, 0, 0, 0, 'Hubball');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (54, 'Lisala Airport', 'Project Manager', 'Merrili', 54, 0, 0, 0, 'Cady');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (55, 'Accomack County Airport', 'Geologist II', 'Honor', 55, 0, 0, 0, 'Amber');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (56, 'Municipal de Linares Airport', 'Research Nurse', 'Ashby', 56, 0, 0, 0, 'Larmuth');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (57, 'Wrangell Airport', 'Professor', 'Sydel', 57, 0, 0, 0, 'Tuer');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (58, 'Querétaro Intercontinental Airport', 'Senior Developer', 'Paige', 58, 0, 0, 0, 'Kann');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (59, 'Ruhengeri Airport', 'Food Chemist', 'Mathe', 59, 0, 0, 0, 'Mapston');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (60, 'Berbérati Airport', 'Research Associate', 'Mandi', 60, 0, 0, 0, 'Lacroutz');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (61, 'Aratika Nord Airport', 'Web Developer IV', 'Dinny', 61, 0, 0, 0, 'Rolley');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (62, 'Kuusamo Airport', 'Legal Assistant', 'Brody', 62, 0, 0, 0, 'Charrett');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (63, 'Vila Bela da Santíssima Trindade Airport', 'Programmer Analyst IV', 'Berget', 63, 0, 0, 0, 'MacComiskey');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (64, 'Lai Airport', 'Financial Advisor', 'Suzy', 64, 0, 0, 0, 'Pellman');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (65, 'Maintirano Airport', 'Paralegal', 'Creight', 65, 0, 0, 0, 'D''Alesio');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (66, 'Curitibanos Airport', 'Staff Accountant IV', 'Bale', 66, 0, 0, 0, 'Jessop');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (67, 'Huahine-Fare Airport', 'Senior Editor', 'Melinda', 67, 0, 0, 0, 'Baskerfield');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (68, 'Solano Airport', 'Tax Accountant', 'Nowell', 68, 0, 0, 0, 'Wrightim');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (69, 'Nikunau Airport', 'Legal Assistant', 'Hi', 69, 0, 0, 0, 'Clamp');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (70, 'Merced Regional Macready Field', 'Senior Editor', 'Kelbee', 70, 0, 0, 0, 'Shervil');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (71, 'Humberto Delgado Airport (Lisbon Portela Airport)', 'Dental Hygienist', 'Sharai', 71, 0, 0, 0, 'McAteer');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (72, 'La Grande Rivière Airport', 'Editor', 'Oralie', 72, 0, 0, 0, 'Klemz');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (73, 'Sidney Municipal-Lloyd W Carr Field', 'Recruiting Manager', 'Gabbie', 73, 0, 0, 0, 'Bunten');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (74, 'Pathankot Airport', 'Safety Technician III', 'Kyle', 74, 0, 0, 0, 'Springell');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (75, 'Half Moon Bay Airport', 'Project Manager', 'Gamaliel', 75, 0, 0, 0, 'Emms');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (76, 'Lübeck Blankensee Airport', 'Automation Specialist I', 'Wilbert', 76, 0, 0, 0, 'Morgans');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (77, 'Purdue University Airport', 'Data Coordinator', 'Xenia', 77, 0, 0, 0, 'Boxe');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (78, 'Sui Airport', 'Registered Nurse', 'Gertrudis', 78, 0, 0, 0, 'Durbridge');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (79, 'Talkeetna Airport', 'VP Quality Control', 'Tamra', 79, 0, 0, 0, 'Mowsdale');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (80, 'Chacalluta Airport', 'Safety Technician IV', 'Blair', 80, 0, 0, 0, 'Thurlow');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (81, 'N''Délé Airport', 'Engineer III', 'Heidie', 81, 0, 0, 0, 'Maw');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (82, 'Nanuque Airport', 'Database Administrator IV', 'Fanni', 82, 0, 0, 0, 'Bessell');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (83, 'Nipa Airport', 'Environmental Specialist', 'Arlan', 83, 0, 0, 0, 'Clitheroe');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (84, 'Soldotna Airport', 'Assistant Media Planner', 'Gerta', 84, 0, 0, 0, 'Merriton');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (85, 'Proserpine Whitsunday Coast Airport', 'Clinical Specialist', 'Maryellen', 85, 0, 0, 0, 'Ouldcott');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (86, 'Dubai International Airport', 'General Manager', 'Travis', 86, 0, 0, 0, 'Bogace');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (87, 'Dalton Municipal Airport', 'Human Resources Assistant I', 'Jeanie', 87, 0, 0, 0, 'Pitson');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (88, 'Salem Airport', 'Help Desk Technician', 'Nanete', 88, 0, 0, 0, 'Braxton');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (89, 'Warren "Bud" Woods Palmer Municipal Airport', 'Food Chemist', 'Claudia', 89, 0, 0, 0, 'Bernardotte');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (90, 'Palm Beach International Airport', 'Financial Analyst', 'Allard', 90, 0, 0, 0, 'Fillgate');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (91, 'Marinduque Airport', 'Mechanical Systems Engineer', 'Lars', 91, 0, 0, 0, 'Timoney');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (92, 'Cape Cod Coast Guard Air Station', 'Product Engineer', 'Dante', 92, 0, 0, 0, 'Kaubisch');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (93, 'Capitán Av. German Quiroga G. Airport', 'VP Sales', 'Kory', 93, 0, 0, 0, 'Quail');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (94, 'Nyagan Airport', 'Food Chemist', 'Cristionna', 94, 0, 0, 0, 'Betser');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (95, 'Tynda Airport', 'Professor', 'Inessa', 95, 0, 0, 0, 'Wratten');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (96, 'Mumias Airport', 'Assistant Media Planner', 'Vally', 96, 0, 0, 0, 'Dumigan');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (97, 'Qikiqtarjuaq Airport', 'Programmer II', 'Elmer', 97, 0, 0, 0, 'Pashenkov');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (98, 'McGhee Tyson Airport', 'Project Manager', 'Leda', 98, 0, 0, 0, 'Swales');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (99, 'Awar Airport', 'Engineer II', 'Dyanna', 99, 0, 0, 0, 'Popplewell');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (100, 'Barnaul Airport', 'Software Engineer III', 'Dulsea', 100, 0, 0, 0, 'Mothersole');

select * from board2;

commit;

delete board2 where bno=11;
delete board2 where bno=12;
delete board2 where bno=16;
delete board2 where bno=21;
delete board2 where bno=22;
delete board2 where bno=25;
delete board2 where bno=29;
delete board2 where bno=35;
delete board2 where bno=38;
delete board2 where bno=44;
delete board2 where bno=46;
delete board2 where bno=57;
delete board2 where bno=61;
delete board2 where bno=66;
delete board2 where bno=74;
delete board2 where bno=88;
delete board2 where bno=95;
delete board2 where bno=96;
delete board2 where bno=98;


