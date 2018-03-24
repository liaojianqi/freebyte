#!/usr/bin/env bash
exec nohup gunicorn --bind unix:/tmp/freebyte.sock freebyte.wsgi:application &
