from flask import Flask, request
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
    return '{"status": "ADDED"}'

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
    return '{"status": "success"}'

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


# url/<resource> <--- GET POST
@app.route('/customers', methods=['GET', 'POST'])
def get_or_post_customer():
    if request.method == 'GET': return json.dumps(convert_to_json(repo.get_all(Customers)))
    if request.method == 'POST':
        #  {"username": "1i1y", "password": "passw0rd", "email": "lily@jb.com", "first_name":"lily", "last_name":"musnikov", "address":"narnia22", "phone_number":"0565452243", "credit_card_number":"65546765534", "user_id":8}
        new_customer = request.get_json()
        if repo.get_by_id(Users,new_customer['user_id']): return 'Input violates restrictions!'
    return add_customer_user(new_customer)

@app.route('/customers/<int:id>', methods=['GET', 'PUT', 'DELETE', 'PATCH'])
def get_customer_by_id(id):
    if request.method == 'GET':
        for c in convert_to_json(repo.get_all(Customers)):
            if c["id"] == id:
                return json.dumps(c)
        return '{}'
    if request.method == 'PUT':
        #  {"username": "1i1y", "password": "passw0rd", "email": "lily@jb.com", "first_name":"lily", "last_name":"musnikov", "address":"narnia22", "phone_number":"0565452243", "credit_card_number":"65546765534", "user_id":8}
        updated_new_customer = request.get_json()
        if repo.get_by_id(Customers, id) != None: return update_customer(updated_new_customer, id)
        return add_customer_user(updated_new_customer)
    if request.method == 'PATCH':
        # {"username": "1i1y", "password": "passw0rd", "email": "lily@jb.com", "first_name":"lily", "last_name":"musnikov", "address":"narnia22", "phone_number":"0565452243", "credit_card_number":"65546765534", "user_id":8}
        updated_customer = request.get_json()
        if repo.get_by_id(Customers, id) != None: return update_customer(updated_customer, id)
        return '{"status": "not found"}'
    if request.method == 'DELETE':
        deleted_customer = request.get_json()
        customers_json = convert_to_json(repo.get_all(Customers))
        for c in customers_json:
            if c["id"] == id:
                repo.delete_by_id(Customers, Customers.id, id)
                repo.delete_by_id(Users, Users.id, c["user_id"])
        return f'{json.dumps(deleted_customer)} deleted'
    return '{"status": "not found"}'

app.run()