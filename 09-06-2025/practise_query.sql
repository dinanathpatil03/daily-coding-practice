

-- List all students' names and their classes.

select * from dbo.students

select name, class from dbo.students

-- Find students who are older than 15 years.
select name, age from students where age>15

-- Count total number of students.
select count(name) [Total number of student] from students 

-- Show subjects available in the system.
select subject_name from subjects

-- Find students with names starting with 'A'.
select * from students where name like 'A%'

-- List students along with their marks in each subject.
select * from students
select * from subjects 
select * from marks

select s.name, sub.subject_name, m.marks from marks m join students s on m.student_id = s.student_id
join subjects sub on m.subject_id = sub.subject_id

-- Find average marks obtained by each student.
select * from students
select * from marks

select s.name, avg(m.marks) as [Average marks] from students s join marks m on s.student_id = m.student_id
group by s.name

-- Display student names who scored more than 80 in any subject.

select distinct s.name from marks m join students s on m.student_id = s.student_id
where m.marks > 80

-- Find the subject in which each student scored the least.

SELECT s.name, sub.subject_name, m.marks
FROM Marks m
JOIN Students s ON m.student_id = s.student_id
JOIN Subjects sub ON m.subject_id = sub.subject_id
WHERE (m.student_id, m.marks) IN (
    SELECT student_id, MIN(marks)
    FROM Marks
    GROUP BY student_id
)

-- Write a query to get the class-wise average marks.

select * from marks
select * from students

select s.class, avg(m.marks) as [Average marks] from students s join marks m on m.student_id = s.student_id
group by s.class

-- Find students who failed in any subject (assuming pass mark is 40)

select DISTINCT s.student_id, s.name, sub.subject_name, m.marks from marks m join students s on m.student_id = s.student_id
join subjects sub on m.subject_id = sub.subject_id
where m.marks < 40

-- Show gender-wise average marks for each subject

select s.gender, avg(m.marks) as avg_marks, sub.subject_name from marks m join students s on m.student_id = s.student_id
join subjects sub on m.subject_id = sub.subject_id
group by s.gender, sub.subject_name







