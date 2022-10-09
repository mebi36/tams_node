from typing import Any

import PySimpleGUI as sg

from app.basegui import BaseGUIWindow


class FingerprintGenericWindow(BaseGUIWindow):
    """Base window. Provides the layout for the fingerprint capture
    window for the application."""

    @classmethod
    def window(cls) -> sg.Window:
        """Construct layout/appearance of window."""
        layout = [
            [sg.Push(), sg.Text(cls.window_title()), sg.Push()],
            [sg.Push(), cls.message_display_field(), sg.Push()],
            [sg.VPush()],
            [
                sg.Push(),
                sg.Image(cls.get_icon("fingerprint_grey", 1.3)),
                sg.Push(),
            ],
            [sg.VPush()],
            [
                sg.Push(),
                cls.get_camera_button(),
                sg.Button(
                    image_data=cls.get_icon("cancel", 0.6),
                    button_color=cls.ICON_BUTTON_COLOR,
                    key="cancel",
                    use_ttk_buttons=True,
                ),
                sg.Push(),
            ],
        ]
        window = sg.Window(
            "Fingerprint Verification", layout, **cls.window_init_dict()
        )
        return window

    @classmethod
    def get_camera_button(cls) -> Any:
        """Return camera button for GUI window layout.

        Will be visible if only if a verification window is open.
        """
        if "verification" in cls.__name__.lower():
            return sg.pin(
                sg.Button(
                    image_data=cls.get_icon("camera", 0.6),
                    button_color=cls.ICON_BUTTON_COLOR,
                    key="camera",
                    visible=True,
                    use_ttk_buttons=True,
                )
            )
        else:
            return sg.pin(
                sg.Button(
                    image_data=cls.get_icon("camera", 0.6),
                    button_color=cls.ICON_BUTTON_COLOR,
                    key="camera",
                    visible=False,
                    use_ttk_buttons=True,
                )
            )

    @classmethod
    def window_title(cls) -> str:
        """Title of GUI window."""
        return "Fingerprint Scan"
