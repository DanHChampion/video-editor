import tkinter
import customtkinter
import time
from tkinter.filedialog import askopenfile
from video import Video

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

# class LayerRow(Frame):
#   def __init__(self, master, name, percentage, domain):
#     Frame.__init__(self, master, bd=2, relief='raised')
#     Label(self, text='%3d%%'%percentage, font=('Arial', 24), fg='#88F', width=4, anchor='e').grid(row=0, column=0, rowspan=2)
#     Label(self, text=name, font=('Aria', 16, 'bold'), fg='black', width=15, anchor='w').grid(row=0, column=1)
#     Label(self, text=', '.join(domain), font=('Aria', 10), fg='black').grid(row=1, column=1, sticky='w')
#     Button(self, text='View', fg='white', bg='#44F').grid(row=0, column=2, rowspan=2, padx=10)
#     self.columnconfigure(1, weight=1)

class Editor_Window(customtkinter.CTk):

    def __init__(self):
        super().__init__()
        # self.tk = customtkinter.CTk()
        # self.tk.title("Video Editor")
        # self.frame = Frame(self.tk)
        # self.tk.state('zoomed')

        # # configure grid layout
        # self.tk.grid_columnconfigure((0,1,2), weight=1)
        # self.tk.grid_rowconfigure((0,1), weight=1)


        # # create sidebar frame with buttons and video library (from folder)
        # self.left_sidebar_frame = customtkinter.CTkFrame(self.tk, width=200, corner_radius=0)
        # self.left_sidebar_frame.grid(row=0, column = 0, rowspan=2, sticky="nsew")

        # self.logo_label = customtkinter.CTkLabel(self.left_sidebar_frame, text="CustomTkinter", font=customtkinter.CTkFont(size=20, weight="bold"))
        # self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        # self.sidebar_button_1 = customtkinter.CTkButton(self.left_sidebar_frame, text = "Import Video" , command= self.open_file)
        # self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        # self.sidebar_button_2 = customtkinter.CTkButton(self.left_sidebar_frame,  text = "Add Layer" , command= self.add_layer)
        # self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)


        # # create main frame
        # self.main_frame = customtkinter.CTkFrame(self.tk, width=1000, corner_radius=0, fg_color="transparent")
        # self.main_frame.grid(row=0, column = 1, rowspan=2, sticky="nsew")
        # self.main_frame.grid_columnconfigure((0), weight=1)
        # self.main_frame.grid_rowconfigure((0,1,2), weight=1)

        # self.video_container = customtkinter.CTkFrame(self.main_frame, width=1000, corner_radius=0, fg_color="black")
        # self.video_container.grid(row=0, column = 0, rowspan=1, sticky="nsew")

        # self.video_frame = customtkinter.CTkLabel(master=self.video_container, text="Video")
        # self.video_frame.pack(expand=True, fill="both")

        # self.video_bar = customtkinter.CTkFrame(self.main_frame, corner_radius=0, fg_color="blue")
        # self.video_bar.grid(row=1, column = 0, rowspan=1, sticky="nsew")

        # self.video_slider = customtkinter.CTkSlider(master=self.video_bar, from_=0, to=1, width=1000, height = 20, command= self.slide)
        # self.video_slider.grid(row=0, column=1, rowspan=1, padx=(10, 10), pady=(10, 10), sticky="ns")


        # self.video = Video()
        # # self.video.load(r"temp/happy_seal.mp4")
        # # self.display_frame(0)



        # # create bottom frame where timeline is seen with layers
        

        # self.bottom_frame = customtkinter.CTkFrame(self.main_frame, width=1000, corner_radius=0, fg_color="transparent")
        # # self.bottom_frame.grid(row=2, column = 0, rowspan=1, sticky="nsew")



        # self.scroll_canvas = customtkinter.CTkCanvas(master = self.bottom_frame)

        # v = Scrollbar(self.scroll_canvas)
        # v.pack(side = RIGHT, fill = Y)

        # self.scroll_canvas.configure(yscrollcommand = v.set)

        # # create right frame which changes frames to allow changing values of algorithms
        # self.right_sidebar_frame = customtkinter.CTkFrame(self.tk, width=200, corner_radius=0)
        # self.right_sidebar_frame.grid(row=0, column=2, rowspan=2, sticky="nsew")

        # self.checkbox_1 = customtkinter.CTkCheckBox(master=self.right_sidebar_frame)
        # self.checkbox_1.grid(row=1, column=0, pady=(20, 10), padx=20, sticky="n")
        # self.checkbox_2 = customtkinter.CTkCheckBox(master=self.right_sidebar_frame)
        # self.checkbox_2.grid(row=2, column=0, pady=10, padx=20, sticky="n")
        # self.switch_1 = customtkinter.CTkSwitch(master=self.right_sidebar_frame, command=lambda: print("switch 1 toggle"))
        # self.switch_1.grid(row=3, column=0, pady=10, padx=20, sticky="n")
        # self.switch_2 = customtkinter.CTkSwitch(master=self.right_sidebar_frame)
        # self.switch_2.grid(row=4, column=0, pady=(10, 20), padx=20, sticky="n")
        # configure window
        self.title("CustomTkinter complex_example.py")
        self.geometry(f"{1600}x{900}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=250, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="CustomTkinter", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, text = "Import Video", command= self.open_file, width=230)
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, text = "Add Layer", command= self.add_layer, width=230)
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame)
        self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))

        # create video

        # self.video_container = customtkinter.CTkFrame(self.main_frame, width=1000, corner_radius=0, fg_color="black")
        # self.video_container.grid(row=0, column = 0, rowspan=1, sticky="nsew")

        self.video_frame = customtkinter.CTkLabel(self, text="", height= 600, width=250)
        self.video_frame.grid(row=0, column=1, columnspan=2, padx=(10, 0), pady=(10, 0), sticky="new")

        self.video = Video()
        
        # self.textbox = customtkinter.CTkTextbox(self, width=250)
        # self.textbox.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")

        # # create tabview
        # self.tabview = customtkinter.CTkTabview(self, width=250)
        # self.tabview.grid(row=0, column=2, padx=(20, 0), pady=(20, 0), sticky="nsew")
        # self.tabview.add("CTkTabview")
        # self.tabview.add("Tab 2")
        # self.tabview.add("Tab 3")
        # self.tabview.tab("CTkTabview").grid_columnconfigure(0, weight=1)  # configure grid of individual tabs
        # self.tabview.tab("Tab 2").grid_columnconfigure(0, weight=1)

        # self.optionmenu_1 = customtkinter.CTkOptionMenu(self.tabview.tab("CTkTabview"), dynamic_resizing=False,
        #                                                 values=["Value 1", "Value 2", "Value Long Long Long"])
        # self.optionmenu_1.grid(row=0, column=0, padx=20, pady=(20, 10))
        # self.combobox_1 = customtkinter.CTkComboBox(self.tabview.tab("CTkTabview"),
        #                                             values=["Value 1", "Value 2", "Value Long....."])
        # self.combobox_1.grid(row=1, column=0, padx=20, pady=(10, 10))
        # self.string_input_button = customtkinter.CTkButton(self.tabview.tab("CTkTabview"), text="Open CTkInputDialog",
        #                                                    command=self.open_input_dialog_event)
        # self.string_input_button.grid(row=2, column=0, padx=20, pady=(10, 10))
        # self.label_tab_2 = customtkinter.CTkLabel(self.tabview.tab("Tab 2"), text="CTkLabel on Tab 2")
        # self.label_tab_2.grid(row=0, column=0, padx=20, pady=20)

        # create adjustments frame
        self.adjustments_widgets = []
        self.adjustments_frame = customtkinter.CTkFrame(self, width=250)
        self.adjustments_frame.grid(row=0, column=3, rowspan=1,  padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.adjustments_frame.grid_columnconfigure(1, weight=1)
        self.adjustments_frame.grid_rowconfigure(1, weight=1)

        # create checkbox and switch frame
        self.layers_frame = customtkinter.CTkFrame(self, width=250)
        self.layers_frame.grid(row=1, column=3, rowspan=2, padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.layers_frame.grid_columnconfigure(1, weight=1)
        self.layers_frame.grid_rowconfigure(1, weight=1)

        self.layer_buttons = []

        # create slider and progressbar frame
        self.slider_progressbar_frame = customtkinter.CTkFrame(self, fg_color="transparent")
        self.slider_progressbar_frame.grid(row=1, column=1, columnspan=2, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.slider_progressbar_frame.grid_columnconfigure(0, weight=1)
        self.slider_progressbar_frame.grid_rowconfigure(4, weight=1)
        self.play_button = customtkinter.CTkButton(self.slider_progressbar_frame, height = 20, text= "Play",command= self.play)
        self.play_button.grid(row=3, column=0, padx=(20, 10), pady=(10, 10))
        self.video_slider = customtkinter.CTkSlider(self.slider_progressbar_frame, from_=0, to=1, height = 20, command= self.slide)
        self.video_slider.grid(row=4, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")

        # set default values
        self.sidebar_button_3.configure(state="disabled", text="Disabled CTkButton")
        self.appearance_mode_optionemenu.set("Dark")
        self.scaling_optionemenu.set("100%")
        # self.optionmenu_1.set("CTkOptionmenu")
        # self.combobox_1.set("CTkComboBox")
        # self.textbox.insert("0.0", "CTkTextbox\n\n" + "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua.\n\n" * 20)
        # self.seg_button_1.configure(values=["CTkSegmentedButton", "Value 2", "Value 3"])
        # self.seg_button_1.set("Value 2")

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def display_frame(self, frame_num):
        image = self.video.get_frame(frame_num)
        frame_size = self.video.get_framesize()
        frame_width = min(frame_size[0], 1000) # self.video_container.winfo_width()
        frame_height = min(frame_size[1], 600) # self.video_container.winfo_height() #
        current_image = customtkinter.CTkImage(light_image=image,dark_image=image, size=(int(frame_width),int(frame_height)))
        self.video_frame.configure(image = current_image)
        
    def slide(self, value):
        self.display_frame(round(value))
    
    def open_file(self):
        file = askopenfile(mode="r", filetypes=[('Video Files', ['*.mp4'])])
        if file is not None:
            self.video.load(r"{}".format(file.name))
            self.update_layers_list()
            # self.video_frame.pack(expand=True, fill="both")
            self.display_frame(0)
            frame_count = self.video.get_framecount()
            self.video_slider.set(0)
            self.video_slider.configure(to=frame_count)
            # for widgets in self.layers_frame.winfo_children():
            #     widgets.destroy()

        # # config menu bar at top
        # self.menu = Menu(self.tk)
        # self.file = Menu(self.menu)
        # self.menu.add_cascade(label="File", menu=self.file)
        # self.edit = Menu(self.menu)
        # self.edit.add_command(label="Undo")
        # self.menu.add_cascade(label="Edit", menu=self.edit)

    def play(self):
        self.forward_frame()
        # self.paused = False
        # current_frame = round(self.video_slider.get())
        # framerate = self.video.get_framerate()
        # framecount = self.video.get_framecount()
        # if current_frame<framecount and not self.paused:
        #     self.forward_frame()
        # self.video_frame.after(1, self.play())


    def pause(self):
        self.paused = True

    def revert_frame(self):
        current_frame = self.video_slider.get()
        if current_frame > 0:
            self.display_frame(round(current_frame)-1)
            self.video_slider.set(round(current_frame)-1)


    def forward_frame(self):
        current_frame = self.video_slider.get()
        if current_frame < self.video.get_framecount():
            self.display_frame(round(current_frame)+1)
            self.video_slider.set(round(current_frame)+1)


    def add_layer(self):
        self.layers = self.video.layers
        if len(self.layers) < 5:
            self.video.create_new_layer("contrast")
        
        self.update_layers_list()
        self.display_frame(self.video_slider.get())

    def delete_layer(self):
        for widgets in self.adjustments_frame.winfo_children():
            widgets.destroy()
        self.layers = self.video.layers
        self.layers.pop(self.selected_layer)
        self.update_layers_list()
        self.display_frame(self.video_slider.get())

    def update_layers_list(self):
        # creates rows or layers (includes label, dropdown )
        self.layers = self.video.layers
        for widgets in self.layers_frame.winfo_children():
            widgets.destroy()
        self.layer_buttons = []
        for i, layer in enumerate(self.layers):
            if layer.process == None:
                name = "Empty Layer"
            else:
                name = str(layer.process).capitalize()
            if layer.hidden:
                colour = "grey"
                hover_colour = "dark grey"
            else:
                colour = None
                hover_colour = None
            text = f"Layer {i+1}: {name}" 
            layer_button = customtkinter.CTkButton(self.layers_frame, text=text, width=230, fg_color=colour, hover_color= hover_colour, command = lambda index = i : self.select_layers(index))
            layer_button.grid(row = i, column = 1, padx=10, pady=10)
            self.layer_buttons.append(layer_button)
        self.layers_frame.grid_rowconfigure(len(self.layers), weight=1)

    def edit_layer(self, value):
        # get adjustments that affect layers GUI
        hidden = False
        process = ""
        for i, widgets in enumerate(self.adjustments_frame.winfo_children()):
            if i == 1:
                process = widgets.get()
            if i == 2:
                hidden = widgets.get()
                        
        # update values in video
        self.video.update_layer(index = self.selected_layer, process = process, hidden=hidden)
        self.update_layers_list()

        # refresh image
        self.display_frame(self.video_slider.get())

    def make_adjustments(self, value):
        # update values in layers without updating layers GUI
        params = {}
        for i, widgets in enumerate(self.adjustments_frame.winfo_children()):
            if i == 3:
                params['value1'] = widgets.get()
                print(params["value1"])
                        
        # update values in video
        self.video.update_layer(index = self.selected_layer, parameters = params)

        # refresh image
        self.display_frame(self.video_slider.get())

    def select_layers(self, layer_index):
        self.selected_layer = layer_index
        for widgets in self.adjustments_frame.winfo_children():
            widgets.destroy()
        
        # if self.video.layers[layer_index].process == None:
        #     heading = "Empty Layer"
        # else:
        #     heading = str(self.video.layers[layer_index].process).capitalize()
        # labels created
        layer_label = customtkinter.CTkLabel(self.adjustments_frame, text=f"Layer {layer_index+1}", font=customtkinter.CTkFont(size=16, weight="bold"))
        layer_label.grid(row = 0, column = 1, padx=10, pady=10, sticky="nsew")


        # selecting process
        processes = [ "Contrast", "Brightness", "Film Grain", "Noise Removal", "Colour Matching" ]
        select_process = customtkinter.CTkOptionMenu(self.adjustments_frame, dynamic_resizing=False, values=processes, height = 30, width=230, command = lambda _: self.edit_layer(_))
        select_process.grid(row = 1, column = 1, padx=20, pady=20)
        select_process.set(self.layers[layer_index].process.capitalize())
        self.adjustments_widgets.append(layer_label)
        self.adjustments_widgets.append(select_process)

        # toggle hide layer
        hide_switch = customtkinter.CTkSwitch(self.adjustments_frame, text = "Hide Layer", command = lambda : self.edit_layer(""))
        hide_switch.grid(row = 2, column = 1, padx=20, pady=20)
        hide_switch.deselect()
        if (self.layers[layer_index].hidden):
            hide_switch.select()
        self.adjustments_widgets.append(hide_switch)

        # value slider
        value1_slider = customtkinter.CTkSlider(self.adjustments_frame, from_=-50, to=50, height = 20, command = lambda _: self.make_adjustments(_))
        value1_slider.grid(row=3, column=1, padx=(20, 10), pady=(10, 10), sticky="ew")
        value1_slider.set(self.layers[layer_index].parameters['value1'])
        self.adjustments_widgets.append(value1_slider)

        # delete layer button
        delete_button = customtkinter.CTkButton(self.adjustments_frame, text="Delete Layer", width=230, command = lambda : self.delete_layer())
        delete_button.grid(row = 4, column = 1, padx=10, pady=10)
        self.adjustments_widgets.append(delete_button)
        self.adjustments_frame.grid_rowconfigure(len(self.adjustments_widgets), weight=1)
        

if __name__ == '__main__':
    app = Editor_Window()
    app.mainloop()



# # Use CTkButton instead of tkinter Button
# button = customtkinter.CTkButton(master=app, text="CTkButton", command=button_function)
# button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
