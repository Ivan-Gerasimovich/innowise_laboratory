-- Student Grades Manager - SQL Queries

-- 4.1. Create tables
-- Creating the 'students' table with ID, full_name, and birth_year
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    full_name TEXT,
    birth_year INTEGER
);

-- Creating the 'grades' table with Foreign Key linking to students
CREATE TABLE IF NOT EXISTS grades (
    id INTEGER PRIMARY KEY,
    student_id INTEGER,
    subject TEXT,
    grade INTEGER,
    FOREIGN KEY (student_id) REFERENCES students(id)
);

-- 4.2. Insert data
-- Inserting students
INSERT INTO students (full_name, birth_year) VALUES 
('Alice Johnson', 2005),
('Brian Smith', 2004),
('Carla Reyes', 2006),
('Daniel Kim', 2005),
('Eva Thompson', 2003),
('Felix Nguyen', 2007),
('Grace Patel', 2005),
('Henry Lopez', 2004),
('Isabella Martinez', 2006);

-- Inserting grades (using student_ids corresponding to the order above)
INSERT INTO grades (student_id, subject, grade) VALUES 
(1, 'Math', 88), (1, 'English', 92), (1, 'Science', 85),
(2, 'Math', 75), (2, 'History', 83), (2, 'English', 79),
(3, 'Science', 95), (3, 'Math', 91), (3, 'Art', 89),
(4, 'Math', 84), (4, 'Science', 88), (4, 'Physical Education', 93),
(5, 'English', 90), (5, 'History', 85), (5, 'Math', 88),
(6, 'Science', 72), (6, 'Math', 78), (6, 'English', 81),
(7, 'Art', 94), (7, 'Science', 87), (7, 'Math', 90),
(8, 'History', 77), (8, 'Math', 83), (8, 'Science', 80),
(9, 'English', 96), (9, 'Math', 89), (9, 'Art', 92);

-- 4.3. Find all grades for a specific student (Alice Johnson)
SELECT s.full_name, g.subject, g.grade 
FROM grades g
JOIN students s ON g.student_id = s.id
WHERE s.full_name = 'Alice Johnson';

-- 4.4. Calculate the average grade per student
SELECT s.full_name, AVG(g.grade) as average_grade
FROM students s
JOIN grades g ON s.id = g.student_id
GROUP BY s.id, s.full_name;

-- 4.5. List all students born after 2004
SELECT * 
FROM students 
WHERE birth_year > 2004;

-- 4.6. Create a query that lists all subjects and their average grades
SELECT subject, AVG(grade) as average_grade
FROM grades
GROUP BY subject;

-- 4.7. Find the top 3 students with the highest average grades
SELECT s.full_name, AVG(g.grade) as average_grade
FROM students s
JOIN grades g ON s.id = g.student_id
GROUP BY s.id, s.full_name
ORDER BY average_grade DESC
LIMIT 3;

-- 4.8. Show all students who have scored below 80 in any subject
SELECT DISTINCT s.full_name
FROM students s
JOIN grades g ON s.id = g.student_id
WHERE g.grade < 80;

-- Indexes to optimize queries
CREATE INDEX IF NOT EXISTS idx_student_name ON students(full_name);
CREATE INDEX IF NOT EXISTS idx_grade_student_id ON grades(student_id);
