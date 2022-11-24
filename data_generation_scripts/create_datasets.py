from Employee import Employee
from Response import Response
import pandas as pd
import uuid
import json

filepath = "hr_survey_simulation/"

question_bank = [
    "Do you find your work engaging?",
    "Are your immediate co-workers committed to the organization's goals?",
    "Would you recommend this organization as a great place to work?",
    "Is your job in alignment with your career goals?",
    "Do you have career growth and development opportunities at this organization?",
    "Do you have the materials and equipment you need to do your job?",
    "Do you have the information you need to do your job?",
    "Do you think your opinions count at work?",
    "When the organization makes changes, do you understand why?",
    "Do you feel that changes are made in a way that is consistent with the company’s mission and long-term vision?",
    "When you contribute to the organization's success, do you feel recognized?",
    "Does your job give you the flexibility to meet the needs of your personal life?",
    "Do you feel that your immediate manager cares about you as a person?",
    "Do you regularly receive constructive performance feedback from your manager?",
    "Are goals and accountabilities clear to everyone on your team?",
    "Are your teammates or co-workers committed to producing top quality work?",
    "Do the senior leaders of this organization demonstrate integrity?",
    "Do you trust our senior leaders to lead the organization to future success?",
    "Do you understand the company's plans for future success?",
    "Do you know how you fit into the organization's future plans?"
]

def create_questions():
    
    questions = []

    for question in question_bank:
        question_dict = {}
        question_dict["Question_ID"] = str(uuid.uuid4()) 
        question_dict["Question"] = question
        questions.append(question_dict)
            
    questions_df = pd.DataFrame.from_dict(questions)
    questions_df.to_csv(filepath + "data/questions.csv", index=False)
    
    return questions_df
    
def create_employees(num_employees):
    
    employees = []
    
    for i in range(num_employees):
        employee = Employee()
        employees.append(employee.entry)
            
    employees_df = pd.DataFrame.from_dict(employees)
    employees_df.to_csv(filepath + "data/employees.csv", index=False)
    
    return employees_df
    
def create_survey_responses(questions_df, employees_df):
    
    employee_ids = employees_df["Employee_ID"].tolist()
    question_ids = questions_df["Question_ID"].tolist()
    
    responses = []
    
    for employee_id in employee_ids:
        for question_id in question_ids:
            response = Response(question_id=question_id, employee_id=employee_id)
            responses.append(response.entry)
    
    responses_df = pd.DataFrame.from_dict(responses)
    responses_df.to_csv(filepath + "data/responses.csv", index=False)
    
    return responses_df

def create_datasets(num_employees):
    
    questions_df = create_questions()
    employees_df = create_employees(num_employees)
    responses_df = create_survey_responses(questions_df, employees_df)
    
    return questions_df, employees_df, responses_df
    