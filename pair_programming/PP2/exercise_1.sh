#!/bin/bash

# prompt user to specify file
echo Please enter a file to upload
read -r -p 'File: ' filevar

# git add file
git add $filevar

# print git status
git status

# ask user if they wish to continue
echo Do you wish to continue?
read -r -p 'Y/N? ' YNvar1

# if Y, prompt user to enter commit message and git commit -m
if [[ $YNvar1 = 'Y' ]]
then
    read -r -p 'Enter commit message: ' commitvar
    git commit -m "$commitvar"
# if N, exit
elif [[ $YNvar1 = 'N' ]]
then
    exit 1
# if neither Y nor N, print message and exit
else
    echo Neither Y nor N, please try again
    exit 1
fi

# print git status
git status

# ask user if they wish to continue
echo Do you wish to continue?
read -r -p 'Y/N? ' YNvar2

# if Y, git push
if [[ $YNvar2 = 'Y' ]]
then
    git push
# if N, exit
elif [[ $YNvar2 = 'N' ]]
then
    exit 1
# if neither Y nor N, print message and exit
else
    echo Neither Y nor N, please try again
    exit 1
fi