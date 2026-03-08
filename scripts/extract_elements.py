"""
Compact linear trace of Elements.__init__ to reconstruct element registrations.
Prints each instruction's opname + argval, filtered to the interesting ones.
"""
import dis
import marshal

SRC = "/Applications/Ableton Live 12 Suite.app/Contents/App-Resources/MIDI Remote Scripts/MiniLab_3/elements.pyc"

SHOW_OPS = {
    "LOAD_CONST", "LOAD_GLOBAL", "LOAD_ATTR", "LOAD_METHOD",
    "STORE_FAST", "STORE_ATTR",
    "CALL", "PRECALL", "KW_NAMES",
    "BUILD_LIST", "BUILD_TUPLE", "BUILD_MAP",
    "CALL_METHOD",
}


def load_pyc(path):
    with open(path, "rb") as f:
        f.read(16)
        return marshal.loads(f.read())


def find_code(code, name):
    for c in code.co_consts:
        if hasattr(c, "co_code") and c.co_name == name:
            return c
        if hasattr(c, "co_code"):
            r = find_code(c, name)
            if r:
                return r
    return None


def compact_trace(code):
    for instr in dis.get_instructions(code):
        if instr.opname not in SHOW_OPS:
            continue
        val = instr.argval
        # Skip boring None/0 consts
        if instr.opname == "LOAD_CONST" and val in (None, 0, 1, True, False):
            continue
        print(f"  {instr.offset:4d}  {instr.opname:<30} {repr(val)}")


module = load_pyc(SRC)
elements_class = find_code(module, "Elements")
init_code = find_code(elements_class, "__init__") if elements_class else None

if init_code:
    print("=== Elements.__init__ (filtered instructions) ===\n")
    compact_trace(init_code)
else:
    print("Could not find Elements.__init__")
