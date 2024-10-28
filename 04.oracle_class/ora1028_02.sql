--select * from employees;

--select * from customers;

--select * from products;

-- 테이블 생성
-- no,name,kore,eng,math,total,avg,rank
create table students (
no number(4),
name varchar2(20),
kor number(3),
eng number(3),
math number(3),
total number(3),
avg number(10),
rank number(4)
);

-- 테이블 삭제
--drop table students;

-- 데이터 입력, 임시 저장된 것이며, commit을 해야 저장이 됨
insert into students(no,name,kor,eng,math,total,avg,rank) values(
 1,'홍길동',100,100,99,299,(299/3),1
);

insert into students(no,name,kor,eng,math,total,avg,rank) values(
 2,'유관순',100,90,99,289,(289/3),1
);

-- 검색
select no,name,kor,eng,math,total,avg,rank from students;

-- 롤백
rollback;

-- 데이터가 사라짐
select * from students;

-- 데이터 입력, 임시 저장된 것이며, commit을 해야 저장이 됨
insert into students(no,name,kor,eng,math,total,avg,rank) values(
 1,'홍길동',100,100,99,299,(299/3),1
);

insert into students(no,name,kor,eng,math,total,avg,rank) values(
 2,'유관순',100,90,99,289,(289/3),1
);

-- 커밋
commit;

-- 롤백
rollback;

-- 커밋을 했기에 롤백을 해도 데이터가 사라지지 않음
select * from students;

select * from employees;

create table member(
 id varchar2(20) primary key,
 pw varchar2(20),
 name varchar2(20),
 phone varchar2(20)
);

-- aa 1111 홍길동 000-1111-1111
insert into member(id, pw, name, phone) values(
'aaa','1111','홍길동','010-1111-1111'
);

select * from member;

commit;

-- 데이터 모두 넣을 꺼면 굳이 variable 안적어도 됨
insert into member values(
 'bbb','1111','유관순','010-2222-2222'
);

select * from member;

-- 일부 데이터만 입력할 것이면 variable 적어야됨
insert into member(id,name) values(
'ccc','이순신'
);

-- 일부만 출력하고 싶다면 아래와 같이
select id, name from member;

-- 모두 출력할 것이면 별표
select * from member;

-- 근로자 이름과 샐러리만 확인
select emp_name,salary from employees;

select * from employees;

select * from member;

-- 데이터 수정
update member set name='홍길자' where id='aaa';

-- 아이디가 ccc인 데이터 삭제
delete member where id='ccc';

commit;

select * from member;

-- 데이터 확정
commit; -- 확정
rollback; -- 되돌리기


