from Util import print_color
import os

print_color("Welcome to the Build Script CLI", 4, 154, 211)
print_color("Here you can install buildscript onto any project you're working on.\n", 4, 154, 211)
print_color("Press enter to continue", 51, 184, 100)
input()
if os.path.exists("Build-Script"):
        print_color("Project already contains Build Script", 255, 24, 8)
        exit(1)
os.system("cls")
if not os.path.isfile("config.json"):
    print_color("Would you like to add a config.json file to your project", 4, 154, 211)
    while True:
        makeConfig = input('[Y/n] ')
        if makeConfig.lower() == "y":
            open("config.json", "w").write("""{
    "postCompileActon": "main.exe"
}""")
            break
        elif makeConfig.lower() == "n":
            break
        elif makeConfig.lower() != "n" and makeConfig != "":
            print_color("Invalid Choice. Respond with Y or N", 255, 24, 8)
        else:
            open("config.json", "w").write("""{
    "postCompileActon": "main.exe"
}""")
            break
else:
    print_color("config.json found in project", 51, 184, 100)
os.system("git clone https://github.com/Ohm-Interactive/Build-Script.git")