import os
import shutil

# File categories
categories = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".doc", ".docx", ".txt"],
    "Audio": [".mp3", ".wav", ".aac"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Excel": [".xlsx", ".xls", ".csv"],
    "Programming": [".py", ".java", ".cpp", ".c"],
    "Archives": [".zip", ".rar", ".7z"]
}

# Get folder from user
folder_path = input("Enter folder path: ")

if not os.path.exists(folder_path):
    print("❌ Folder does not exist.")
    exit()

# Store files that will be moved
files_to_move = []

# Find files
for file in os.listdir(folder_path):

    file_path = os.path.join(folder_path, file)

    # Ignore folders
    if os.path.isdir(file_path):
        continue

    extension = os.path.splitext(file)[1].lower()

    category = "Others"

    for folder, extensions in categories.items():
        if extension in extensions:
            category = folder
            break

    files_to_move.append((file, category))


# Preview
print("\n========== PREVIEW ==========\n")

if not files_to_move:
    print("No files found to organize.")
    exit()

for file, category in files_to_move:
    print(f"{file}  →  {category}")


# Confirmation
print("\n=============================")

choice = input("\nDo you want to organize these files? (y/n): ").lower()

if choice != "y":
    print("\n❌ Operation cancelled.")
    exit()


# Move files
count = 0

for file, category in files_to_move:

    source = os.path.join(folder_path, file)

    # Create category folder
    category_path = os.path.join(folder_path, category)
    os.makedirs(category_path, exist_ok=True)

    destination = os.path.join(category_path, file)

    # Handle duplicate filename
    if os.path.exists(destination):

        name, extension = os.path.splitext(file)

        counter = 1

        while os.path.exists(destination):
            new_name = f"{name}_{counter}{extension}"
            destination = os.path.join(category_path, new_name)
            counter += 1

    shutil.move(source, destination)

    print(f"Moved: {file} → {category}")
    count += 1


# Final summary
print("\n================================")
print("      ORGANISATION COMPLETE")
print("================================")

print(f"Total files organized: {count}")
print("✅ Done!")