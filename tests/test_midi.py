from iamkat_MiniLab_3.midi import (
    SYSEX_START,
    SYSEX_END,
    SYSEX_HEADER,
    LED_HEADER,
    CONNECTION_MESSAGE,
    DISCONNECTION_MESSAGE,
    LED_COLORS,
    _led,
)

SYSEX_START_BYTE = 0xF0
SYSEX_END_BYTE = 0xF7


class TestSysexConstants:
    def test_sysex_header_starts_and_contains_vendor(self):
        assert SYSEX_HEADER[0] == SYSEX_START_BYTE
        # Arturia manufacturer ID: 00 20 6B
        assert SYSEX_HEADER[1:4] == (0x00, 0x20, 0x6B)

    def test_led_header_extends_sysex_header(self):
        assert LED_HEADER[:len(SYSEX_HEADER)] == SYSEX_HEADER

    def test_connection_message_is_valid_sysex(self):
        assert CONNECTION_MESSAGE[0] == SYSEX_START_BYTE
        assert CONNECTION_MESSAGE[-1] == SYSEX_END_BYTE

    def test_disconnection_message_is_valid_sysex(self):
        assert DISCONNECTION_MESSAGE[0] == SYSEX_START_BYTE
        assert DISCONNECTION_MESSAGE[-1] == SYSEX_END_BYTE

    def test_connection_and_disconnection_differ_only_in_last_data_byte(self):
        # Same prefix, different trailing byte before SYSEX_END
        assert CONNECTION_MESSAGE[:-2] == DISCONNECTION_MESSAGE[:-2]
        assert CONNECTION_MESSAGE[-2] != DISCONNECTION_MESSAGE[-2]


class TestLed:
    def test_led_is_valid_sysex(self):
        msg = _led(52, 0, 70, 70)
        assert msg[0] == SYSEX_START_BYTE
        assert msg[-1] == SYSEX_END_BYTE

    def test_led_contains_pad_id_and_rgb(self):
        msg = _led(52, 10, 20, 30)
        assert 52 in msg
        assert 10 in msg
        assert 20 in msg
        assert 30 in msg

    def test_led_data_bytes_in_valid_midi_range(self):
        msg = _led(52, 0, 70, 70)
        # Data bytes (everything between start and end) must be 0-127
        for byte in msg[1:-1]:
            assert 0 <= byte <= 127, f"Data byte {byte} out of MIDI range"


class TestLedColors:
    def test_correct_count(self):
        # One message per mapped button: Arp, Pad, Delete, Undo, Stop, Play, Record, Tap
        assert len(LED_COLORS) == 8

    def test_all_valid_sysex(self):
        for msg in LED_COLORS:
            assert msg[0] == SYSEX_START_BYTE
            assert msg[-1] == SYSEX_END_BYTE

    def test_all_data_bytes_in_valid_midi_range(self):
        for msg in LED_COLORS:
            for byte in msg[1:-1]:
                assert 0 <= byte <= 127, f"Data byte {byte} out of MIDI range"

    def test_all_messages_unique(self):
        # Each button should have a distinct SysEx ID (no duplicates)
        assert len(set(LED_COLORS)) == len(LED_COLORS)
