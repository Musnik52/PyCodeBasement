from logger import Logger
from tickets import Tickets
from flights import Flights
from customers import Customers
from facade_base import FacadeBase
from error_invalid_input import InvalidInput
from error_invalid_token import InvalidToken
from error_no_more_tickets import NoMoreTicketsLeft
from error_flight_not_found import FlightNotFound
from error_ticket_not_found import TicketNotFound
from error_customer_not_found import CustomerNotFound

class CustomerFacade(FacadeBase):

    def __init__(self, repo, login_token):
        super().__init__(repo)
        self.login_token = login_token
        self.logger = Logger.get_instance()

    def update_customer(self, customer, customer_id):
        self.logger.logger.debug(f'Attempting to update customer #{customer_id}...')
        if not isinstance(customer_id, int): 
            self.logger.logger.error(f'{InvalidInput} - Input must be an integer!')
            raise InvalidInput('Input must be an integer!')
        elif not isinstance(customer, dict): 
            self.logger.logger.error(f'{InvalidInput} - Input must be an integer!')
            raise InvalidInput('input must be a dictionary!')
        elif self.repo.get_by_id(Customers, customer_id) == None: 
            self.logger.logger.error(f'{CustomerNotFound} - Customer #{customer_id} was not found!')
            raise CustomerNotFound
        else:
            customer_check = self.repo.get_by_id(Customers, customer_id)
            if self.login_token.id != customer_check.user_id:
                self.logger.logger.error(f'{InvalidToken} - you cannot edit other customers!')
                raise InvalidToken
            else: 
                self.logger.logger.info(f'Customer #{customer_id} Updated!')
                self.repo.update_by_id(Customers, Customers.id, customer_id, customer)

    def add_ticket(self, ticket):
        self.logger.logger.debug(f'Attempting to create ticket...')
        if not isinstance(ticket, Tickets): 
            self.logger.logger.error(f'{InvalidInput} - Input must be an "Tickets" object!')
            raise InvalidInput('Input must be an "Tickets" object!')
        flight = super().get_flight_by_id(ticket.flight_id)
        if flight == None: 
            self.logger.logger.error(f'{FlightNotFound} - Flight #{ticket.flight_id} was not found!')
            raise FlightNotFound
        else:
            customer_check = self.repo.get_by_id(Customers, ticket.customer_id)
            if self.login_token.id != customer_check.user_id:
                self.logger.logger.error(f'{InvalidToken} - you cannot edit for other customers!')
                raise InvalidToken
            else:
                self.repo.add(ticket)
                self.repo.update_by_id(Flights, Flights.id, ticket.flight_id, {'remaining_tickets': flight.remaining_tickets - 1})
                self.logger.logger.info(f'Ticket created!')
                if flight.remaining_tickets < 0:
                    self.repo.update_by_id(Flights, Flights.id, ticket.flight_id, {'remaining_tickets': 0})
                    self.repo.delete_by_id(Tickets, Tickets.id, ticket.id)
                    self.logger.logger.error(f'{NoMoreTicketsLeft} - No seats available. Ticket canceled!')
                    raise NoMoreTicketsLeft

    def remove_ticket(self, ticket):
        self.logger.logger.debug(f'Attempting to remove ticket #{ticket}...')
        if not isinstance(ticket, int): 
            self.logger.logger.error(f'{InvalidInput} - Input must be an integer!!')
            raise InvalidInput('Input must be an integer!')
        elif self.repo.get_by_id(Tickets, ticket) == None: 
            self.logger.logger.error(f'{TicketNotFound} - Ticket #{ticket} was not found!')
            raise TicketNotFound
        else: 
            ticket_delete = self.repo.get_by_id(Tickets, ticket)
            customer = self.repo.get_by_id(Customers, ticket_delete.customer_id)
            if self.login_token.id != customer.user_id:
                self.logger.logger.error(f'{InvalidToken} - you cannot edit for other customers!')
                raise InvalidToken
            else:
                flight = super().get_flight_by_id(ticket_delete.flight_id) 
                self.repo.update_by_id(Flights, Flights.id, flight.id, {'remaining_tickets': flight.remaining_tickets + 1})
                self.repo.delete_by_id(Tickets, Tickets.id, ticket)
                self.logger.logger.info(f'Ticket #{ticket} Deleted!')

    def get_ticket_by_customer(self, customer):
        self.logger.logger.debug(f'Attempting to fetch ticket(s) for customer #{customer}...')
        if not isinstance(customer, int): 
            self.logger.logger.error(f'{InvalidInput} - Input must be an integer!!')
            raise InvalidInput('Input must be an integer!')
        elif self.repo.get_by_id(Customers, customer) == None: 
            self.logger.logger.error(f'{CustomerNotFound} - Customer #{customer} was not found!')
            raise CustomerNotFound
        else: 
            customer_check = self.repo.get_by_id(Customers, customer)
            if self.login_token.id != customer_check.user_id:
                self.logger.logger.error(f'{InvalidToken} - you cannot edit for other customers!')
                raise InvalidToken
            else:
                self.logger.logger.info(f'Ticket(s) for #{customer} Displayed!')
                return self.repo.get_by_column_value(Tickets, Tickets.customer_id, customer)

    def __str__(self):
        return f'{super().__init__}'
