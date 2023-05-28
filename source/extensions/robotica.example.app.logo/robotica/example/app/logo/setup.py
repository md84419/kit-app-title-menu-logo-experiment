# Copyright (c), ROBOTICA MACHINE LEARNING LIMITED, 2022.
# License: Apache 2.0

import asyncio
from pathlib import Path

import carb.imgui as _imgui
import carb.settings
import carb.tokens
import omni.ext
import omni.kit.ui as ui
import omni.kit.menu.utils
from omni.kit.menu.utils import MenuLayout
from omni.kit.quicklayout import QuickLayout
from omni.kit.window.title import get_main_window_title

from .logo_menu import LogoMenu

async def _load_layout(layout_file: str):
    """this private methods just help loading layout, you can use it in the Layout Menu"""
    await omni.kit.app.get_app().next_update_async()
    QuickLayout.load_file(layout_file)


# This extension is mostly loading the Layout updating menu
class SetupExtension(omni.ext.IExt):
    # ext_id is current extension id. It can be used with extension manager to query additional information, like where
    # this extension is located on filesystem.
    def on_startup(self, ext_id):

        # get the settings
        self._settings = carb.settings.get_settings()

        self._await_layout = asyncio.ensure_future(self._delayed_layout())
        # setup the menu and their layout
        self._setup_menu()

        # setup the Application Title
        window_title = get_main_window_title()
        window_title.set_app_version(self._settings.get("/app/titleVersion"))

        # setup some imgui Style overide
        imgui = _imgui.acquire_imgui()
        imgui.push_style_color(_imgui.StyleColor.ScrollbarGrab, carb.Float4(0.4, 0.4, 0.4, 1))
        imgui.push_style_color(_imgui.StyleColor.ScrollbarGrabHovered, carb.Float4(0.6, 0.6, 0.6, 1))
        imgui.push_style_color(_imgui.StyleColor.ScrollbarGrabActive, carb.Float4(0.8, 0.8, 0.8, 1))

        imgui.push_style_var_float(_imgui.StyleVar.DockSplitterSize, 1)

        self._is_darker_mode = False
        self._toggle_darker_mode()

        self._logo_menu = LogoMenu()
        self._logo_menu.register_menu_widgets()

    def _toggle_darker_mode(self):
        """Update Imgui to be on its darker Mode state vs the default Create/View mode"""
        self._is_darker_mode = not self._is_darker_mode
        if self._is_darker_mode:
            black = carb.Float4(0.0, 0.0, 0.0, 1)
            dark0 = carb.Float4(0.058, 0.058, 0.058, 1)  # title bar colour
            dark1 = carb.Float4(0.09, 0.094, 0.102, 1)
            # dark2 = carb.Float4(0.122, 0.129, 0.149, 1)  # carb.Float4(0.129, 0.129, 0.149, 1)
            # mid1 = carb.Float4(0.157, 0.157, 0.157, 1)  # carb.Float4(0.157, 0.157, 0.18, 1)
            mid2 = carb.Float4(0.22, 0.22, 0.22, 1)  # colour of the bottom info bar
            blue = carb.Float4(0.058, 0.058, 1, 1)

            menu_bar = dark0
            title_bar = dark0
            background = dark0
            popup_bg = black
            tab = dark0
            tab_unfocussed = dark0
            frame = dark1
            window_bg = mid2
        else:
            menu_bar = carb.Float4(0.27, 0.27, 0.27, 1)
            title_bar = carb.Float4(0.12, 0.12, 0.12, 1)
            popup_bg = carb.Float4(0.22, 0.22, 0.22, 1)
            tab = carb.Float4(0.192, 0.192, 0.192, 1)
            background = menu_bar
            tab_unfocussed = carb.Float4(0.27 / 1.5, 0.27 / 1.5, 0.27 / 1.5, 1)
            frame = title_bar

        imgui = _imgui.acquire_imgui()
        imgui.push_style_color(_imgui.StyleColor.MenuBarBg, menu_bar)
        imgui.push_style_color(_imgui.StyleColor.TitleBg, title_bar)
        imgui.push_style_color(_imgui.StyleColor.TitleBgActive, title_bar)

        imgui.push_style_color(_imgui.StyleColor.PopupBg, popup_bg)

        imgui.push_style_color(_imgui.StyleColor.FrameBg, frame)
        imgui.push_style_color(_imgui.StyleColor.NavHighlight, blue)
        imgui.push_style_color(_imgui.StyleColor.NavWindowingDimBg, blue)

        imgui.push_style_color(_imgui.StyleColor.WindowBg, window_bg)
        imgui.push_style_color(_imgui.StyleColor.Border, window_bg)
        imgui.push_style_color(_imgui.StyleColor.ChildBg, background)

        imgui.push_style_color(_imgui.StyleColor.Tab, tab)
        imgui.push_style_color(_imgui.StyleColor.TabActive, tab)
        imgui.push_style_color(_imgui.StyleColor.TabUnfocusedActive, tab_unfocussed)
        imgui.push_style_color(_imgui.StyleColor.TabUnfocused, tab_unfocussed)
        imgui.push_style_color(_imgui.StyleColor.TabHovered, tab)

    async def _delayed_layout(self):

        # few frame delay to allow automatic Layout of window that want their own positions
        for i in range(4):
            await omni.kit.app.get_app().next_update_async()

        settings = carb.settings.get_settings()
        # setup the Layout for your app
        layouts_path = carb.tokens.get_tokens_interface().resolve("${robotica.example.app.logo}/layouts")
        layout_file = Path(layouts_path).joinpath(f"{settings.get('/app/layout/name')}.json")
        asyncio.ensure_future(_load_layout(f"{layout_file}"))

        # using imgui directly to adjust some color and Variable
        imgui = _imgui.acquire_imgui()

        # DockSplitterSize is the variable that drive the size of the Dock Split connection
        imgui.push_style_var_float(_imgui.StyleVar.DockSplitterSize, 2)

        editor_menu = ui.get_editor_menu()
        editor_menu.set_priority("File", -96)

    def _setup_menu(self):
        editor_menu = ui.get_editor_menu()
        # you can have some file Menu
        self._file_open = editor_menu.add_item("File/Open", self._open_file)

        # some Menu Item
        self._help_menu = editor_menu.add_item("Help/Show", self._show_help)

        # from omni.kit.menu.utils import MenuLayout
        # self._menu_layout = [
        #         MenuLayout.Menu("Window", [
        #             MenuLayout.Item("MyWindow"),
        #         ]),
        # ]
        # omni.kit.menu.utils.add_layout(self._menu_layout)

    def _show_help(self, menu, toggled):
        print("Help is Coming")

    def _open_file(self, menu, toggled):
        print("Open the File you want")

    def on_shutdown(self):
        self._logo_menu.unregister_menu_widgets()
