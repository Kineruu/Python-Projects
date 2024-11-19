import customtkinter as ct

Window = ct.CTk()
Window.geometry("600x400")

Window.grid_rowconfigure(0, weight=1)
Window.grid_columnconfigure(0, weight=1)

button = ct.CTkButton(Window, text="Button", width=125, height=50)
button.grid(row=0, column=0, sticky="n")

Window.mainloop()