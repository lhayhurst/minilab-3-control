from ableton.v3.control_surface import Component
from ableton.v3.control_surface.controls import EncoderControl


class VolumeComponent(Component):
    """Maps rotaries 1-7 to track volumes 1-7 and rotary 8 to master volume."""

    rotary_1 = EncoderControl()
    rotary_2 = EncoderControl()
    rotary_3 = EncoderControl()
    rotary_4 = EncoderControl()
    rotary_5 = EncoderControl()
    rotary_6 = EncoderControl()
    rotary_7 = EncoderControl()
    rotary_8 = EncoderControl()

    def _set_track_volume(self, track_idx, value):
        tracks = self.song.tracks
        if track_idx < len(tracks):
            param = tracks[track_idx].mixer_device.volume
            param.value = value / 127.0 * param.max

    def _set_master_volume(self, value):
        param = self.song.master_track.mixer_device.volume
        param.value = value / 127.0 * param.max

    @rotary_1.value
    def rotary_1(self, value, _): self._set_track_volume(0, value)

    @rotary_2.value
    def rotary_2(self, value, _): self._set_track_volume(1, value)

    @rotary_3.value
    def rotary_3(self, value, _): self._set_track_volume(2, value)

    @rotary_4.value
    def rotary_4(self, value, _): self._set_track_volume(3, value)

    @rotary_5.value
    def rotary_5(self, value, _): self._set_track_volume(4, value)

    @rotary_6.value
    def rotary_6(self, value, _): self._set_track_volume(5, value)

    @rotary_7.value
    def rotary_7(self, value, _): self._set_track_volume(6, value)

    @rotary_8.value
    def rotary_8(self, value, _): self._set_master_volume(value)
