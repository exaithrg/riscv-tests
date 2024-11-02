import os
import re

def collect_instructions(dump_dir):
    # Regular expression to match lines with the specified format
    pattern = re.compile(r'^(8[0-9a-f]{7}):\s+([0-9a-f]{4,8})\s+([.\w]+)\s+.*$', re.MULTILINE)

    # List to store all matched instruction lines
    instructions = []
    
    # Iterate over all .dump files in the specified directory
    for filename in os.listdir(dump_dir):
        if filename.endswith('.dump'):
            filepath = os.path.join(dump_dir, filename)
            
            # Open each file and read its content
            with open(filepath, 'r') as file:
                content = file.readlines()  # Read lines one by one
                
                # Find all matching lines using the regular expression
                for line in content:
                    match = pattern.match(line)
                    if match:
                        instructions.append(line.rstrip())  # Append the original line

    # Return the list of instructions and their total count
    return instructions, len(instructions)

# Directory to search for .dump files
dump_directory = '../build'

# Call the function and get the results
instr_list, instr_count = collect_instructions(dump_directory)

# Write all matched lines to the collected_insts.txt file
output_file = 'collected_insts.txt'
with open(output_file, 'w') as file:
    for line in instr_list:
        file.write(line + '\n')  # Write original lines

# Print the results
print(f"Found {instr_count} matching instruction lines and written to {output_file}")
