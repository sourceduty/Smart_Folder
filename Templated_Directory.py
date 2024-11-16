import os
import shutil

def create_project_structure(base_path):
    """
    Creates a templated directory structure for Python projects.
    """
    directories = [
        'src',              # Source files
        'tests',            # Test files
        'docs',             # Documentation files
        'configs',          # Configuration files
        'scripts',          # Utility scripts
        'data',             # Data files
        'notebooks',        # Jupyter notebooks
        'static',           # Static files like images, CSS, JS
        'logs',             # Log files
    ]
    for dir_name in directories:
        dir_path = os.path.join(base_path, dir_name)
        os.makedirs(dir_path, exist_ok=True)

def categorize_file(file_name):
    """
    Categorizes a file into the appropriate project folder.
    """
    if file_name.startswith('test_'):
        return 'tests'
    elif file_name.endswith('.ipynb'):
        return 'notebooks'
    elif file_name.endswith('.py'):
        return 'src'
    elif file_name.endswith(('.json', '.yaml', '.yml')):
        return 'configs'
    elif file_name.endswith(('.png', '.jpg', '.jpeg', '.svg', '.css', '.js')):
        return 'static'
    elif file_name.endswith('.log'):
        return 'logs'
    else:
        return 'scripts'

def organize_files(source_path, base_path):
    """
    Organizes files in the source directory into the templated structure.
    """
    for root, _, files in os.walk(source_path):
        for file in files:
            src_file_path = os.path.join(root, file)
            category = categorize_file(file)
            target_dir = os.path.join(base_path, category)
            os.makedirs(target_dir, exist_ok=True)
            target_file_path = os.path.join(target_dir, file)
            shutil.move(src_file_path, target_file_path)
            print(f"Moved: {src_file_path} -> {target_file_path}")

if __name__ == "__main__":
    source_directory = input("Enter the source directory path: ")
    base_directory = input("Enter the base directory path for the organized structure: ")
    
    if not os.path.exists(source_directory):
        print("Error: Source directory does not exist.")
    else:
        create_project_structure(base_directory)
        organize_files(source_directory, base_directory)
        print("Files have been organized successfully.")
