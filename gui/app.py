import tkinter as tk
from tkinter import messagebox


# Import core modules
from core.blocker import WebsiteBlocker

# =========================
# GUI FUNCTIONS
# =========================
def check_website():
    url = entry_url.get().strip()

    if not url:
        messagebox.showwarning("Warning", "Vui lòng nhập website")
        return

    try:
        result = blocker.enforce(url)

        if "BLOCK" in result:
            label_result.config(
                text=f"AI dự đoán: NGUY HIỂM -> Sẽ bị chặn",
                fg="red"
            )
        else:
            label_result.config(
                text=f"AI dự đoán: AN TOÀN",
                fg="green"
            )

    except Exception as e:
        messagebox.showerror("Error", f"Lỗi predictor: {e}")
def block_site():
    url = entry_url.get().strip()

    if not url:
        messagebox.showwarning("Warning", "Vui lòng nhập website")
        return

    try:
        blocker.block_website(url)

        if url not in listbox_blocked.get(0, tk.END):
            listbox_blocked.insert(tk.END, url)

        label_status.config(text=f"Đã chặn: {url}", fg="red")

    except Exception as e:
        messagebox.showerror("Error", f"Lỗi block: {e}")
def unblock_site():
    selected = listbox_blocked.curselection()

    if not selected:
        messagebox.showwarning("Warning", "Chọn website để bỏ chặn")
        return

    url = listbox_blocked.get(selected)

    try:
        blocker.unblock(url)
        listbox_blocked.delete(selected)

        label_status.config(text=f"Đã bỏ chặn: {url}", fg="blue")

    except Exception as e:
        messagebox.showerror("Error", f"Lỗi unblock: {e}")

def auto_check_and_block():
    url = entry_url.get().strip()
    if not url:
        messagebox.showwarning("Warning", "Vui lòng nhập website")
        return
    try:
        result = blocker.enforce(url)
        if "BLOCK" in result:
            if url not in listbox_blocked.get(0, tk.END):
                listbox_blocked.insert(tk.END, url)
            label_status.config(
                text=f"AI phát hiện nguy hiểm -> Đã chặn {url}",
                fg="red"
            )
        else:
            label_status.config(
                text=f"Website an toàn",
                fg="green"
            )

    except Exception as e:
        messagebox.showerror("Error", f"Lỗi hệ thống: {e}")

# =========================
# MAIN WINDOW
# =========================

app = tk.Tk()
app.title("Website Blocker AI")
app.geometry("500x500")
blocker = WebsiteBlocker()

# =========================
# TITLE
# =========================

label_title = tk.Label(
    app,
    text="WEBSITE BLOCKER AI",
    font=("Arial", 16, "bold")
)
label_title.pack(pady=10)

# =========================
# INPUT
# =========================

frame_input = tk.Frame(app)
frame_input.pack(pady=10)

label_url = tk.Label(frame_input, text="Nhập website:")
label_url.pack(side=tk.LEFT)

entry_url = tk.Entry(frame_input, width=30)
entry_url.pack(side=tk.LEFT, padx=5)

# =========================
# BUTTONS
# =========================

frame_buttons = tk.Frame(app)
frame_buttons.pack(pady=10)

btn_check = tk.Button(
    frame_buttons,
    text="Check AI",
    width=12,
    command=check_website
)
btn_check.grid(row=0, column=0, padx=5)

btn_block = tk.Button(
    frame_buttons,
    text="Block",
    width=12,
    command=block_site
)
btn_block.grid(row=0, column=1, padx=5)

btn_unblock = tk.Button(
    frame_buttons,
    text="Unblock",
    width=12,
    command=unblock_site
)
btn_unblock.grid(row=0, column=2, padx=5)

btn_auto = tk.Button(
    frame_buttons,
    text="Auto Block (AI)",
    width=15,
    command=auto_check_and_block
)
btn_auto.grid(row=1, column=0, columnspan=3, pady=5)

# =========================
# RESULT LABEL
# =========================

label_result = tk.Label(app, text="", font=("Arial", 11))
label_result.pack(pady=5)

label_status = tk.Label(app, text="", font=("Arial", 11))
label_status.pack(pady=5)

# =========================
# BLOCKED LIST
# =========================

label_list = tk.Label(app, text="Danh sách website đã chặn:")
label_list.pack(pady=5)

listbox_blocked = tk.Listbox(app, width=50, height=10)
listbox_blocked.pack(pady=10)

# =========================
# RUN APP
# =========================

if __name__ == "__main__":
    app.mainloop()
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

