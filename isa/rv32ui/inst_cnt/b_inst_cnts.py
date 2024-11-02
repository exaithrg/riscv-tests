from collections import defaultdict
import pdb

def count_instructions(input_file, output_file):
    # Dictionary to store instruction counts
    instruction_counts = defaultdict(int)

    # Read the collected instructions from the input file
    with open(input_file, 'r') as file:
        for line in file:
            # Split the line to get the instruction (the third column)
            parts = line.split()
            if len(parts) >= 3:
                instruction = parts[2]  # Get the instruction
                instruction_counts[instruction] += 1  # Increment the count

    # Sort instructions by name
    sorted_instructions = sorted(instruction_counts.items())

    # Calculate total instruction count
    total_count = sum(count for _, count in sorted_instructions)

    # Write the total count and sorted counts to the output file
    with open(output_file, 'w') as file:
        file.write(f"Instruction Types: {len(sorted_instructions)}\n")
        #pdb.set_trace()
        file.write(f"Instruction Count: {total_count}\n")
        for instruction, count in sorted_instructions:
            file.write(f"{instruction} {count}\n")

# Input and output file names
input_file = 'collected_insts.txt'
output_file = 'inst_cnts.txt'

# Count instructions and output results
count_instructions(input_file, output_file)

print(f"Instruction counts written to {output_file}.")
