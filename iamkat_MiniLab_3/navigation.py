from ableton.v3.control_surface import Component
from ableton.v3.control_surface.controls import ButtonControl


class SceneNavigationComponent(Component):
    """Moves the selected scene up or down in the Session View."""
    scene_up_button = ButtonControl()
    scene_down_button = ButtonControl()

    @scene_up_button.pressed
    def scene_up_button(self, _):
        scenes = self.song.scenes
        selected = self.song.view.selected_scene
        idx = list(scenes).index(selected)
        if idx > 0:
            self.song.view.selected_scene = scenes[idx - 1]

    @scene_down_button.pressed
    def scene_down_button(self, _):
        scenes = self.song.scenes
        selected = self.song.view.selected_scene
        idx = list(scenes).index(selected)
        if idx < len(scenes) - 1:
            self.song.view.selected_scene = scenes[idx + 1]
