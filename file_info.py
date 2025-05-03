import os

def get_file_info(path='.'):
    file_list = []
    
    # Walk through the directory and subdirectories
    for root, dirs, files in os.walk(path):
        for filename in files:
            file_path = os.path.join(root, filename)
            
            # Skip if it's a broken symlink (optional)
            if not os.path.exists(file_path):
                continue
            
            file_size = os.path.getsize(file_path)
            file_list.append({
                "name": filename,
                "size": file_size,
                "full_path": file_path  # Optional: include full path
            })
    
    return file_list

# Test the function
if __name__ == "__main__":
    files = get_file_info()
    print(files)