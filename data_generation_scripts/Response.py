import uuid
import random

class Response():
    def __init__(self, question_id, employee_id):
        self.response_id = str(uuid.uuid4())
        self.question_id = question_id
        self.employee_id = employee_id
        self.response = random.randint(1,5)
        
        self.entry = {
            "Response_ID": self.response_id,
            "Question_ID": self.question_id,
            "Employee_ID": self.employee_id,
            "Response": self.response
        }
        
        return