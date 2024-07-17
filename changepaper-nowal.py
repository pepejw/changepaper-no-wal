#!/usr/bin/python3
import argparse
from glob import glob as ls
from os.path import expanduser as xpuser
from os import system as sh
from random import randint as rng
#cmdline args
parser = argparse.ArgumentParser(
        prog='changepaper',
        description='Change the wallpaper')


parser.add_argument('-L', action='store_true') #list
parser.add_argument('-d', default=xpuser('~/wallpapers')) #different directory
parser.add_argument('-f') #what file
parser.add_argument('-r', action='store_true') # random file
args = parser.parse_args()


def main():
  valid = False
  file_path = ""
  if args.L: #List wallpapers
    print("Available wallpapers are:")
    files = ls(args.d+'/*.png')
    for file in files:
      print(file)

  if args.f:
    file_path = args.d+'/'+args.f
    files = ls(args.d+'/*.png')
    for file in files:
      if file == file_path:
        valid = True

    if not valid:
      print("File not found")

  elif args.r:
    files = ls(args.d+'/*.png')
    file_path = f"{args.d}/{rng(0,len(files))}.png"
    valid = True

  if valid == True:
    sh("swww img "+file_path+" --transition-step 10 --transition-type any")
if __name__ == '__main__':
    main()
