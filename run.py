import winreg
import ctypes

def set_registry_key(base_key, sub_key, name, value):
    try:
        key = winreg.OpenKey(base_key, sub_key, 0, winreg.KEY_SET_VALUE)
    except FileNotFoundError:
        key = winreg.CreateKey(base_key, sub_key)

    winreg.SetValueEx(key, name, 0, winreg.REG_DWORD, value)
    winreg.CloseKey(key)

def show_message_box(message):
    ctypes.windll.user32.MessageBoxW(0, message, "Notification", 1)

def fix_xbox_game_bar():
    try:
        # Step 2: Check or create HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\GameDVR
        base_key = winreg.HKEY_LOCAL_MACHINE
        sub_key = r"SOFTWARE\Policies\Microsoft\Windows\GameDVR"
        name = "AllowGameDVR"
        value = 1
        set_registry_key(base_key, sub_key, name, value)

        # Step 3: Modify HKEY_CURRENT_USER\System\GameConfigStore\GameDVR_Enabled
        base_key = winreg.HKEY_CURRENT_USER
        sub_key = r"System\GameConfigStore"
        name = "GameDVR_Enabled"
        set_registry_key(base_key, sub_key, name, value)

        # Step 4: Modify HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\GameDVR\AppCaptureEnabled
        sub_key = r"SOFTWARE\Microsoft\Windows\CurrentVersion\GameDVR"
        name = "AppCaptureEnabled"
        set_registry_key(base_key, sub_key, name, value)

        show_message_box("Xbox Game Bar settings updated successfully.")
    except Exception as e:
        show_message_box("Xbox Game Bar settings updated Failed")

if __name__ == "__main__":
    fix_xbox_game_bar()
