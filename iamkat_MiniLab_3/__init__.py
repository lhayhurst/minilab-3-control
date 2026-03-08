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
from .monitoring import MonitoringComponent
from .navigation import SceneNavigationComponent
from .midi import (
    CONNECTION_MESSAGE,
    DISCONNECTION_MESSAGE,
    LED_COLORS,
    SYSEX_START,
)


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
