#!/usr/bin/env bash
# -*- coding: utf-8 -*-

nginx;
gunicorn -c gunicorn.conf.py;
