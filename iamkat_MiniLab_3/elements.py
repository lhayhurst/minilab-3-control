from ableton.v3.control_surface import MIDI_NOTE_TYPE, ElementsBase, MapMode
from ableton.v3.control_surface.elements import EncoderElement

NUM_TRACKS = 8
NUM_SCENES = 1


class Elements(ElementsBase):
    def __init__(self, *a, **k):
        super().__init__(*a, **k)

        # Main encoder (relative, sends CC 28)
        self.add_encoder(28, 'Display_Encoder', map_mode=MapMode.LinearBinaryOffset)

        # Transport / function buttons — MIDI mode, ch9
        # Physical: Arp=36, Pad=37, Prog/Delete=38, Undo=39, Stop=40, Play=41, Record=42, Tap=43
        self.add_button(36, 'Arp_Button',       msg_type=MIDI_NOTE_TYPE, channel=9)
        self.add_button(37, 'Pad_Button',       msg_type=MIDI_NOTE_TYPE, channel=9)
        self.add_button(38, 'Delete_Button',    msg_type=MIDI_NOTE_TYPE, channel=9)
        self.add_button(39, 'Undo_Button',      msg_type=MIDI_NOTE_TYPE, channel=9)
        self.add_button(40, 'Stop_Button',      msg_type=MIDI_NOTE_TYPE, channel=9)
        self.add_button(41, 'Play_Button',      msg_type=MIDI_NOTE_TYPE, channel=9)
        self.add_button(42, 'Record_Button',    msg_type=MIDI_NOTE_TYPE, channel=9)
        self.add_button(43, 'Tap_Tempo_Button', msg_type=MIDI_NOTE_TYPE, channel=9)

        # Faders (factory MIDI mode CCs)
        self.add_element('Volume_Fader', EncoderElement, 14)
        self.add_element('Send_A_Fader', EncoderElement, 15)
        self.add_element('Send_B_Fader', EncoderElement, 30)
        self.add_element('Pan_Fader',    EncoderElement, 31)
