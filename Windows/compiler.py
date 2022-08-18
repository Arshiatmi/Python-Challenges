import os

folders = ['1', '2', '3', '4', '5', '6']

for folder in folders:
    os.system(f"pyinstaller.exe --onefile ./{folder}/code.txt")
    os.system(f"del ./{folder}/vuln.exe")
    os.system(f"move dist/code.exe {folder}/vuln.exe")
    os.system("del -r dist")
    os.system("del -r build")
    os.system("del code.spec")
