from os import remove
from flask import Flask, request, render_template
import json
from db_repo import DbRepo
from db_config import local_session
from customers import Customers

repo = DbRepo(local_session)
app = Flask(__name__)

#customers = [repo.get_all(Customers)] WHEN NO DB


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
    if request.method == 'GET':
        # pseudo - select * from Customers
        # parsing
        # turn to json
        #return json.dumps(customers1[0])
        customers1 = [c.__dict__ for c in repo.get_all(Customers)]
        return json.dumps(dict(customers1))
    if request.method == 'POST':
        #  {'id': 4 [not be sent with DB], 'name': 'david', 'address': 'herzeliya'}
        new_customer = request.get_json()
        customers.append(new_customer)
        return '{"status": "success"}'

@app.route('/customers/<int:id>', methods=['GET', 'PUT', 'DELETE', 'PATCH'])
def get_customer_by_id(id):
    global customers
    if request.method == 'GET':
        # pseudo - select * from Customers where Customer.id == id
        # parsing
        # turn to json
        for c in customers:
            if c["id"] == id:
                return json.dumps(c)
        return '{}'
    if request.method == 'PUT':
        #  {'id': 4 [not be sent with DB], 'name': 'david', 'address': 'herzeliya'}
        # 1. if not exist --> add
        # 2. if exist, update fields with given data
        # 3.           missing fields will have None value
        updated_new_customer = request.get_json()
        for c in customers:
            if c["id"] == id:
                c["id"] = updated_new_customer["id"] if "id" in updated_new_customer.keys() else None
                c["name"] = updated_new_customer["name"] if "name" in updated_new_customer.keys() else None
                c["address"] = updated_new_customer["address"] if "address" in updated_new_customer.keys() else None
                return json.dumps(updated_new_customer)
        customers.append(updated_new_customer)
        return json.dumps(updated_new_customer)
    if request.method == 'PATCH':
        #  {'id': 4 [not be sent with DB], 'name': 'david', 'address': 'herzeliya'}
        # 1. if not exist --> return
        # 2. if exist, update fields with given data
        # 3.           missing fields will remain the same
        updated_customer = request.get_json()
        for c in customers:
            if c["id"] == id:
                c["id"] = updated_customer["id"] if "id" in updated_customer.keys() else c["id"]
                c["name"] = updated_customer["name"] if "name" in updated_customer.keys() else c["name"]
                c["address"] = updated_customer["address"] if "address" in updated_customer.keys() else c["address"]
                return json.dumps(updated_customer)
        return '{"status": "not found"}'
    if request.method == 'DELETE':
        customers = [c for c in customers if c["id"] != id]
        return json.dumps(customers)

app.run()

# download post-man
# activate:
# GET, GET/ID, POST, PUT, PATCH, DELETE -- check if they work
# connect the project to a DB (sqlite, postgresql, w/o alchemy)