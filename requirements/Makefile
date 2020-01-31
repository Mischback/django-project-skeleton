# Makefile to compile/update the actual requirements files using pip-tools'
# 'pip-compile' command.

# get a list of all *.in files
OBJECTS = $(wildcard *.in)

# construct the list of output files
OUTPUTS := $(OBJECTS:.in=.txt)

# Make the command to actually compile the *.in files into *.txt configurable;
# the provided 'pip-compile' should be working within a 'tox' environment.
COMPILE_CMD = pip-compile


### RECEIPTS ###

# by default update all requirements
all: $(OUTPUTS)

# this is the actually compile step in generic form
%.txt: %.in
	$(COMPILE_CMD) --allow-unsafe --generate-hashes --output-file $@ $<


# dependency chain
development.txt: common.txt
production.txt: common.txt

.PHONY: all
