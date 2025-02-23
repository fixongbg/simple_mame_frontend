import os
import curses
import subprocess

# Path to your MAME executable and ROMs directory
MAME_CMD = "SDL_VIDEODRIVER=kmsdrm /usr/lib/mame/groovymame -switchres"
ROMS_DIR = "/home/arcade/shared/roms/mame"

# Number of visible items in the list
VISIBLE_ITEMS = 20  

# Left padding for the ROM list
PADDING = 5 # Adjust this to control the left position of the list

ROMS_DIR = os.path.expanduser(ROMS_DIR)
ROM_TITLES_FILE = "rom_titles.txt"

def load_rom_titles(filename=ROM_TITLES_FILE):
    rom_titles = {}
    if not os.path.exists(filename):
        return rom_titles
    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                parts = line.strip().split(maxsplit=1)
                if len(parts) == 2:
                    rom_titles[parts[0].lower()] = parts[1].strip('"')
    except Exception as e:
        print(f"Error reading {filename}: {e}")
    return rom_titles

def get_rom_list():
    rom_titles = load_rom_titles()
    if not os.path.exists(ROMS_DIR):
        return []
    roms = sorted(os.listdir(ROMS_DIR))
    roms_no_ext = {os.path.splitext(rom)[0]: rom for rom in roms}
    return [(roms_no_ext[rom], rom_titles.get(rom.lower(), rom)) for rom in roms_no_ext]

def run_mame(rom):
    subprocess.run(f"{MAME_CMD} {rom} > /dev/null 2>&1", shell=True)

def exit_prompt(stdscr):
    options = ["No", "Yes (Shell)", "Shutdown"]
    index = 0
    h, w = stdscr.getmaxyx()
    menu_width = max(len(opt) for opt in options) + 4
    x_start = (w - menu_width) // 2
    y_start = h // 2
    
    while True:
        stdscr.clear()
        stdscr.addstr(y_start - 2, x_start, "Exit?", curses.A_BOLD)
        
        for i, option in enumerate(options):
            if i == index:
                stdscr.addstr(y_start + i, x_start, f"> {option} <", curses.A_REVERSE)
            else:
                stdscr.addstr(y_start + i, x_start, f"  {option}  ")
        
        stdscr.refresh()
        key = stdscr.getch()
        
        if key == curses.KEY_UP:
            index = max(0, index - 1)
        elif key == curses.KEY_DOWN:
            index = min(len(options) - 1, index + 1)
        elif key == 10:
            return options[index]

def truncate_text(text, max_width):
    """Truncates text to fit within max_width, adding '...' if needed."""
    if len(text) > max_width:
        return text[:max_width - 3] + "..."
    return text

def main(stdscr):
    curses.curs_set(0)
    stdscr.keypad(1)
    stdscr.nodelay(0)

    roms = get_rom_list()
    if not roms:
        stdscr.addstr(0, PADDING, "No ROMs found in " + ROMS_DIR, curses.A_BOLD)
        stdscr.refresh()
        stdscr.getch()
        return
    
    index = 0
    top_index = 0
    h, w = stdscr.getmaxyx()
    max_available_width = w - PADDING - 2  # Ensure we don't overflow the screen width
    
    y_start = max(0, (h - VISIBLE_ITEMS) // 2)
    
    def draw_list():
        stdscr.erase()
        for i in range(VISIBLE_ITEMS):
            rom_idx = top_index + i
            if rom_idx >= len(roms):
                break
            y = y_start + i
            
            rom_name = truncate_text(roms[rom_idx][1], max_available_width)
            
            if rom_idx == index:
                stdscr.addstr(y, PADDING, "> " + rom_name, curses.A_REVERSE)
            else:
                stdscr.addstr(y, PADDING, "  " + rom_name)
        stdscr.refresh()
    
    draw_list()
    
    while True:
        key = stdscr.getch()
        prev_index = index
        
        if key == curses.KEY_UP:
            if index > 0:
                index -= 1
                if index < top_index:
                    top_index -= 1
        elif key == curses.KEY_DOWN:
            if index < len(roms) - 1:
                index += 1
                if index >= top_index + VISIBLE_ITEMS:
                    top_index += 1
        elif key == curses.KEY_LEFT:
            current_letter = roms[index][1][0].lower()
            for i in range(index - 1, -1, -1):
                if roms[i][1][0].lower() != current_letter:
                    index = i
                    break
            if index < top_index:
                top_index = index
        elif key == curses.KEY_RIGHT:
            current_letter = roms[index][1][0].lower()
            for i in range(index + 1, len(roms)):
                if roms[i][1][0].lower() != current_letter:
                    index = i
                    break
            if index >= top_index + VISIBLE_ITEMS:
                top_index = max(0, index - VISIBLE_ITEMS + 1)
        elif key == 10:
            run_mame(roms[index][0])
        elif key == 27:
            choice = exit_prompt(stdscr)
            if choice == "Yes (Shell)":
                return
            elif choice == "Shutdown":
                subprocess.run("shutdown now", shell=True)
                return
        
        if index != prev_index:
            draw_list()

if __name__ == "__main__":
    curses.wrapper(main)
