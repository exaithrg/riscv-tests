def count_duplicate_csr_instructions(input_file, output_file):
    # Dictionary to store counts of CSR instructions
    csr_counts = {}

    # Open the input file for reading
    with open(input_file, 'r') as file:
        # Read all lines
        lines = file.readlines()

    # Iterate over each line
    for line in lines:
        # Remove leading/trailing whitespace
        line = line.strip()
        if line:  # Only process non-empty lines
            # Count occurrences of each line
            if line in csr_counts:
                csr_counts[line] += 1
            else:
                csr_counts[line] = 1

    total_count = sum(csr_counts.values())
    
    # Open the output file for writing
    with open(output_file, 'w') as file:
        file.write(f"Total CSR Instructions: {total_count}\n")
        # Write the counts to the output file in the desired format
        for instruction, count in csr_counts.items():
            file.write(f"[{count}] {instruction}\n")  # Format the output

# Input and output file names
input_file = 'collected_csr_insts.txt'
output_file = 'csr_inst_cnts.txt'

# Call the function to count duplicate CSR instructions
count_duplicate_csr_instructions(input_file, output_file)

print(f"CSR instruction counts written to {output_file}.")
