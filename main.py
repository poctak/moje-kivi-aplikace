
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class Calculator(BoxLayout):
    def calculate(self):
        try:
            self.ids.result.text = str(eval(self.ids.input.text))
        except:
            self.ids.result.text = "Chyba"

class CalculatorApp(App):
    def build(self):
        return Calculator()

if __name__ == "__main__":
    CalculatorApp().run()
