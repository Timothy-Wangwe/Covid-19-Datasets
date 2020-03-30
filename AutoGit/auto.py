def git():
    from os import system

    system("git pull")
    system("git add *")
    system("git commit -m 'Automated hourly dataset update'")
    system("git push")
    system("git status")
