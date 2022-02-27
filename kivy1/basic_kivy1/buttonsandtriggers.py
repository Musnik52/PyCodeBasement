import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyGridAndButton(GridLayout):

    def __init__(self, **kwargs):
        super(MyGridAndButton, self).__init__(**kwargs)
        self.cols = 1# #הגדרת רשת ראשית בעלת עמודה אחת
        self.inside = GridLayout() #יצירת רשת פנימית
        self.inside.cols = 2#הגדרת רשת פנימית בעלת 2 עמודות
        # כאן יוצגו הנתונים ברשת הפנימית
        self.inside.add_widget(Label(text = "Airline Companies: "))
        self.airline_companies=TextInput(multiline = False)
        self.inside.add_widget(self.airline_companies)
        self.inside.add_widget(Label(text="Customers: "))
        self.customers=TextInput(multiline=False)
        self.inside.add_widget(self.customers)
        self.inside.add_widget(Label(text="Administrators: "))
        self.administrators=TextInput(multiline=False)
        self.inside.add_widget(self.administrators)
        self.inside.add_widget(Label(text="Flights Per Company: "))
        self.flights_per_company=TextInput(multiline=False)
        self.inside.add_widget(self.flights_per_company)
        self.inside.add_widget(Label(text="Tickets Per Customer: "))
        self.tickets_per_customer=TextInput(multiline=False)
        self.inside.add_widget(self.tickets_per_customer)
        self.inside.add_widget(Label(text="Countries: "))
        self.countries=TextInput(multiline=False)
        self.inside.add_widget(self.countries)
        #כאן הנתונים שיוצגו ברשת הראשית
        self.add_widget(self.inside) # Add the interior layout to the main
        self.submit = Button(text="Submit", font_size=40, size_hint_y=None, height=50)
        self.submit.bind(on_press = self.pressed)
        '''self.submit.bind =  קישור פעולה לכפתור שהגדרנו
        self.pressed = שם הפעולה (פונ') המקושרת'''
        self.add_widget(self.submit) # Add the button to the main layout

    def pressed(self, instance):
        # Get the value of all of the tex inputs
        airline_companies =self.airline_companies.text
        customers = self.customers.text
        administrators = self.administrators.text
        flights_per_company = self.flights_per_company.text
        tickets_per_customer = self.tickets_per_customer.text
        countries =self.countries.text
        # print the values to the console
        print(  "Airline Companies:", airline_companies, 
                "Customers:", customers,
                "Administrators:", administrators,
                "Flights Per Company:", flights_per_company,
                "Tickets Per Customer:", tickets_per_customer,
                "Countries:", countries)
        # Reset text to blank in each text input
        self.airline_companies.text =""
        self.customers.text =""
        self.administrators.text =""
        self.flights_per_company.text =""
        self.tickets_per_customer.text =""
        self.countries.text =""

class MyApp(App): #הרצת האפליקציה
    def build(self):
        return MyGridAndButton()#קריאה לאפליקציית העמודות

if __name__ == "__main__":
    MyApp().run() #הרצה בפועל של האפליקציה
