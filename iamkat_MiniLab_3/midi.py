from ableton.v3.control_surface.midi import SYSEX_END, SYSEX_START  # noqa: F401 (re-exported)

SYSEX_HEADER = (SYSEX_START, 0, 32, 107, 127, 66)
LED_HEADER = SYSEX_HEADER + (2, 2, 22)

_make_connection_message = lambda byte: SYSEX_HEADER + (2, 0, 64, 106, byte, SYSEX_END)
CONNECTION_MESSAGE = _make_connection_message(33)
DISCONNECTION_MESSAGE = _make_connection_message(32)

# LED color messages — sent on connect to color-code each button's function
# Format: LED_HEADER + (sysex_id, r, g, b, SYSEX_END)  — values 0-127
def _led(sysex_id, r, g, b):
    return LED_HEADER + (sysex_id, r, g, b, SYSEX_END)

LED_COLORS = (
    _led(52,   0,  70,  70),   # Arp (36)    — teal        scene up
    _led(53,   0,  70,  70),   # Pad (37)    — teal        scene down
    _led(54, 100,  40,   0),   # Delete (38) — orange      arm track
    _led(55, 100,  75,   0),   # Undo (39)   — yellow      monitoring
    _led(56, 100,   0,   0),   # Stop (40)   — red
    _led(57,   0, 100,   0),   # Play (41)   — green
    _led(58, 100,   0,  15),   # Record (42) — crimson
    _led(59,   0,  20, 100),   # Tap (43)    — blue
)
