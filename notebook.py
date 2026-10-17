import tkinter as tk
from tkinter import filedialog, messagebox
import os


class MiniNotepad:
    def __init__(self, root):
        self.root = root
        self.root.title("小本")
        self.root.geometry("600x420")
        self.current_file = None

        self.text = tk.Text(root, undo=True, wrap="word",
                            font=("Microsoft YaHei", 11))
        self.text.pack(fill=tk.BOTH, expand=True)

        menubar = tk.Menu(root)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="新建", command=self.new_file)
        filemenu.add_command(label="打开", command=self.open_file)
        filemenu.add_command(label="保存", command=self.save_file)
        filemenu.add_command(label="另存为", command=self.save_as)
        filemenu.add_separator()
        filemenu.add_command(label="退出", command=self.on_close)
        menubar.add_cascade(label="文件", menu=filemenu)
        root.config(menu=menubar)

        root.protocol("WM_DELETE_WINDOW", self.on_close)

    def new_file(self):
        self.text.delete("1.0", tk.END)
        self.current_file = None
        self.root.title("小本 - 未命名")

    def open_file(self):
        path = filedialog.askopenfilename(
            filetypes=[("文本文件", "*.txt"), ("所有文件", "*.*")])
        if not path:
            return
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        self.text.delete("1.0", tk.END)
        self.text.insert("1.0", content)
        self.current_file = path
        self.root.title(f"小本 - {os.path.basename(path)}")

    def save_file(self):
        if self.current_file:
            with open(self.current_file, "w", encoding="utf-8") as f:
                f.write(self.text.get("1.0", tk.END).rstrip("\n"))
            messagebox.showinfo("提示", "已保存")
        else:
            self.save_as()

    def save_as(self):
        path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("文本文件", "*.txt")])
        if not path:
            return
        with open(path, "w", encoding="utf-8") as f:
            f.write(self.text.get("1.0", tk.END).rstrip("\n"))
        self.current_file = path
        self.root.title(f"小本 - {os.path.basename(path)}")
        messagebox.showinfo("提示", "已保存")

    def on_close(self):
        self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    MiniNotepad(root)
    root.mainloop()