# Xbox Game Bar Fix Tool

## Overview
This Python script automates the process of fixing issues with the Xbox Game Bar on Windows by modifying specific registry settings. The tool ensures that the necessary configurations are enabled for the Xbox Game Bar to function correctly.

## Features
- Automatically modifies registry keys to enable GameDVR.
- Displays a success or failure message after the operation.

## Prerequisites
- Python 3.x installed on your system.
- Administrator privileges are required to run the script as it modifies system registry keys.

## Usage

1. **Clone the Repository:**
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Run the Script:**
   ```bash
   python xbox_game_bar_fix.py
   ```

3. **Notification:**
   - A message box will appear indicating whether the operation was successful or failed.

## Registry Modifications
The script modifies the following registry keys:

1. **HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\GameDVR**
   - Creates or updates the `AllowGameDVR` key to `1`.

2. **HKEY_CURRENT_USER\System\GameConfigStore**
   - Updates the `GameDVR_Enabled` key to `1`.

3. **HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\GameDVR**
   - Updates the `AppCaptureEnabled` key to `1`.

## Error Handling
- If any error occurs during the registry modification, a failure message will be displayed.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue to discuss potential changes.

## Disclaimer
Use this script at your own risk. Modifying the Windows registry can cause system instability if not done correctly.

