import dis
import marshal
import sys

MINILAB_SRC = "/Applications/Ableton Live 12 Suite.app/Contents/App-Resources/MIDI Remote Scripts/MiniLab_3"


def full_dis(code, indent=0):
    prefix = "  " * indent
    print(f"\n{prefix}{'='*60}")
    print(f"{prefix}CODE: {code.co_name}  (line {code.co_firstlineno})")
    print(f"{prefix}  consts:   {[c for c in code.co_consts if not hasattr(c, 'co_code')]}")
    print(f"{prefix}  names:    {list(code.co_names)}")
    print(f"{prefix}  vars:     {list(code.co_varnames)}")
    print(f"{prefix}  freevars: {list(code.co_freevars)}")
    print()
    dis.dis(code)
    for c in code.co_consts:
        if hasattr(c, "co_code"):
            full_dis(c, indent + 1)


def load_pyc(path):
    with open(path, "rb") as f:
        f.read(16)  # skip header
        return marshal.loads(f.read())


if __name__ == "__main__":
    name = sys.argv[1] if len(sys.argv) > 1 else "elements"
    path = f"{MINILAB_SRC}/{name}.pyc"
    print(f"Disassembling: {path}\n")
    full_dis(load_pyc(path))
