from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen

from myfirebase import Login

Builder.load_string('''
<MDTextFieldCustom@MDTextFieldRound>
    pos_hint: {"center_x": .5}
    normal_color: 1, 1, 1, 1
    color_active: 0, .5, 1, .5

<LoginScreen>:
    name: "login_screen"

    Image:
        size_hint_y: .2
        source: "resources/logo2.jpeg"
        pos_hint: {"center_x": .5, "center_y": .85}

    MDTextFieldCustom:
        id: email
        hint_text: "correo@ejemplo.com"
        icon_left: 'email'
        size_hint_x: .7
        pos_hint: {"center_x": .5, "center_y": .6}
        on_text_validate: password.focus = True

    MDTextFieldCustom:
        id: password
        hint_text: "password"
        icon_left: 'key-variant'
        password: True
        size_hint_x: .7
        pos_hint: {"center_x": .5, "center_y": .55}

    MDRaisedButton:
        id: login_button
        text: "Ingresar"
        size_hint_y: .06
        pos_hint: {"center_x": .5, "center_y": .45}
        font_size: 30
    
    MDTextButton:
        text: "Olvidaste tu contraseña?"
        pos_hint: {"center_x": .5, "center_y": .4}
        size_hint_x: .4
        custom_color: 0, 0, 0, 1

    MDLabel:
        id: error
        pos_hint: {"center_x": .5, "center_y": .3}
        size_hint_x: .3
        theme_text_color: "Error"
        halign: "center"

    MDTextButton:
        id: signup_button
        text: "Aún no tienes cuenta? [color=#2E97F6]Crear una[/color]"
        pos_hint: {"center_x": .5, "center_y": .03}
        size_hint_x: .8
        markup: True
        custom_color: 0, 0, 0, 1
''')

APP = MDApp.get_running_app()
LOGIN = Login()

class LoginScreen(MDScreen):
    def on_pre_enter(self, *args):
        """[summary]
        When entering the screen it initializes the functions
        to their respective buttons within it
        """
        self.ids.signup_button.bind(on_release=self.load_signup_screen)
        self.ids.login_button.bind(on_release=self.login)

    def load_signup_screen(self, instance):
        """[summary]
        If the signup_screen has not been created, it is created and
        redirected to it by pressing the button Create a new account
        """
        if not APP.root.has_screen("signup_screen"):
            from signup_screen import SignupScreen
            self.signup_screen = SignupScreen()
            APP.root.add_widget(self.signup_screen)

        APP.root.current = "signup_screen"
        
    def login(self, instance):
        """[summary]
        Function in charge of collecting the information entered by the user and checking
        if the user exists in case of being false the error is displayed on the screen
        """
        email = self.ids.email.text
        password = self.ids.password.text
        if email != "":
            if password != "":
                self.login_return = LOGIN.login(email=email, password=password)
                
                if not self.login_return == "True":
                    self.ids.error.text = str(self.login_return)
            else:
                self.ids.error.text = "Favor Ingresar Contraseña"
        else:
            self.ids.error.text = "Debes Ingresar un Correo"