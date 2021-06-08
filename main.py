from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder
from kivy.metrics import dp

from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivymd.uix.datatables import MDDataTable

class W1(Screen):

    pass

class W2(Screen):

    data = {
        "Pause":"motion-pause-outline",
        "Skip Question":'skip-next-outline',
        "Leave Quiz":'location-exit',
        "Exit Application":'exit-to-app'
    }
    def callback(self, instance):
        
        if instance.icon == 'exit-to-app':

            MDApp.get_running_app().stop()

        elif instance.icon == 'location-exit':

            pass

        elif instance.icon == 'skip-next-outline':
            
            pass
        
        elif instance.icon == 'motion-pause-outline':
            
            pass
        
        else:
            
            pass

class W3(Screen):

    pass

class W4(Screen):

    pass

class W5(Screen):

    pass

class W6(Screen):

    def show_table(self):
    
        self.data_tables = MDDataTable(
            size_hint=(1, 0.7),
            use_pagination=False,
            check=False,
            column_data=[
                ("No.", dp(70)),
                ("Player Name", dp(60)),
                ("Score", dp(40)),
            ],
            row_data=[
                ("1", "Nithish", "2049"),
                ("2", "Kishore", "4903"),
                ("3", "Abimama", "4344"),
                ("4", "DhyanuMama", "0390"),
            ],
            sorted_on="Score",
            sorted_order="ASC",
            elevation=5
        )
        self.data_tables.bind(on_row_press=self.activate)
        self.add_widget(self.data_tables)
    def activate(self, instance_table, instance_row):
        print(instance_table, instance_row)
        self.ids.edit_player.disabled = False
    
class W7(Screen):
    
    def start(self):

        self.ids.l.start()

class Wm1(ScreenManager):

    dialog = None
    
    def ask_confirmation(self):

        if not self.dialog:

            self.dialog = MDDialog(
                title = 'Confirm Exit?',
                text = 'Do you Really want to Exit?',
                buttons = [
                    MDFlatButton(
                        text = "Cancel", on_release = self.close_dialog
                    ),
                    MDFlatButton(
                        text = "Exit", on_release = self.close
                    ),
                ],
            )
        
        self.dialog.open()
    
    def lol(self):
        self.current = 'playerstats'
        self.transition.direction = 'left'
        
    def close_dialog(self, *args):

        self.dialog.dismiss()
        
    def back(self):

        self.current = 'screen1'
        self.transition.direction = 'right'

    def close(self, *args):

        MDApp.get_running_app().stop()

class QuizApp(MDApp):

    def build(self):

        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "LightBlue"
        self.theme_cls.accent_palette = 'Red'
        
        return Builder.load_file('app_design.kv')
    def darkmode(self, var):
        if var == 'on':
            self.theme_cls.theme_style = "Dark"
        elif var == 'off':
            self.theme_cls.theme_style = "Light"
QuizApp().run()