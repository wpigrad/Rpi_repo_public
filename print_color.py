# title: print_color.py

# ANSI escape sequence uses "\"
# Select Graphic Rendition Subset
# Using RGB ranging from 0 to 255

# Codes: 38, 48, 2=RGB
# RGB basic colors = {0,128,255}

# foreground (text) = 38
print('\033[38;2;255;0;0mHello World!\033[0m')

# background = 48
print('\033[48;2;0;0;255mHello World!\033[0m')

# both
print('\033[38;2;255;0;0;48;2;0;0;255mHello World!\033[0m')

