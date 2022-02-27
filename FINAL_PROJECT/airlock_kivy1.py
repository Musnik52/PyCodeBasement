from kivy.app import App
import time
import threading
from kivy.uix.progressbar import ProgressBar
from kivy.uix.popup import Popup
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.core.window import Window

class myThread (threading.Thread):

   def __init__(self, progress_bar):
      threading.Thread.__init__(self)
      self.progress_bar = progress_bar

   def run(self):
        while self.progress_bar.value < 100:
            self.progress_bar.value += 1
            print(self.progress_bar.value)
            time.sleep(1/25)

class MyWidget(Widget):
  
    progress_bar = ObjectProperty()
    airline_companies = ObjectProperty(None)
    customers = ObjectProperty(None)
    administrators = ObjectProperty(None)
    flights_per_company = ObjectProperty(None)
    tickets_per_customer = ObjectProperty(None)
    countries = ObjectProperty(None)
      
    def __init__(self, **kwa):
        super(MyWidget, self).__init__(**kwa)
        self.progress_bar = ProgressBar()
        self.popup = Popup(title ='Importing', content = self.progress_bar)
        self.popup.bind(on_open = self.puopen)

    def pop(self):
        print(  "Airline Companies:", self.airline_companies.text,
                "Customers:", self.customers.text,
                "Administrators:", self.administrators.text,
                "Flights Per Company:", self.flights_per_company.text,
                "Tickets Per Customer:", self.tickets_per_customer.text,
                "Countries:", self.countries.text)
        self.progress_bar.value = 1
        self.popup.open()

    def next(self, dt):
        if self.progress_bar.value>= 100:
            return False
        self.progress_bar.value += 1
      
    def puopen(self, instance):
        t1 = myThread (self.progress_bar)
        t1.start()

class MyApp(App):
    def build(self):
        return MyWidget()

if __name__ in ("__main__"):
    MyApp().run()