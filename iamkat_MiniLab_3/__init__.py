from ableton.v3.control_surface import ControlSurface, ControlSurfaceSpecification
from ableton.v3.control_surface.capabilities import (
    AUTO_LOAD_KEY,
    CONTROLLER_ID_KEY,
    NOTES_CC,
    PORTS_KEY,
    SCRIPT,
    controller_id,
    inport,
    outport,
)

from .elements import NUM_SCENES, NUM_TRACKS, Elements
from .mappings import create_mappings
from .clip_launch import ClipLaunchComponent
from .monitoring import MonitoringComponent
from .navigation import SceneNavigationComponent
from .midi import (
    CONNECTION_MESSAGE,
    DISCONNECTION_MESSAGE,
    LED_COLORS,
    SYSEX_START,
)

# Rotary CC → track index (0-6 = tracks 1-7, 7 = master)
_ROTARY_CC_TO_IDX = {86: 0, 87: 1, 89: 2, 90: 3, 110: 4, 111: 5, 116: 6, 117: 7}


def get_capabilities():
    return {
        AUTO_LOAD_KEY: True,
        PORTS_KEY: [
            inport(props=[NOTES_CC, SCRIPT]),
            inport(props=[NOTES_CC]),
            outport(props=[NOTES_CC, SCRIPT]),
            outport(props=[NOTES_CC]),
        ],
        CONTROLLER_ID_KEY: controller_id(
            vendor_id=7285,
            product_ids=[8715],
            model_name=['Minilab3'],
        ),
    }


def create_instance(c_instance):
    return IamkatMiniLab3(specification=Specification, c_instance=c_instance)


class Specification(ControlSurfaceSpecification):
    elements_type = Elements
    num_tracks = NUM_TRACKS
    num_scenes = NUM_SCENES
    link_session_ring_to_track_selection = True
    create_mappings_function = create_mappings
    identity_response_id_bytes = (0, 32, 107, 2, 0, 4)
    hello_messages = (CONNECTION_MESSAGE,) + LED_COLORS
    goodbye_messages = (DISCONNECTION_MESSAGE,)
    component_map = {
        'ClipLaunch': ClipLaunchComponent,
        'Monitoring': MonitoringComponent,
        'SceneNavigation': SceneNavigationComponent,
    }


class IamkatMiniLab3(ControlSurface):
    def __init__(self, *a, **k):
        super().__init__(*a, **k)
        self._c_instance.log_message('iamkat_MiniLab_3: loaded')

    def _do_send_midi(self, midi_event_bytes):
        if midi_event_bytes[0] == SYSEX_START:
            super()._do_send_midi(midi_event_bytes)

    def receive_midi(self, midi_bytes):
        # Intercept CC-on-ch0 messages for the 8 rotaries and set volume directly
        # from the absolute CC value (0-127), bypassing EncoderControl's delta
        # tracking which caused pickup jumps and a false volume floor.
        if len(midi_bytes) == 3:
            status, cc, value = midi_bytes
            if (status & 0xF0) == 0xB0 and (status & 0x0F) == 0:
                idx = _ROTARY_CC_TO_IDX.get(cc)
                if idx is not None:
                    self._set_rotary_volume(idx, value)
                    return
        super().receive_midi(midi_bytes)

    def _set_rotary_volume(self, idx, raw):
        try:
            normalized = raw / 127.0
            if idx < 7:
                tracks = self.song.tracks
                if idx < len(tracks):
                    param = tracks[idx].mixer_device.volume
                    param.value = max(param.min, min(param.max, normalized * param.max))
            else:
                param = self.song.master_track.mixer_device.volume
                param.value = max(param.min, min(param.max, normalized * param.max))
        except Exception as e:
            self._c_instance.log_message(f'iamkat rotary err: {e!r}')
