# -*- coding: utf-8 -*-

import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
import time,random,sys,json,codecs,threading,glob,re,requests,urllib
from gtts import gTTS
from bs4 import BeautifulSoup
import goslate
import time
import os


cl = LINETCR.LINE()
cl.login(token="Emea2zZWDTaiWK8V6ST9.MZrkjd9u6Oz3cBqGai+WIq.v68AtOIgGt2DvIsYrdZMmzka9CKX0xmSH0jRWX0WWL8=")
cl.loginResult()



print "login success"
reload(sys)
sys.setdefaultencoding('utf-8')

helpMessage ="""test"""


KAC=[cl]
mid = cl.getProfile().mid

Bots=[mid,"uc216d8664c4e1f43772c98b1b0b8956e","ubecd98a04cbf74a830b6c95b67bd6b74"]
admin=["uc216d8664c4e1f43772c98b1b0b8956e","ubecd98a04cbf74a830b6c95b67bd6b74"]
wait = {
    'contact':True,
    'autoJoin':True,
    'autoCancel':{"on":True,"members":50},
    'leaveRoom':True,
    'timeline':False,
    'autoAdd':True,
    'message':"戦神SelfBOT\n作者:http://line.me/ti/p/4-ZKcjagH0\n[Made In Taiwan]",
    "lang":"JP",
    "comment":"台湾戦神☆style",
    "commentOn":True,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":False,
    "cName":" ",
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "atjointicket":True,
    "Protectcancl":False,
    }

wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
    }
    
setTime = {}
setTime = wait2['setTime']
mulai = time.time()

def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1
    
def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    return '%02d Jam %02d Menit %02d Detik' % (hours, mins, secs)
    
def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)    
def yt(query):
    with requests.session() as s:
         isi = []
         if query == "":
             query = "S1B tanysyz"   
         s.headers['user-agent'] = 'Mozilla/5.0'
         url    = 'http://www.youtube.com/results'
         params = {'search_query': query}
         r    = s.get(url, params=params)
         soup = BeautifulSoup(r.content, 'html5lib')
         for a in soup.select('.yt-lockup-title > a[title]'):
            if '&list=' not in a['href']:
                if 'watch?v' in a['href']:
                    b = a['href'].replace('watch?v=', '')
                    isi += ['youtu.be' + b]
         return isi
def NOTIFIED_READ_MESSAGE(op):
    try:
        if op.param1 in wait2['readPoint']:
            Name = cl.getContact(op.param2).displayName
            if Name in wait2['readMember'][op.param1]:
                pass
            else:
                wait2['readMember'][op.param1] += "\n・" + Name
                wait2['ROM'][op.param1][op.param2] = "・" + Name
        else:
            pass
    except:
        pass

#---------------------------[AutoLike-nya]---------------------------#
def autolike():
     for zx in range(0,100):
        hasil = cl.activity(limit=100)
        if hasil['result']['posts'][zx]['postInfo']['liked'] == False:
          try:    
            cl.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
	    cl.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"台湾戦神☆style")
            print "Like"
          except:
            pass
        else:
            print "Already Liked"
     time.sleep(500)
thread2 = threading.Thread(target=autolike)
thread2.daemon = True
thread2.start()
#---------------------------[AutoLike-nya]---------------------------#















#-------------------

def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                cl.findAndAddContactsByMid(op.param1)
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    cl.sendText(op.param1,str(wait["message"]))



        if op.type == 13:
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.acceptGroupInvitation(op.param1)
			    try:
                                cl.sendText(op.param1,"人數未達50人,無法入群.")
		            except:
			        pass
                            cl.leaveGroup(op.param1)
                        else:
                                cl.acceptGroupInvitation(op.param1)
				try:
					c = Message(to=op.param1, from_=None, text=None, contentType=13)
                	        	c.contentMetadata={'mid':"u85a9b62af4ce6248cfe05324e474e226"}
					cl.sendText(op.param1,"戦神已讀功能機\n請打[/help]查看指令\n\nBOT作者:戦神\n\n戦神販賣所↓")
					cl.sendMessage(c)
				except:
					pass
                    else:
                        cl.acceptGroupInvitation(op.param1)
			cl.sendText(op.param1,"戦神已讀功能機\n請打[/help]查看指令\n\nBOT作者:戦神\n\n戦神販賣所↓")
			c = Message(to=op.param1, from_=None, text=None, contentType=13)
                	c.contentMetadata={'mid':"u85a9b62af4ce6248cfe05324e474e226"}
			cl.sendMessage(c)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)

#-------------------------------------------------------------------------------

                    
        if op.type == 22:
                cl.leaveRoom(op.param1)
        if op.type == 24:
                cl.leaveRoom(op.param1)


	if op.type == 26:
            msg = op.message
            try:
		if msg.contentType == 0:
		    try:
			if msg.to in wait2['readPoint']:
			    if msg.from_ in wait2["ROM"][msg.to]:
				del wait2["ROM"][msg.to][msg.from_]
			else:
			    pass
		    except:
		        pass
		else:
	    	    pass
	    except KeyboardInterrupt:
		sys.exit(0)
	    except Exception as error:
		print error
		print ("RECEIVE_MESSAGE")
		return

        if op.type == 26:
	    msg = op.message

            if msg.toType == 1:
                if wait["leaveRoom"] == True:
                    cl.leaveRoom(msg.to)
            if msg.contentType == 16:
                url = msg.contentMetadata("line://home/post?userMid="+mid+"&postId="+"new_post")
                cl.like(url[25:58], url[66:], likeType=1001)
        if op.type == 26:
            msg = op.message
            if msg.contentType == 13:
                    msg.contentType = 0
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
			if msg.contentMetadata["mid"] in wait["blacklist"]:
                             cl.sendText(msg.to,msg.contentMetadata["mid"])
                        else:
			     cl.sendText(msg.to,msg.contentMetadata["mid"])
            elif msg.contentType == 16:
                if wait["timeline"] == True:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = "" + msg.contentMetadata["postEndUrl"]
                    cl.sendText(msg.to,msg.text)
            elif msg.text is None:
                return
            elif msg.text in ["/help"]:
                    cl.sendText(msg.to,helpMessage)
		
            elif msg.text in ["/me","/Me"]:
		msg.contentType = 13
		X = msg.from_
                msg.contentMetadata = {"mid": X }
		cl.sendMessage(msg)
                cl.sendText(msg.to,msg.from_)
		
            elif msg.text in ["/author","/Author","/作者"]:
		msg.contentType = 13
                msg.contentMetadata = {"mid":"u85a9b62af4ce6248cfe05324e474e226"}
		cl.sendMessage(msg)
		cl.sendText(msg.to,"作者:戦神\nMade In Taiwan")
		
            elif msg.text in ["/mid","/Mid"]:
                cl.sendText(msg.to,msg.from_)
		
            elif msg.text in ["/Gid","/gid"]:
                cl.sendText(msg.to, msg.to)
		
            elif msg.text in ["/Ginfo","/ginfo"]:
                    ginfo = cl.getGroup(msg.to)
                    gurl = cl.reissueGroupTicket(msg.to)
                    try:
                        gCreator = ginfo.creator.displayName
                    except:
                        gCreator = ginfo.members[0].displayName
                    if wait["lang"] == "JP":
                        if ginfo.invitee is None:
                            sinvitee = "0"
                        else:
                            sinvitee = str(len(ginfo.invitee))
                        if ginfo.preventJoinByTicket == True:
                            u = "關閉"
                        else:
                            u = "開啟"
		    try:
                        cl.sendText(msg.to,"[戦神SelfBOT代行]\n[群組名稱]\n" + str(ginfo.name) + "\n[群組gid]\n" + msg.to + "\n[創立群組者]\n" + gCreator + "\n[群圖網址]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\n成員人數:" + str(len(ginfo.members)) + "人\n招待中人數:" + sinvitee + "人\n網址URL:" + u + "中\nline://ti/g/" + gurl)
                    except:
                        cl.sendText(msg.to,"[戦神SelfBOT代行]\n[群組名稱]\n" + str(ginfo.name) + "\n[群組gid]\n" + msg.to + "\n[創立群組者]\n" + gCreator + "\n[群圖網址]\nerror" + "\n成員人數:" + str(len(ginfo.members)) + "人\n招待中人數:" + sinvitee + "人\n群組網址:" + u + "中\nline://ti/g/" + gurl)
                    cl.sendText(msg)
		
            elif "/mid:" in msg.text:
                mmid = msg.text.replace("/mid:","")
                msg.contentType = 13
                msg.contentMetadata = {"mid":mmid}
                cl.sendMessage(msg)
		
            elif ("/Mid:" in msg.text):
                   key = eval(msg.contentMetadata["MENTION"])
                   key1 = key["MENTIONEES"][0]["M"]
                   mi = cl.getContact(key1)
                   cl.sendText(msg.to,"" +  key1)
		
            elif "/Mc:" in msg.text:
		key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                msg.contentType = 13
                msg.contentMetadata = {"mid":key1}
                cl.sendMessage(msg)
            elif "/mc:" in msg.text:
		key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                msg.contentType = 13
                msg.contentMetadata = {"mid":key1}
                cl.sendMessage(msg)
		

            elif "/User:" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = cl.getContact(key1)
                cu = cl.channel.getCover(key1)
                try:
                    cl.sendText(msg.to,"[戦神SelfBOT]\n\n[名字]\n" + contact.displayName + "\n[mid]\n" + contact.mid + "\n[個簽]\n" + contact.statusMessage + "\n[頭貼網址]\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[封面網址]\n" + str(cu))
                except:
                    cl.sendText(msg.to,"[戦神SelfBOT]\n\n[名字]\n" + contact.displayName + "\n[mid]\n" + contact.mid + "\n[個簽]\n" + contact.statusMessage + "\n[封面網址]\n" + str(cu))
		
            elif "/user:" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = cl.getContact(key1)
                cu = cl.channel.getCover(key1)
                try:
                    cl.sendText(msg.to,"[戦神SelfBOT]\n\n[名字]\n" + contact.displayName + "\n[mid]\n" + contact.mid + "\n[個簽]\n" + contact.statusMessage + "\n[頭貼網址]\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[封面網址]\n" + str(cu))
                except:
                    cl.sendText(msg.to,"[戦神SelfBOT]\n\n[名字]\n" + contact.displayName + "\n[mid]\n" + contact.mid + "\n[個簽]\n" + contact.statusMessage + "\n[封面網址]\n" + str(cu))
		
		
		
            elif msg.text in ["/gift","/Gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '3'}
                msg.text = None
                cl.sendMessage(msg)
		
            elif msg.text in ["/Time","/時刻","/time","/Now","/now"]:
                cl.sendText(msg.to, "" + datetime.datetime.today().strftime('%Y/%m/%d  %H:%M:%S.%f'))
		
            elif msg.text in ["/Cancel","/cancel"]:
                    group = cl.getGroup(msg.to)
                    if group.invitee is not None:
                        gInviMids = [contact.mid for contact in group.invitee]
                        cl.cancelGroupInvitation(msg.to, gInviMids)
                        cl.sendText(msg.to,"[戦神SelfBOT代行]\n取消了 "+ str(len(group.invitee)) + " 個邀請\n(´∀｀)♡")
                    else:
                            cl.sendText(msg.to,"邀請中沒人><")
				
            elif msg.text in ["/url","/Url"]:
                    g = cl.getGroup(msg.to)
                    gurl = cl.reissueGroupTicket(msg.to)
                    cl.sendText(msg.to,"line://ti/g/" + gurl)
		


         #-------------Fungsi Change Clock Finish-----------------#
            elif "Gift @" in msg.text:
                _name = msg.text.replace("Gift @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                    	msg.contentType = 9
                        msg.contentMetadata={'PRDID': '89131c1a-e549-4bd5-9e60-e24de0d2e252',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '10'}
                        msg.text = None
                        cl.sendMessage(msg,g)

#--------------------#

            elif msg.text in ["/Groupcreator","/群長","/Gc","/gc","/groupcreator","群長"]:
             if msg.from_ in admin + staff + staff2 + staff3 + staff4 + staff5 + staff6:
              if msg.toType == 2:
		 source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;/!&%$#'
		 name = "".join([random.choice(source_str) for x in xrange(9)])
                 ginfo = cl.getGroup(msg.to)
                 try:
                        gCreator = ginfo.creator.displayName
                 except:
                        gCreator = ginfo.members[0].displayName
		 
		 msg.contentType = 13
		 try:
                        gCreator1 = ginfo.creator.mid
                 except:
                        gCreator1 = ginfo.members[0].mid
		 msg.contentMetadata={'mid':gCreator1}
		 ki.sendMessage(msg)
		 ki.sendText(msg.to,"[群長]\n->" + gCreator + "\n\n" + datetime.datetime.today().strftime('%H:%M:%S') + " [" + name)
              else:
		pass


            elif "#mc:" in msg.text:
              if msg.from_ in admin + staff:
		key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                msg.contentType = 13
                msg.contentMetadata = {"mid":key1}
                ki.sendMessage(msg)
#-------------------#

	    elif "/head:" in msg.text:
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                        try:
                            contact = cl.getContact(key1)
                            path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
			    cl.sendImageWithURL(msg.to, path)
                        except:
                            pass


	    elif "/home:" in msg.text:
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                        try:
                            contact = cl.getContact(key1)
                            cu = cl.channel.getCover(key1)
                            path = str(cu)
                            cl.sendImageWithURL(msg.to, path)
                        except:
                            pass
		

	    elif "/group" in msg.text:
                   group = cl.getGroup(msg.to)
                   path =("http://dl.profile.line-cdn.net/" + group.pictureStatus)
                   cl.sendImageWithURL(msg.to, path)

#--------------------------------------------------------            
#--------------------------------------------------------
#--------------------------------------------------------
            elif '/instagram:' in msg.text.lower():
                try:
                    instagram = msg.text.lower().replace(".instagram:","")
                    html = requests.get('https://www.instagram.com/' + instagram + '/?')
                    soup = BeautifulSoup(html.text, 'html5lib')
                    data = soup.find_all('meta', attrs={'property':'og:description'})
                    text = data[0].get('content').split()
                    data1 = soup.find_all('meta', attrs={'property':'og:image'})
                    text1 = data1[0].get('content').split()
                    user = "名字: " + text[-2] + "\n"
                    user1 = "用戶名字: " + text[-1] + "\n"
                    followers = "粉絲: " + text[0] + "\n"
                    following = "追蹤數: " + text[2] + "\n"
                    post = "發文數: " + text[4] + "\n"
                    link = "網址: " + "https://www.instagram.com/" + instagram
                    detail = "========INSTAGRAM 用戶詳情========\n"
                    details = ""
                    cl.sendText(msg.to, detail + user + user1 + followers + following + post + link + details)
                    cl.sendImageWithURL(msg.to, text1[0])
                except Exception as njer:
                	cl.sendText(msg.to, str(njer))
			
            elif "/ig:" in msg.text.lower():
                arg = msg.text.split(' ');
                nk0 = msg.text.replace("/ig:","")
                nk1 = nk0.rstrip('  ')
                if len(arg) > 1:
                    proc = subprocess.Popen('curl -s https://www.instagram.com/'+nk1+'/?__a=1',shell=True, stdout=subprocess.PIPE)
                    x = proc.communicate()[0]
                    parsed_json = json.loads(x)
                    if(len(x) > 10):
                        username = (parsed_json['user']['username'])
                        fullname = (parsed_json['user']['full_name'])
                        followers = (parsed_json['user']['followed_by']['count'])
                        following = (parsed_json['user']['follows']['count'])
                        media = (parsed_json['user']['media']['count'])
                        bio = (parsed_json['user']['biography'])
                        url = (parsed_json['user']['external_url'])
                        cl.sendText(msg.to,"名字: "+username+"\n用戶名字: "+fullname+"\n粉絲: "+str(followers)+"\n追蹤數: "+str(following))
                        print '[Command] Instagram'
                    else:
                        cl.sendText(msg.to,"找不到...")
                else:
                    pass
                	
#----------------------------------------------------------
#-----------------------------------------------

            elif msg.text.lower() == '.reboot':
                if msg.from_ in admin:
                    try:
                        cl.sendText(msg.to,"Restarting...")
                        restart_program()
                    except:
                        cl.sendText(msg.to,"Please wait")
                        restart_program()
                        pass
	    elif "/say:" in msg.text:
                 psn = msg.text.replace("/say:","")
                 tts = gTTS(psn, lang='id', slow=False)
                 tts.save('tts.mp3')
                 cl.sendAudio(msg.to, 'tts.mp3')
            elif "/Say:" in msg.text:
                say = msg.text.replace("/Say:","")
                lang = 'id'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")
#-----------------------------------------------

	    elif "/歌詞:" in msg.text.lower():
                songname = msg.text.replace("/歌詞:","")
                params = {"songname":songname}
                r = requests.get('https://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                data = r.text
                data = json.loads(data)
                for song in data:
                    cl.sendText(msg.to,song[5])

            elif "/音樂:" in msg.text.lower():
                songname = msg.text.replace("/音樂:","")
                params = {"songname":songname}
                r = requests.get('https://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                data = r.text
                data = json.loads(data)
                for song in data:
                    cl.sendText(msg.to,"TEST1: " + song[0] + "\nTEST2: " + song[1])
                    cl.sendAudioWithURL(msg.to,song[3])

            elif "/youtube:" in msg.text:
                query = msg.text.replace("/youtube:","")
                with requests.session() as s:
                    s.headers['user-agent'] = 'Mozilla/5.0'
                    url = 'http://www.youtube.com/results'
                    params = {'search_query': query}
                    r = s.get(url, params=params)
                    soup = BeautifulSoup(r.content, 'html5lib')
                    hasil = ""
                    for a in soup.select('.yt-lockup-title > a[title]'):
                        if '&list=' not in a['href']:
                            hasil += ''.join((a['title'],'\nhttp://www.youtube.com' + a['href'],'\n\n'))
                    cl.sendText(msg.to,hasil)

#-------------------------------------------------------
	    elif "Gbc:" in msg.text:
	      if msg.from_ in admin:
		bctxt = msg.text.replace("Gbc:", "")
    		n = cl.getGroupIdsJoined()
    	        for manusia in n:
	            cl.sendText(manusia, (bctxt))

	    elif "Cbc:" in msg.text:
	      if msg.from_ in admin:
    		bctxt = msg.text.replace("Cbc:", "")
    		t = cl.getAllContactIds()
    		for manusia in t:
         	    cl.sendText(manusia, (bctxt))
#--------------------------------- TRANSLATE --------------------------------
	    elif "/t-en:" in msg.text:
                txt = msg.text.replace("/t-en:","")
                try:
                    gs = goslate.Goslate()
                    trs = gs.translate(txt,'en')
                    cl.sendText(msg.to,trs)
                except:
                    cl.sendText(msg.to,'Error.')
		
	    elif "/t-zh:" in msg.text:
                txt = msg.text.replace("/t-zh:","")
                try:
                    gs = goslate.Goslate()
                    trs = gs.translate(txt,'zh')
                    cl.sendText(msg.to,trs)
                except:
                    cl.sendText(msg.to,'Error.')

            elif "/t-id:" in msg.text:
                txt = msg.text.replace("/t-id:","")
                try:
                    gs = goslate.Goslate()
                    trs = gs.translate(txt,'id')
                    cl.sendText(msg.to,trs)
                except:
                    cl.sendText(msg.to,'Error.')


#----------------------



	#-------------------------------#



         #-------------Fungsi Jam Update Start---------------------#            

         #-------------Fungsi Jam Update Finish-------------------#
	    elif msg.text in ["/set"]:
		 if msg.toType == 2:
		    cl.sendText(msg.to, "已讀點設置完成")
		    try:
			del wait2['readPoint'][msg.to]
			del wait2['readMember'][msg.to]
		    except:
			pass
 		    wait2['readPoint'][msg.to] = msg.id
 		    wait2['readMember'][msg.to] = ""
 		    wait2['setTime'][msg.to] = datetime.today().strftime('%Y/%m/%d %H:%M:%S.%f')
 		    wait2['ROM'][msg.to] = {}


	    elif msg.text in ["/tes"]:
 		 if msg.toType == 2:
 		    print "\nSider check aktif..."
  		    if msg.to in wait2['readPoint']:
 			if wait2["ROM"][msg.to].items() == []:
 			    chiya = ""
 			else:
			    chiya = ""
			    for rom in wait2["ROM"][msg.to].items():
 				print rom
				chiya += rom[1] + "\n"
 			cl.sendText(msg.to, "已讀者:\n%s\n\n\n已讀點設置時間:\n[%s]" % (wait2['readMember'][msg.to],setTime[msg.to]))
		    else:
			cl.sendText(msg.to, "請先打[/set]設置已讀點")



#-----------------------------------------------





	if op.type == 55:
	    try:
		if op.param1 in wait2['readPoint']:
		    Name = cl.getContact(op.param2).displayName
		    if Name in wait2['readMember'][op.param1]:
			pass
		    else:
			wait2['readMember'][op.param1] += "\n・ " + Name + datetime.today().strftime(' [%d - %H:%M:%S]')
			wait2['ROM'][op.param1][op.param2] = "・ " + Name
			wait2['setTime'][msg.to] = datetime.today().strftime('%Y/%m/%d %H:%M:%S.%f')
		else:
		    pass
	    except:
		pass

        if op.type == 59:
            print op


    except Exception as error:
        print error



def nameUpdate():
    while True:
        try:
                profile = cl.getProfile()
                profile.displayName = "戦神_freebot"
                cl.updateProfile(profile)
		profile = cl.getProfile()
		fid =  cl.getAllContactIds()
		profile.statusMessage = "台湾戦神☆style\nFriend: " + str(len(fid)) + "\n\nMade in Taiwan"
		cl.updateProfile(profile)
                time.sleep(180)
        except:
            pass
thread1 = threading.Thread(target=nameUpdate)
thread1.daemon = True
thread1.start()


while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)
