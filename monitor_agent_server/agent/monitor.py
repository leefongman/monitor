"""
需求：
    收集服务器的CPU、内存、硬盘使用状况等数据
    定时收集被控服务器的信息，以json格式发送给远程服务器
    支持远程服务器通过主动调用的方式获取被控服务器的信息
    记录每一次信息的收集和发送事件
"""

import json
from subprocess import getstatusoutput

import requests


def run_for_text(cmd):
    st, text = getstatusoutput(cmd)
    if st == 0:
        return text
    else:
        raise OSError('command failed')


def collect():
    """Collect system state info"""
    cpu_text = run_for_text('uptime')
    cpu_loads = cpu_text.split()[-3:]
    cpu_loads = [float(x.strip(',')) for x in cpu_loads]
    cpu_info_fields = ['1min', '5min', '15min']
    cpu_info = dict(zip(cpu_info_fields, cpu_loads))

    ram_text = run_for_text('free -b')
    ram_usage = ram_text.splitlines()[1].split()[1:]
    ram_usage = [int(x) for x in ram_usage]
    ram_info_fields = ['total', 'used', 'free', 'shared', 'buffers', 'cached']
    ram_info = dict(zip(ram_info_fields, ram_usage))

    hd_text = run_for_text('df -B1 /')
    hd_usage = hd_text.splitlines()[-1].split()
    hd_usage[1:4] = [int(x) for x in hd_usage[1:4]]
    hd_info_fields = ['dev', 'total', 'used', 'available', 'percent', 'mpoint']
    hd_info = dict(zip(hd_info_fields, hd_usage))

    return {'cpu': cpu_info, 'ram': ram_info, 'hd': hd_info}


def serialize(data):
    return json.dumps(data)


def send(url, text):
    r = requests.post(url, data={'data': text})
    if r.status_code == 200:
        print('sent')
        log('sent state to %s' % url)
    else:
        print('failed to sent')


def log(msg):
    import logging
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    hdlr = logging.FileHandler('monitor.log')
    hdlr.setFormatter(formatter)
    logger = logging.getLogger('myapp')
    logger.addHandler(hdlr)
    logger.setLevel(logging.INFO)
    logger.info(msg)


if __name__ == '__main__':
    url = 'http://localhost:8000/upload/'
    text = collect()
    text = serialize(text)
    send(url, text)
