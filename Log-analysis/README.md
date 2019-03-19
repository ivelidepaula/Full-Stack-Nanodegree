# Logs Analysis

##  Project Overview

This is the first project for Udacity's Full Stack Nanodegree program. A live database with newspaper articles and over a million rows was provided and the goal of this project was to create an internal reporting tool that will use information from the database to discover what kind of articles the site's readers like. This program doesn't take any input and it runs from the command line.

## Requirements
You need to download the following items:
 - Python 3  
 - Vagrant   
 - Virtual Box  
 - PostgreSQL  
 - The [database](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) file

## How to execute
- Install Virtual Box and Vagrant
- Download and unzip the database file
- Use a Unix-style terminal. If you are a Windows user, Git Bash is recommended.

### Launching the virtual machine:
- Launch the virtual machine inside the downloaded repository:
`$ vagrant up`  
- Log into  it:
`$ vagrant ssh`  
- Change directory to /vagrant and look around with `ls`  

### Launch the database:
- Use the following command:
`psql -d news -f newsdata.sql`   

### Running the program:
- Run the script
`python3 data.py`
