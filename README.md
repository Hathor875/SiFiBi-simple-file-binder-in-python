# SiFiBi - Simple File Binder

**SiFiBi (Simple File Binder)** is a lightweight Python tool designed to automatically organize files in a directory based on their file extensions. Using a configuration file, SiFiBi can move files into specified folders according to their types.

## 🌟 Features

- **Automatic Organization**: SiFiBi monitors your directory and sorts files based on their extensions.
- **Custom Configuration**: Define your file types and target directories using a JSON configuration file.
- **Size Threshold**: Specify a maximum file size for processing to ensure larger files are left untouched.

## 🔧 Setup & Usage

1. **Clone the Repository**:
git clone https://github.com/Hathor875/SiFiBi-simple-file-binder-in-python.git

2. **Navigate to the Directory**:
cd SiFiBi-simple-file-binder-in-python

3. **Configuration**:
  Edit the `config.json` file to define the file extensions and corresponding directories. Set your desired size threshold to exclude larger files.

4. **Run SiFiBi**:

## ⚙ Configuration

    -settings.size_threshold: Define the maximum file size (in MB) that SiFiBi will process. Files larger than this threshold will be ignored.
    
    -file_types: Map file extensions to desired destination folders. In the example above, .jpg files will be moved to a photo_files directory.


```json
{
    "settings": {
        "size_threshold": 100
    },
    "file_types": {
        ".jpg": "photo_files",
        ".mp3": "audio_files",
        ".pdf": "document_files"
    }
}

```

This project is open-source and available under the MIT License.
