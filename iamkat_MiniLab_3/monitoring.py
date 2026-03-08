from ableton.v3.control_surface import Component
from ableton.v3.control_surface.controls import ButtonControl


class MonitoringComponent(Component):
    """Cycles selected track monitoring state: In → Auto → Off → In → ..."""
    monitor_button = ButtonControl()

    @monitor_button.pressed
    def monitor_button(self, _):
        track = self.song.view.selected_track
        if hasattr(track, 'current_monitoring_state'):
            track.current_monitoring_state = (track.current_monitoring_state + 1) % 3
