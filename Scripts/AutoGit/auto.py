def git():
    from os import system

    system("git pull")
    system("git add *")
    system("git commit -m 'Automated every 6th hour dataset update'")
    system("git push")
    system("git status")
