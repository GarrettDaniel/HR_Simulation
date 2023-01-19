-- Query 1: Get a quick overview of each employee and their responses to each
-- survey question
SELECT 
    e.First_Name, 
    e.Last_Name, 
    e.Age, 
    e.Role_Type,
    q.Question,
    r.Response
FROM Employees e
JOIN Responses r
ON e.Employee_ID = r.Employee_ID
JOIN Questions q
ON q.Question_ID = r.Question_ID;


-- Query 2: Show which role_types had the highest average 
-- survey responses per question
SELECT 
    e.Role_Type,
    q.Question,
    AVG(r.Response)
FROM Employees e
JOIN Responses r
ON e.Employee_ID = r.Employee_ID
JOIN Questions q
ON q.Question_ID = r.Question_ID
GROUP BY q.Question, e.Role_Type
ORDER BY q.Question;

-- Query 3: Show average age of current, remote employees 
-- with a salary > 70,000
SELECT 
    AVG(e.Age)
FROM Employees e
WHERE e.Salary > 70000
AND e.Current_Employee = True
AND e.Remote_Employee = True;

-- Query 4: Show how many employees are of each role type
-- and their average salary
SELECT
    e.Role_Type,
    COUNT(e.Role_Type) as total_employees,
    AVG(e.Salary) as average_salary
FROM Employees e
GROUP BY e.Role_Type, e.Remote_Employee;

-- Query 5: Show percent of remote employees per state
-- and their average distance to work
SELECT
    e.State_Code,
    (COUNT(e.State_Code) / (SELECT COUNT(*) FROM EMPLOYEES)) * 100 as percent_remote,
    AVG(e.Miles_to_Work) as avg_miles_to_work
FROM Employees e
WHERE e.Remote_Employee = True
GROUP BY e.State_Code, e.Role_Type, e.Miles_to_Work
ORDER BY percent_remote DESC;