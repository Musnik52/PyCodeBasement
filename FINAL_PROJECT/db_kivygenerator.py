import time
import threading
from kivy.app import App
from kivy.uix.popup import Popup
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.progressbar import ProgressBar

class myThread(threading.Thread):
    
   def __init__(self, progress_bar):
      threading.Thread.__init__(self)
      self.progress_bar = progress_bar

   def run(self):
        while self.progress_bar.value < 100:
            time.sleep(1/25)
            self.progress_bar.value += 1
        print('Data Imported')

class MyWidget(Widget):
  
    progress_bar = ObjectProperty()
    airline_companies = ObjectProperty(None)
    customers = ObjectProperty(None)
    flights_per_company = ObjectProperty(None)
    tickets_per_customer = ObjectProperty(None)
      
    def __init__(self, **kwa):
        super(MyWidget, self).__init__(**kwa)
        self.progress_bar = ProgressBar()
        self.popup = Popup(title ='Importing', content = self.progress_bar)
        self.popup.bind(on_open = self.puopen)
    
    def pop(self):

        print(  "Airline Companies:", self.airline_companies.text,
                "Customers:", self.customers.text,
                "Flights Per Company:", self.flights_per_company.text,
                "Tickets Per Customer:", self.tickets_per_customer.text)
        self.progress_bar.value = 0
        self.popup.open()
      
    def puopen(self, instance):
        t1 = myThread(self.progress_bar)
        t1.start()
    
    def switchstate1(self):
        self.ids.rbutton1.state = 'down'
        self.ids.rbutton2.state = 'normal'

    def switchstate2(self):
        self.ids.rbutton2.state = 'down'
        self.ids.rbutton1.state = 'normal'

class MyApp(App):
    def build(self): return MyWidget()

if __name__ in ("__main__"): MyApp().run()