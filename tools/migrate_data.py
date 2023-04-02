#  Created by btrif Trif on 03-06-2022 , 3:38 PM.
# Tool to migrate data from JSON file to SQLite db using the Django ORM Model
'''
https://stackoverflow.com/questions/26082128/improperlyconfigured-you-must-either-define-the-environment-variable-django-set
'''

# Setting Environment Variables
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hr_system.settings')

# We need to setup Django
import django

django.setup()

import pandas as pd
from employee.models import Employee


def main():
    with open('Pandas test large data set\MOCK_DATA.json', 'r') as json_file:
        data = pd.read_json(json_file)

        '''
        ERROR : How to Fix: ValueError: cannot convert float NaN to integer
        https://www.statology.org/valueerror-cannot-convert-float-nan-to-integer/
        The default data  type for  years_of_experience is FLOAT. Some of them are NaN
        We must get of them with the following two lines of code :    
        '''
        data['years_of_experience'] = data['years_of_experience'].fillna(0)
        data['years_of_experience'] = data['years_of_experience'].astype(int)

        print(data)
        print(f'\n data info : \n{data.info}')
        print(f'\nvalue_counts : \n {data.value_counts()}')
        print('\n---------------------')
        print(f'\n df.head  : \n{data.head(10)}')
        print('-----' * 25)
        data_dict = data.to_dict()
        # data_dict = data.head(10**2).to_dict()
        print(data_dict)
        print('-----' * 25)
        for key, val in data_dict['id'].items():
            id = val
            first_name = data_dict['first_name'][key]
            last_name = data_dict['last_name'][key]
            email = data_dict['email'][key]
            gender = data_dict['gender'][key]
            date_of_birth_temp = data_dict['date_of_birth'][key]
            date_of_birth = '-'.join(date_of_birth_temp.split('/')[::-1])

            industry = data_dict['industry'][key]
            salary = data_dict['salary'][key]
            years_of_experience = int(data_dict['years_of_experience'][key])
            print(
                f"id = {id}, first_name= {first_name}, last_name= {last_name}, g={gender}, "
                f"salary={salary}, years={years_of_experience}   {type(years_of_experience)}")

            person = Employee(
                first_name=first_name,
                last_name=last_name,
                email=email,
                gender=gender,
                date_of_birth=date_of_birth,
                industry=industry,
                salary=salary,
                years_of_experience=years_of_experience
            )
            print(f'person object = {person} \n')
            person.save()


if __name__ == '__main__':
    main()
