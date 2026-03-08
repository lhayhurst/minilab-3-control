from ableton.v3.control_surface import Component
from ableton.v3.control_surface.controls import ButtonControl


class SoloComponent(Component):
    """Toggles solo on the selected track."""
    solo_button = ButtonControl()

    @solo_button.pressed
    def solo_button(self, _):
        track = self.song.view.selected_track
        if hasattr(track, 'solo'):
            track.solo = not track.solo
