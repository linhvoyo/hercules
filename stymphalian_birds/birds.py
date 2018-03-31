import os
import sys
from git import Repo
import shutil


# directory = os.getcwd()

"""
Current run command
    python birds.py fdf c
"""

def git_pull(repo_link, repo_name):
    """
    Git clone repo
    """
    print "Git clone :" + repo_link + "\t./" + repo_name
    try:
        Repo.clone_from(repo_link, PROJECT + '/src/' + repo_name)
    except:
        print "Git pull for " + repo_name + " failed..."
        shutil.rmtree(PROJECT)
        sys.exit(1)

def makefile():
    """
    Generating Makefile
    """
    print "Generating Makefile..."
    mfile = open(PROJECT + '/Makefile', 'w')
    mfile.write('NAME = ' + PROJECT + '\n\n')
    mfile.write('$(NAME):\n\n\n')
    mfile.write('all: $(NAME)\n\n')
    mfile.write('clean:\n\t@rm -rf *.o\n\n')
    mfile.write('fclean: clean\n\t@rm -rf $(NAME)\n\n')
    mfile.write('re: fclean all\n')
    mfile.close()

def gitignore(c_gitignore):
    """
    Generating .gitignore file for c
    """
    print "Generating .gitignore for " + sys.argv[2] + " ..."
    git_ignore = open(PROJECT + '/.gitignore', 'w')
    git_ignore.write(c_gitignore)
    git_ignore.close()

def create_c():
    """
    Automating file creation for c
    """
    print ("Creating template for " + sys.argv[2]) + " ..."
    # os.makedirs(PROJECT)
    try:
        os.makedirs(PROJECT)
    except OSError:
        print PROJECT + " folder already exists"
        sys.exit(1)
    os.makedirs(PROJECT + '/src')
    os.makedirs(PROJECT + '/includes')
    author_file = open(PROJECT + '/author', 'w')
    author_file.write("lilam\n")
    author_file.close()
    makefile()
    c_gitignore = "# Prerequisites\n*.d\n\n" +\
    "# Object files\n*.o\n*.ko\n*.obj\n*.elf\n\n" +\
    "# Linker output\n*.ilk\n*.map\n*.exp\n\n" +\
    "# Precompiled Headers\n*.gch\n*.pch\n\n" +\
    "# Libraries\n*.lib\n*.a\n*.la\n*.lo\n\n" +\
    "# Shared objects (inc. Windows DLLs)\n*.dll\n*.so\n*.so.*\n*.dylib\n\n" +\
    "# Executables\n*.exe\n*.out\n*.app\n*.i*86\n*.x86_64\n*.hex\n\n" +\
    "# Debug files\n*.dSYM/\n*.su\n*.idb\n*.pdb\n\n" +\
    "# Kernel Module Compile Results\n*.mod*\n*.cmd\n.tmp_versions/\nmodules.order\n" +\
    "Module.symvers\nMkfile.old\ndkms.conf"
    gitignore(c_gitignore)
    git_pull('https://github.com/linhvoyo/libft', 'libft')


PROJECT = sys.argv[1]
if sys.argv[2] == "c":
    create_c()


#Command line
    python birds.py fdf c


# length = len(sys.argv)
#
#
# for i in range(3, length):
#     if i == 'libft' or i == 'gnl'
#         print
#     print sys.argv[i]

# print sys.argv[3]
