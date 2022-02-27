import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty, StringProperty

class MyGrid(Widget):

    airline_companies = ObjectProperty(None)
    customers = ObjectProperty(None)
    administrators = ObjectProperty(None)
    flights_per_company = ObjectProperty(None)
    tickets_per_customer = ObjectProperty(None)
    countries = ObjectProperty(None)

    slabel1 = StringProperty()
    slabel2 = StringProperty()

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

    def savedstate(self):
        # Here we can retrieve user saved radio button state if one exists
        # Assign optional label values
        self.slabel1 = 'On'
        self.slabel2 = 'Off'
        return ['down', 'normal']

    def switchstate1(self):
        # Switch radio button 1 on and process event trigger
        # Force 'down' state to avoid deselecting all radio buttons (Kivything)
        self.ids.rbutton1.state = 'down'
        # Update optional label values
        self.slabel1 = 'on'
        self.slabel2 = 'off'
        print
        self.ids.rbutton1.state, self.ids.rbutton2.state

    def switchstate2(self):
        # Switch radio button 2 on and process event trigger
        # Force 'down' state to avoid deselecting all radio buttons (Kivything)
        self.ids.rbutton2.state = 'down'
        # Update optional label values
        self.slabel1 = 'off'
        self.slabel2 = 'on'
        print
        self.ids.rbutton1.state, self.ids.rbutton2.state
    
    def spinner_clicked(self, value):
        # get selected dropdown value and change the label text
        self.ids.selected_value.text = f"You have selected {value}"



class MyApp(App):
    def build(self):
        return MyGrid()

if __name__ == "__main__":
    MyApp().run() 
