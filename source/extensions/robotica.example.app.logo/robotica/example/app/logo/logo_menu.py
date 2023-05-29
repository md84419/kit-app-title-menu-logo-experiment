# Copyright (c), ROBOTICA MACHINE LEARNING LIMITED, 2022.
# License: Apache 2.0

from pathlib import Path
import omni.client

from omni.kit.menu.utils import MenuItemDescription, MenuAlignment
import omni.ext
import omni.kit.app
import omni.ui as ui
import omni.kit.menu.utils
from typing import Union

import omni.kit.window.modifier.titlebar

DATA_PATH = Path(__file__).parent.parent.parent.parent.parent


class RoboticaLogoDelegate(ui.MenuDelegate):
    def destroy(self):
        pass

    def build_item(self, item: ui.MenuHelper):
        with ui.HStack(width=0):
            ui.Spacer(width=0)
            with ui.HStack(content_clipping=1, width=0):
                with ui.Placer(offset_x=-36, offset_y=-1):
                    with ui.Frame(width=80, horizontal_clipping=True):
                        ui.Image(
                            f"{DATA_PATH}/data/icon.png",
                            width=90,
                            height=32,
                            alignment=ui.Alignment.BOTTOM,
                            fill_policy=ui.FillPolicy.PRESERVE_ASPECT_CROP
                        )
            ui.Spacer(width=6)

    def get_menu_alignment(self):
        return MenuAlignment.DEFAULT

    def update_menu_item(self, menu_item: Union[ui.Menu, ui.MenuItem], menu_refresh: bool):
        if isinstance(menu_item, ui.MenuItem):
            menu_item.visible = False


class LogoMenu:
    """
    Place the bottom half of the Robotica logo as the first item in the menu, so it lines up with the top half of
    the Robotica logo from the title bar.
    """
    def __init__(self):
        self._live_menu_name = "Robotica logo Widget"
        self._menu_list = [MenuItemDescription(name="placeholder", show_fn=lambda: False)]

    def register_menu_widgets(self):
        self._cache_state_delegate = RoboticaLogoDelegate()
        omni.kit.menu.utils.add_menu_items(self._menu_list, name=self._live_menu_name, menu_index=-98, delegate=self._cache_state_delegate)
        self._cache_state_delegate.build_item(self._live_menu_name)

    def unregister_menu_widgets(self):
        omni.kit.menu.utils.remove_menu_items(self._menu_list, self._live_menu_name)
        if self._cache_state_delegate:
            self._cache_state_delegate.destroy()
        self._cache_state_delegate = None
        self._menu_list = None
