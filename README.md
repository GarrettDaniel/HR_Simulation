# hr_survey_simulation
This is an example project to practice creating simulated HR survey data, loading that data into RDS, performing queries, and analyzing the data.

Completed Tasks:
- Created classes for employees (job role, pay, name, address, etc.) and survey responses (scale from 1-5 where 1 is strongly disagree, and 5 is strongly agree)
- Created functions to populate datasets for 10,000 synthetic employees, a question bank of 20 common engagement survey questions, and their synthetic responses to said survey on a scale from 1-5.
- Set up Amazon RDS PostgreSQL DB and tables for employees, questions, and survey
- Fixed issues with address parsing
- Fixed issues with boolean datatype conversion

Need to do:
- Create Workflow diagram
- Create a dashboard to showcase simulated survey responses
- Add additional data for things like benefits.
- Practice ML and Risk modeling
- Consider creating infrastructure and management with Terraform
