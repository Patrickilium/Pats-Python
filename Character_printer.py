

import curses

print("Preparing to initialize screen...")

def print_center(message):
    message2 = str(" ") + str(message) + str(" ")
    screen.addch(y_pos, x_position, message)
    screen.addstr(0, 0, message2)
    num_rows, num_cols = screen.getmaxyx()
    rows_cols = str("Rows: ") + str(num_rows) + str(" Columns: ") + str(num_cols) + str(" ")
    
    screen.addstr(1, 0, rows_cols)
    screen.addstr(2, 0, str(x_position) + str("   ") + str(y_pos)+ str(" ") )

    # Actually print the screen
    screen.refresh()

index_count = 0

screen = curses.initscr()
num_rows, num_cols = screen.getmaxyx()
#rows_cols = str("Rows: ") + str(num_rows) + str(" Columns: ") + str(num_cols)

x_position = 0
y_pos = 0

#screen.addstr(20, 0, rows_cols)

for index_count in range(20,10000):
    print_center(index_count)
   # screen.addstr(15, 10, str(index_count))
   
   
    x_position = x_position + 1
    if x_position == num_cols:
       y_pos = y_pos + 1
       x_position = 0
       curses.napms(50)
    

    if y_pos == num_rows - 1:
        screen.clear()
        screen.refresh()
        x_position = 0
        y_pos = 0
        curses.beep()


# Wait and cleanup
curses.napms(20000)
curses.endwin()
