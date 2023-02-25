<h1 align="center">Aliasify</h1>
<p align="center">
    <strong>Easily create a permanant aliases for files on your terminal</strong>
 </p>
<p align="center">
    <img src="https://img.shields.io/badge/Made%20with-Python-blue.svg" alt="Made with Python">
</p>


aliasify is a Python script that makes it easy to create aliases for frequently used commands or scripts. The script takes two parameters - the alias name and the file to add as an alias - and creates an alias that is permanent and available in all future terminal sessions.

<h2>Usage</h2>

To use aliasify, simply run the script with the alias name and file as parameters:
```bash
python3 aliasify.py myalias /path/to/myfile
```
This will create an alias called myalias that points to the file located at /path/to/myfile.

You can even create and alias for the aliasify itself.
```bash
python3 aliasify.py aliasify aliasify.py
```
Now you can run the aliasify command on any file from any where in you bash(or zsh).

The alias will be saved to the appropriate shell configuration file `(~/.bashrc for Bash or ~/.zshrc for Zsh)`
