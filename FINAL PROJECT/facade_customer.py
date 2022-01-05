from facade_base import FacadeBase
from db_config import local_session, create_all_entities
from db_repo import DbRepo
from customers import Customers
from tickets import Tickets

repo = DbRepo(local_session)

class CustomerFacade(FacadeBase):

    def __init__(self):
        super().__init__

    def update_customer(self, customer):
        repo.update_by_id(Customers, Customers.id, customer.id, customer)

    def add_ticket(self, ticket):
        repo.add(ticket)

    def remove_ticket(self, ticket):
        repo.delete_by_id(Tickets, Tickets.id, ticket.id)

    def get_ticket_by_customer(self, customer):
        repo.get_by_column_value(Tickets, Tickets.customer_id, customer.id)

    def __str__(self):
        return f'{super().__init__}'
