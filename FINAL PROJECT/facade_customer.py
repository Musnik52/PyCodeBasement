from facade_base import FacadeBase
from customers import Customers
from tickets import Tickets

class CustomerFacade(FacadeBase):

    def __init__(self, repo):
        super().__init__(repo)

    def update_customer(self, customer):
        self.repo.update_by_id(Customers, Customers.id, customer.id, customer)

    def add_ticket(self, ticket):
        self.repo.add(ticket)

    def remove_ticket(self, ticket):
        self.repo.delete_by_id(Tickets, Tickets.id, ticket.id)

    def get_ticket_by_customer(self, customer):
        return self.repo.get_by_column_value(Tickets, Tickets.customer_id, customer.id)

    def __str__(self):
        return f'{super().__init__}'
