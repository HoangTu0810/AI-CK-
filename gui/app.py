import tkinter as tk
from tkinter import messagebox

from core.blocker import WebsiteBlocker


class BlockerApp:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Website Blocker AI")
        self.root.geometry("520x260")
        self.blocker = WebsiteBlocker()

        self._build_ui()

    def _build_ui(self):
        tk.Label(self.root, text="Nhập URL website:", font=("Segoe UI", 11)).pack(pady=(18, 6))

        self.url_entry = tk.Entry(self.root, width=60)
        self.url_entry.pack(pady=4)

        self.check_button = tk.Button(self.root, text="Kiểm tra", command=self.check_url)
        self.check_button.pack(pady=10)

        self.block_button = tk.Button(self.root, text="Block", command=self.block_url)
        self.block_button.pack(pady=4)

        self.unblock_button = tk.Button(self.root, text="Unblock", command=self.unblock_url)
        self.unblock_button.pack(pady=4)

        self.result_label = tk.Label(self.root, text="Kết quả sẽ hiển thị ở đây.", font=("Segoe UI", 10))
        self.result_label.pack(pady=6)

        self.log_button = tk.Button(self.root, text="Xem lịch sử", command=self.show_history)
        self.log_button.pack(pady=4)

    def check_url(self):
        url = self.url_entry.get().strip()
        if not url:
            messagebox.showwarning("Cảnh báo", "Vui lòng nhập một URL hợp lệ.")
            return

        decision = self.blocker.enforce(url)
        color = "red" if decision == "BLOCK" else "green"
        self.result_label.config(text=f"Đánh giá: {decision}", fg=color)

    def unblock_url(self):
        url = self.url_entry.get().strip()
        if not url:
            messagebox.showwarning("Cảnh báo", "Vui lòng nhập URL.")
            return

        result = self.blocker.unblock_website(url)
        self.result_label.config(text=result, fg="blue")

    def block_url(self):
        url = self.url_entry.get().strip()
        if not url:
            messagebox.showwarning("Cảnh báo", "Vui lòng nhập URL.")
            return

        result = self.blocker.block_website(url)
        self.result_label.config(text=result, fg="red")

    def show_history(self):
        history = self.blocker.history
        if not history:
            messagebox.showinfo("Lịch sử", "Chưa có lượt kiểm tra nào.")
            return

        lines = [f"[{item['timestamp']}] {item['url']} → {item['decision']}" for item in history]
        messagebox.showinfo("Lịch sử", "\n".join(lines))