from tkinter import *
import customtkinter
from tkinter.filedialog import askopenfile
from video import Video

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

class Editor_Window:

    def __init__(self):
        self.tk = customtkinter.CTk()
        self.tk.title("Video Editor")
        self.frame = Frame(self.tk)
        self.tk.state('zoomed')

        # configure grid layout
        self.tk.grid_columnconfigure((0,1,2), weight=1)
        self.tk.grid_rowconfigure((0,1), weight=1)


        # create sidebar frame with buttons and video library (from folder)
        self.left_sidebar_frame = customtkinter.CTkFrame(self.tk, width=200, corner_radius=0)
        self.left_sidebar_frame.grid(row=0, column = 0, rowspan=2, sticky="nsew")

        self.logo_label = customtkinter.CTkLabel(self.left_sidebar_frame, text="CustomTkinter", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.sidebar_button_1 = customtkinter.CTkButton(self.left_sidebar_frame, text = "Import Video" , command= self.open_file)
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_button_2 = customtkinter.CTkButton(self.left_sidebar_frame,  text = "Add Layer" , command= self.add_layer)
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.sidebar_button_3 = customtkinter.CTkButton(self.left_sidebar_frame, command= self.sidebar_button_event)
        self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)
        # self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.left_sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
        #                                                        command=self.change_scaling_event)
        # self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))
        
        # create main frame
        self.main_frame = customtkinter.CTkFrame(self.tk, width=1000, corner_radius=0, fg_color="transparent")
        self.main_frame.grid(row=0, column = 1, rowspan=2, sticky="nsew")
        self.main_frame.grid_columnconfigure((0), weight=1)
        self.main_frame.grid_rowconfigure((0,1,2), weight=1)

        self.video_container = customtkinter.CTkFrame(self.main_frame, width=1000, corner_radius=0, fg_color="black")
        self.video_container.grid(row=0, column = 0, rowspan=1, sticky="nsew")

        self.video_frame = customtkinter.CTkLabel(master=self.video_container)
        self.video_frame.pack(expand=True, fill="both")

        self.video_bar = customtkinter.CTkFrame(self.main_frame, corner_radius=0, fg_color="blue")
        self.video_bar.grid(row=1, column = 0, rowspan=1, sticky="nsew")

        self.video_slider = customtkinter.CTkSlider(master=self.video_bar, from_=0, to=1, width=1000, height = 20, command= self.slide)
        self.video_slider.grid(row=0, column=1, rowspan=1, padx=(10, 10), pady=(10, 10), sticky="ns")


        self.video = Video()
        self.video.load(r"temp/happy_seal.mp4")
        self.display_frame(0)



        # create bottom frame where timeline is seen with layers
        self.bottom_frame = customtkinter.CTkFrame(self.main_frame, width=1000, corner_radius=0, fg_color="transparent")
        self.bottom_frame.grid(row=2, column = 0, rowspan=1, sticky="nsew")



        self.label1 = customtkinter.CTkLabel(master = self.bottom_frame, text="Layers: None", fg_color="transparent", text_color="white")
        self.label1.place(x=50,y=80)

        # create right frame which changes frames to allow changing values of algorithms
        self.right_sidebar_frame = customtkinter.CTkFrame(self.tk, width=200, corner_radius=0)
        self.right_sidebar_frame.grid(row=0, column=2, rowspan=2, sticky="nsew")

        self.checkbox_1 = customtkinter.CTkCheckBox(master=self.right_sidebar_frame)
        self.checkbox_1.grid(row=1, column=0, pady=(20, 10), padx=20, sticky="n")
        self.checkbox_2 = customtkinter.CTkCheckBox(master=self.right_sidebar_frame)
        self.checkbox_2.grid(row=2, column=0, pady=10, padx=20, sticky="n")
        self.switch_1 = customtkinter.CTkSwitch(master=self.right_sidebar_frame, command=lambda: print("switch 1 toggle"))
        self.switch_1.grid(row=3, column=0, pady=10, padx=20, sticky="n")
        self.switch_2 = customtkinter.CTkSwitch(master=self.right_sidebar_frame)
        self.switch_2.grid(row=4, column=0, pady=(10, 20), padx=20, sticky="n")


    def display_frame(self, frame_num):
        image = self.video.get_frame(frame_num)
        frame_width = 1000 # self.video_container.winfo_width()
        frame_height = 600 # self.video_container.winfo_height() #
        current_image = customtkinter.CTkImage(light_image=image,dark_image=image, size=(int(frame_width),int(frame_height)))
        self.video_frame.configure(image = current_image)
        
    def slide(self, value):
        self.display_frame(round(value))

    def sidebar_button_event(self):
        print("sidebar_button click")
    
    def open_file(self):
        file = askopenfile(mode="r", filetypes=[('Video Files', ['*.mp4'])])
        if file is not None:
            self.video.load(r"{}".format(file.name))
            self.update_layers_list()
            self.video_frame.pack(expand=True, fill="both")
            self.display_frame(0)
            frame_count = self.video.get_framecount()
            self.video_slider.set(0)
            self.video_slider.configure(to=frame_count)

        # # config menu bar at top
        # self.menu = Menu(self.tk)
        # self.file = Menu(self.menu)
        # self.menu.add_cascade(label="File", menu=self.file)
        # self.edit = Menu(self.menu)
        # self.edit.add_command(label="Undo")
        # self.menu.add_cascade(label="Edit", menu=self.edit)

    def add_layer(self):
        self.video.create_new_layer("contrast")
        self.update_layers_list()
        self.display_frame(self.video_slider.get())

    def update_layers_list(self):
        layers = self.video.layers
        text = ""
        for layer in layers:
            text += f"Layer: {layer.process}\n"  
        self.label1.configure(text=text)

if __name__ == '__main__':
    w = Editor_Window()
    w.tk.mainloop()


def button_function():
    print("button pressed")

# # Use CTkButton instead of tkinter Button
# button = customtkinter.CTkButton(master=app, text="CTkButton", command=button_function)
# button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
