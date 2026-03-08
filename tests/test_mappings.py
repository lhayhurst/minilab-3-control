from unittest.mock import MagicMock
from iamkat_MiniLab_3.mappings import create_mappings


def mappings():
    return create_mappings(MagicMock())


class TestMappingsStructure:
    def test_all_components_present(self):
        m = mappings()
        assert "View_Control" in m
        assert "Transport" in m
        assert "View_Based_Recording" in m
        assert "Mixer" in m
        assert "Monitoring" in m
        assert "SceneNavigation" in m
        assert "ViewToggle" in m

    def test_view_control(self):
        m = mappings()
        assert m["View_Control"]["track_encoder"] == "display_encoder"

    def test_transport(self):
        m = mappings()
        t = m["Transport"]
        assert t["play_button"] == "play_button"
        assert t["stop_button"] == "stop_button"

    def test_view_toggle(self):
        m = mappings()
        assert m["ViewToggle"]["view_toggle_button"] == "tap_tempo_button"

    def test_recording(self):
        m = mappings()
        assert m["View_Based_Recording"]["record_button"] == "record_button"

    def test_mixer_arm(self):
        m = mappings()
        assert m["Mixer"]["target_track_arm_button"] == "delete_button"

    def test_mixer_all_faders(self):
        m = mappings()
        mixer = m["Mixer"]
        assert mixer["target_track_volume_control"] == "volume_fader"
        assert mixer["target_track_send_a_control"] == "send_a_fader"
        assert mixer["target_track_send_b_control"] == "send_b_fader"
        assert mixer["target_track_pan_control"] == "pan_fader"

    def test_monitoring(self):
        m = mappings()
        assert m["Monitoring"]["monitor_button"] == "undo_button"

    def test_scene_navigation(self):
        m = mappings()
        nav = m["SceneNavigation"]
        assert nav["scene_up_button"] == "arp_button"
        assert nav["scene_down_button"] == "pad_button"
