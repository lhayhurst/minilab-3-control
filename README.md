# iamkat MiniLab 3 — Ableton Live Remote Script

I wrote this for a musician I work with for whom the stock MiniLab 3 control script didn't work:
they wanted a toggle to arm the track, a toggle to move between input monitoring states, and a
simpler way to move around tracks — turning the rotary encoder, rather than shift-turning it.

## Controls

| Control | Action |
|---|---|
| Main encoder | Select previous / next track |
| Arp button | Select scene up |
| Pad button | Select scene down |
| Prog/Delete button | Arm / disarm selected track |
| Undo button | Cycle input monitoring: In → Auto → Off |
| Stop button | Stop transport |
| Play button | Play / continue |
| Record button | Record (arms track first if needed) |
| Tap button | Tap tempo |
| Fader 1 | Selected track volume |
| Fader 2 | Selected track Send A |
| Fader 3 | Selected track Send B |
| Fader 4 | Selected track pan |
| Rotaries 1–7 | Track volumes 1–7 |
| Rotary 8 | Master volume |
| Bank B pads 1–8 | Launch clip on tracks 1–8 at selected scene |

Buttons light up with color-coded LEDs on connect (teal = navigation, orange = arm,
yellow = monitoring, red = stop, green = play, crimson = record, blue = tap tempo).

## Requirements

- Arturia MiniLab 3 set to **DAW mode** (hold Shift + press 3rd Prog pad until display shows DAW)
- Ableton Live 12

## Installation

1. Set your MiniLab 3 to **DAW mode**: hold **Shift** and press the **3rd Prog pad** until the display shows **DAW**. The script will not work in the default Arturia mode.
2. Download the latest `iamkat_MiniLab_3.zip` from the [Releases](../../releases) page
3. Unzip it — you'll get a folder called `iamkat_MiniLab_3`
4. Move that folder into your Ableton Remote Scripts directory:
   - **Mac:** `~/Music/Ableton/User Library/Remote Scripts/`
   - **Windows:** `C:\Users\[you]\Documents\Ableton\User Library\Remote Scripts\`
5. Restart Ableton Live
6. Open **Preferences → MIDI** and set Control Surface to `iamkat_MiniLab_3` — the Input port may auto-select to `Minilab3 MIDI`; if not, set it manually
7. In the same MIDI preferences, find `Minilab3 MIDI` in the Input list and enable **Track** and **Remote**

## License

MIT
