#!/usr/bin/env python3
from pwn import *

context.terminal = ['tmux', 'splitw', '-h']

exe = ELF("./1-format-me/format-me")

r = process([exe.path])
# For debugging. Make sure to run `tmux` before running this 
# script with the following line uncommented
# gdb.attach(r)

# Your exploit script goes here

r.interactive()
