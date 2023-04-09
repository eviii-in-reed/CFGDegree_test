 -- Change the maximum mark of the cyber security exam to 100 
UPDATE exams SET Max_Mark = 100 WHERE Exam_ID = 2;



-- Write a query to list the lowest-achieving student across the exams.  
-- Output their full name along with their total score. 

SELECT CONCAT(s.FORENAME, " ", s.SURNAME) AS Full_name, MIN(r.Mark) AS Total_score 
FROM students s, results r GROUP BY r.Student_ID;



-- All students who failed an exam (received a mark of less than 40)  have now chosen to leave this program. 
-- Remove them from the students table.
// It says I cannot delete parent column?

 SET SQL_SAFE_UPDATES = 0;
 DELETE FROM students 
 WHERE FORENAME IN (
	SELECT sr.FORENAME FROM (
		SELECT s.FORENAME FROM results r 
		RIGHT JOIN students s ON r.Student_ID = s.Student_ID WHERE r.Mark < 40
	) AS sr
    );
    
DELETE FROM students
WHERE student_id IN (
    SELECT sid FROM (
        SELECT DISTINCT s.student_id AS sid from students as s join results as r on s.student_id = r.student_id 
		INNER JOIN students ON s.student_id=s.student_id
        where mark < 40
    ) as s
);
