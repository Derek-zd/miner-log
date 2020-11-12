# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os
import re
from datetime import date, timedelta
import configparser
import logging
import time

list_track=""

#初始化日志
logging.basicConfig(level= logging.INFO,format='%(asctime)-10s    %(levelname)-10s    %(name)-20s        %(message)-s')

conf= configparser.ConfigParser()
def readConf():
    logger = logging.getLogger("readConf")
    #获取当前文件的路径
    root_path = os.path.dirname(os.path.abspath(__file__))
    
    logger.info(root_path)
    if  root_path.find('\\') != -1: 
        conf.read(root_path + '\config\config.ini') 
        logger.info("readConfig:{}".format(root_path + '\config\config.ini'))
    else:
        conf.read(root_path + '/config/config.ini')
        logger.info("readConfig:{}".format(root_path + '/config/config.ini'))
    minerID = conf.get("miner", "minerID")
    logger.info("minerID:{}".format(minerID))
    return minerID




def miner_log():
    
    logger = logging.getLogger("miner_log")

    # 获取当前日期的前一天日期，并格式化输出
    yesterday = (date.today() + timedelta(days=-1)).strftime("%Y-%m-%d")
    logger.info(yesterday)
    # 获取前一天的日志到临时文件中
    val = os.system("sed -n /{}T00:00:00/,/{}T23:59:59/p ../miner.log >./miner-log.tmp ".format("2020-11-08", "2020-11-08"))
    #print("日志提取: {}".format(val))
    logger.info("日志提取：{}".format(val))


#sector track_time 单位转换，转换后单位是s
def sector_time(track_sectorTIME):
    logger = logging.getLogger('Calculate_time')

    if track_sectorTIME.find('µs') != -1:
        time = float(track_sectorTIME.split('µs')[0].strip())
        return time
    elif track_sectorTIME.find('ms') != -1:
        time = float(track_sectorTIME.split('ms')[0].strip())
        return time
    elif track_sectorTIME.find('h') != -1:
        time_h = float(track_sectorTIME.split('h')[0].strip())
        time_m = float(track_sectorTIME.split('h')[1].split('m')[0].strip())
        time_s = float(track_sectorTIME.split('m')[1].split('s')[0].strip())
        #logger.info('{}"h"{}"m"{}s'.format(time_h, time_m, time_s))
        time = time_h * 60 * 60 + time_m * 60 + time_s
        logger.info(time)
        return  time
    elif track_sectorTIME.find('m') != -1:
        time_m = float(track_sectorTIME.split('m')[0].strip())
        time_s = float(track_sectorTIME.split('m')[1].split('s')[0].strip())
        #logger.info('{}m{}s'.format(time_m, time_s))
        time = time_m * 60 + time_s
        logger.info(time)
        return time
    else:
        time = float(track_sectorTIME.split('s')[0].strip()) 
        #logger.info("{}".format(time))  
        return time



def read_log():
    logger = logging.getLogger("read_log")
    logger.info("11")
    
    with open("{}\miner-log.tmp".format(os.path.dirname(os.path.abspath(__file__))), 'r', encoding='utf-8') as log:
        lines = log.readlines()
        for line in lines:
            #logger.info(line)
            line1 = line.strip()
            if line1.find("track time") != -1:   
                track_sectorID = line1.split('{')[1].split('}')[0].split(' ')[1].strip()            
               # logger.info("{}".format(track_sectorID))
                track_sectorTASK = line1.split('}')[1].split('-')[1].split(' ')[0].strip()
                #logger.info("{}".format(track_sectorTASK))
                track_sectorTIME = line1.split('took:')[1].strip()
               # logger.info("{}".format(track_sectorTIME))
                logger.info("SectorID:{}  TASK:{}  took:{}".format(track_sectorID,track_sectorTASK,track_sectorTIME))
                logger.info("{}".format(sector_time(track_sectorTIME)))




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    readConf()
    miner_log()
    read_log()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
