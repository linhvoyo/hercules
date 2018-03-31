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

def errors():
    """
    Usage
    """
    print "usage: python birds.py <PROJECT NAME> <LANGUAGE>\n"
    print "LANGUAGE = c or python"
    sys.exit(1)

def create_python():
    """
    Automating file creation for python
    """
    print ("Creating template for " + sys.argv[2]) + " ..."
    # os.makedirs(PROJECT)
    try:
        os.makedirs(PROJECT)
    except OSError:
        print PROJECT + " folder already exists"
        sys.exit(1)
    py_file = open(PROJECT + '/' + PROJECT + '.py', 'w')
    py_file.write('')
    py_file.close()
    py_gitignore = "# Byte-compiled / optimized / DLL files\n__pycache__/\n*.py[cod]\n*$py.class\n\n# C extensions\n*.so\n\n# Distribution / packaging\n.Python\nbuild/\ndevelop-eggs/\ndist/\ndownloads/\neggs/\n.eggs/\nlib/\nlib64/\nparts/\nsdist/\nvar/\nwheels/\n*.egg-info/\n.installed.cfg\n*.egg\nMANIFEST\n\n# PyInstaller\n#  Usually these files are written by a python script from a template\n#  before PyInstaller builds the exe, so as to inject date/other infos into it.\n*.manifest\n*.spec\n\n# Installer logs\npip-log.txt\npip-delete-this-directory.txt\n\n\n# Unit test / coverage reports\nhtmlcov/\n.tox/\n.coverage\n.coverage.*\n.cache\nnosetests.xml\ncoverage.xml\n*.cover\n.hypothesis/\n.pytest_cache/\n\n# Translations\n*.mo\n*.pot\n\n# Django stuff:\n*.log\nlocal_settings.py\ndb.sqlite3\n\n# Flask stuff:\ninstance/\n.webassets-cache\n\n\n# Scrapy stuff:\n.scrapy\n\n\n# Sphinx documentation\ndocs/_build/\n\n\n# PyBuilder\ntarget/\n\n# Jupyter Notebook\n.ipynb_checkpoints\n\n# pyenv\n.python-version\n\n# celery beat schedule file\ncelerybeat-schedule\n\n# SageMath parsed files\n*.sage.py\n\n# Environments\n.env\n.venv\nenv/\nvenv/\nENV/\nenv.bak/\nvenv.bak/\n\n# Spyder project settings\n.spyderproject\n.spyproject\n\n# Rope project settings\n.ropeproject\n\n# mkdocs documentation\n/site\n\n# mypy\n.mypy_cache/"
    gitignore(py_gitignore)

if len(sys.argv) != 3:
    errors()
PROJECT = sys.argv[1]
if sys.argv[2] == 'c':
    create_c()
elif sys.argv[2] == 'python':
    create_python()
else:
    sys.exit(1)
    errors()
