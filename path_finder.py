import os
import platform

def get_config_path(username):
    try:
        system = platform.system().lower()
        if system == "windows":
            config_dir = os.path.join(os.getenv("APPDATA"), "Cursor", "User", "globalStorage")
        elif system == "darwin":  # macOS
            config_dir = os.path.join("/Users", username, "Library", "Application Support", "Cursor", "User", "globalStorage")
        elif system == "linux":
            config_dir = os.path.join("/home", username, ".config", "Cursor", "User", "globalStorage")
        else:
            raise ValueError(f"Unsupported operating system: {system}")
        
        return os.path.join(config_dir, "storage.json")
    except Exception as e:
        return str(e)

# Example usage:
username = "XXXXXXXXXX"  # Replace this with the actual username
path = get_config_path(username)
print(path)

