import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import os
import shutil

# ==========================================
# FILE CATEGORIES
# ==========================================

categories = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".doc", ".docx", ".txt"],
    "Audio": [".mp3", ".wav", ".aac"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Excel": [".xlsx", ".xls", ".csv"],
    "Programming": [".py", ".java", ".cpp", ".c"],
    "Archives": [".zip", ".rar", ".7z"]
}

# Stores files moved during the last operation
# for the Undo feature
last_operations = []

# ==========================================
# COLORS
# ==========================================

BG_COLOR = "#f4f6f8"
CARD_COLOR = "#ffffff"
TEXT_COLOR = "#1f2937"
SUBTEXT_COLOR = "#6b7280"
PRIMARY_COLOR = "#2563eb"
SUCCESS_COLOR = "#16a34a"
DANGER_COLOR = "#dc2626"
WARNING_COLOR = "#f59e0b"

# ==========================================
# MAIN WINDOW
# ==========================================

window = tk.Tk()

window.title("Smart File Organiser")
window.geometry("800x760")
window.resizable(False, False)
window.configure(bg=BG_COLOR)

# ==========================================
# TITLE
# ==========================================

title = tk.Label(
    window,
    text="SMART FILE ORGANISER",
    font=("Arial", 26, "bold"),
    bg=BG_COLOR,
    fg=TEXT_COLOR
)

title.pack(pady=(20, 5))


subtitle = tk.Label(
    window,
    text="Organize your files quickly and automatically",
    font=("Arial", 12),
    bg=BG_COLOR,
    fg=SUBTEXT_COLOR
)

subtitle.pack(pady=(0, 20))

# ==========================================
# FOLDER CARD
# ==========================================

folder_card = tk.Frame(
    window,
    bg=CARD_COLOR,
    padx=20,
    pady=15
)

folder_card.pack(
    padx=45,
    fill="x"
)


folder_label = tk.Label(
    folder_card,
    text="SELECT FOLDER",
    font=("Arial", 11, "bold"),
    bg=CARD_COLOR,
    fg=TEXT_COLOR
)

folder_label.pack(anchor="w")


folder_frame = tk.Frame(
    folder_card,
    bg=CARD_COLOR
)

folder_frame.pack(
    fill="x",
    pady=(8, 0)
)


path_entry = tk.Entry(
    folder_frame,
    font=("Arial", 11),
    relief="solid",
    bd=1
)

path_entry.pack(
    side="left",
    fill="x",
    expand=True,
    ipady=7
)

# ==========================================
# BROWSE FUNCTION
# ==========================================

def browse_folder():

    folder = filedialog.askdirectory()

    if folder:

        path_entry.delete(
            0,
            tk.END
        )

        path_entry.insert(
            0,
            folder
        )

        status_label.config(
            text="● Folder selected",
            fg=PRIMARY_COLOR
        )


browse_button = tk.Button(
    folder_frame,
    text="Browse",
    command=browse_folder,
    font=("Arial", 10, "bold"),
    bg=PRIMARY_COLOR,
    fg="white",
    activebackground=PRIMARY_COLOR,
    activeforeground="white",
    relief="flat",
    padx=18,
    pady=7,
    cursor="hand2"
)

browse_button.pack(
    side="left",
    padx=(10, 0)
)

# ==========================================
# STATISTICS
# ==========================================

stats_frame = tk.Frame(
    window,
    bg=BG_COLOR
)

stats_frame.pack(
    pady=15
)

# ------------------------------------------
# FILES FOUND CARD
# ------------------------------------------

found_card = tk.Frame(
    stats_frame,
    bg=CARD_COLOR,
    width=210,
    height=90
)

found_card.grid(
    row=0,
    column=0,
    padx=8
)

found_card.pack_propagate(False)


found_title = tk.Label(
    found_card,
    text="FILES FOUND",
    font=("Arial", 10, "bold"),
    bg=CARD_COLOR,
    fg=SUBTEXT_COLOR
)

found_title.pack(
    pady=(13, 2)
)


files_found_label = tk.Label(
    found_card,
    text="0",
    font=("Arial", 22, "bold"),
    bg=CARD_COLOR,
    fg=PRIMARY_COLOR
)

files_found_label.pack()

# ------------------------------------------
# FILES ORGANIZED CARD
# ------------------------------------------

organized_card = tk.Frame(
    stats_frame,
    bg=CARD_COLOR,
    width=210,
    height=90
)

organized_card.grid(
    row=0,
    column=1,
    padx=8
)

organized_card.pack_propagate(False)


organized_title = tk.Label(
    organized_card,
    text="FILES ORGANIZED",
    font=("Arial", 10, "bold"),
    bg=CARD_COLOR,
    fg=SUBTEXT_COLOR
)

organized_title.pack(
    pady=(13, 2)
)


organized_label = tk.Label(
    organized_card,
    text="0",
    font=("Arial", 22, "bold"),
    bg=CARD_COLOR,
    fg=SUCCESS_COLOR
)

organized_label.pack()

# ==========================================
# CATEGORY SECTION
# ==========================================

category_card = tk.Frame(
    window,
    bg=CARD_COLOR,
    padx=20,
    pady=12
)

category_card.pack(
    padx=45,
    fill="x"
)


category_title = tk.Label(
    category_card,
    text="FILE CATEGORIES",
    font=("Arial", 11, "bold"),
    bg=CARD_COLOR,
    fg=TEXT_COLOR
)

category_title.pack(
    anchor="w"
)


category_label = tk.Label(
    category_card,
    text="No files scanned yet",
    font=("Arial", 10),
    bg=CARD_COLOR,
    fg=SUBTEXT_COLOR,
    justify="left"
)

category_label.pack(
    anchor="w",
    pady=(6, 0)
)

# ==========================================
# PROGRESS BAR
# ==========================================

progress = ttk.Progressbar(
    window,
    orient="horizontal",
    length=700,
    mode="determinate"
)

progress.pack(
    pady=(15, 7)
)

# ==========================================
# ACTIVITY LOG
# ==========================================

activity_title = tk.Label(
    window,
    text="ACTIVITY LOG",
    font=("Arial", 11, "bold"),
    bg=BG_COLOR,
    fg=TEXT_COLOR
)

activity_title.pack(
    anchor="w",
    padx=50
)


activity_frame = tk.Frame(
    window,
    bg=CARD_COLOR
)

activity_frame.pack(
    padx=45,
    pady=(5, 8),
    fill="x"
)


activity_log = tk.Text(
    activity_frame,
    width=80,
    height=6,
    font=("Consolas", 9),
    bg="#ffffff",
    fg=TEXT_COLOR,
    relief="flat",
    padx=10,
    pady=8
)

activity_log.pack(
    side="left",
    fill="both",
    expand=True
)


scrollbar = tk.Scrollbar(
    activity_frame,
    command=activity_log.yview
)

scrollbar.pack(
    side="right",
    fill="y"
)


activity_log.config(
    yscrollcommand=scrollbar.set
)

# ==========================================
# FIND FILES
# ==========================================

def find_files(folder_path):

    files_to_move = []

    for root, folders, files in os.walk(folder_path):

        for file in files:

            source = os.path.join(
                root,
                file
            )

            extension = os.path.splitext(
                file
            )[1].lower()

            category = "Others"

            for folder, extensions in categories.items():

                if extension in extensions:

                    category = folder
                    break

            current_folder = os.path.basename(
                root
            )

            # Skip files already in the correct folder
            if current_folder == category:
                continue

            files_to_move.append(
                (
                    source,
                    file,
                    category
                )
            )

    return files_to_move

# ==========================================
# SHOW SCAN RESULTS
# ==========================================

def show_scan_results(files_to_move):

    files_found_label.config(
        text=str(len(files_to_move))
    )

    category_counts = {}

    for source, file, category in files_to_move:

        category_counts[category] = (
            category_counts.get(category, 0) + 1
        )

    if category_counts:

        category_text = "    ".join(
            f"{category}: {count}"
            for category, count
            in category_counts.items()
        )

        category_label.config(
            text=category_text
        )

    else:

        category_label.config(
            text="No files need to be organized"
        )

# ==========================================
# SCAN ONLY
# ==========================================

def scan_only():

    folder_path = path_entry.get()

    if not folder_path:

        messagebox.showwarning(
            "Warning",
            "Please select a folder first."
        )

        return

    if not os.path.exists(folder_path):

        messagebox.showerror(
            "Error",
            "Selected folder does not exist."
        )

        return

    files_to_move = find_files(
        folder_path
    )

    show_scan_results(
        files_to_move
    )

    activity_log.delete(
        "1.0",
        tk.END
    )

    if not files_to_move:

        activity_log.insert(
            tk.END,
            "✓ Scan complete. "
            "No files need to be organized.\n"
        )

        status_label.config(
            text="● Scan complete - nothing to organize",
            fg=SUCCESS_COLOR
        )

        return

    activity_log.insert(
        tk.END,
        f"SCAN RESULT: "
        f"{len(files_to_move)} file(s) found\n"
    )

    for source, file, category in files_to_move:

        activity_log.insert(
            tk.END,
            f"• {file} → {category}\n"
        )

    activity_log.see(
        tk.END
    )

    status_label.config(
        text=f"● Scan complete - "
             f"{len(files_to_move)} file(s) ready",
        fg=PRIMARY_COLOR
    )

# ==========================================
# ORGANIZE FILES
# ==========================================

def organize_files():

    global last_operations

    folder_path = path_entry.get()

    if not folder_path:

        messagebox.showwarning(
            "Warning",
            "Please select a folder first."
        )

        return

    if not os.path.exists(folder_path):

        messagebox.showerror(
            "Error",
            "Selected folder does not exist."
        )

        return

    files_to_move = find_files(
        folder_path
    )

    if not files_to_move:

        show_scan_results([])

        messagebox.showinfo(
            "Information",
            "No files need to be organized."
        )

        return

    show_scan_results(
        files_to_move
    )

    # ======================================
    # PREVIEW
    # ======================================

    preview = (
        "Files to be organized:\n\n"
    )

    for source, file, category in files_to_move:

        preview += (
            f"{file}  →  {category}\n"
        )

    preview += (
        "\nDo you want to continue?"
    )

    answer = messagebox.askyesno(
        "Preview",
        preview
    )

    if not answer:

        status_label.config(
            text="● Operation cancelled",
            fg=DANGER_COLOR
        )

        return

    # ======================================
    # RESET
    # ======================================

    activity_log.delete(
        "1.0",
        tk.END
    )

    progress["value"] = 0

    progress["maximum"] = (
        len(files_to_move)
    )

    # Remove previous Undo history
    last_operations = []

    # ======================================
    # MOVE FILES
    # ======================================

    count = 0

    for source, file, category in files_to_move:

        category_path = os.path.join(
            folder_path,
            category
        )

        os.makedirs(
            category_path,
            exist_ok=True
        )

        destination = os.path.join(
            category_path,
            file
        )

        # ==================================
        # DUPLICATE HANDLING
        # ==================================

        if os.path.exists(destination):

            name, extension = (
                os.path.splitext(file)
            )

            counter = 1

            while os.path.exists(
                destination
            ):

                new_name = (
                    f"{name}_{counter}"
                    f"{extension}"
                )

                destination = os.path.join(
                    category_path,
                    new_name
                )

                counter += 1

        try:

            shutil.move(
                source,
                destination
            )

            # Save the operation for Undo
            last_operations.append(
                (
                    destination,
                    source
                )
            )

            count += 1

            # Update progress
            progress["value"] = count

            moved_name = os.path.basename(
                destination
            )

            # Activity log
            activity_log.insert(
                tk.END,
                f"✓ {moved_name} → {category}\n"
            )

            activity_log.see(
                tk.END
            )

            organized_label.config(
                text=str(count)
            )

            status_label.config(
                text=f"● Organizing... "
                     f"{count}/{len(files_to_move)}",
                fg=PRIMARY_COLOR
            )

            window.update_idletasks()

        except Exception as error:

            activity_log.insert(
                tk.END,
                f"✗ Could not move "
                f"{file}: {error}\n"
            )

            activity_log.see(
                tk.END
            )

    # ======================================
    # COMPLETE
    # ======================================

    if count > 0:

        status_label.config(
            text=f"● {count} files "
                 f"organized successfully!",
            fg=SUCCESS_COLOR
        )

        # Enable Undo
        undo_button.config(
            state="normal"
        )

    else:

        status_label.config(
            text="● No files were organized.",
            fg=DANGER_COLOR
        )

    messagebox.showinfo(
        "Complete",
        f"Organization complete!\n\n"
        f"Total files organized: {count}"
    )

# ==========================================
# UNDO LAST ACTION
# ==========================================

def undo_last_action():

    global last_operations

    if not last_operations:

        messagebox.showinfo(
            "Undo",
            "There is no organization action "
            "to undo."
        )

        return

    answer = messagebox.askyesno(
        "Undo Last Action",
        "Do you want to restore the files "
        "to their original locations?"
    )

    if not answer:
        return

    restored = 0
    failed = 0

    # Restore in reverse order
    for destination, original_path in reversed(
        last_operations
    ):

        try:

            if not os.path.exists(
                destination
            ):

                failed += 1

                activity_log.insert(
                    tk.END,
                    f"✗ File not found: "
                    f"{os.path.basename(destination)}\n"
                )

                continue

            original_folder = os.path.dirname(
                original_path
            )

            os.makedirs(
                original_folder,
                exist_ok=True
            )

            restore_path = original_path

            # Don't overwrite an existing file
            if os.path.exists(
                restore_path
            ):

                name, extension = (
                    os.path.splitext(
                        os.path.basename(
                            original_path
                        )
                    )
                )

                counter = 1

                while os.path.exists(
                    restore_path
                ):

                    new_name = (
                        f"{name}_restored_"
                        f"{counter}{extension}"
                    )

                    restore_path = os.path.join(
                        original_folder,
                        new_name
                    )

                    counter += 1

            shutil.move(
                destination,
                restore_path
            )

            restored += 1

            activity_log.insert(
                tk.END,
                f"↶ {os.path.basename(destination)} "
                f"→ original location\n"
            )

            activity_log.see(
                tk.END
            )

        except Exception as error:

            failed += 1

            activity_log.insert(
                tk.END,
                f"✗ Undo failed: "
                f"{error}\n"
            )

            activity_log.see(
                tk.END
            )

    # Clear Undo history
    last_operations = []

    organized_label.config(
        text="0"
    )

    progress["value"] = 0

    undo_button.config(
        state="disabled"
    )

    if failed == 0:

        status_label.config(
            text=f"● {restored} files "
                 f"restored successfully!",
            fg=SUCCESS_COLOR
        )

    else:

        status_label.config(
            text=f"● Restored {restored}; "
                 f"{failed} failed",
            fg=DANGER_COLOR
        )

    messagebox.showinfo(
        "Undo Complete",
        f"Files restored: {restored}\n"
        f"Failed: {failed}"
    )

# ==========================================
# CLEAR FUNCTION
# ==========================================

def clear_all():

    global last_operations

    path_entry.delete(
        0,
        tk.END
    )

    files_found_label.config(
        text="0"
    )

    organized_label.config(
        text="0"
    )

    category_label.config(
        text="No files scanned yet"
    )

    activity_log.delete(
        "1.0",
        tk.END
    )

    progress["value"] = 0

    # Clear Undo history
    last_operations = []

    undo_button.config(
        state="disabled"
    )

    status_label.config(
        text="● Ready",
        fg=TEXT_COLOR
    )

# ==========================================
# BUTTON FRAME
# ==========================================

button_frame = tk.Frame(
    window,
    bg=BG_COLOR
)

button_frame.pack(
    pady=5
)

# ==========================================
# ORGANIZE BUTTON
# ==========================================

organize_button = tk.Button(
    button_frame,
    text="ORGANIZE FILES",
    command=organize_files,
    font=("Arial", 10, "bold"),
    bg=PRIMARY_COLOR,
    fg="white",
    activebackground=PRIMARY_COLOR,
    activeforeground="white",
    relief="flat",
    width=17,
    height=2,
    cursor="hand2"
)

organize_button.grid(
    row=0,
    column=0,
    padx=3
)

# ==========================================
# SCAN ONLY BUTTON
# ==========================================

scan_button = tk.Button(
    button_frame,
    text="SCAN ONLY",
    command=scan_only,
    font=("Arial", 10, "bold"),
    bg="#64748b",
    fg="white",
    activebackground="#64748b",
    activeforeground="white",
    relief="flat",
    width=13,
    height=2,
    cursor="hand2"
)

scan_button.grid(
    row=0,
    column=1,
    padx=3
)

# ==========================================
# UNDO BUTTON
# ==========================================

undo_button = tk.Button(
    button_frame,
    text="UNDO LAST ACTION",
    command=undo_last_action,
    font=("Arial", 10, "bold"),
    bg=WARNING_COLOR,
    fg="white",
    activebackground=WARNING_COLOR,
    activeforeground="white",
    relief="flat",
    width=17,
    height=2,
    cursor="hand2",
    state="disabled"
)

undo_button.grid(
    row=0,
    column=2,
    padx=3
)

# ==========================================
# CLEAR BUTTON
# ==========================================

clear_button = tk.Button(
    button_frame,
    text="CLEAR",
    command=clear_all,
    font=("Arial", 10, "bold"),
    bg="#e5e7eb",
    fg=TEXT_COLOR,
    activebackground="#d1d5db",
    relief="flat",
    width=9,
    height=2,
    cursor="hand2"
)

clear_button.grid(
    row=0,
    column=3,
    padx=3
)

# ==========================================
# STATUS
# ==========================================

status_label = tk.Label(
    window,
    text="● Ready",
    font=("Arial", 10, "bold"),
    bg=BG_COLOR,
    fg=TEXT_COLOR
)

status_label.pack(
    pady=(5, 10)
)

# ==========================================
# RUN APPLICATION
# ==========================================

window.mainloop()