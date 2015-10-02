# This is the Python version of the example application
# For a C++ implementation, see 'src/example.cpp'

import nanogui
import math
import time

from nanogui import Color, Screen, Window, GroupLayout, BoxLayout, \
                    ToolButton, Vector2i, Label, Button, Widget, \
                    PopupButton, CheckBox, MessageDialog, VScrollPanel, \
                    ImagePanel, ImageView, ComboBox, ProgressBar, Slider, \
                    TextBox, ColorWheel, Graph, VectorXf, GridLayout

from nanogui import GLFW, ENTYPO


class TestApp(Screen):
    def __init__(self):
        super(TestApp, self).__init__(Vector2i(1024, 768), "NanoGUI Test")

        window = Window(self, "Button demo")
        window.setPosition(Vector2i(15, 15))
        window.setLayout(GroupLayout())

        Label(window, "Push buttons", "sans-bold")
        b = Button(window, "Plain button")

        def cb():
            print("pushed!")
        b.setCallback(cb)

        b = Button(window, "Styled", ENTYPO.ICON_ROCKET)
        b.setBackgroundColor(Color(0, 0, 255, 25))
        b.setCallback(cb)

        Label(window, "Toggle buttons", "sans-bold")
        b = Button(window, "Toggle me")
        b.setFlags(Button.Flags.ToggleButton)

        def change_cb(state):
            print("Toggle button state: %s" % str(state))
        b.setChangeCallback(change_cb)

        Label(window, "Radio buttons", "sans-bold")
        b = Button(window, "Radio button 1")
        b.setFlags(Button.Flags.RadioButton)
        b = Button(window, "Radio button 2")
        b.setFlags(Button.Flags.RadioButton)

        Label(window, "A tool palette", "sans-bold")
        tools = Widget(window)
        tools.setLayout(BoxLayout(BoxLayout.Orientation.Horizontal,
                                  BoxLayout.Alignment.Middle, 0, 6))

        ToolButton(tools, ENTYPO.ICON_CLOUD)
        ToolButton(tools, ENTYPO.ICON_FF)
        ToolButton(tools, ENTYPO.ICON_COMPASS)
        ToolButton(tools, ENTYPO.ICON_INSTALL)

        Label(window, "Popup buttons", "sans-bold")
        popupBtn = PopupButton(window, "Popup", ENTYPO.ICON_EXPORT)
        popup = popupBtn.popup()
        popup.setLayout(GroupLayout())
        Label(popup, "Arbitrary widgets can be placed here")
        CheckBox(popup, "A check box")
        popupBtn = PopupButton(popup, "Recursive popup", ENTYPO.ICON_FLASH)
        popup = popupBtn.popup()
        popup.setLayout(GroupLayout())
        CheckBox(popup, "Another check box")

        window = Window(self, "Basic widgets")
        window.setPosition(Vector2i(200, 15))
        window.setLayout(GroupLayout())

        Label(window, "Message dialog", "sans-bold")
        tools = Widget(window)
        tools.setLayout(BoxLayout(BoxLayout.Orientation.Horizontal,
                                  BoxLayout.Alignment.Middle, 0, 6))

        def cb2(result):
            print("Dialog result: %i" % result)

        b = Button(tools, "Info")

        def cb():
            dlg = MessageDialog(self, MessageDialog.Type.Information, "Title",
                                "This is an information message")
            dlg.setCallback(cb2)
        b.setCallback(cb)

        b = Button(tools, "Warn")

        def cb():
            dlg = MessageDialog(self, MessageDialog.Type.Warning, "Title",
                                "This is a warning message")
            dlg.setCallback(cb2)
        b.setCallback(cb)

        b = Button(tools, "Ask")

        def cb():
            dlg = MessageDialog(self, MessageDialog.Type.Warning, "Title",
                                "This is a question message", "Yes", "No",
                                True)
            dlg.setCallback(cb2)
        b.setCallback(cb)

        import os
        import sys
        os.chdir(sys.path[0])
        icons = nanogui.loadImageDirectory(self.nvgContext(), "icons")

        Label(window, "Image panel & scroll panel", "sans-bold")
        imagePanelBtn = PopupButton(window, "Image Panel")
        imagePanelBtn.setIcon(ENTYPO.ICON_FOLDER)
        popup = imagePanelBtn.popup()
        vscroll = VScrollPanel(popup)
        imgPanel = ImagePanel(vscroll)
        imgPanel.setImages(icons)
        popup.setFixedSize(Vector2i(245, 150))
        Label(window, "Selected image", "sans-bold")
        img = ImageView(window)
        img.setFixedSize(Vector2i(40, 40))
        img.setImage(icons[0][0])

        def cb(i):
            print("Selected item %i" % i)
            img.setImage(icons[i][0])
        imgPanel.setCallback(cb)

        Label(window, "File dialog", "sans-bold")
        tools = Widget(window)
        tools.setLayout(BoxLayout(BoxLayout.Orientation.Horizontal,
                                  BoxLayout.Alignment.Middle, 0, 6))
        b = Button(tools, "Open")
        valid = [("png", "Portable Network Graphics"), ("txt", "Text file")]

        def cb():
            result = nanogui.file_dialog(valid, False)
            print("File dialog result = %s" % result)

        b.setCallback(cb)
        b = Button(tools, "Save")

        def cb():
            result = nanogui.file_dialog(valid, True)
            print("File dialog result = %s" % result)

        b.setCallback(cb)

        Label(window, "Combo box", "sans-bold")
        ComboBox(window, ["Combo box item 1", "Combo box item 2",
                          "Combo box item 3"])
        Label(window, "Check box", "sans-bold")

        def cb(state):
            print("Check box 1 state: %s" % state)
        chb = CheckBox(window, "Flag 1", cb)
        chb.setChecked(True)

        def cb(state):
            print("Check box 2 state: %s" % state)
        CheckBox(window, "Flag 2", cb)

        Label(window, "Progress bar", "sans-bold")
        self.progress = ProgressBar(window)

        Label(window, "Slider and text box", "sans-bold")

        panel = Widget(window)
        panel.setLayout(BoxLayout(BoxLayout.Orientation.Horizontal,
                                  BoxLayout.Alignment.Middle, 0, 20))

        slider = Slider(panel)
        slider.setValue(0.5)
        slider.setFixedWidth(80)

        textBox = TextBox(panel)
        textBox.setFixedSize(Vector2i(60, 25))
        textBox.setValue("50")
        textBox.setUnits("%")

        def cb(value):
            textBox.setValue("%i" % int(value * 100))
        slider.setCallback(cb)

        def cb(value):
            print("Final slider value: %i" % int(value * 100))
        slider.setFinalCallback(cb)
        textBox.setFixedSize(Vector2i(60, 25))
        textBox.setFontSize(20)
        textBox.setAlignment(TextBox.Alignment.Right)

        window = Window(self, "Misc. widgets")
        window.setPosition(Vector2i(425, 15))
        window.setLayout(GroupLayout())
        Label(window, "Color wheel", "sans-bold")
        ColorWheel(window)
        Label(window, "Function graph", "sans-bold")
        graph = Graph(window, "Some function")
        graph.setHeader("E = 2.35e-3")
        graph.setFooter("Iteration 89")
        values = VectorXf(100)
        for i in range(100):
            values[i] = 0.5 * (0.5 * math.sin(i / 10.0) +
                               0.5 * math.cos(i / 23.0) + 1)
        graph.setValues(values)

        window = Window(self, "Grid of small widgets")
        window.setPosition(Vector2i(425, 288))
        layout = GridLayout(GridLayout.Orientation.Horizontal, 2,
                            GridLayout.Alignment.Middle, 15, 5)
        layout.setColAlignment(
            [GridLayout.Alignment.Maximum, GridLayout.Alignment.Fill])
        layout.setSpacing(0, 10)
        window.setLayout(layout)

        Label(window, "Floating point :", "sans-bold")
        textBox = TextBox(window)
        textBox.setEditable(True)
        textBox.setFixedSize(Vector2i(100, 20))
        textBox.setValue("50")
        textBox.setUnits("GiB")
        textBox.setDefaultValue("0.0")
        textBox.setFontSize(16)
        textBox.setFormat("[-]?[0-9]*\\.?[0-9]+")

        Label(window, "Positive integer :", "sans-bold")
        textBox = TextBox(window)
        textBox.setEditable(True)
        textBox.setFixedSize(Vector2i(100, 20))
        textBox.setValue("50")
        textBox.setUnits("Mhz")
        textBox.setDefaultValue("0.0")
        textBox.setFontSize(16)
        textBox.setFormat("[1-9][0-9]*")

        Label(window, "Checkbox :", "sans-bold")

        cb = CheckBox(window, "Check me")
        cb.setFontSize(16)
        cb.setChecked(True)

        Label(window, "Combo box :", "sans-bold")
        cobo = ComboBox(window, ["Item 1", "Item 2", "Item 3"])
        cobo.setFontSize(16)
        cobo.setFixedSize(Vector2i(100, 20))

        Label(window, "Color button :", "sans-bold")
        popupBtn = PopupButton(window, "", 0)
        popupBtn.setBackgroundColor(Color(255, 120, 0, 255))
        popupBtn.setFontSize(16)
        popupBtn.setFixedSize(Vector2i(100, 20))
        popup = popupBtn.popup()
        popup.setLayout(GroupLayout())

        colorwheel = ColorWheel(popup)
        colorwheel.setColor(popupBtn.backgroundColor())

        colorBtn = Button(popup, "Pick")
        colorBtn.setFixedSize(Vector2i(100, 25))
        c = colorwheel.color()
        colorBtn.setBackgroundColor(c)

        def cb(value):
            colorBtn.setBackgroundColor(value)

        colorwheel.setCallback(cb)

        def cb(pushed):
            if (pushed):
                popupBtn.setBackgroundColor(colorBtn.backgroundColor())
                popupBtn.setPushed(False)
        colorBtn.setChangeCallback(cb)

        self.performLayout(self.nvgContext())

    def draw(self, ctx):
        self.progress.setValue(math.fmod(time.time() / 10, 1))
        super(TestApp, self).draw(ctx)

    def keyboardEvent(self, key, scancode, action, modifiers):
        if super(TestApp, self).keyboardEvent(key, scancode,
                                              action, modifiers):
            return True
        if key == GLFW.KEY_ESCAPE and action == GLFW.PRESS:
            self.setVisible(False)
            return True
        return False

if __name__ == "__main__":
    nanogui.init()
    test = TestApp()
    test.drawAll()
    test.setVisible(True)
    nanogui.mainloop()
    nanogui.shutdown()
