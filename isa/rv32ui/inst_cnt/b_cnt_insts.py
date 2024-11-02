import re
from collections import Counter

def count_instructions(input_file, output_file):
    # Regular expression to extract the instruction name from each line
    pattern = re.compile(r'^\s*[0-9a-fA-F]+:\s+[0-9a-fA-F]{8}\s+(\S+)')
    
    # List to store all instruction names
    instructions = []
    
    # Read the input file and extract instruction names
    with open(input_file, 'r') as file:
        for line in file:
            match = pattern.match(line)
            if match:
                instructions.append(match.group(1))
    
    # Count the occurrences of each instruction
    instruction_counts = Counter(instructions)
    
    # Sort the instructions alphabetically
    sorted_instructions = sorted(instruction_counts.items())
    
    # Write the sorted instructions and their counts to the output file
    with open(output_file, 'w') as file:
        for instruction, count in sorted_instructions:
            file.write(f"{instruction} {count}\n")

# Input and output file paths
input_file = 'collected_insts.txt'
output_file = 'inst_cnts.txt'

# Call the function to count instructions and write the results
count_instructions(input_file, output_file)

# Print a message indicating the task is complete
print(f"Instruction counts have been written to {output_file}")
