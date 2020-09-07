import os
import argparse

parser = argparse.ArgumentParser(description='Repository name')
parser.add_argument('path', type=str, help='Name of the folder')
args = parser.parse_args()
path = args.path
os.system(f"hub create {path}")
os.system(f"hub clone https://github.com/SubhadityaMukherjee/{path}.git")


def make_files():
    with open(f'{path}/README.md', 'w') as f:
        f.write("# README\n-This file is for ")

    with open(f'{path}/.gitignore', 'w') as f:
        f.write("*.pth\n*.csv\n*checkpoint*\n*.v2")
    os.makedirs(f'{path}/data', exist_ok=True)
    with open(f'{path}/data/.gitignore', 'w') as f:
        f.write('*\n"*"')


make_files()
