from kivy.config import Config
Config.read('config.ini')
from kivy.core.window import Window
Window.clearcolor = 1, 1, 1, 1
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.properties import StringProperty
from kivy.clock import Clock
from screens import *
from password_generator import generate_password


class App(App):
    '''Generic Kivy app'''
    screen_manager = ScreenManager()
    display_string = StringProperty('')
    password = StringProperty('Secure Password Generator')

    def build(self):
        self.main_screen = MainScreen(callback=self.button_pressed)
        self.screen_manager.add_widget(self.main_screen)
        self.display_string = self.password
        return self.screen_manager

    def button_pressed(self, btn):
        if btn.text == 'Generate':
            self.password = generate_password(25)

    def on_password(self, _, text):
        print(text)
        self.char_index = len(text)-1
        Clock.schedule_interval(self._update_password, .0001)

    def _update_password(self, _):
        i = self.char_index
        op, od = ord(self.password[i]), ord(self.display_string[i])
        c = chr(od + (op > od) - (op < od))
        self.display_string = c.join(
            [self.display_string[:i], self.display_string[i+1:]])
        self.char_index -= self.password[i] == self.display_string[i]
        return self.password != self.display_string

    def on_display_string(self, _, text):
        self.main_screen.update_display(text)


if __name__ == '__main__':
    App().run()