from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.graphics import (Color, Ellipse, Rectangle, Line)


class PainterWidget(Widget):

    def on_touch_down(self, touch):
        with self.canvas:
            Color(0, 1, 0, 1)
            rad = 20
            Ellipse(pos=(touch.x - rad / 2, touch.y - rad / 2), size=(rad, rad))
            touch.ud['Line'] = Line(points=(touch.x, touch.y), width=10)

    def on_touch_move(self, touch):
        touch.ud['Line'].points += (touch.x, touch.y)


class PainApp(App):
    def build(self):
        parent = Widget()
        self.painter = PainterWidget()
        parent.add_widget(self.painter)
        parent.add_widget(Button(text='Clear', on_press = self.clear_canvas, size=(100, 50)))
        return parent

    def clear_canvas(self, instance):
        self.painter.canvas.clear()


if __name__ == '__main__':
    PainApp().run()
