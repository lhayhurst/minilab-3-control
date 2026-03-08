from ableton.v3.control_surface import Component
from ableton.v3.control_surface.controls import ButtonControl


class ClipLaunchComponent(Component):
    """Fires the clip at the selected scene row for each of the 8 session tracks."""

    clip_launch_1_button = ButtonControl()
    clip_launch_2_button = ButtonControl()
    clip_launch_3_button = ButtonControl()
    clip_launch_4_button = ButtonControl()
    clip_launch_5_button = ButtonControl()
    clip_launch_6_button = ButtonControl()
    clip_launch_7_button = ButtonControl()
    clip_launch_8_button = ButtonControl()

    def _launch(self, track_idx):
        tracks = self.song.tracks
        scenes = self.song.scenes
        scene_idx = list(scenes).index(self.song.view.selected_scene)
        if track_idx < len(tracks):
            tracks[track_idx].clip_slots[scene_idx].fire()

    @clip_launch_1_button.pressed
    def clip_launch_1_button(self, _): self._launch(0)

    @clip_launch_2_button.pressed
    def clip_launch_2_button(self, _): self._launch(1)

    @clip_launch_3_button.pressed
    def clip_launch_3_button(self, _): self._launch(2)

    @clip_launch_4_button.pressed
    def clip_launch_4_button(self, _): self._launch(3)

    @clip_launch_5_button.pressed
    def clip_launch_5_button(self, _): self._launch(4)

    @clip_launch_6_button.pressed
    def clip_launch_6_button(self, _): self._launch(5)

    @clip_launch_7_button.pressed
    def clip_launch_7_button(self, _): self._launch(6)

    @clip_launch_8_button.pressed
    def clip_launch_8_button(self, _): self._launch(7)
