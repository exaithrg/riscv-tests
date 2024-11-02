#=======================================================================
# Makefile for rv32ui tests
# Author: H GENG
# Notes: This Makefile is dedicated to rv32ui 
#        and includes -g debug flag.
#-----------------------------------------------------------------------

# Include Makefrag for test definitions
include Makefrag

# Compiler and tools
RISCV_GCC ?= riscv64-unknown-elf-gcc
RISCV_LD ?= riscv64-unknown-elf-ld
RISCV_OBJDUMP ?= riscv64-unknown-elf-objdump
RISCV_OBJCOPY ?= riscv64-unknown-elf-objcopy
SED = sed
CHMOD = chmod

# Compiler and linker flags
CFLAGS = -march=rv32g -mabi=ilp32 -static -mcmodel=medany -fvisibility=hidden -nostdlib -nostartfiles
LDFLAGS = -m elf32lriscv -T $(LINKER_SCRIPT) -nostdlib
INCLUDE_DIRS = -I$(SRC_DIR)/../../env/p -I$(SRC_DIR)/../macros/scalar
LINKER_SCRIPT = $(SRC_DIR)/../../env/p/link.ld

# Source and include paths
SRC_DIR := .
ASSEMBLY_FILES := $(wildcard *.S)

# Define the build directory
BUILD_DIR := build

# Ensure the build directory exists
$(shell mkdir -p $(BUILD_DIR))

# Define all object, binary, dump, text hex, and data hex files with build directory
OBJECT_FILES := $(addprefix $(BUILD_DIR)/, $(ASSEMBLY_FILES:.S=.o))
ELF_FILES := $(addprefix $(BUILD_DIR)/, $(ASSEMBLY_FILES:.S=.elf))
DUMP_FILES := $(ELF_FILES:%.elf=%.dump)
TEXT_HEX_FILES := $(ELF_FILES:%.elf=%.text.hex)
DATA_HEX_FILES := $(ELF_FILES:%.elf=%.data.hex)

# Default target
all: $(DUMP_FILES) $(TEXT_HEX_FILES) $(DATA_HEX_FILES)

# Rule to compile assembly files to object files
$(OBJECT_FILES): $(BUILD_DIR)/%.o: %.S
	$(RISCV_GCC) $(CFLAGS) $(INCLUDE_DIRS) -c $< -o $@

# Rule to link object files to ELF files
$(ELF_FILES): $(BUILD_DIR)/%.elf: $(BUILD_DIR)/%.o
	$(RISCV_LD) $(LDFLAGS) -o $@ $<

# Rule to generate .dump files from ELF files
$(DUMP_FILES): $(BUILD_DIR)/%.dump: $(BUILD_DIR)/%.elf
	$(RISCV_OBJDUMP) --disassemble-all --disassemble-zeroes --section=.text --section=.text.startup --section=.text.init --section=.data $< > $@

# Rule to generate text hex files from ELF files
$(TEXT_HEX_FILES): $(BUILD_DIR)/%.text.hex: $(BUILD_DIR)/%.elf
	$(RISCV_OBJCOPY) -O verilog --only-section .text $< $@
	$(SED) -i 's/@800/@000/g' $@
	@echo "Address @80000000 replaced with @00000000 in $@"

# Rule to generate data hex files from ELF files
$(DATA_HEX_FILES): $(BUILD_DIR)/%.data.hex: $(BUILD_DIR)/%.elf
	$(RISCV_OBJCOPY) -O verilog --only-section .data $< $@
	$(SED) -i 's/@000/@000/g' $@
	@echo "Address @00000000 replaced with @00000000 in $@"

# Clean up
clean:
	rm -rf $(BUILD_DIR)

.PHONY: all clean