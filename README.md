# kkh_chatbot
Kakao chatbot for HeXA


# About
This is a chatbot for the study and project management of the UNIST club HeXA.

6/30

The team leader can register for study/project attendance through the command below.  
/등록 [project name]  

Team members can attend the study/project using the command below.  
/출석 [project name] [name]  


# Installation
This project uses an unofficial Python library [Notion API](https://github.com/jamalex/notion-py).

### Library error & fix
#### 5/3
**Error**  
`requests.exceptions.HTTPError: Invalid input.`  

**Fix**  
Change client.py & store.py's limit to 100.  
Solved by [this](https://stackoverflow.com/questions/66513210/cant-get-page-title-from-notion-using-api).  

#### 6/30
**Error**  
page.children does not work.  
`asdf`  
**Fix**  
Delete line 198 in `block.py`.  
`#self._client.refresh_records(block=children_ids)`  
This is a way to use children, not a definite solution.  

### Install

1.install Python3

2.install notion library  
pip install notion

3.perform `Library error & fix`

### Configuration 

Set configs/configs.py - using sample_configs.py

# Kakao chatbot Setting
TBD  



# Development Environment
This bot is developed on python version 3.7.