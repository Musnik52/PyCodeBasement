from flask import Flask, request, Response
import json
from db_repo import DbRepo
from db_config import local_session
from customers import Customers
from users import Users

repo = DbRepo(local_session)
app = Flask(__name__)

def convert_to_json(_list):
    json_list = []
    for i in _list:
        _dict = i.__dict__
        _dict.pop('_sa_instance_state', None)
        json_list.append(_dict)
    return json_list

def add_customer_user(_input):
    repo.add(Users(     id=_input['user_id'],
                        username=_input['username'], 
                        password=_input['password'],
                        email=_input['email'],
                        user_role=3))
    repo.add(Customers( id=_input['id'],
                        first_name=_input['first_name'], 
                        last_name=_input['last_name'], 
                        address=_input['address'], 
                        phone_number=_input['phone_number'], 
                        credit_card_number=_input['credit_card_number'], 
                        user_id=_input['user_id']))
    return Response(f'"new-item": "{request.url}/{_input["id"]}"', status=201, mimetype='application/json')

def update_customer(_input, id):
    customers_json = convert_to_json(repo.get_all(Customers))
    for c in customers_json:
        if c["id"] == id:
            c["id"] = _input["id"] if "id" in _input.keys() else None
            c["first_name"] = _input["first_name"] if "first_name" in _input.keys() else None
            c["last_name"] = _input["last_name"] if "last_name" in _input.keys() else None
            c["address"] = _input["address"] if "address" in _input.keys() else None
            c["phone_number"] = _input["phone_number"] if "phone_number" in _input.keys() else None
            c["credit_card_number"] = _input["credit_card_number"] if "credit_card_number" in _input.keys() else None
            repo.update_by_id(Customers, Customers.id, id, c)
    return Response(f'"Updated-item": "{request.url}"', status=200, mimetype='application/json')

# localhost:5000/
# static page
# dynamic page
@app.route("/")
def home():
    print('hi')
    return '''
        <html>
            Customers!
            Countries!
            Administrators!
            Airline Companies!
            Users!
            User-Roles!
            Flights!
            Tickets!
        </html>
    '''

@app.route('/customers', methods=['GET', 'POST'])
def get_or_post_customer():
    customers = convert_to_json(repo.get_all(Customers))
    if request.method == 'GET':
        print(request.args.to_dict())
        search_args = request.args.to_dict()
        if len(search_args) == 0: Response(json.dumps(customers), status=200, mimetype='application/json')
        results = []
        for c in customers:
            if "first_name" in search_args.keys() and c["first_name"].find(search_args["first_name"]) < 0: continue
            if "last_name" in search_args.keys() and c["last_name"].find(search_args["last_name"]) < 0: continue
            if "address" in search_args.keys() and c["address"].find(search_args["address"]) < 0: continue
            if "phone_number" in search_args.keys() and c["phone_number"].find(search_args["phone_number"]) < 0: continue
            if "credit_card_number" in search_args.keys() and c["credit_card_number"].find(search_args["credit_card_number"]) < 0: continue
            results.append(c)
        if len(results) == 0: return Response("[]", status=404, mimetype='application/json')
        return Response(json.dumps(customers), status=200, mimetype='application/json')
    if request.method == 'POST':
        #  {"username": "1i1y", "password": "passw0rd", "email": "lily@jb.com", "first_name":"lily", "last_name":"musnikov", "address":"narnia22", "phone_number":"0565452243", "credit_card_number":"65546765534", "user_id":8}
        new_customer = request.get_json()
        if repo.get_by_id(Users,new_customer['user_id']): return 'Input violates restrictions!'
    return add_customer_user(new_customer)

@app.route('/customers/<int:id>', methods=['GET', 'PUT', 'DELETE', 'PATCH'])
def get_customer_by_id(id):
    customers = convert_to_json(repo.get_all(Customers))
    if request.method == 'GET':
        for c in customers:
            if c["id"] == id: return Response(json.dumps(c), status=200, mimetype='application/json')
        return Response("[]", status=404, mimetype='application/json')
    if request.method == 'PUT':
        #  {"username": "1i1y", "password": "passw0rd", "email": "lily@jb.com", "first_name":"lily", "last_name":"musnikov", "address":"narnia22", "phone_number":"0565452243", "credit_card_number":"65546765534", "user_id":8}
        updated_new_customer = request.get_json()
        if repo.get_by_id(Customers, id) != None: return update_customer(updated_new_customer, id)
        return add_customer_user(updated_new_customer)
    if request.method == 'PATCH':
        # {"username": "1i1y", "password": "passw0rd", "email": "lily@jb.com", "first_name":"lily", "last_name":"musnikov", "address":"narnia22", "phone_number":"0565452243", "credit_card_number":"65546765534", "user_id":8}
        updated_customer = request.get_json()
        if repo.get_by_id(Customers, id) != None: return update_customer(updated_customer, id)
        return Response("[]", status=404, mimetype='application/json')
    if request.method == 'DELETE':
        deleted_customer = request.get_json()
        for c in customers:
            if c["id"] == id:
                repo.delete_by_id(Customers, Customers.id, id)
                repo.delete_by_id(Users, Users.id, c["user_id"])
                return f'{json.dumps(deleted_customer)} deleted'
        return Response("[]", status=404, mimetype='application/json')

app.run()