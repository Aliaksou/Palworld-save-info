# Palworld save info

## 📃 Description
Given a .sav file, prints the last 10 recipes unlocked by the user and all the pals they captured. It helps identifying which save corresponds to each player when migrating saves from Game pass to Steam.

This little project was made to complete the [host-save-fix](https://github.com/xNul/palworld-host-save-fix) project which helps migrating saves from Game pass to Steam. 

(I done this because it was helpful for me to migrate my coop save from Game pass to Steam, so i share it with you)

## ✨ How to use ?

### 1 ─ Download python 3 on Microsoft store 
You can run ```python``` in terminal, that will lead directly in the Microsoft store.

Check if it is installed running ```python --version```

### 2 ─ Install uesave
You need to download uesave.exe, which helps converting .sav files to .json files :

Link to the github where you can download it : [uesave](https://github.com/trumank/uesave-rs)

### 3 ─ Get the path to the .sav file you want to get information on and get the path of uesave.exe

Those are needed to run the script, so i recommend you to copy the path to these.

### 4 ─ Run the script !

In terminal, run this :
```bash
python infosavpalworld.py <path_to_uesave.exe> <path_to_.sav_file>
``` 
Example : 
```bash
python infosavpalworld.py "C:\...\Downloads\uesave.exe" "C:\...\E57C4EC13ZF0000.sav"
``` 
