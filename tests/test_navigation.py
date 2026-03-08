from unittest.mock import MagicMock


def _make_song(num_scenes, selected_idx):
    """Build a mock song with a list of scenes and a selected one."""
    song = MagicMock()
    scenes = [MagicMock(name=f"scene_{i}") for i in range(num_scenes)]
    song.scenes = scenes
    song.view.selected_scene = scenes[selected_idx]
    return song


def _nav_up(song):
    scenes = song.scenes
    selected = song.view.selected_scene
    idx = list(scenes).index(selected)
    if idx > 0:
        song.view.selected_scene = scenes[idx - 1]


def _nav_down(song):
    scenes = song.scenes
    selected = song.view.selected_scene
    idx = list(scenes).index(selected)
    if idx < len(scenes) - 1:
        song.view.selected_scene = scenes[idx + 1]


class TestSceneNavigation:
    def test_down_moves_to_next_scene(self):
        song = _make_song(3, 0)
        _nav_down(song)
        assert song.view.selected_scene is song.scenes[1]

    def test_up_moves_to_previous_scene(self):
        song = _make_song(3, 2)
        _nav_up(song)
        assert song.view.selected_scene is song.scenes[1]

    def test_up_does_nothing_at_first_scene(self):
        song = _make_song(3, 0)
        _nav_up(song)
        assert song.view.selected_scene is song.scenes[0]

    def test_down_does_nothing_at_last_scene(self):
        song = _make_song(3, 2)
        _nav_down(song)
        assert song.view.selected_scene is song.scenes[2]

    def test_down_then_up_returns_to_start(self):
        song = _make_song(3, 0)
        _nav_down(song)
        _nav_up(song)
        assert song.view.selected_scene is song.scenes[0]

    def test_single_scene_neither_direction_moves(self):
        song = _make_song(1, 0)
        _nav_up(song)
        assert song.view.selected_scene is song.scenes[0]
        _nav_down(song)
        assert song.view.selected_scene is song.scenes[0]
