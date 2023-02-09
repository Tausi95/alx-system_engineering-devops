note: double spaces are used between "#!/bin/bash" and a command name to indicate that when writing the actual script in Vim/vi or emacs these are two seperate senteces each begining a new line.
this exercise had 19 questions all were attempted and for those where the scripts did not work you are allowed to go through them and edit. Please provide a fully explanation on has changed and why it is working.
1. TASK 0 <#!/bin/bash  pwd> is a builtin command that print the current path name.
2. TASK 1 <#!/bin/bash  ls> is a two line used to list or view files in a directory.
3. TASK 2 <#!/bin/bash  cd> is a 2 line script used to navigate back to the home directory in a terminal. 
4. TASK 3 <#!/bin/bash  ls -l> is a 2 line scripts for listing files in a long format.
5. TASK 4 <#!/bin/bash  ls -la> is used to list files in a long format together with hidden files starting with character (.).
6. TASK 5 <#!/bin/bash  ls -lna> this is a two line shell script listing files in a long format using numbers.
7. TASK 6 <#!/bin/bash  mkdir /tmp/my_first_directory> this script create a dir my_first_directory in the dir /tmp/.
8. TASK 7 <#!/bin/bash  mv /tmp/betty /tmp/my_first_directory> this script will move a file betty from /tmp/ to /tmp/my_first_directory/.
9. TASK 8 <#!/bin/bash  rm /tmp/my_first_directory/betty> this script if executed deletes the file betty in the path /tmp/my_first_directory_betty.
10. TASK 9 <#!/bin/bash  rm -r /tmp/my_first_directory> this script deletes the directory my_first_directory in the path name /tmp/my_first_directory.
11. TASK 10 <#!/bin/bash  cd -> this script if executed in terminal will change the working directory to the previous one.
12. TASK 11 <#!/bin/bash  ls -la . ../boot> this two line scripts displays all files (even ones with names beginning with a period character, which are normally hidden) in the current directory and the parent of the working directory and the /boot directory (in this order), in long format.
13. TASK 12 <#!/bin/bash  file> prints the type of the file named iamafile. The file iamafile will be in the /tmp directory when we will run your script.
14. TASK 13 <#!/bin/bash  ln -s /bin/ls  __ls__> Create a symbolic link to /bin/ls, named __ls__. The symbolic link should be created in the current working directory. 
15. TASK 14 <#!/bin/bash  cp -um*.html> this a two line script that copies all the HTML files from the current working directory to the parent of the working directory, but only copy files that did not exist in the parent of the working directory or were newer than the versions in the parent of the working directory.
16. TASK 15 <#!/bin/bash mv [[:upper:]]* /tmp/u > script that moves all files beginning with an uppercase letter to the directory /tmp/u.
17. TASK 16 <#!/bin/bash  rm *~> this is a two line script that deletes all files in the current working directory that end with the character ~.
18 TASK 17 <#!/bin/bash  mkdir -p welcome/to/school >script that creates the directories welcome/, welcome/to/ and welcome/to/school in the current directory.
19. TASK 18 <#!/bin/bash  ls -A | sort -t. -k1,1 | awk "BEGIN{OFS=","}END"> command that lists all the files and directories of the current directory, separated by commas (,).
20 TASK 19 <#!/bin/bashfile -m /path/to/school.mgc myfile.dat> this is command creating a magic file school.mgc that can be used with the command file to detect School data files. School data files always contain the string SCHOOL at offset 0.
