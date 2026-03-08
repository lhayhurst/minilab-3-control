"""
Raw MIDI monitor — run this while Ableton is open, then press buttons on the MiniLab 3.
Shows exactly what MIDI messages the controller sends on each port.
"""
import mido

print("Available MIDI inputs:")
for i, name in enumerate(mido.get_input_names()):
    print(f"  {i}: {name}")

print()

# Try to open all MiniLab3 ports simultaneously
minilab_ports = [n for n in mido.get_input_names() if 'Minilab3' in n or 'MiniLab' in n]
print(f"Opening MiniLab3 ports: {minilab_ports}")
print("Press buttons on the MiniLab 3. Ctrl+C to stop.\n")

import threading

def listen(port_name):
    try:
        with mido.open_input(port_name) as port:
            for msg in port:
                if msg.type != 'sysex':
                    print(f"[{port_name}]  {msg}")
    except Exception as e:
        print(f"[{port_name}] ERROR: {e}")

threads = [threading.Thread(target=listen, args=(p,), daemon=True) for p in minilab_ports]
for t in threads:
    t.start()

try:
    for t in threads:
        t.join()
except KeyboardInterrupt:
    print("\nDone.")
