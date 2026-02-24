CREATE TABLE students (
    student_id INTEGER,
    name TEXT,
    department TEXT,
    year INTEGER
);

CREATE TABLE subjects (
    subject_id INTEGER,
    subject_name TEXT,
    department TEXT
);

CREATE TABLE marks (
    student_id INTEGER,
    subject_id INTEGER,
    marks INTEGER
);

-- JOIN 
SELECT 
    s.department,
    AVG(m.marks) AS mean_marks,
    COUNT(*) AS total_records,
    
    -- Variance calculation
    (AVG(m.marks * m.marks) - 
     AVG(m.marks) * AVG(m.marks)) AS variance_marks,
    
    -- Standard deviation
    SQRT(AVG(m.marks * m.marks) - 
         AVG(m.marks) * AVG(m.marks)) AS std_dev_marks

FROM students s
JOIN marks m ON s.student_id = m.student_id
GROUP BY s.department;

SELECT * FROM students;
SELECT * FROM marks;

INSERT INTO students VALUES (1, 'Asha', 'CSE', 3);
INSERT INTO students VALUES (2, 'Rahul', 'CSE', 3);
INSERT INTO students VALUES (3, 'Meena', 'ECE', 2);
INSERT INTO students VALUES (4, 'Kiran', 'ECE', 2);
INSERT INTO students VALUES (5, 'Arjun', 'MECH', 4);

INSERT INTO subjects VALUES (101, 'DSA', 'CSE');
INSERT INTO subjects VALUES (102, 'Networks', 'CSE');
INSERT INTO subjects VALUES (201, 'Signals', 'ECE');
INSERT INTO subjects VALUES (301, 'Thermodynamics', 'MECH');

INSERT INTO marks VALUES (1, 101, 85);
INSERT INTO marks VALUES (1, 102, 90);
INSERT INTO marks VALUES (2, 101, 75);
INSERT INTO marks VALUES (3, 201, 88);
INSERT INTO marks VALUES (4, 201, 60);
INSERT INTO marks VALUES (5, 301, 92);

SELECT COUNT(*) FROM students;
SELECT COUNT(*) FROM marks;

--Aggregate Function
SELECT 
    s.department,
    AVG(m.marks) AS mean_marks,
    COUNT(*) AS total_records,
    
    (AVG(m.marks * m.marks) - 
     AVG(m.marks) * AVG(m.marks)) AS variance_marks,
    
    SQRT(AVG(m.marks * m.marks) - 
         AVG(m.marks) * AVG(m.marks)) AS std_dev_marks

FROM students s
JOIN marks m ON s.student_id = m.student_id
GROUP BY s.department;

SELECT 
    s.student_id,
    s.name,
    AVG(m.marks) AS avg_marks
FROM students s
JOIN marks m ON s.student_id = m.student_id
GROUP BY s.student_id
ORDER BY avg_marks DESC;

SELECT name FROM sqlite_master WHERE type='table';
