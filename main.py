import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Redação App")
        self.geometry("400x400")

        self.frame1 = tk.Frame(self)
        self.frame1.pack(pady=20)

        self.label = tk.Label(self.frame1, text="tema da redação")
        self.label.pack()

        self.text_input = tk.Text(self.frame1, height=10, width=50)
        self.text_input.pack()
        self.text_input.bind("<KeyRelease>", self.limit_text)

        self.next_button = tk.Button(self.frame1, text="next", command=self.show_frame2)
        self.next_button.pack(side="left", padx=10, pady=10)

        self.quit_button = tk.Button(self.frame1, text="quit", command=self.quit)
        self.quit_button.pack(side="right", padx=10, pady=10)

        # Frame 2
        self.frame2 = tk.Frame(self)

        # Radio button groups
        self.radio_vars = []
        for i in range(5):
            group_frame = tk.LabelFrame(self.frame2, text=f"Grupo {i+1}", padx=10, pady=10)
            group_frame.pack(padx=10, pady=5, anchor="w")

            var = tk.IntVar(value=-1) # Initialize with a value that represents no selection
            self.radio_vars.append(var)

            options = [("Opção 1", 1), ("Opção 2", 2), ("Opção 3", 3)] # Example options
            for text, value in options:
                rb = tk.Radiobutton(group_frame, text=text, variable=var, value=value)
                rb.pack(anchor="w")


        # Buttons for Frame 2
        button_frame = tk.Frame(self.frame2)
        button_frame.pack(pady=10)

        self.back_button = tk.Button(button_frame, text="back", command=self.show_frame1)
        self.back_button.pack(side="left", padx=10, pady=10)

        self.grade_button = tk.Button(button_frame, text="grade now", command=self.grade_now)
        self.grade_button.pack(side="left", padx=10, pady=10)

        self.quit_button2 = tk.Button(button_frame, text="quit", command=self.quit)
        self.quit_button2.pack(side="right", padx=10, pady=10)


    def limit_text(self, event):
        content = self.text_input.get("1.0", "end-1c")
        if len(content) > 500:
            self.text_input.delete("1.0 + 500 chars", "end")

    def show_frame1(self):
        self.frame2.pack_forget()
        self.frame1.pack(pady=20)

    def show_frame2(self):
        self.frame1.pack_forget()
        self.frame2.pack(pady=20)

    def grade_now(self):
        # Placeholder for grading logic
        print("Grading...")


if __name__ == "__main__":
    app = App()
    app.mainloop()