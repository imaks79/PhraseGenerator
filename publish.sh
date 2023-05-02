#!/bin/bash
git status 
git add . 
read -p 'Введите содержание изменения: ' commit_desc 
git commit -m "$commit_desc"
git push origin main
