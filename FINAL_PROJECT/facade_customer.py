from facade_base import FacadeBase
from customers import Customers
from tickets import Tickets
from flights import Flights
from error_ticket_not_found import TicketNotFound
from error_customer_not_found import CustomerNotFound
from error_no_more_tickets import NoMoreTicketsLeft
from error_flight_not_found import FlightNotFound

class CustomerFacade(FacadeBase):

    def __init__(self, repo):
        super().__init__(repo)

    def update_customer(self, customer, customer_id):
        if self.repo.get_by_id(Customers, customer_id) == None: raise CustomerNotFound
        else: self.repo.update_by_id(Customers, Customers.id, customer_id, customer)

    def add_ticket(self, ticket):
        try:
            flight = super().get_flight_by_id(ticket.flight_id)
            if flight == None: raise FlightNotFound
            self.repo.add(ticket)
            self.repo.update_by_id(Flights, Flights.id, ticket.flight_id, {'remaining_tickets': flight.remaining_tickets - 1})
            flight = super().get_flight_by_id(ticket.flight_id)
            if flight.remaining_tickets < 0: raise NoMoreTicketsLeft
        except FlightNotFound as q: print(q, 'Flight not found. Check again!')
        except NoMoreTicketsLeft as e:
            self.repo.update_by_id(Flights, Flights.id, ticket.flight_id, {'remaining_tickets': 0})
            self.repo.delete_by_id(Tickets, Tickets.id, ticket.id)
            print(e, 'No more tickets available.')
        except: print('Customer ID invalid. Please check again!')

    def remove_ticket(self, ticket):
        if self.repo.get_by_id(Tickets, ticket) == None: raise TicketNotFound
        else: self.repo.delete_by_id(Tickets, Tickets.id, ticket)

    def get_ticket_by_customer(self, customer):
        if self.repo.get_by_column_value(Tickets, Tickets.customer_id, customer) == None: raise TicketNotFound
        else: return self.repo.get_by_column_value(Tickets, Tickets.customer_id, customer)

    def __str__(self):
        return f'{super().__init__}'
