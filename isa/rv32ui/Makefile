#=======================================================================
# Makefile for rv32ui tests
# Author: H GENG
# Notes: This Makefile is dedicated to rv32ui 
# 		and includes -g debug flag.
#-----------------------------------------------------------------------

# Include Makefrag for test definitions
include Makefrag

# Compiler and options
RISCV_GCC ?= riscv64-unknown-elf-gcc
RISCV_GCC_OPTS ?= -static -mcmodel=medany -fvisibility=hidden -nostdlib -nostartfiles -g
RISCV_OBJDUMP ?= riscv64-unknown-elf-objdump

# Source and include paths
SRC_DIR := .
INCLUDE_DIRS := -I$(SRC_DIR)/../../env/p -I$(SRC_DIR)/../macros/scalar
LINKER_SCRIPT := $(SRC_DIR)/../../env/p/link.ld

# Define all source files
ASSEMBLY_FILES := $(wildcard *.S)

# Define all binary and dump files
BINARY_FILES := $(rv32ui_p_tests)
DUMP_FILES := $(BINARY_FILES:%=%.dump)

# Default target
all: $(DUMP_FILES)

# Rule to compile assembly files to binary files
$(BINARY_FILES): rv32ui-p-%: %.S
	$(RISCV_GCC) -march=rv32g -mabi=ilp32 $(RISCV_GCC_OPTS) $(INCLUDE_DIRS) -T$(LINKER_SCRIPT) $< -o $@

# Rule to generate .dump files from binary files
$(DUMP_FILES): %.dump: %
	$(RISCV_OBJDUMP) --disassemble-all --disassemble-zeroes --section=.text --section=.text.startup --section=.text.init --section=.data $< > $@

# Clean up
clean:
	rm -f $(BINARY_FILES) $(DUMP_FILES)

.PHONY: all clean