1)Install VSCode and configure it for for python development
2) Install the following plugins:
Python
Remote-SSH
Git lens
WSL
3)Configure VSCode for Python development
The important thing to note here is that User settings apply to all projects on your system. Project specific settings are referred to as Workspace settings and are stored in the location .vscode/settings.json file in your workspace folder (The folder you opened in VSCode).

4)Ensure the following tools are configured in your user settings.
Linter: use flake8
Sorted Imports: use isort
Auto-formatter: use black
Python code defaults: 4 spaces for tab, remove trailing whitespaces

Ensure the following configurations are set in your workspace settings
Python Path
Run auto-formatter and sort imports everytime the file is saved.
Custom parameters to the code-formatting tools (if needed)
5) Create a PR with the auto-formatted code.
6) create a new branch of the git tag 'v01' then open the nonstandard_code.py in vs code and ensure it automatically formats the script on save.
7)Fix the problems highlighted in VSCode until it indicates there are no problems with the script.
8) Create a PR from the new branch and share your VSCode workspace settings in the PR. Ensure the JSON content (workspace settings) is properly formatted using GitHub markdown.

Fix any merge conflicts

Note that GitHub might complain about a merge conflict. Fix the merge conflict using a master merge, i.e. pull the latest master to your local machine and then merge master into your branch. Fix any conflicts, commit your changes and push to remote. The conflict should now be resolved
