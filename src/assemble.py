import re
import sys

from src.constants import opcode, pseudo
from src.errors import *

def assemble(
        content: str
) -> str:
    """
    The function takes plain text RISCV 32I ISA instructions and assembles it into binary machine code.
    
    :param content: .asm file content
    :type content: str
    :return: assembled content in binary
    :rtype: str
    """
    metadata = {
        'labels': {},
        'address': 0,
    }

    assembled_lines = []

    for line in content.splitlines():
        # Comments or empty lines
        if line == '' or line.startswith('#'):
            continue 
        
        assembled_line = assemble_line(line, metadata)

        if assembled_line:
            assembled_lines.append(assembled_line)

    return '\n'.join(assembled_lines)

def assemble_line(
        line: str,
        metadata: dict
) -> str:
    """
    Assembles a single line of RISCV 32I ISA instruction into binary machine code.
    
    :param line: single line of .asm file content
    :type line: str
    :param metadata: dictionary containing labels and address
    :type metadata: dict
    :return: assembled line in binary
    :rtype: str
    """
    labels = metadata['labels']

    # Operation-handling ----------------------------
    op, non_op = parse_op(line)

    # Label-handling ----------------
    if op.endswith(':'):
        labels[op[:-1]] = metadata['address']
        return
    else:
        metadata['address'] += 4

    # Instruction-handling --------------------------


def parse_op(
    line: str
) -> tuple[str, str]:
    """Parses a line into operation and non-operation parts."""
    line = line.strip()
    match = re.search(r'\s*(\w+)\s+(.*)', line)
    if not match:
        raise MissingOperationError(f"Missing operation in line: {line}")
    return match.group(1), match.group(2)

if __name__ == "__main__":
    assemble(sys.argv[1])