# This app allows me to open any application of my choosing with a single button
import customtkinter as ctk

# programs I will use
music_programs = {
    'ProTools': 'Launching ProTools...',
    'Studio One': 'Launching Studio One...',
    'Ableton': 'Launching Ableton Live...',
    'Fl Studio': 'Launching FL Studio...',
}

coding_programs = {
    'Visual Studio': 'Launching Visual Studio...',
    'Command Prompt': 'Launching Terminal...',
    'Github': 'Launching GitHub Desktop...',
    'Notepad': 'Launching Notepad...',
}

fun_programs = {
    'Play Chess': 'Opening Chess.com...',
    'Open Youtube': 'Opening Youtube...',
    'Browse the Web': 'Browsing the Web...',
}


# function to run any program selected
def run_program(program_var, program_dict):
    program = program_var.get()
    if program != 'Choose a Program':
        print(program_dict.get(program, 'Program Not Found'))
    else:
        print('No Program selected')

# main window and settings
app = ctk.CTk()
app.geometry('700x400')
app.maxsize(700,400)
app.minsize(700,400)
app._set_appearance_mode('dark')
app.title('Application Program Launcher')
TITLE_FONT = ctk.CTkFont('Arial', 30)
TEXT_FONT = ctk.CTkFont('Arial', 15)

# frames section 
music_frame = ctk.CTkFrame(app, border_width=3, border_color='#ffffff', width=200)
code_frame = ctk.CTkFrame(app, border_width=3, border_color='#ffffff', width=200)
fun_frame = ctk.CTkFrame(app, border_width=3, border_color='#ffffff', width=200)

music_frame.pack(fill='both', side='left', padx=10, pady=10)
code_frame.pack(fill='both', side='left', padx=10, pady=10)
fun_frame.pack(fill='both', side='left', padx=10, pady=10)

# music settings
music_title = ctk.CTkLabel(music_frame, text="MUSIC", width=200, height=25, bg_color='transparent', font=TITLE_FONT)
music_title.pack(pady=50)
music_var = ctk.StringVar(value='ProTools')
music_select = ctk.CTkOptionMenu(music_frame, width=150, values=list(music_programs.keys()), font=TEXT_FONT, variable=music_var)
music_select.set('Choose a Program')
music_select.pack()

launch_music = ctk.CTkButton(music_frame, text='Open Selected Music App', font=TEXT_FONT, height=50, command= lambda: run_program(music_var, music_programs))
launch_music.pack()

# coding settings
code_title = ctk.CTkLabel(code_frame, text="CODING", width=200, height=25, bg_color='transparent', font=TITLE_FONT)
code_title.pack(pady=50)
code_var = ctk.StringVar(value='Visual Studio')
code_select = ctk.CTkOptionMenu(code_frame, width=150, values=list(coding_programs.keys()), font=TEXT_FONT, variable=code_var)
code_select.set('Choose a Program')
code_select.pack()

launch_code = ctk.CTkButton(code_frame, text='Open Selected Coding App', font=TEXT_FONT, height=50, command= lambda: run_program(code_var, coding_programs))
launch_code.pack()

# leisure settings
fun_title = ctk.CTkLabel(fun_frame, text="LEISURE", width=200, height=25, bg_color='transparent', font=TITLE_FONT)
fun_title.pack(pady=50)
fun_var = ctk.StringVar(value='Browse The Web')
fun_select = ctk.CTkOptionMenu(fun_frame, width=150, values=list(fun_programs.keys()), font=TEXT_FONT, variable=fun_var)
fun_select.set('Choose a Program')
fun_select.pack()

launch_fun = ctk.CTkButton(fun_frame, text='Open Selected Fun App', font=TEXT_FONT, height=50, command= lambda: run_program(fun_var, fun_programs))
launch_fun.pack()


# run program
app.mainloop()