# Paranuara APIs

This project aims to provides several Restful APIs for providing information about people and companies in Paranuara.

## Getting Started

Clone paranuara project to your local computer by (git clone https://github.com/guo2017/Paranuara.git) 

### Prerequisites

On your computer, you need to install python3.6, flask, flask_restful and unittest to run this application.

### Installing

1. create virtual environment (virtualenv --no-site-packages env)
2. activate the environment (source env/bin/activate)
3. install flask(pip install flask)
4. install flask_restful(pip install flask_restful)
5. install unittest (pip install unittest)
6. start application (python3 server.py)
7. visit service by 127.0.0.1:5000

## API documentation
1. url (http://127.0.0.1:5000/companies): return all companies by Json
2. url (http://127.0.0.1:5000/people): return all people by Json
3. url (http://127.0.0.1:5000/employees/<company_id>): return all employees of a company with <company_id> by Json
4. url (http://127.0.0.1:5000/commonfriends/<people01_id>/<people02_id>): return information of people with <people01_id>, 
   information of people with <people02_id> and information of their common friends who are alive and with brown eyes.
5. url (http://127.0.0.1:5000/fruits/<people_id>)): return information of people with <people_id> and separate fruits with
   vegetables from favoriate food

## Automated Testing
1. run unittest : python -m unittest test_server.py

## Unit Test documentation
1. test_home_status_code: 
   test the server can return status code "200" when request home page
2. test_home_data: 
   test "http://127.0.0.1:5000" return default page
3. test_compnay_employees: 
   test "http://127.0.0.1:5000/employees/<company_id>" return correct set of employees. 
   For example
   "http://127.0.0.1:5000/employees/101" returns error message with error code 204 because it has no employees
   "http://127.0.0.1:5000/employees/1" returns 7 employees
4. test_common_friends:
   test "http://127.0.0.1:5000/commonfriends/<people01_id>/<people02_id>" return right set of common friends
   For example:
   "http://127.0.0.1:5000/commonfriends/1/2" returns 1 common friend with name 'Decker Mckenzie'
5. test_fruits_vegetables:
   test "http://127.0.0.1:5000/fruits/<people_id>" returns separated fruits sets for people with <people_id> by Json
   For example:
   "http://127.0.0.1:5000/fruits/2" returns a people with age "54", fruit set (orange, banana, strawberry) and vegetable set (beetroot)
