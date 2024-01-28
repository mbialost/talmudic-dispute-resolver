# Define compiler
CC := gcc

# Define compiler flags
CFLAGS := -Wall -Iinclude

# Define source, object, and binary directories
SRCDIR := src
OBJDIR := obj
BINDIR := bin

# Define source and object files
SOURCES := $(wildcard $(SRCDIR)/*.c)
OBJECTS := $(patsubst $(SRCDIR)/%.c, $(OBJDIR)/%.o, $(SOURCES))

# Define the target executable
TARGET := $(BINDIR)/TalmudicDisputeResolver

# Default target
all: $(TARGET)

# Rule to create the target directory
$(BINDIR):
	mkdir -p $(BINDIR)

# Rule to create the object directory
$(OBJDIR):
	mkdir -p $(OBJDIR)

# Rule to create the target executable
$(TARGET): $(OBJECTS) | $(BINDIR)
	$(CC) $^ -o $@

# Rule to create object files
$(OBJDIR)/%.o: $(SRCDIR)/%.c | $(OBJDIR)
	$(CC) $(CFLAGS) -c $< -o $@

# Clean target
clean:
	rm -rf $(OBJDIR) $(BINDIR)

# Phony targets
.PHONY: all clean
