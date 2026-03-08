import logging

from ableton.v3.control_surface import Component
from ableton.v3.control_surface.controls import EncoderControl

logger = logging.getLogger(__name__)


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

    @staticmethod
    def _apply(param, value):
        logger.warning('iamkat vol: value=%r type=%s min=%r max=%r',
                       value, type(value).__name__, param.min, param.max)
        scaled = max(param.min, min(param.max, value * param.max))
        logger.warning('iamkat vol: scaled=%r', scaled)
        param.value = scaled

    def _set_track_volume(self, track_idx, value):
        tracks = self.song.tracks
        if track_idx < len(tracks):
            self._apply(tracks[track_idx].mixer_device.volume, value)

    def _set_master_volume(self, value):
        try:
            self._apply(self.song.master_track.mixer_device.volume, value)
        except Exception as e:
            logger.warning('iamkat master vol error: %r', e)

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
