DROP TABLE IF EXISTS mentors;

CREATE TABLE mentors (
    mentor_id INTEGER PRIMARY KEY,
    mentor_name TEXT,
    track TEXT
);

INSERT INTO mentors VALUES (1, 'Dr. Rao', 'Data Science');
INSERT INTO mentors VALUES (2, 'Ms. Priya', 'Web Dev');
INSERT INTO mentors VALUES (3, 'Mr. Ahmed', 'AI/ML');

SELECT 
    interns.name,
    interns.track,
    mentors.mentor_name
FROM interns
INNER JOIN mentors
ON interns.track = mentors.track;