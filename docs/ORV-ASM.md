# Writing the assembly file

## Instructions
The ORV ISA instructions are categorized into six types:

Refer to the [ORV ISA documentation](ORV-ISA.md) for detailed information on each instruction type and their formats.

## Structuring the Assembly File
1. Create a new text file with a `.asm` extension.

2. Make sure instructions are written one per line.

3. Use comments to explain sections of your code. Comments start with a `#` symbol and continue to the end of the line.

4. Use labels to mark positions in your code for jumps and branches. A label is defined by writing a name followed by a colon (`:`) at the beginning of a line.

## Example
```asm
# Example ORV Assembly File
start:
    addi r1, r0, 10      # Load immediate value 10 into r1
    addi r2, r0, 20      # Load immediate value 20 into r2
    add r3, r1, r2       # Add r1 and r2, store result in r3
    beq r3, r0, end      # If r3 is zero, branch to end
    sub r4, r2, r1       # Subtract r1 from r2, store result in r4
end:
    nop                   # No operation
```