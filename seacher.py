"""This File be made for seaching link about Free Subject"""
import requests

def function_1():
    """fdsafsdfsdfsd"""
    print("select your kana that u want")
    print("1 : สังคมศาสตร์")
    if input() == "1":
        kuy = 'http://www.reg.kmitl.ac.th/teachtable_v20/teachtable_show.php?&faculty_id=03&dept_id=x&curr_id=0&curr2_id=x&year=2559&semester=2&class=9'
        openthetext = requests.get(kuy)
        print("if u want to dooooo type : 1")
        if input() == "1":
            print(openthetext.text)
function_1()
