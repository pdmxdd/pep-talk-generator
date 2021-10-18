#!/bin/bash

mail -s "Pep alert: $(date)" -a 'From:paul@pdmxdd' 'paul@paulmatthews.dev' <<< $(python3 main.py)