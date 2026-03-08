import Live

from ableton.v3.control_surface import Component
from ableton.v3.control_surface.controls import ButtonControl


class ViewToggleComponent(Component):
    """Toggles between Session and Arrangement views."""
    view_toggle_button = ButtonControl()

    @view_toggle_button.pressed
    def view_toggle_button(self, _):
        view = Live.Application.get_application().view
        if view.focused_document_view == 'Session':
            view.show_view('Arranger')
        else:
            view.show_view('Session')
