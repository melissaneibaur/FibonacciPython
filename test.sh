#!/usr/bin bash

python3 ./test.py

python3 socketClient.py 1000000 &
python3 socketClient.py 99 &
python3 socketClient.py 1111111 &
python3 socketClient.py 62 &
python3 socketClient.py 4

wait < <(jobs -p)
