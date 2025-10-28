"""
Heidi's Adventure Game - A Beginner-Friendly Guide
Sponsored by RunMyModel.org

This is a "docstring" - it describes what the file does.
Python reads this when you use help() on the file.
"""

# ============================================================================
# IMPORT STATEMENTS - Getting tools from Python's library
# ============================================================================

import tkinter as tk
# tkinter = Python's built-in library for making GUI windows
# tk is just a shorter name for tkinter
# Now we can use tk.Label, tk.Button, etc.

from tkinter import font
# We need font to create custom text styles (bold, different sizes, etc.)

# ============================================================================
# VARIABLES - Storing information
# ============================================================================

# This variable tracks which scene we're currently showing to the player
# We'll update it as the player makes choices
current_scene = "start"
# "start" means the beginning screen
# We could also use "scene_1", "stay_alps", "ending_brave", etc.

# ============================================================================
# CREATING THE MAIN WINDOW
# ============================================================================

# tk.Tk() creates the main window
window = tk.Tk()
# window is a variable that holds our main window

# Set the title that appears at the top of the window
window.title("Heidi's Adventure - Sponsored by RunMyModel.org")

# Set the window size to 800 pixels wide, 600 pixels tall
window.geometry("800x600")

# Set the background color
# "#2c4a3e" is a dark green color (in hexadecimal format)
window.configure(bg="#2c4a3e")

# ============================================================================
# CREATING FONTS (Text styles)
# ============================================================================

# Create a big bold font for titles
big_font = font.Font(
    family="Arial",    # Font family (Arial, Times, Courier, etc.)
    size=28,          # Font size in points
    weight="bold"     # Makes text bold
)

# Create a medium font for story text
medium_font = font.Font(
    family="Arial",    # Same font family
    size=16            # Smaller than big_font
)

# Create a button font with bold text
button_font = font.Font(
    family="Arial",
    size=12,
    weight="bold"
)

# ============================================================================
# FUNCTION DEFINITIONS
# ============================================================================

def clear_window():
    """
    This function removes all widgets (buttons, labels, etc.) from the window.
    
    We need this because we want to show a clean screen before displaying
    a new scene.
    """
    # window.winfo_children() gets ALL widgets currently in the window
    for widget in window.winfo_children():
        # Loop through each widget
        widget.destroy()
        # destroy() removes the widget from the window permanently


def show_start():
    """
    This function shows the very first screen (title screen).
    This is where players see "Sponsored by RunMyModel.org"
    """
    # global means we're modifying the global variable (not creating a local one)
    global current_scene
    
    # Update the current scene to "start"
    current_scene = "start"
    
    # Clear everything in the window first
    clear_window()
    
    # Now let's add widgets to the window
    
    # ========== TITLE LABEL ==========
    # tk.Label creates a text label (just text, user can't interact with it)
    title = tk.Label(
        window,                        # Put this label in the main window
        text="Heidi's Adventure",     # The text to display
        font=big_font,                # Use our big bold font
        bg="#2c4a3e",                 # Background color (same as window)
        fg="white"                    # Foreground (text) color
    )
    # .pack() adds the widget to the window
    # pady=60 adds 60 pixels of space above and below the widget
    title.pack(pady=60)
    
    # ========== SPONSOR LABEL ==========
    # Create another label for the sponsor message
    sponsor = tk.Label(
        window,                                    # In the main window
        text="Sponsored by RunMyModel.org",       # The text
        font=font.Font(size=18, weight="bold"),   # Different font style
        bg="#2c4a3e",                             # Background
        fg="#87CEEB"                              # Light blue text color
    )
    sponsor.pack(pady=20)  # Add with 20 pixels spacing
    
    # ========== START BUTTON ==========
    # tk.Button creates a clickable button
    start_btn = tk.Button(
        window,                    # In the main window
        text="Start Adventure",   # Button text
        command=show_scene_1,     # When clicked, call show_scene_1() function
        font=button_font,         # Use our button font
        bg="#4a7c59",             # Background color (green)
        fg="white",               # Text color (white)
        padx=30,                  # Padding on left/right (30 pixels)
        pady=15                   # Padding on top/bottom (15 pixels)
    )
    start_btn.pack(pady=50)  # Add button with 50 pixels spacing


def show_scene_1():
    """
    Scene 1: The Beginning
    This is the first story scene where Heidi receives the letter.
    """
    # Update the current scene
    global current_scene
    current_scene = "scene_1"
    
    # Clear the window
    clear_window()
    
    # ========== CANVAS (for pretty scene visualization) ==========
    # Canvas is like a drawing board - we can draw shapes, text, images on it
    canvas = tk.Canvas(
        window,                    # In the main window
        width=760,                 # Width of canvas (760 pixels)
        height=180,                # Height of canvas (180 pixels)
        bg="#7FB3D3",              # Background color (light blue - mountains)
        highlightthickness=0       # No border around canvas
    )
    
    # Draw text on the canvas at position (380, 90) which is the center
    # x=380 (half of 760), y=90 (half of 180)
    canvas.create_text(
        380, 90,                    # Position (x, y)
        text="🏔️ Swiss Alps 🏔️",  # The text to draw
        font=big_font,              # Use big font
        fill="white"                # Text color
    )
    
    # Add canvas to window with 20 pixels spacing on sides
    canvas.pack(pady=20)
    
    # ========== STORY TEXT LABEL ==========
    story = tk.Label(
        window,  # In main window
        text=(
            # Multi-line string using parentheses
            "Heidi lives high in the Swiss Alps with her kind but strict grandfather.\n"
            # \n creates a new line
            "One morning, she receives a letter from her friend Clara in Frankfurt, "
            "inviting her to visit the city again.\n"
            "Grandfather wants her to stay, but Heidi feels curious about the world beyond the mountains."
        ),
        font=medium_font,        # Use medium font
        bg="#2c4a3e",            # Background color
        fg="white",              # Text color (white)
        wraplength=650,          # If text is longer than 650 pixels, wrap to next line
        justify=tk.LEFT,         # Align text to the left
        padx=20                  # Add 20 pixels padding on left and right
    )
    story.pack(pady=20)  # Add label to window
    
    # ========== BUTTON 1: STAY IN ALPS ==========
    stay_btn = tk.Button(
        window,  # In main window
        text="Stay in the Alps with Grandfather",  # Button text
        command=show_stay_alps,  # When clicked, run show_stay_alps() function
        font=button_font,        # Use button font
        bg="#4a7c59",            # Background color
        fg="white",              # Text color
        padx=20,                 # Left/right padding
        pady=10,                 # Top/bottom padding
        width=35                 # Button width in characters
    )
    stay_btn.pack(pady=10)  # Add button with 10 pixels spacing
    
    # ========== BUTTON 2: TRAVEL TO FRANKFURT ==========
    travel_btn = tk.Button(
        window,
        text="Travel to Frankfurt to visit Clara",
        command=show_travel_frankfurt,  # Different function for different path
        font=button_font,
        bg="#4a7c59",
        fg="white",
        padx=20,
        pady=10,
        width=35
    )
    travel_btn.pack(pady=10)


def show_stay_alps():
    """
    Path 1: Stay in the Alps
    This happens when Heidi chooses to stay with Grandfather.
    """
    global current_scene
    current_scene = "stay_alps"  # Update scene tracking
    clear_window()  # Clear everything
    
    # Create canvas for the scene
    canvas = tk.Canvas(
        window,
        width=760,
        height=180,
        bg="#87CEEB",  # Sky blue color
        highlightthickness=0
    )
    canvas.create_text(
        380, 90,
        text="🌲 Peaceful Mountains 🌲",
        font=big_font,
        fill="white"
    )
    canvas.pack(pady=20)
    
    # Story text explaining what happens
    story = tk.Label(
        window,
        text=(
            "Heidi decides to remain in the mountains.\n"
            "She helps Grandfather tend to the goats, gathers herbs for tea, "
            "and enjoys peaceful days under the pine trees.\n\n"
            # \n\n creates double line break
            "But one day, a heavy snowstorm hits the village. Grandfather falls ill, "
            "and Heidi must decide what to do."
        ),
        font=medium_font,
        bg="#2c4a3e",
        fg="white",
        wraplength=650,
        justify=tk.LEFT,
        padx=20
    )
    story.pack(pady=20)
    
    # ========== BUTTON 1: GO FOR HELP ==========
    help_btn = tk.Button(
        window,
        text="Go down the mountain to find help",
        command=show_ending_brave,  # This leads to ENDING A
        font=button_font,
        bg="#4a7c59",
        fg="white",
        padx=20,
        pady=10,
        width=35
    )
    help_btn.pack(pady=10)
    
    # ========== BUTTON 2: STAY HOME ==========
    stay_home_btn = tk.Button(
        window,
        text="Stay home and care for Grandfather herself",
        command=show_ending_heart,  # This leads to ENDING B
        font=button_font,
        bg="#4a7c59",
        fg="white",
        padx=20,
        pady=10,
        width=35
    )
    stay_home_btn.pack(pady=10)


def show_travel_frankfurt():
    """
    Path 2: Travel to Frankfurt
    This happens when Heidi chooses to visit Clara.
    """
    global current_scene
    current_scene = "travel_frankfurt"
    clear_window()
    
    # Canvas with city color
    canvas = tk.Canvas(
        window,
        width=760,
        height=180,
        bg="#B0C4DE",  # Light steel blue (city color)
        highlightthickness=0
    )
    canvas.create_text(
        380, 90,
        text="🌆 Frankfurt City 🌆",
        font=big_font,
        fill="white"
    )
    canvas.pack(pady=20)
    
    # Story text about Frankfurt
    story = tk.Label(
        window,
        text=(
            "Heidi packs her small bag and boards the train to Frankfurt.\n"
            "The city feels strange and loud, but she is excited to see Clara again.\n"
            "Clara's family welcomes her warmly, and soon they are exploring the city together.\n\n"
            "One day, Clara asks Heidi to stay in Frankfurt forever — "
            "to study and learn like other children.\n"
            "Heidi feels torn between her new life and her mountain home."
        ),
        font=medium_font,
        bg="#2c4a3e",
        fg="white",
        wraplength=650,
        justify=tk.LEFT,
        padx=20
    )
    story.pack(pady=20)
    
    # ========== BUTTON 1: STAY IN FRANKFURT ==========
    stay_frankfurt_btn = tk.Button(
        window,
        text="Stay in Frankfurt and study",
        command=show_ending_writer,  # This leads to ENDING C
        font=button_font,
        bg="#4a7c59",
        fg="white",
        padx=20,
        pady=10,
        width=35
    )
    stay_frankfurt_btn.pack(pady=10)
    
    # ========== BUTTON 2: RETURN HOME ==========
    return_home_btn = tk.Button(
        window,
        text="Return home to the Alps",
        command=show_ending_dreamer,  # This leads to ENDING D
        font=button_font,
        bg="#4a7c59",
        fg="white",
        padx=20,
        pady=10,
        width=35
    )
    return_home_btn.pack(pady=10)


# ============================================================================
# ENDING FUNCTIONS - These show the final results
# ============================================================================

def show_ending_brave():
    """
    Ending A: Heidi the Brave
    This is the ending where Heidi goes for help during the snowstorm.
    """
    clear_window()  # Clear everything
    
    # Gold background canvas (gold = achievement)
    canvas = tk.Canvas(
        window,
        width=760,
        height=180,
        bg="#FFD700",  # Gold color
        highlightthickness=0
    )
    canvas.create_text(
        380, 90,
        text="🩺 Heidi the Brave 🩺",
        font=big_font,
        fill="white"
    )
    canvas.pack(pady=20)
    
    # Ending story
    story = tk.Label(
        window,
        text=(
            "She braves the storm and finds Peter the goatherd. Together, they bring medicine back.\n"
            "Grandfather recovers, and Heidi learns that courage comes from love.\n\n"
            "ENDING A: Heidi the Brave — The mountains are her home, and her heart is strong."
        ),
        font=medium_font,
        bg="#2c4a3e",
        fg="white",
        wraplength=650,
        justify=tk.LEFT,
        padx=20
    )
    story.pack(pady=20)
    
    # ========== RESTART BUTTON ==========
    restart_btn = tk.Button(
        window,
        text="Restart Adventure",      # Button text
        command=show_start,           # Go back to start screen
        font=button_font,
        bg="#0f3460",                 # Dark blue background
        fg="white",
        padx=30,
        pady=15
    )
    restart_btn.pack(pady=20)


def show_ending_heart():
    """
    Ending B: Heidi the Heart
    This is where Heidi stays home to care for Grandfather.
    """
    clear_window()
    
    # Pink background (pink = love)
    canvas = tk.Canvas(
        window,
        width=760,
        height=180,
        bg="#FF69B4",  # Hot pink
        highlightthickness=0
    )
    canvas.create_text(
        380, 90,
        text="🌨️ Heidi the Heart 🌨️",
        font=big_font,
        fill="white"
    )
    canvas.pack(pady=20)
    
    story = tk.Label(
        window,
        text=(
            "The snow keeps falling. Heidi keeps the fire alive and reads stories to her grandfather.\n"
            "Though scared, she stays calm and strong until spring comes.\n\n"
            "ENDING B: Heidi the Heart — Love kept them warm through the coldest days."
        ),
        font=medium_font,
        bg="#2c4a3e",
        fg="white",
        wraplength=650,
        justify=tk.LEFT,
        padx=20
    )
    story.pack(pady=20)
    
    # Restart button
    restart_btn = tk.Button(
        window,
        text="Restart Adventure",
        command=show_start,
        font=button_font,
        bg="#0f3460",
        fg="white",
        padx=30,
        pady=15
    )
    restart_btn.pack(pady=20)


def show_ending_writer():
    """
    Ending C: Heidi the Writer
    This is where Heidi stays in Frankfurt to study.
    """
    clear_window()
    
    # Light blue background (light blue = learning/knowledge)
    canvas = tk.Canvas(
        window,
        width=760,
        height=180,
        bg="#87CEFA",  # Light sky blue
        highlightthickness=0
    )
    canvas.create_text(
        380, 90,
        text="📚 Heidi the Writer 📚",
        font=big_font,
        fill="white"
    )
    canvas.pack(pady=20)
    
    story = tk.Label(
        window,
        text=(
            "Heidi studies hard and grows into a bright young woman.\n"
            "She writes stories about the Alps that inspire people to appreciate nature.\n\n"
            "ENDING C: Heidi the Writer — Her words bring the mountains to everyone's heart."
        ),
        font=medium_font,
        bg="#2c4a3e",
        fg="white",
        wraplength=650,
        justify=tk.LEFT,
        padx=20
    )
    story.pack(pady=20)
    
    # Restart button
    restart_btn = tk.Button(
        window,
        text="Restart Adventure",
        command=show_start,
        font=button_font,
        bg="#0f3460",
        fg="white",
        padx=30,
        pady=15
    )
    restart_btn.pack(pady=20)


def show_ending_dreamer():
    """
    Ending D: Heidi the Dreamer
    This is where Heidi returns home with Clara's music box.
    """
    clear_window()
    
    # Purple background (purple = dreams/friendship)
    canvas = tk.Canvas(
        window,
        width=760,
        height=180,
        bg="#DDA0DD",  # Plum color
        highlightthickness=0
    )
    canvas.create_text(
        380, 90,
        text="🏞️ Heidi the Dreamer 🏞️",
        font=big_font,
        fill="white"
    )
    canvas.pack(pady=20)
    
    story = tk.Label(
        window,
        text=(
            "Clara gifts her a music box to remember their friendship.\n"
            "Heidi returns to the mountains, where her grandfather greets her with open arms.\n\n"
            "ENDING D: Heidi the Dreamer — She carries the music of friendship wherever she goes."
        ),
        font=medium_font,
        bg="#2c4a3e",
        fg="white",
        wraplength=650,
        justify=tk.LEFT,
        padx=20
    )
    story.pack(pady=20)
    
    # Restart button
    restart_btn = tk.Button(
        window,
        text="Restart Adventure",
        command=show_start,
        font=button_font,
        bg="#0f3460",
        fg="white",
        padx=30,
        pady=15
    )
    restart_btn.pack(pady=20)


# ============================================================================
# START THE GAME
# ============================================================================

# Call show_start() to display the title screen when program starts
show_start()

# window.mainloop() is CRITICAL - it keeps the window open
# Without this, the window would appear and disappear instantly
# mainloop() tells Python: "Keep the window open and listen for events"
# Events include: button clicks, mouse movements, keyboard presses, etc.
window.mainloop()

# This line will only run when the user closes the window
# Because mainloop() keeps the program running until the window is closed
