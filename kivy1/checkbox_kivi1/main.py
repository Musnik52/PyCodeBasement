import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

class MyGrid(Widget):

    airline_companies = ObjectProperty(None)
    customers = ObjectProperty(None)
    administrators = ObjectProperty(None)
    flights_per_company = ObjectProperty(None)
    tickets_per_customer = ObjectProperty(None)
    countries = ObjectProperty(None)

    def btn(self):
        print(  "Airline Companies:", self.airline_companies.text,
                "Customers:", self.customers.text,
                "Administrators:", self.administrators.text,
                "Flights Per Company:", self.flights_per_company.text,
                "Tickets Per Customer:", self.tickets_per_customer.text,
                "Countries:", self.countries.text)
        self.airline_companies.text =""
        self.customers.text =""
        self.administrators.text =""
        self.flights_per_company.text =""
        self.tickets_per_customer.text =""
        self.countries.text =""
    
    def checkbox_click(self, instance, value):
        if value is True:
            print("Checkbox Checked")
        else:
            print("Checkbox Unchecked")



class MyApp(App):
    def build(self):
        return MyGrid()

if __name__ == "__main__":
    MyApp().run() 
