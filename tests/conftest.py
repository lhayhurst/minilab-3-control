"""
Mock the ableton.v3 framework before any test imports.
This runs at collection time so all modules can be imported outside Live.
"""
import sys
from unittest.mock import MagicMock

# MIDI constants the real module re-exports
_midi = MagicMock()
_midi.SYSEX_START = 0xF0
_midi.SYSEX_END = 0xF7

# Component base class — plain object so subclassing works normally
_cs = MagicMock()
_cs.Component = object
_cs.MIDI_NOTE_TYPE = 1

sys.modules.setdefault("Live", MagicMock())
sys.modules.setdefault("ableton", MagicMock())
sys.modules.setdefault("ableton.v3", MagicMock())
sys.modules.setdefault("ableton.v3.control_surface", _cs)
sys.modules.setdefault("ableton.v3.control_surface.controls", MagicMock())
sys.modules.setdefault("ableton.v3.control_surface.elements", MagicMock())
sys.modules.setdefault("ableton.v3.control_surface.midi", _midi)
sys.modules.setdefault("ableton.v3.control_surface.capabilities", MagicMock())
