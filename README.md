# Custom-CMD-Commands
Steps to create a custom cmd command in Windows

### The following steps demonstrate how to create a custom command to run a python script from cmd
- Create a batch file (.bat) with the following line
    ```
    @START "python" "path-of-file-with-filename"
    ```
    Example - @START "python" "C:\Users\ABC\Downloads\helloWorld.py"
- Save this file in C:\Windows\System32 with the name of the custom command.
    For example, if the file is named hello then the command to be used to call the script will be hello  
- Once the file is saved in the correct directory, the custom command (ex - hello) can be used to run the script  
![image](https://github.com/Renita1206/Custom-CMD-Commands/assets/66276711/6ec6c176-cef7-4dbc-ad28-4546a9937693)


### The following steps demonstrate how to create a custom command to open file in notepad
- Create a batch file (.bat) with the following line
    ```
    @START "path-to-notepad" "%1"
    ```
    Example - @START "c:\Program Files\Notepad\notepad.exe" "%1"
- Save this file in C:\Windows\System32 with the name of the custom command.



Source - <a href="https://stackoverflow.com/questions/5181709/custom-commands-in-windows-command-prompt"> link </a>
