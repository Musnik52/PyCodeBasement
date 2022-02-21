import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols =2
        self.add_widget(Label(text="Airline Companies: "))
        self.name =TextInput(multiline=False)
        self.add_widget(self.name)
        self.add_widget(Label(text="Customers: "))
        self.lastName =TextInput(multiline=False)
        self.add_widget(self.lastName)
        self.add_widget(Label(text="Administrators: "))
        self.email =TextInput(multiline=False)
        self.add_widget(self.email)
        self.add_widget(Label(text="Flights Per Company: "))
        self.name =TextInput(multiline=False)
        self.add_widget(self.name)
        self.add_widget(Label(text="Tickets Per Customer: "))
        self.lastName =TextInput(multiline=False)
        self.add_widget(self.lastName)
        self.add_widget(Label(text="Countries: "))
        self.email =TextInput(multiline=False)
        self.add_widget(self.email)


class MyApp(App): #הרצת האפליקציה
    def build(self):
        return MyGrid()#קריאה לאפליקציית העמודות

if __name__ == "__main__":
    MyApp().run() #הרצה בפועל של האפליקציה
