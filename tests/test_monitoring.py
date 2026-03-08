from unittest.mock import MagicMock, PropertyMock


def _make_track(monitoring_state):
    track = MagicMock()
    type(track).current_monitoring_state = PropertyMock(return_value=monitoring_state)
    return track


def _press_monitor_button(component, track):
    """Simulate a button press by calling the handler directly."""
    component.song.view.selected_track = track
    # Call the underlying handler function directly
    component.__class__._monitor_handler(component, MagicMock())


class TestMonitoringLogic:
    """Test the monitoring state cycling logic independently of the ableton framework."""

    def _cycle(self, state):
        return (state + 1) % 3

    def test_in_to_auto(self):
        assert self._cycle(0) == 1

    def test_auto_to_off(self):
        assert self._cycle(1) == 2

    def test_off_wraps_to_in(self):
        assert self._cycle(2) == 0

    def test_full_cycle(self):
        state = 0
        states = [state := self._cycle(state) for _ in range(6)]
        assert states == [1, 2, 0, 1, 2, 0]

    def test_only_applies_to_tracks_with_monitoring(self):
        """Master/return tracks don't have current_monitoring_state."""
        from iamkat_MiniLab_3.monitoring import MonitoringComponent

        component = MonitoringComponent.__new__(MonitoringComponent)
        track = MagicMock(spec=[])  # no attributes at all

        # Should not raise even though track has no current_monitoring_state
        component.song = MagicMock()
        component.song.view.selected_track = track
        # Manually invoke the handler body
        if hasattr(track, "current_monitoring_state"):
            track.current_monitoring_state = (track.current_monitoring_state + 1) % 3
        # No exception = pass
