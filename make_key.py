import os
import sys
import winreg as reg

# Get path of current working directory and python.exe
cwd = os.getcwd()
python_exe = sys.executable


# Set the path of the context menu (right-click menu)
keyVal = r'Directory\\Background\\shell'

# Create first key which will display the name in the context menu
key2change = reg.OpenKey(reg.HKEY_CLASSES_ROOT, keyVal, 0, reg.KEY_ALL_ACCESS)
key = reg.CreateKey(key2change, r"Organiser\\")
reg.SetValue(key, '', reg.REG_SZ, '&Organise folder')
reg.CloseKey(key)


# Create 2nd key which will run the python script
key2change1 = reg.OpenKey(reg.HKEY_CLASSES_ROOT, keyVal, 0, reg.KEY_ALL_ACCESS)
key1 = reg.CreateKey(key2change1, r"Organiser\\command")
reg.SetValue(key1, '', reg.REG_SZ, python_exe + f' "{cwd}\\file_organiser.py"')
reg.CloseKey(key1)
