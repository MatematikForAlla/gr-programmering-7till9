# en lista att spara kommandohistoriken i.
history = []
# v�r dictionary som h�ller koll p� var programmet
# finns f�r att k�ra ett visst kommando.
cmds = {"ls" : "/usr/bin/ls",
    "cp" : "/usr/bin/cp",
    "mv" : "/usr/bin/mv",
    "res" : "/usr/local/bin/res",
    "course" : "/usr/local/bin/course",
    "python" : "/opt/sfw/bin/python",
    "emacs" : "/usr/local/bin/emacs",
    "vim" : "/opt/sfw/bin/vim",
    "g++" : "/usr/sfw/bin/g++",
    "cc" : "/usr/local/bin/cc",
    "gdb" : "/opt/sfw/bin/gdb"}

cmd = raw_input("Enter command: ")
while cmd != "":
    try:
        print cmds[cmd]
        # koden nedan kommer aldrig intr�ffa om det blir
        # en exception i cmds[cmd], d� hoppar den direkt
        # till except nedan.
        history.append(cmd)
    except KeyError:
        print "Sorry, that command is not in the dictionary."
    except:
        print "There is something seriously wrong here."
    cmd = raw_input("Enter command: ")

for cmd in history:
    print cmd,

