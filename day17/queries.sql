CREATE TABLE interns (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    track TEXT NOT NULL,
    stipend INTEGER
);

INSERT INTO interns (name, track, stipend) VALUES
('Aisha', 'Data Science', 15000),
('Rahul', 'Web Dev', 12000),
('Sneha', 'Machine Learning', 18000),
('Arjun', 'Data Science', 16000),
('Meera', 'Web Dev', 11000);

SELECT name, track FROM interns;