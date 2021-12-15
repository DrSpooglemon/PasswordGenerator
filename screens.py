from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.label import Label


class MainScreen(Screen):
    '''Generic Kivy screen'''
    def __init__(self, callback, **kwargs):
        super().__init__(**kwargs)
        #self.add_widget(
        self.password_display = Label(
                color=(0, 0, 0, 1),
                font_size=25,
                size_hint=(None, None),
                pos_hint={'center_x': .5,
                          'center_y': .6})

        # self.password_display = Label(
        #     color=(0, 0, 0, 1),
        #     size_hint=(None, None),
        #     pos_hint={'center_x': .5,
        #               'center_y': .5})
        self.add_widget(self.password_display)

        self.add_widget(
            Button(
                text='Generate',
                on_release=callback,
                size_hint=(None, None),
                size=(120, 40),
                pos_hint={'center_x': .5,
                          'center_y': .5}))

    def update_display(self, text):
        self.password_display.text = text