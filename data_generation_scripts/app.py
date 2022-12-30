from create_datasets import create_datasets
from create_db import create_db

questions_df, employees_df, responses_df = create_datasets(num_employees=10000)

### Need to rerun this so that it also includes role_type and salary for the employees