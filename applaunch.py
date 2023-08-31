# This app allows me to open any application of my choosing with a single button
import customtkinter as ctk

# main window
app = ctk.CTk()
app.geometry('700x400')
app.maxsize(700,400)
app.minsize(700,400)
app._set_appearance_mode('dark')
app.title('Application Program Launcher')

# frames section 
music_frame = ctk.CTkFrame(app, border_width=3, border_color='#ffffff')
code_frame = ctk.CTkFrame(app, border_width=3, border_color='#ffffff')
fun_frame = ctk.CTkFrame(app, border_width=3, border_color='#ffffff')

# music_frame.grid(row=0, column=0, padx=10, sticky='news')
# code_frame.grid(row=0, column=1, padx=10, sticky='news')
# fun_frame.grid(row=0, column=2, padx=10, sticky='news')
music_frame.pack(fill='both', side='left', padx=10, pady=10)
code_frame.pack(fill='both', side='left', padx=10, pady=10)
fun_frame.pack(fill='both', side='left', padx=10, pady=10)



# run program
app.mainloop()