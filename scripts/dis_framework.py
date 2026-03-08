import dis, marshal

def load_pyc(path):
    with open(path, 'rb') as f:
        f.read(16)
        return marshal.loads(f.read())

def collect_names(code, depth=0, max_depth=2):
    if depth <= max_depth:
        for c in code.co_consts:
            if hasattr(c, 'co_code'):
                print(f"{'  '*depth}{c.co_name}")
                collect_names(c, depth+1, max_depth)

BASE = "/Applications/Ableton Live 12 Suite.app/Contents/App-Resources/MIDI Remote Scripts"

# Check v2 SimpleControlSurface for MIDI method names
print("=== v2 SimpleControlSurface methods ===")
try:
    scs = load_pyc(f"{BASE}/ableton/v2/control_surface/simple_control_surface.pyc")
    collect_names(scs)
except Exception as e:
    print(f"error: {e}")

# Also check v2 ControlSurface
print("\n=== v2 ControlSurface methods (midi-related only) ===")
try:
    cs = load_pyc(f"{BASE}/ableton/v2/control_surface/control_surface.pyc")
    def midi_methods(code, depth=0):
        for c in code.co_consts:
            if hasattr(c, 'co_code'):
                if any(x in c.co_name.lower() for x in ('midi', 'receive', 'handle', 'sysex', 'input')):
                    print(f"{'  '*depth}{c.co_name}")
                midi_methods(c, depth+1)
    midi_methods(cs)
except Exception as e:
    print(f"error: {e}")
