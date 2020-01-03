import sys
sys.path.append("../RedditVk/")
from UploadingPics import UploadingPics as UP
import vk_api
import requests
import time
import datetime
import os
import calendar

class UploadingPicsVK(UP):
    def __init__(self):
        self.__vk = None
        self.__server = None
        self.__group_id = None

    def initVK(self, token):
        self.__vk = vk_api.VkApi(token=token).get_api()
    
    def initServer(self, group_id):
        self.__server = self.__vk.photos.getWallUploadServer(group_id=group_id)
        self.__group_id = group_id

    def upload(self, path, startDay, startMonth, startHour):
        day = startDay
        month = startMonth
        hour = startHour

        for file in os.listdir(path):

            files = {'file': open(path + "/" + file, 'rb')}
            
            r = requests.post(self.__server['upload_url'], files=files).json()

            s = self.__vk.photos.saveWallPhoto(group_id=self.__group_id, server=r['server'], 
                    photo=r['photo'], hash=r['hash'])

            if day == 31 and month == 12:
                day = startDay
                month = startMonth
                hour += 8
            
            date = str(day)+"."+str(month)+".2020 "+str(hour)+":00:00"
            
            unixtime = 0.0
            
            try:
                unixtime = time.mktime(datetime.datetime.strptime(date, "%d.%m.%Y %H:%M:%S").timetuple())
            except ValueError:
                day = 1
                month += 1
                date = str(day)+"."+str(month)+".2020 "+str(hour)+":00:00"
                unixtime = time.mktime(datetime.datetime.strptime(date, "%d.%m.%Y %H:%M:%S").timetuple())

            self.__vk.wall.post(owner_id=f"-{self.__group_id}", 
                    attachments=f"photo{s[0]['owner_id']}_{s[0]['id']}",
                        publish_date=unixtime)
            day += 1
