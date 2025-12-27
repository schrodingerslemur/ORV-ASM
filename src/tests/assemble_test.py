import sys

from src.assemble import parse_op

def test_parse_op_valid():
    line = "ADD R1, R2, R3"
    op, non_op = parse_op(line)
    assert op == "ADD"
    assert non_op == "R1, R2, R3"

    line = "  SUB R4, R5, R6  "
    op, non_op = parse_op(line)
    print(non_op)
    assert op == "SUB"
    assert non_op == "R4, R5, R6"