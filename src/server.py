from flask import Flask, json, jsonify
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


@app.route('/')
def index():
    return "This is Parranuara"

#return all companies
class Companies(Resource):
    def get(self):
        file_name = 'companies.json'
        with open(file_name) as f:
            json_data = json.load(f)
            return json_data

#return all employees
class People(Resource):
    def get(self):
        file_name = 'people.json'
        with open(file_name) as f:
            json_data = json.load(f)
            print(type(json_data))
            return json_data

#return employees based on company id
class CompanyEmployees(Resource):
    def get(self, company_id):
        file_name = 'people.json'
        matched_employees = []
        json_data = None
        with open(file_name) as f:
            json_data = json.load(f)

        for employee in json_data:
            if str(employee["company_id"]) == company_id:
                matched_employees.append(employee)
        if len(matched_employees) == 0:
            return jsonify({"error": {"code": 204, "message": "no employees found"}})
        else:
            return jsonify(matched_employees)

#return common friends of two employees
class CommonFriends(Resource):
    def get(self, people01_id, people02_id):
        file_name = 'people.json'
        p1 = None
        p2 = None
        p1_friends = []
        p2_friends = []
        json_data = None
        common_friends_ids = []
        common_friends = []

        with open(file_name) as f:
            json_data = json.load(f)

        for people in json_data:
            if str(people["index"]) == people01_id:
                p1 = {"name": people["name"], "age": people["age"], "address": people["address"],
                      "phone": people["phone"]}
                for x in people["friends"]:
                    p1_friends.append(x["index"])

            if str(people["index"]) == people02_id:
                p2 = {"name": people["name"], "age": people["age"], "address": people["address"],
                      "phone": people["phone"]}
                for x in people["friends"]:
                    p2_friends.append(x["index"])
        common_friends_ids = [x for x in p1_friends if x in p2_friends]

        for people in json_data:
            if people["index"] in common_friends_ids and people["eyeColor"] == 'brown' and people['has_died'] == False:
                common_friends.append(people)
        result = {"people_one": p1, "people_two": p2, "common_friends": common_friends}

        return jsonify(result)

#return fruits and vegetables separately for a given employee
class FruitsVegetables(Resource):
    def get(self, people_id):
        fruit_list = ['apple', 'orange', 'banana', 'strawberry']
        fruits = []
        vegetables = []
        target_people = None
        json_data = None
        file_name = "people.json"
        with open(file_name) as f:
            json_data = json.load(f)
        for people in json_data:
            if str(people["index"]) == people_id:
                target_people = people
        favorite_food = target_people["favouriteFood"]
        fruits = [x for x in favorite_food if x in fruit_list]
        vegetables = [x for x in favorite_food if x not in fruit_list]
        result = {"username": target_people["name"], "age": str(target_people["age"]), "fruits": fruits,
                  "vegetables": vegetables}

        return jsonify(result)


api.add_resource(Companies, '/companies')
api.add_resource(People, '/people')
api.add_resource(CompanyEmployees, '/employees/<company_id>')
api.add_resource(CommonFriends, '/commonfriends/<people01_id>/<people02_id>')
api.add_resource(FruitsVegetables, '/fruits/<people_id>')

if __name__ == '__main__':
    app.run(debug=True)
