# -*- coding: utf-8 -*-
#--------------------------------------------------------
#  creado por quequeQ para PalcoTV
# (http://forum.rojadirecta.es/member.php?1370946-quequeQ)
# (http://xbmcspain.com/foro/miembro/quequino/)
# Version 0.8.1 (23.11.2018)(28.10.2015)
#--------------------------------------------------------
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# http://quequino.pythonanywhere.com/
# https://arenavision.herokuapp.com/
# http://arenacipq.appspot.com/
# https://stackoverflow.com/questions/41843266/microsoft-windows-python-3-6-pycrypto-installation-error
#
# set FLASK_ENV=development
# set FLASK_APP=main.py
# flask run #flask run --cert=adhoc
#
#heroku login
#heroku git:clone -a arenavision
#cd arenavision
#git config --global user.email "cipromario@gmail.com"
#git add .
#git commit -am "make it better"
#git push heroku master
#--------------------------------------------------------
#
#https://source.cloud.google.com/arenacipqq/arenacipqqrepo?authuser=1
# console.cloud.google.com/gcr/images/arenacipqq/EU/appengine (container registry)
# gcloud auth login
# gcloud init && git config --global credential.https://source.developers.google.com.helper gcloud.cmd
# git remote add google https://source.developers.google.com/p/arenacipqq/r/arenacipqqrepo
# git init
# git add . -A
# git commit -m ""
# gcloud app deploy
# git push --all google
# git push google master
#--------------------------------------------------------
#
__Author__ = 'quequino'
import requests,re,time,json,urllib,cfscrape,base64;
create_scraper = cfscrape.CloudflareScraper
try:import http.cookiejar as cookielibs;
except ImportError:from cookielib import CookieJar as cookielibs
try:
 import googleclouddebugger
 googleclouddebugger.enable()
except ImportError:pass
try:from urllib.parse import unquote;#python 3.x
except:pass;#python 2.x
global ref;global headers;global cookieJar;global cooks;global cookie;cookieJar=cookielibs.LWPCookieJar();global cipq;cooks='';cookie='';ref='https://linkotes.com/arenavision/';
ua='Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.0.11700 Safari/537.36';headers={'Referer':ref,'User-Agent':ua};
fanart='http://i.imgur.com/UTKznp5.png';thumb='i.imgur.com/5kfMn1T.png';cipqdeb='■'*35;cipqdeb='*'*35;cipq=__Author__;
html1='html1.html';html2='html2.html';
def atstp():return str(int(time.time())+19360000*1000)
#cipher=AES.new('cipq'*4,AES.MODE_ECB);
### HTTPS  !!!
#https://medium.com/tek-society/how-to-secure-your-python-flask-routes-with-basic-auth-in-5-minutes-6e3cea1448a4

from flask import Flask,request,render_template
from flask_httpauth import HTTPBasicAuth
auth = HTTPBasicAuth()
app = Flask(__name__)

@app.route('/')
 
def source():
 cabeza="[COLOR=blue][B]Programacion ArenaVision[/B][/COLOR]";q='leaf"><a href="([^"]+?)"[^>]*>(.+?)</a';cookie='';channels={};chans={};guia='';
 q='<tr.*?>(.*?)<\/tr';z='(\d{2}\/\d{2}\/\d{4})';p='<td.*?>(.*?)<\/td';link='';ndata={};cookies='';
 ''' OFFLINE MODE !!!
 try:
  f=open(html1,'r');data=f.read();f.close();data=re.findall(q,data.decode('utf-8','ignore'),re.DOTALL)[1:-1];guia=data[0][0];#print (data,guia,cipqdeb);
  for i,j in data[1:]:channels.update({j+' ':i});
 f=open(html2,'rb');data=f.read();f.close();ndata={};
 print(data,ndata,cipqdeb);
 except:pass
 '''
 d=create_scraper();b=d.get(ref,headers=headers);resp=b.text;heads=b.headers;cooks=b.cookies;data=[];chans={};iz=-1;
 try:zi=re.findall(z,resp);
 except:pass;
 try:
  data=re.findall(q,resp,re.DOTALL)#[1:-1];guia=data[0][0][1:];print (data,guia,cipqdeb);
 except:print('Incorect 1 page response!!!',cipqdeb);pass
 #print(guia,cipqdeb,channels,cipqdeb);#sys.exit();
 for i in data:
  #print i[0];#ziua
  events=re.findall(p,i,re.DOTALL);
  try:
    r='(\w{2,3}):.*?\#(.*?)\"';link=re.findall(r,events[3],re.DOTALL);links={};
    for w in link:links.update({w[0]:w[1]})
  except:pass
  #for j in events:
   #evenimente j
  try:chans.update({events[2]:{'hora':events[0],'sport':events[1],'link':links}});channels.update({zi[iz]:chans});
  except:iz+=1;chans={};pass
 #for i in channels:print(i,channels[i])
 
 table='''<!DOCTYPE html>
<html><head><title>CipQ Arena Flask Python Heroku</title><link rel="icon" type="image/png" href="static/fanav.ico" sizes="96x96">
<link href="static/style.css" rel='stylesheet' type='text/css'><script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js"></script>
<script>$(document).ready(function(){ $('.address').on('click',function(){var address=$(this).parent().find('.address');var html=$(this).parent().find('.address').html();var data=JSON.stringify({'page':encodeURIComponent($(this).parent().find('input[name=data]').val())});$.ajax({type:'POST',url:'arena2',beforeSend:function(){address.html('Loading...')},data:data,contentType:'application/json;charset=UTF-8',success:function(raspuns){if(raspuns.length>0) address.attr('href',raspuns);address.html(html);}})})});</script>
<script>function SwitchMenu(obj){if(document.getElementById){var el=document.getElementById(obj);var ar=document.getElementById("menutitle").getElementsByTagName("span");if(el.style.display!="block"){for(var i=0;i<ar.length;i++){if(ar[i].className=="submenu") ar[i].style.display="none"}el.style.display="block"}else{el.style.display="none"}}}</script>
<script>jQuery(document).ready(function($){$(".clickable-row").click(function() {window.location = $(this).data("href");});});</script>
</head>
<body>''';
 
 x=0;fecha='';
 #for i in channels:print(i)
 for i in channels:
  fecha='''<table class="tg"><colgroup><col style="width: 16%"><col style="width: 31%"><col style="width: 40%"></colgroup><tbody><tr id="menutitle"><td class="tg-11" rowspan="2"><p style="color:blue">'''+i+'''</p></td><td class="tg-31"></td><td class="tg-301"></td></tr><tr id="menutitle"><td class="tg-21" colspan="2"><img src="static/logo_av2015.png" style="display:block; width:100%; height:auto;"></img></td></tr></tbody></tbody></table>''';
  x+=1;lang='';link='';strx="'"+str(x)+"'";subm='';
  table+=fecha;
  for j in channels[i]:
   num='1' if x%2==0 else ''
   strx="'"+str(x)+"'";title=j.split('(');comp=title[1].split(')')[0];title=title[0];#CHILE-BRAZIL (FIFA WORLD CUP QUALIFIERS)
   tabl='''
	<table class="tg"><tbody><colgroup><col style="width: 16%"><col style="width: 31%"><col style="width: 40%"></colgroup>
	<tr id="menutitle" onclick="SwitchMenu('''+strx+''');">
    <td class="tg-1'''+num+'''" rowspan="2">'''+channels[i][j]['hora']+'''</td>
    <td class="tg-3'''+num+'''">'''+channels[i][j]['sport']+'''</td>
    <td class="tg-30'''+num+'''">'''+comp+'''</td>
	</tr>
	<tr id="menutitle" onclick="SwitchMenu('''+strx+''');">
    <td class="tg-2'''+num+'''" colspan="2">'''+title+'''</td>
	</tbody>
	</table>
	''';
   x+=1;submn='';submn1='';submn2='';
   for k in channels[i][j]['link']:
    submn+='''<tr><td class="tg-submenu1" colspan="2">'''+str(k)+'''</td><td class="tg-submenu2"><a class="address">AV'''+str(channels[i][j]['link'][k][2:])+'''<input type="hidden" name="data" value="'''+str(channels[i][j]['link'][k])+'''"></td></tr>''';
   table+=tabl+'''<table class="submenu" id='''+strx+''' style="display: none;"><tbody>'''+submn+'''</tbody></table>''';
 return table;#return json.dumps(chans);
 

@app.route('/arena2', methods=['GET','POST'])
def arena2():
 r='jQuery\.ajax\(\{method:"GET",url:"(.*?)",dataType:"json",data:\{format:"json",id:"(.*?)"\}';
 p='Clappr\.Player.*?\.atob\(\'?"?([^\'?"?]+)';resp='N/A';ref='https://linkotes.com/arenavision/';
 canal=urllib.parse.unquote(request.get_json()['page'])[2:];url=ref+'aj_canal.php';post={ 'id': canal, 'nocatxe': '0' };
 '''
 try:url=XOR.new(cipq).decrypt(base64.b64decode(unquote(requests.get_json()['page']))).decode('utf8');print(url);#python 2.x
 except:url=XOR.new(cipq).decrypt(base64.b64decode(urllib.unquote(requests.get_json()['page'])));print(url);pass;#python 3.x
 url1=base64.b64decode(urllib.unquote(requests.get_json()['page']))
 print('url1'+url1);
 url2=base64.b64encode(XOR.new(cipq).encrypt(url1))
 print('url2'+url2);
 url3=XOR.new(cipq).decrypt(base64.b64decode(urllib.unquote(url2)))
 print('url3'+url3);
 try:url=base64.b64decode(unquote(requests.get_json()['page'])).decode('utf8');print(url);#python 2.x
 except:url=base64.b64decode(urllib.unquote(requests.get_json()['page']));print(url);pass;#python 3.x
 '''
 try:
  d=create_scraper();b=d.post(url,data=post);resp=b.text;heads=b.headers;cooks=b.cookies;data=resp.encode('utf-8','ignore');resp=eval(resp)['ace'].replace('\\','');
  return resp;
 except:pass;
 #print(ace.replace('\\',''),cipqdeb)#acestream://906d233b75a11a880f08a47f2bcfbb6cada400ca
 try:#regex r
  #data=re.findall(r,resp,re.DOTALL);
  #m3u8='%s?format=json&id=%s'%(data[0][0],data[0][1]);#print heads,m3u8;
  #resp='acestream://'+data[0][1];#d=create_scraper();b=d.get(m3u8,headers=headers);resp=b.text;heads=b.headers;cooks=b.cookies;data=json.loads(resp.encode('utf-8','ignore'))['response'];
  #print data,heads,cookie,m3u8,cipqdeb;#print data,heads,m3u8;#sys.exit()
  return resp;
 except:pass;
 try:#regex p
  #data=re.findall(p,resp,re.DOTALL);resp=re.findall('id=([^\&]+)',base64.b64decode(data[0]).decode('utf-8'),re.DOTALL)[0];
  m3u8='http://127.0.0.1:6878/ace/manifest.m3u8?format=json&sid=0.6075956649146974&use_api_events=1&use_api_stop=1&use_timeshift=1&transcode_audio=1&transcode_mp3=0&id='+resp
  d=create_scraper();b=d.get(m3u8,headers=headers);resp=b.text;heads=b.headers;cooks=b.cookies;resp=json.loads(resp.encode('utf-8','ignore'))['response']['playback_url'];
  return resp;
 except:pass;
 #print(json.loads(resp[0].encode('utf-8','ignore'))['response']['playback_url'],resp.get_json()['response']['playback_url']);
def b64_error(b64_str):
 missing_padding=4-len(b64_str)%4
 if missing_padding: b64_str+=b'='*missing_padding;return b64_str
if __name__ == '__main__':app.debug=True;app.run(host = "0.0.0.0", port = 5000)
#source()
 #if not 'SOCCER'.upper() in data:print 'TRY TO CHANGE ARENAVISION SCHEDULE URL',cipqdeb;
#arena0({'title':'[COLOR=red]Arena[COLOR=yellow]Vision[/COLOR][/COLOR]','url':'http://es.arenavision.in/','thumbnail':'http://oi59.tinypic.com/n1ay50.jpg','fanart':'http://www.hdwallpapers.in/walls/birds_nest_stadium_beijing_china-HD.jpg','folder':True});