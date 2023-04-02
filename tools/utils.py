#  Created by btrif Trif on 06-06-2022 , 12:54 PM.

from datetime import datetime
import pandas as pd

json_data_file = 'Pandas test large data set\MOCK_DATA.json'


def get_age_from_birthday(dob: str) -> int:
    birth_date = datetime.strptime(dob, "%Y-%m-%d")
    print(f'birth_Date : {birth_date}')
    year, month, day = birth_date.year, birth_date.month, birth_date.day
    print(f'year : {year}, month : {month}, day: {day}')
    age = datetime.now().year - year
    print(f'Age = {age}')
    return age


def get_pandas_dataset(json_data_file):
    with open(json_data_file, 'r') as json_file:
        dataset = pd.read_json(json_file)
    return dataset


if __name__ == '__main__':
    from random import randint

    date_of_birth = '-'.join((str(i) for i in [randint(1900, 2010), randint(1, 12), randint(1, 28)]))
    print(f'date_of_birth  =  {date_of_birth}')
    get_age_from_birthday(date_of_birth)
