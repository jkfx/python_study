import os

libs = {
    'numpy', 'matplotlib', 'pillow', 'sklearn', 'requests', 'beautifulsoup4',
    'jieba', 'wheel', 'pyinstaller', 'django', 'flask', 'werobot', 'sympy',
    'pandas', 'networkx', 'pyqt5', 'pyopengl', 'pypdf2', 'docopt', 'pygame'
}

try:
    for lib in libs:
        os.system('pip install ' + lib)
    print('\n' * 3)
    print('------Successful installtion!')
except:
    print('------Failed Somehow')

os.system('pause')
