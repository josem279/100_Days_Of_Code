import random
import pandas as pd


############ List comprehension instead of loops
numbers = [1, 2, 3]
new_list = [n + 1 for n in numbers]
# print(new_list)

name = "Jose"
letters = [l for l in name]
# print(letters)

range_list = [num * 2 for num in range(1, 5)]
# print(range_list)

### Conditional List Comprehension
names = ["jose", "ana", "estrella", "lysette"]
short_names = [name for name in names if len(name) < 6]
# print(short_names)
long_names = [name.upper() for name in names if len(name) > 5]
# print(long_names)

############ Dictionary Comprehension
student_scores = {name:random.randint(1, 100) for name in names}
# print(student_scores)
passed_students = {name: score for (name, score) in student_scores.items() if score > 70}
# print(passed_students)

############ Iterating through a pandas Df
student_dict = {
    "student": ["jose", "isaiah", "jj"],
    "score": [58, 93, 46]
}

student_df = pd.DataFrame(student_dict)
# print(student_df)
### Looping through the df:

# poor way:
# for (key, value) in student_df.items():
#     print(key)
#     print(value)

# better way:
for (index, row) in student_df.iterrows():
    # print(index)
    # print(row.student)
    if row.student == "jose":
        print(row.score)