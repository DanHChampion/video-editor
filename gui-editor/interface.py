import tkinter
import customtkinter
import time
from tkinter.filedialog import askopenfile
from video import Video
import math

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
        self.title("Video Editor")
        self.geometry(f"{1600}x{900}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=250, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Video Editor", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, text = "Import Video", command= self.open_file, width=230)
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, text = "Export Video", command= self.export_file, width=230)
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame, text = "Add Layer", command= self.add_layer, width=230)
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
        self.video_frame = customtkinter.CTkLabel(self, text="", height= 600, width=250)
        self.video_frame.grid(row=0, column=1, columnspan=2, padx=(10, 0), pady=(10, 0), sticky="new")

        self.video = Video()

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
        self.slider_progressbar_frame.grid_columnconfigure(2, weight=1)
        self.slider_progressbar_frame.grid_rowconfigure(4, weight=1)
        self.back_button = customtkinter.CTkButton(self.slider_progressbar_frame, height = 20, width=150, text= "Back",command= self.revert_frame)
        self.back_button.grid(row=3, column=0, padx=(20, 10), pady=(10, 10) , sticky="ew")
        self.next_button = customtkinter.CTkButton(self.slider_progressbar_frame, height = 20, width=150, text= "Forward",command= self.forward_frame)
        self.next_button.grid(row=3, column=1, padx=(20, 10), pady=(10, 10), sticky="ew")
        self.video_slider = customtkinter.CTkSlider(self.slider_progressbar_frame, from_=0, to=1, height = 20, command= self.slide)
        self.video_slider.grid(row=4, column=0, columnspan=3, padx=(20, 10), pady=(10, 10), sticky="ew")

        # set default values
        self.appearance_mode_optionemenu.set("Dark")
        self.scaling_optionemenu.set("100%")

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def display_frame(self, frame_num):
        image = self.video.get_frame(frame_num)
        frame_size = self.video.get_framesize()
        frame_width = min(frame_size[0], 1000) # self.video_container.winfo_width()
        frame_height = min(frame_size[1], 600) # self.video_container.winfo_height()
        current_image = customtkinter.CTkImage(light_image=image,dark_image=image, size=(int(frame_width),int(frame_height)))
        self.video_frame.configure(image = current_image)
        
    def slide(self, value):
        self.display_frame(math.floor(value))
    
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


    def export_file(self):
        self.video.export()

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
        # creates rows or layers (includes label, dropdown)
        self.layers = self.video.layers
        for widgets in self.layers_frame.winfo_children():
            widgets.destroy()
        self.layer_buttons = []
        for i, layer in enumerate(self.layers):
            if layer.process == None:
                name = "Empty Layer"
            else:
                name = str(layer.process).title()
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
        # get adjustments that affect editor GUI
        hidden = False
        process = ""
        for i, widgets in enumerate(self.adjustments_frame.winfo_children()):
            if i == 1:
                process = widgets.get()
            if i == 2:
                hidden = widgets.get()

        # change values numbers in                 
        
        # update values in video
        self.video.update_layer(index = self.selected_layer, process = process, hidden=hidden)
        self.update_layers_list()
        self.select_layers(self.selected_layer)

        # refresh image
        self.display_frame(self.video_slider.get())

    def make_adjustments(self, value):
        # update values in layers without updating layers GUI
        params = {}
        # sliders = 0
        for i, widgets in enumerate(self.adjustments_frame.winfo_children()):
            # if i % 2 == 0 and i != 2:
            #     params[f"value{sliders}"] = widgets.get()
            #     sliders += 1
            if i == 4:
                params['value1'] = widgets.get()
            if i == 6:
                params['value2'] = widgets.get()
            if i == 8:
                params['value3'] = widgets.get()
                        
        # update values in video
        self.video.update_layer(index = self.selected_layer, parameters = params)

        # refresh image
        self.display_frame(self.video_slider.get())

    def select_layers(self, layer_index):
        self.selected_layer = layer_index
        for widgets in self.adjustments_frame.winfo_children():
            widgets.destroy()
        
        layer_label = customtkinter.CTkLabel(self.adjustments_frame, text=f"Layer {layer_index+1}", font=customtkinter.CTkFont(size=16, weight="bold"))
        layer_label.grid(row = 0, column = 1, padx=10, pady=10, sticky="nsew")

        # selecting process
        processes = [ "Contrast",
                    "Brightness",
                    "Colour Balance",
                    "Colour Correction - Histogram Manipulation Linear",
                    "Colour Correction - Histogram Manipulation Cauchy",
                    "Colour Correction - Histogram Manipulation Logistic",
                    "Colour Transfer - Linear Histogram Matching",
                    "Colour Transfer - Principal Component Color Matching",
                    "Colour Transfer - Reinhard et al.",
                    "Film Grain - Gaussian",
                    "Film Grain - Varying Grain Size",
                    "Film Grain - Inhomogenous Boolean Model",
                    "Noise Removal - Median Blur",
                    "Noise Removal - Bilateral Filter",
                    "Noise Removal - Non Local Means"
                    ]
        select_process = customtkinter.CTkOptionMenu(self.adjustments_frame, dynamic_resizing=False, values=processes, height = 30, width=230, command = lambda _: self.edit_layer(_))
        select_process.grid(row = 1, column = 1, padx=20, pady=20)
        select_process.set(self.layers[layer_index].process.title())
        self.adjustments_widgets.append(layer_label)
        self.adjustments_widgets.append(select_process)

        # toggle hide layer
        hide_switch = customtkinter.CTkSwitch(self.adjustments_frame, text = "Hide Layer", command = lambda : self.edit_layer(""))
        hide_switch.grid(row = 2, column = 1, padx=20, pady=20)
        hide_switch.deselect()
        if (self.layers[layer_index].hidden):
            hide_switch.select()
        self.adjustments_widgets.append(hide_switch)

        labels = self.video.get_layer_labels(self.layers[layer_index])

        for i, label in enumerate(labels):
            # create custom and labels sliders
            value_label = customtkinter.CTkLabel(self.adjustments_frame, text=f"{label}:", font=customtkinter.CTkFont(size=16, weight="bold"))
            value_label.grid(row=(2*(i+1)+1), column=1, padx=(20, 10), pady=(10, 10), sticky="ew")

            # value slider
            value_slider = customtkinter.CTkSlider(self.adjustments_frame, from_=-50, to=50, height = 20, command = lambda _: self.make_adjustments(_))
            value_slider.grid(row=(2*(i+1)+2), column=1, padx=(20, 10), pady=(10, 10), sticky="ew")
            value_slider.set(self.layers[layer_index].parameters[f'value{i+1}'] if self.layers[layer_index].parameters[f'value{i+1}'] is not None else 0)
            self.adjustments_widgets.append(value_slider)

        # delete layer button
        delete_button = customtkinter.CTkButton(self.adjustments_frame, text="Delete Layer", width=230, command = lambda : self.delete_layer())
        delete_button.grid(row = (len(self.adjustments_widgets)+1), column = 1, padx=10, pady=10) # PLUS ONE??
        self.adjustments_widgets.append(delete_button)
        self.adjustments_frame.grid_rowconfigure(len(self.adjustments_widgets), weight=1)
        

if __name__ == '__main__':
    app = Editor_Window()
    app.mainloop()


