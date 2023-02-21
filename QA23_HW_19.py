user = {
    "name": "John",
    "age": 23,
    "friends": [
        "Mike", "Bob", "Joe"
    ],
    "skills": ("HTML", "CSS", "JS"),
}

# 1) Find Mike into the user , than if u found Mike create a variable for him
# 2) Print Mike at the console
# 3) Get age of user , and guess when he was born
# 4) Skills must look as : Python , QA , Selenium
# 5) Sort john's friends
# 6) After sort find index position of "Bob"
# 7) Add new friends to friends : "Taras" , "Danya" , "Bidden"
# 8) Show how much skills user has

print(user["friends"][0])
user_age=input("How old are you?: ")
import datetime 
year_of_birth=datetime.date.today().year-int(user_age)
print("Year of birth: ",year_of_birth)

user["skills"]=("Python", "QA", "Selenium")
print("skills: ", user["skills"])

sorted_arr=sorted(user["friends"])
print(sorted_arr)

print(sorted_arr.index("Bob"))

friends_new=["Taras" , "Danya" , "Bidden"]
sorted_arr.extend(friends_new)
print(sorted_arr)

print(len(user["skills"]))
print(user["skills"])




