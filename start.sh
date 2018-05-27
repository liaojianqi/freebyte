#!/usr/bin/env bash
nohup python manage.py runworker &
nohup python manage.py runworker &
nohup python manage.py runworker &
nohup python manage.py runworker &
nohup daphne freebyte.asgi:channel_layer &