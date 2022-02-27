from tkinter import *
from tkinter import messagebox


class App:
    global lorem
    lorem = """Lorem ipsum dolor sit amet. Eum porro aliquid ex quae aliquid qui voluptate aliquam ex quos magnam? Est enim placeat qui distinctio distinctio aut officiis quam ea debitis tempora. Ut nemo pariatur hic dolore Quis est dicta expedita quo animi quaerat id dolores error est optio dolor. Rem Quis maxime et voluptatem sunt ut eveniet vero qui quia magnam ut facere voluptatem.
Et totam consequatur est rerum cumque At ipsum unde. A molestiae doloribus qui expedita exercitationem est illum architecto At voluptate quis aut dolor eos assumenda deleniti. Sed quod excepturi et voluptatem sequi ut molestias tenetur et galisum itaque.
Est ducimus enim non exercitationem dolorem a atque placeat est sint facere ea quia internos et alias nihil. Ab cupiditate reiciendis sunt consequuntur qui quia expedita et dolor omnis et libero velit a praesentium beatae. At harum maiores non sunt corporis eum obcaecati perferendis est sequi impedit aut aperiam libero ex eveniet culpa ea magni fugit."""
    def __init__(self, root):
        self.window = root
        self.window.iconbitmap('icon.ico')
        self.window.geometry('1100x600')
        self.window.resizable(False,False)
        self.window.title("Lorem Ipsum Generator")

        # Textarea
        self.textarea = Text(self.window, width=130, height=35)
        self.textarea.pack()
        #self.textarea.config(state="disabled")

        # Scrollbar
        self.scroll = Scrollbar(self.window)
        self.scroll.pack()
        self.scroll.place(x=1080, height=390)

        # Menu
        self.mainmenu = Menu(self.window)
        self.mainmenu.add_command(label="Generate", command=self.range_window)
        self.mainmenu.add_command(label="Clear", command=self.clear)
        self.mainmenu.add_command(label="Exit", command=self.exit)
        self.window.config(menu=self.mainmenu)

        self.textarea.config(yscrollcommand=self.scroll.set)
        self.scroll.config(command=self.textarea.yview)



        self.window.mainloop()
    
    def exit(self):
        self.window.destroy()
    
    def clear(self):
        self.textarea.delete(1.0, END)


    def range_window(self):
        def generate_lorem():
            self.textarea.delete(1.0, END)
            for i in range(self.in_range.get()):
                self.textarea.insert(1.0, lorem+"\n\n")
            self.new.destroy()


        self.new = Toplevel()
        self.new.iconbitmap('icon.ico')
        self.new.title("Enter a range")
        self.new.geometry('240x50')
        self.new.resizable(False,False)


        # Input range
        self.in_range = IntVar()
        self.input = Entry(self.new, textvariable=self.in_range)
        self.input.pack()
        self.input.place(x=4,y=6, height=25)


        # Button
        self.gen_btn = Button(self.new, text="Generate", command=generate_lorem)
        self.gen_btn.place(x=140,y=5)

    




if __name__=="__main__":
    w = Tk()
    root = App(w)