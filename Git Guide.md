2023-06-12 @17:17

Status: #idea
Tags:  [[𝑪𝑺 📍]]

You know:
- git add .
- git commit -m ""
- git push

But do you know?...
| Technique / Shortcut                                                                 | text                                                                                      |
| ------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------- |
| Commit & Add simultaneously                                                          | git commit -am ""                                                                         |
| Create an Alias for a command                                                        | git config --global alias.NAME "git add ." ...... then use git NAME "" to run the command |
| Change the message of the last Commit                                                | git commit --ammend -m ""                                                                 |
| Overwrite History on Remote                                                          | git push origin main --force                                                              |
| Undo a Commit with a new Commit                                                      | git revert ___                                                                            |
| Remove changes from current Directory to save for later                              | git stash                                                                                 |
| Add Stashed changes back to current Directory                                        | git pop                                                                                   |
| Display a pretty log of Git History                                                  | git log --graph --oneline --decorate                                                      |
| Start from last known working Commit, can then be used to work forward to find error | git bisect ___                                                                            |
| Git Hooks, for running some operation for every commit (Ex: Testing suites!)         | //////                                                                                        |
| Bringing the Main branch to your Local files                                         | git fetch origin ...... git reset --hard main                                                                                          |





