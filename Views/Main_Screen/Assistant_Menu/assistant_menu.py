from customtkinter import CTkFrame, CTkButton, CTkSwitch


class AssistantMenu(CTkFrame):
    def __init__(self, master, size: tuple[int, int]):
        super().__init__(
            master, fg_color=["#EAEAEA", "white"], width=size[0], height=size[1]
        )
        self.grid_columnconfigure(list(range(0, 3)), pad=10)
        self.grid_rowconfigure((0), pad=30)
        self.grid_propagate(False)
        self.upload_btn = CTkButton(
            self,
            width=size[0] // 3,
            height=size[1] * 0.6,
            text="Upload Image",
            corner_radius=10,
        )
        self.upload_btn.grid(row=0, column=0, padx=15)
        self.save_btn = CTkButton(
            self,
            width=size[0] // 3,
            height=size[1] * 0.6,
            text="Save",
            corner_radius=10,
        )
        self.save_btn.grid(row=0, column=1)
        self.theme_switch = CTkSwitch(master=self, text="Dark mode")
        self.theme_switch.grid(row=0, column=2)
