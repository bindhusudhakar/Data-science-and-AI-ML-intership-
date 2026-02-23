
SELECT 
    interns.name,
    interns.track,
    mentors.mentor_name
FROM interns
INNER JOIN mentors
ON interns.track = mentors.track;