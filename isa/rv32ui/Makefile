#=======================================================================
# Makefile for rv32ui tests
# Author: H GENG
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
# No debug support
# CFLAGS = -march=rv32g -mabi=ilp32 -static -mcmodel=medany -fvisibility=hidden -nostdlib -nostartfiles
# GDB support
CFLAGS = -march=rv32g -mabi=ilp32 -static -mcmodel=medany -fvisibility=hidden -nostdlib -nostartfiles -g
LDFLAGS = -m elf32lriscv -T $(LINKER_SCRIPT) -nostdlib
INCLUDE_DIRS = -I$(SRC_DIR)/../../env/p -I$(SRC_DIR)/../macros/scalar
LINKER_SCRIPT = $(SRC_DIR)/../../env/r529/r529.ld

# Source and include paths
SRC_DIR := .
ASSEMBLY_FILES := $(wildcard *.S)

# Define the build directories
BUILD_DIR := build
VERILOG_DIR := verilog

# Ensure the build directories exist
$(shell mkdir -p $(BUILD_DIR))
$(shell mkdir -p $(VERILOG_DIR))

# Source and assembly files
SRC_DIR := .
ASSEMBLY_FILES := $(wildcard *.S)

# Define all object, binary, dump, text hex, and data hex files with build directory
OBJECT_FILES := $(addprefix $(BUILD_DIR)/, $(ASSEMBLY_FILES:.S=.o))
ELF_FILES := $(addprefix $(BUILD_DIR)/, $(ASSEMBLY_FILES:.S=.elf))
DUMP_FILES := $(ELF_FILES:%.elf=%.dump)
TEXT_HEX_FILES := $(addprefix $(VERILOG_DIR)/, $(ASSEMBLY_FILES:.S=.text.hex))
DATA_HEX_FILES := $(addprefix $(VERILOG_DIR)/, $(ASSEMBLY_FILES:.S=.data.hex))

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
$(VERILOG_DIR)/%.text.hex: $(BUILD_DIR)/%.elf
	$(RISCV_OBJCOPY) -O verilog --only-section .text $< $@
	# $(SED) -i 's/@800/@000/g' $@
	# @echo "Address @80000000 replaced with @00000000 in $@"
	$(SED) -i 's/@000/@000/g' $@
	@echo "Address @00000000 replaced with @00000000 in $@"

# Rule to generate data hex files from ELF files
$(VERILOG_DIR)/%.data.hex: $(BUILD_DIR)/%.elf
	$(RISCV_OBJCOPY) -O verilog --only-section .data $< $@
	# $(SED) -i 's/@A00/@000/g' $@
	# @echo "Address @A0000000 replaced with @00000000 in $@"
	$(SED) -i 's/@001/@000/g' $@
	@echo "Address @00100000 replaced with @00000000 in $@"

# Clean up
clean:
	rm -rf $(BUILD_DIR) $(VERILOG_DIR)

cl: clean

.PHONY: all clean cl
