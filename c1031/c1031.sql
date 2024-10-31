select * from member;

update member set id='abc',pw='1111',name='강규석',email='kangmumu@gmail.com' where id='aaa';

commit;

select * from member;

update member set pw='1111' where id='Towell';

select * from member;

commit;

select sysdate-1,sysdate,sysdate+1 from dual;
select hire_date,round(hire_date,'Month') from employees;
select hire_date,trunc(hire_date,'Month') from employees;

select trunc(sysdate,'month') from dual;

select add_months(trunc(sysdate,'month'),1) from dual;
select sysdate from dual;
select sysdate,add_months(trunc(sysdate,'month'),1) from dual;
-- vip요금제로 변경을하면 다음달부터 1일부터 혜택

select * from employees;
select emp_name, hire_date, add_months(trunc(hire_date,'month'),1) from employees;

-- 가입일 기준 1년이 지난
select emp_name, hire_date, add_months(hire_date,12) OneYearLater from employees;

-- 입사 달의 마지막 날짜 알아보기
select hire_date,last_day(hire_date) from employees;

-- 입사일 기준 1년 후 날짜와, 1년 후 마지막 그달의 날짜
select add_months(hire_date, 12), last_day(add_months(hire_date, 12)) from employees;

select sdate from students;

select * from students;

-- 입력일 기준 1년 후 마지막 날짜가 8/31, 9/30, 10/31인 경우
SELECT name, sdate 
FROM students 
WHERE TO_CHAR(LAST_DAY(ADD_MONTHS(sdate, 12)), 'MM/DD') IN ('09/30', '08/31', '10/31');

SELECT name, sdate
FROM students
WHERE LAST_DAY(ADD_MONTHS(sdate, 12)) IN ('2024,11/30', '2024,08/31', '2024,12/31', '2025,11/30', '2025,08/31', '2025,12/31');

SELECT name, sdate
FROM students
WHERE LAST_DAY(ADD_MONTHS(sdate, 12)) IN (
    TO_DATE('2024-09-30', 'YYYY-MM-DD'),
    TO_DATE('2024-08-31', 'YYYY-MM-DD'),
    TO_DATE('2024-10-31', 'YYYY-MM-DD'),
    TO_DATE('2025-09-30', 'YYYY-MM-DD'),
    TO_DATE('2025-08-31', 'YYYY-MM-DD'),
    TO_DATE('2025-10-31', 'YYYY-MM-DD')
);

-- sysdate는 연,월,일까지 가능함
select sysdate from dual;
select extract(year from sysdate) from dual;
select extract(month from sysdate) from dual;
select extract(day from sysdate) from dual;

-- systimestamp 년원일시분초 가능함
select systimestamp from dual;
select extract(hour from systimestamp) from dual;
select extract(minute from systimestamp) from dual;
select extract(second from systimestamp) from dual;

select sdate,extract(month from sdate) from students
where extract(month from sdate) in (8,11,12);

-- extract함수 : 년, 월, 일, 시, 분, 초 만 분리해서 비교 가능
select name, sdate, extract(month from sdate) 학생 from students
where extract(month from sdate) in (12);

select sysdate, substr(sysdate,4,2) from dual;

-- 날짜 형변환
select sysdate from dual;
select sysdate, to_char(sysdate,'yyyy-mm-dd') from dual;
select sysdate, to_char(sysdate,'yyyy-mm-dd hh24:mi:ss') from dual;
select sysdate, to_char(sysdate,'yyyy-MON-dd-DAY hh24:mi:ss') from dual;

-- date타입 -> char타입으로 변경해서 포맷.
select hire_date,to_char(hire_date,'yyyy-mm-dd hh:mi:ss') from employees;

-- 날짜 -> 문자 to_char     ## 날짜포맷
-- 문자 -> 날짜 to_date     ## 날짜 사칙연산
-- 숫자 -> 문자 to_char     ## 천단위, 숫자앞에 0 을표시, 통화표시
-- 문자 -> 숫자 to_number   ## 천단위 표시 , 천단위 삭제해서 사칙연산

select name,kor from students
where kor=70;

-- 숫자타입 -> 문자타입 변경해서 포맷 천단위 표시
select salary*1382.86*12 from employees;

-- 9는 빈공백으로 0은 그대로 표시
select to_char(salary*1382.86*12, '000,000,999') from employees;

select to_char(12,'0000') from dual;

select to_char(123456,'000000000') 영, to_char(123456,'999,999,999') 구 from dual;

commit;

create table chartable2(
no number(4),
kor number(10),
kor_char varchar2(10),
kor_mark varchar2(10)
);

drop table chartable2;

insert into chartable2 values(
3,3000000,3000000,3000000
);

insert into chartable2 values(
3,3000000,3000000,3000000
);


insert into chartable values(
1,10000,to_char(10000,'00000000'),to_char(10000,'0,000,000')
);

select * from chartable;

insert into chartable values(
1,10000,10000,10000
);

select * from chartable;
select * from chartable2;

-- 숫자형타입, 문자형(숫자)타입은 사칙연산 가능
-- 숫자형타입과 문자 천단위 표시 숫자타입은 사칙연산 불가능. ,천단위표시는 문자형 타입
-- 숫자형타입 + 문자(숫자형) 타입 = 두타입 결과값 출력됨.
select kor+kor_char from chartable2;
select kor+kor_mark from chartable2;


desc chartable;
desc chartable2;

-- 문자형 타입 -> 숫자형 타입
-- 천단위 문자형타입 -> 천단위 제외 숫자형 타입
select to_number('20,000','999,999') from dual;

select * from chartable;

select kor,to_number(kor_mark,'999,999,999') from chartable;

delete chartable;

insert into chartable values(
3,30000,'0030000','3,000,000'
);

commit;

-- 숫자형타입 이기에 사칙연산 가능
select kor+to_number(kor_mark,'999,999,999') from chartable;

-- 월급 * 커미션을 계산하시오

select * from employees;

select emp_name, salary, nvl(to_char(commission_pct),'CEO') from employees;

select emp_name, nvl(to_char(department_id),'CEO') from employees;


-- 그룹 함수
-- sum 합계, avg 평균, count 개수, min 최소값, max 최대값
select to_char(sum(salary),'999,999,999') from employees;

select round(avg(salary),4) from employees;
select trunc(avg(salary),4) from employees;

select max(salary) from employees;
select min(salary) from employees;

-- 평균값보다 월급이 높은 사원을 출력하시오.
select emp_name, salary from employees where salary > 6461;

select count(salary) from employees
where salary >= (select avg(salary) from employees);

-- emp_name: 단일 함수, avg(salary): 그룹 함수
-- 그룹함수와 단일함수를 같이 사용할 수 없음
select emp_name,avg(salary) from employees;

-- sum, avg, count, min, max가 그룹함수

-- students 테이블 모든 학생의 kor 점수, 합계, 평균 최대값 최소값을 구하시오
select * from students;

select sum(kor), avg(kor), max(kor), min(kor) from students;

-- 부서번호가 50 사원들의 월급의 합, 평균, 푀대값, 최소값을 입력하시오

select avg(department_id) 부서번호,sum(salary) 합, avg(salary) 평균, max(salary) 최대, min(salary) 최소 from employees where department_id = 50;

-- 단일함수를 출력하고 싶을 때, 단일함수를 입력하면 됨
select department_id,max(salary) from employees
group by department_id;

-- 단일함수,그룹함수 함께 사용하려면, group by 지정
select department_id,avg(salary) from employees
group by department_id;

select emp_name,salary from employees order by salary desc;

-- 수학함수: abs, ceil, floor, round, trunc, mod, power, sqrt
-- 문자,숫자형 타입 -> 날짜형타입 변경가능
-- 숫자,날짜형 타입 -> 문자형타입 변경가능
-- 문자형 타입 -> 숫자형타입 변경가능
-- 날짜형 타입 -> 숫자형타입 변경불가

-- 문자형 합치기, concat 대신 아래 쓰면 됨.
select emp_name||email from employees;

-- lower: 소문자 취환, upper:대문자 취환, initcap: 첫글자 대문자 취환
select * from member
where lower(name)='bryan';

-- lpad, rpad
-- trim, ltrim, rtrim
-- replace
select '  a  b c   ', trim('  a  b c   '), replace('  a  b c   ',' ','') from dual;

-- substr: 특정위치 자르기 (시작위치, 개수)
select 'abcdefg',substr('abcdefg',0,3),substr('abcdefg',2,2) from dual;

-- 입사일이 3월인 사원을 출력하시오.
select * from employees;
select emp_name, hire_date from employees where substr(to_char(hire_date),4,2) = '03';

-- 7월 이상
select hire_date,substr(hire_date,4,2) from employees;

select * from employees;

select emp_name, hire_date from employees where substr(to_char(hire_date),4,2) >= '05';

select 'axyz',translate('axyzxbbcyaccs','xy','ab') from dual;

select name 이름 from students where length(name) >= 5;

-- 사원의 월급의 합, 평균을 구하시오

-- 영어점수의 합, 평균, 최대값, 최소값을 구하시오.

-- students 테이블에서
-- 홍길동, 2023년 12월 02일 등록

select sum(salary) 월급총합, avg(salary) 월급평균 from employees;

select sum(eng) 영어총합, avg(eng) 영어평균, max(eng) 영어최대, min(eng) 영어최소 from students;

select name 이름, to_char(sdate,'"등록일:" yyyy"년" mm"월" dd"일"') 등록일 from students;


