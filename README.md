# SiFiBi - Simple File Binder

**SiFiBi (Simple File Binder)** is a lightweight Python tool designed to automatically organize files in a directory based on their file extensions. Using a configuration file, SiFiBi can move files into specified folders according to their types.

## 🌟 Features

- **Automatic Monitoring**: Continuously watches for changes in the directory and organizes newly added files on-the-fly.
- **Custom Configuration**: Define your file types and target directories using a JSON configuration file.
- **Size Threshold**: Specify a maximum file size for processing to ensure larger files are left untouched.

## 🔧 Setup & Usage

1. **Prerequisites**:
    - **Using pip**:
      ```bash
      pip install watchdog
      ```
    - **For Linux users**: Depending on your distribution, you might be able to install `watchdog` directly using your package manager, for example:
      ```bash
      sudo apt install python3-watchdog  # For Ubuntu/Debian
      sudo pacman -S python-watchdog     # For Arch Linux
      ```

2. **Clone the Repository**:
    ```bash
    git clone https://github.com/Hathor875/SiFiBi-simple-file-binder-in-python.git
    ```

3. **Navigate to the Directory**:
    ```bash
    cd SiFiBi-simple-file-binder-in-python
    ```
    ### Directory Handling

    SiFiBi organizes files in the parent directory of its location. To segregate files in a specific directory, place the SiFiBi directory inside the target directory you wish to organize. The program will        then work on files one level up from its own location.
4. **Configuration**:
    Edit the `config.json` file to define the file extensions and corresponding directories. Set your desired size threshold to exclude larger files.

5. **Run SiFiBi**:
    ```bash
    python main.py
    ```

6. **Autostart**:
  ## 🚀 Autostart Setup

To ensure that SiFiBi runs automatically upon system startup, you can utilize the `cron` job scheduler on Linux systems.

### Linux - Using Cron:

1. **Open the crontab**:
   ```bash
   crontab -e
  Insert the following line, replacing the path with the path to your script:
  @reboot /usr/bin/python3 /path/to/your/script.py



    Save and exit:
    Save the changes to crontab and exit the editor.

    Now, SiFiBi will be automatically executed at every system startup. If your script requires root permissions, you can add it to the root's crontab (sudo crontab -e). Otherwise, a regular user's crontab should suffice.

    Note: Autostart methods might vary based on the operating system. The above method is specific to Linux systems. Depending on your OS, you might need to explore alternative methods for autostart configurations.
  

## ⚙ Configuration
>Note: i add defult config file for easier setup and understanding.  


- **settings.size_threshold**: Define the maximum file size (in MB) that SiFiBi will process. Files larger than this threshold will be ignored.
- **settings.sleep_monitoring_time**: Define sleep time betwen autoscan in second 1 = 1s,0.5 = 0,5s etc.
- **settings.monitoring_Directory**: Define path to scan directory.
- **file_types**: Map file extensions to desired destination folders. For example, `.jpg` files will be moved to a `photo_files` directory.
 

```json
{
    "settings": {
        "size_threshold": 2,
        "sleep_monitoring_time": 2,
        "monitoring_directory": ".."
    },
    "file_types": {
        ".jpg": "photo_files",
        ".mp3": "audio_files",
        ".pdf": "document_files"
    }
}
