# 部署步骤

## 数据库
brew install mysql-server
brew install redis-server

## python数据库驱动
brew install libmysqlclient-dev
brew install python3-dev
pip install mysqlclient

## 创建数据库
CREATE DATABASE freebyte \
CHARACTER SET utf8\
COLLATE utf8_general_ci; 

## 安装redis

## 获取代码
ssh-keygen -t rsa -C "youremail@example.com"
git clone git@github.com:liaojianqi/freebyte.git

## 安装python库依赖
pip install -r requirements/production.txt

## 同步数据
python manage.py migrate

## 启动服务
python manage.py runserver