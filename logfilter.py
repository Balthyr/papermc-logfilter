#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import gzip
import re
from os import listdir

player_list = []
for file_name in listdir('/var/lib/papermc/server/logs/'):
    if file_name.endswith('.log.gz'):
        with gzip.open(file_name, 'rb') as stream:
            for line in stream:
                match_player = re.search(r'^.*\:\s(.*)\[\/(.*):[0-9]{2,}\]\slogged\sin', str(line))
                if match_player is not None:
                    player_list.append({"playerName": match_player.group(1), "ipAddress": match_player.group(2)})
        stream.close()

pre_filter = {(v['ipAddress']): v for v in player_list}.values()

for k in pre_filter:
    print(f'{k}')

# for entry in player_list:
#    for player_name, ip_address in entry.items():
#        print(f'{player_name} --> {ip_address}')
