from kivy.lang import Builder
from kivy.properties import ObjectProperty

from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout

KV = '''
<ContentNavigationDrawer>

    ScrollView:

        MDList:

            OneLineListItem:
                text: "Страница 1"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "scr 1"

            OneLineListItem:
                text: "Страница 2"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "scr 2"
        
            OneLineListItem:
                text: "Страница 3"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "scr 3"
                    
            OneLineListItem:
                text: "Страница 4"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "scr 4"


MDScreen:

    MDToolbar:
        id: toolbar
        pos_hint: {"top": 1}
        elevation: 10
        title: "Это приложение, мать его!"
        left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]

    MDNavigationLayout:
        x: toolbar.height

        ScreenManager:
            id: screen_manager

            MDScreen:
                name: "scr 1"

                MDLabel:
                    
                    text: "Вместе весело шагать по просторам"
                    # halign: "center"
                    pos: "30dp", "210dp"
                    font_size: "40dp"
                    color: [0, 0, 1, 1]
                    

            MDScreen:
                name: "scr 2"
                
                MDLabel:
                    text: "Я люблю тебя жизнь и надеюсь это взаимно"
                    pos: "100dp", "210dp"
                    color: [1, 0, 0, 1]
                    font_size: "30dp"
                    
            MDScreen:
                name: "scr 3"

                MDLabel:
                    text: "Следующая станция метро - 'Пролетарская'"
                    pos: "30dp", "210dp"
                    font_size: "20dp"
        
            MDScreen:
                name: "scr 4"

                MDLabel:
                    text: "У матросов нет вопросов"
                    pos: "30dp", "210dp"
                    

        MDNavigationDrawer:
            id: nav_drawer

            ContentNavigationDrawer:
                screen_manager: screen_manager
                nav_drawer: nav_drawer
'''


class ContentNavigationDrawer(MDBoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class TestNavigationDrawer(MDApp):
    def build(self):
        return Builder.load_string(KV)


TestNavigationDrawer().run()
