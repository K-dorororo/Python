import os
import sys
import urllib.request
client_id = "AjbGZV3FCHl3qUjClpjV"
client_secret = "DZnl0hD_bV"
encText = urllib.parse.quote("올림픽")
url = "https://openapi.naver.com/v1/search/blog?query=" + encText # json 결과

requst = urllib.request.Request(url)
requst.add_header("X-Naver-Client-Id", client_id)
requst.add_header("X-Naver.Client-Secret", client_secret)
response = urllib.request.urlopen(requst)
rescode = response.getcode()
if(rescode == 200) :
  response_body = response.read()
  print(response_body.decode('utf-8'))
else :
  print("Error Code : " + rescode)