#
# Example file for working with os.path module
#
import os
from os import path
import datetime
from datetime import date, time, timedelta
import time


def main():
  # Print the name of the OS
    print(os.name)

  # Check for item existence and type
    print("item is exists: " + str(path.exists("textfile.txt")))
    print("item is a file: " + str(path.isfile("textfile.txt")))
    print("item is a directory: " + str(path.isdorectory("textfile.txt")))
  # Work with file paths

  
  # Get the modification time

  
  # Calculate how long ago the item was modified


  
if __name__ == "__main__":
  main()