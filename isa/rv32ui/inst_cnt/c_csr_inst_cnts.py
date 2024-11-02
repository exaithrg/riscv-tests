def extract_csr_instructions(input_file, output_file):
    # Open the input file for reading
    with open(input_file, 'r') as file:
        # Read all lines
        lines = file.readlines()

    # Open the output file for writing
    with open(output_file, 'w') as file:
        # Iterate over each line
        for line in lines:
            # Check if 'csr' is in the line
            if 'csr' in line:
                # Split the line to extract the desired parts
                parts = line.split()
                # Check if the parts are sufficient to avoid index errors
                if len(parts) >= 3:
                    # Write the instruction part to the output file
                    file.write(f"{parts[1]} {parts[2]} {parts[3]}\n")

# Input and output file names
input_file = 'collected_insts.txt'
output_file = 'csr_insts.txt'

# Call the function to extract CSR instructions
extract_csr_instructions(input_file, output_file)

print(f"CSR instructions written to {output_file}.")
