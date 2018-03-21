'''
Created on 2018年3月15日

@author: 50181
'''
from urllib import request


class HtmlDownloader(object):
    
    
    def download(self,url):
        if url is None:
            return None
          
          
        response = request.urlopen(url)
        
        if  response.getcode()!= 200:
            return None
        
        return response.read().decode("utf-8")
        
    



