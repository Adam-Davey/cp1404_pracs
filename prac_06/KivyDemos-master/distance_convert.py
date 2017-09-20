from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

__author__ = 'Adam Davey'

Miles_to_Kms = 1.60934


class MilesconverterApp(App):
    def build(self):

        Window.size = (400, 200)
        self.title = "miles to kms converter"
        self.root = Builder.load_file('distance_convert.kv')
        return self.root

    def handle_calculate(self, miles_text):

        try:
            kms = float(miles_text) * Miles_to_Kms
            self.root.ids.output_label.text = str("{:.2f}".format(kms))
        except:
            ValueError

    def get_validated_miles(self):
        kms = self.root.ids.input_label.text
        return


        # def handle_increment(self change):
        #     value = self.get_validated_miles() + change
        #     self.root.ids.input_miles.text = str(value)
        #     self.handle_calculate()


MilesconverterApp().run()
