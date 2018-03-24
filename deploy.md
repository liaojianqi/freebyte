# 部署步骤

## 数据库
sudo apt-get -y install mysql-server
sudo apt-get -y install redis-server

## 数据库依赖
sudo apt-get install libmysqlclient-dev
sudo apt install python3-dev
pip install mysqlclient

# 创建数据库
CREATE DATABASE freebyte \
CHARACTER SET utf8\
COLLATE utf8_general_ci; 

## 获取代码
ssh-keygen -t rsa -C "youremail@example.com"
git clone git@github.com:liaojianqi/freebyte.git

## 安装python库依赖
pip install -r requirements/production.txt

## 同步数据
python manage.py migrate

## nginx
sudo apt install nginx

## 启动gunicorn和nginx