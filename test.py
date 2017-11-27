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
cl.login(token="EnVFVST0YE4ULQeViJs3.2XannlnZppIccyjdoNFtaW.soaW4CPYf1dRxNSRQHncCbJd6Olm+XUJJx5/xkpvCtc=")
cl.loginResult()



print "login success"
reload(sys)
sys.setdefaultencoding('utf-8')

helpMessage ="""戦神FreeBOT

[/help]→查看指令
[/author]→作者顯示
[/set]→抓已讀者
[/read]→查看已讀名單
[/me]→顯示自己友資
[/mid]→顯示自己mid
[/gid]→顯示群組
[/ginfo]→顯示群組詳情
[/gc]→顯示創群者
[/url]→取得群組網址
[/cancel]→取消所有邀請
[/mid:]→顯示mid的友資
[/Mid:@]→顯示被標註者的mid
[/mc:@]→顯示被標註者的友資
[/user:@]→查看標註者詳情
[/gift]→發送禮物
[/time]→現在時間
[/bye]→退出群組

注意:此機器僅能邀入50人以上之群組

作者:戦神
https://line.me/R/ti/p/%40cld3625n"""


KAC=[cl]
mid = cl.getProfile().mid

Bots=[mid,"uc216d8664c4e1f43772c98b1b0b8956e","ubecd98a04cbf74a830b6c95b67bd6b74"]
admin=["uc216d8664c4e1f43772c98b1b0b8956e","ubecd98a04cbf74a830b6c95b67bd6b74","udb100d34b3733cf8820982433a77d303","uddf9714006a1010bb6551fc107f52390"]
wait = {
    'contact':True,
    'autoJoin':True,
    'autoCancel':{"on":True,"members":50},
    'leaveRoom':True,
    'timeline':True,
    'autoAdd':True,
    'message':"台湾戦神BOT\n作者:https://line.me/R/ti/p/%40cld3625n\n[Made In Taiwan]",
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
    "Protectcancl":True,
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
                    cl.sendText(op.param1,str(wait["message"]) + "\n\n[" + datetime.today().strftime('%Y/%m/%d  %H:%M:%S.%f') + "]")



        if op.type == 13:
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.acceptGroupInvitation(op.param1)
			    try:
				a1, a2, a3, a4, a5, a6, a7, b1, b2, b3, b4, b5 = "(*｀＾´)=3", "(`皿´)", "(o｀з’*)", "ヽ(｀Д´)ﾉ", "Σ(´д｀;)","(*'A^q)", "(*´>д<)", "(>_<)", "σ(oдolll)", "( #｀Д´)", "(｀А´)", "(#ﾟДﾟ)"
                		omikujilist = [a1,a2,a3,a4,a5,a6,a7,b1,b2,b3,b4,b5]
                                cl.sendText(op.param1,"人數未達50人 " + random.choice(omikujilist) + "\n\nBOT作者:戦神\n戦神販賣所↓")
				c = Message(to=op.param1, from_=None, text=None, contentType=13)
                	        c.contentMetadata={'mid':"u85a9b62af4ce6248cfe05324e474e226"}
				cl.sendMessage(c)
		            except:
			        pass
                            cl.leaveGroup(op.param1)
                        else:
                                cl.acceptGroupInvitation(op.param1)
				try:
					a1, a2, a3, a4, a5, a6, a7, b1, b2, b3, b4, b5 = "ヾ(*´∀｀*)ﾉ", "σ(o'ω'o)", "p(^-^q)", "ψ(｀∇´)ψ", "(#ﾟДﾟ)","(´▽｀)", "p(^-^q)", "ヾ(*´∀｀*)ﾉ", "σ(o'ω'o)", "p(^-^q)", "ψ(｀∇´)ψ", "(´▽｀)"
                			omikujilist = [a1,a2,a3,a4,a5,a6,a7,b1,b2,b3,b4,b5]
					c = Message(to=op.param1, from_=None, text=None, contentType=13)
                	        	c.contentMetadata={'mid':"u85a9b62af4ce6248cfe05324e474e226"}
					cl.sendText(op.param1,"戦神功能機 " + random.choice(omikujilist) + "\n請打[/help]查看指令\n\nBOT作者:戦神\n戦神販賣所↓")
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
                             cl.sendText(msg.to,msg.contentMetadata["mid"] + "\n\n[" + datetime.today().strftime('%Y/%m/%d  %H:%M:%S.%f') + "]")
                        else:
			     cl.sendText(msg.to,msg.contentMetadata["mid"] + "\n\n[" + datetime.today().strftime('%Y/%m/%d  %H:%M:%S.%f') + "]")
            elif msg.contentType == 16:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = msg.contentMetadata["postEndUrl"]
                    cl.sendText(msg.to,msg.text + "\n\n[" + datetime.today().strftime('%Y/%m/%d  %H:%M:%S.%f') + "]")
		
            elif msg.text is None:
                return
            elif msg.text in ["/help","/Help"]:
                    cl.sendText(msg.to,helpMessage + "\n\n[" + datetime.today().strftime('%Y/%m/%d  %H:%M:%S.%f') + "]")
		
            elif msg.text in ["/me","/Me"]:
		msg.contentType = 13
		X = msg.from_
                msg.contentMetadata = {"mid": X }
		cl.sendMessage(msg)
                cl.sendText(msg.to,msg.from_ + "\n\n[" + datetime.today().strftime('%Y/%m/%d  %H:%M:%S.%f') + "]")
		
            elif msg.text in ["/author","/Author","/作者"]:
		msg.contentType = 13
                msg.contentMetadata = {"mid":"u85a9b62af4ce6248cfe05324e474e226"}
		cl.sendMessage(msg)
		cl.sendText(msg.to,"作者:戦神 Made In Taiwan" + "\n\n[" + datetime.today().strftime('%Y/%m/%d  %H:%M:%S.%f') + "]")
		
            elif msg.text in ["/mid","/Mid"]:
                cl.sendText(msg.to,msg.from_ + "\n\n[" + datetime.today().strftime('%Y/%m/%d  %H:%M:%S.%f') + "]")
		
            elif msg.text in ["/Gid","/gid"]:
                cl.sendText(msg.to, msg.to + "\n\n[" + datetime.today().strftime('%Y/%m/%d  %H:%M:%S.%f') + "]")
		
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
                        cl.sendText(msg.to,"[群組名稱]\n" + str(ginfo.name) + "\n[群組gid]\n" + msg.to + "\n[創立群組者]\n" + gCreator + "\n[群圖網址]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\n成員人數:" + str(len(ginfo.members)) + "人\n招待中人數:" + sinvitee + "人\n網址URL:" + u + "中\nline://ti/g/" + gurl + "\n\n[" + datetime.today().strftime('%Y/%m/%d  %H:%M:%S.%f') + "]")
                    except:
                        cl.sendText(msg.to,"[群組名稱]\n" + str(ginfo.name) + "\n[群組gid]\n" + msg.to + "\n[創立群組者]\n" + gCreator + "\n[群圖網址]\nerror" + "\n成員人數:" + str(len(ginfo.members)) + "人\n招待中人數:" + sinvitee + "人\n群組網址:" + u + "中\nline://ti/g/" + gurl + "\n\n[" + datetime.today().strftime('%Y/%m/%d  %H:%M:%S.%f') + "]")
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
                   cl.sendText(msg.to,"" +  key1 + "\n\n[" + datetime.today().strftime('%Y/%m/%d  %H:%M:%S.%f') + "]")
		
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
                    cl.sendText(msg.to,"[名字]\n" + contact.displayName + "\n[mid]\n" + contact.mid + "\n[個簽]\n" + contact.statusMessage + "\n[頭貼網址]\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[封面網址]\n" + str(cu) + "\n\n[" + datetime.today().strftime('%Y/%m/%d  %H:%M:%S.%f') + "]")
                except:
                    cl.sendText(msg.to,"[名字]\n" + contact.displayName + "\n[mid]\n" + contact.mid + "\n[個簽]\n" + contact.statusMessage + "\n[封面網址]\n" + str(cu) + "\n\n[" + datetime.today().strftime('%Y/%m/%d  %H:%M:%S.%f') + "]")
		
            elif "/user:" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = cl.getContact(key1)
                cu = cl.channel.getCover(key1)
                try:
                    cl.sendText(msg.to,"[名字]\n" + contact.displayName + "\n[mid]\n" + contact.mid + "\n[個簽]\n" + contact.statusMessage + "\n[頭貼網址]\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[封面網址]\n" + str(cu) + "\n\n[" + datetime.today().strftime('%Y/%m/%d  %H:%M:%S.%f') + "]")
                except:
                    cl.sendText(msg.to,"[名字]\n" + contact.displayName + "\n[mid]\n" + contact.mid + "\n[個簽]\n" + contact.statusMessage + "\n[封面網址]\n" + str(cu) + "\n\n[" + datetime.today().strftime('%Y/%m/%d  %H:%M:%S.%f') + "]")
		
		
		
            elif msg.text in ["/gift","/Gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '3'}
                msg.text = None
                cl.sendMessage(msg)
		
            elif msg.text in ["/Time","/時刻","/time","/Now","/now"]:
                cl.sendText(msg.to, "" + datetime.today().strftime('%Y/%m/%d  %H:%M:%S.%f'))
		
            elif msg.text in ["/Cancel","/cancel"]:
                    group = cl.getGroup(msg.to)
                    if group.invitee is not None:
                        gInviMids = [contact.mid for contact in group.invitee]
                        cl.cancelGroupInvitation(msg.to, gInviMids)
                        cl.sendText(msg.to,"戦神取消了 "+ str(len(group.invitee)) + " 個邀請\n(´∀｀)♡" + "\n\n[" + datetime.today().strftime('%Y/%m/%d  %H:%M:%S.%f') + "]")
                    else:
                            cl.sendText(msg.to,"邀請中沒人><" + "\n\n[" + datetime.today().strftime('%Y/%m/%d  %H:%M:%S.%f') + "]")
				
            elif msg.text in ["/url","/Url"]:
                    g = cl.getGroup(msg.to)
                    gurl = cl.reissueGroupTicket(msg.to)
                    cl.sendText(msg.to,"line://ti/g/" + gurl + "\n\n[" + datetime.today().strftime('%Y/%m/%d  %H:%M:%S.%f') + "]")
		
	    elif "Gbc:" in msg.text:
	      if msg.from_ in admin:
		bctxt = msg.text.replace("Gbc:", "")
    		n = cl.getGroupIdsJoined()
    	        for manusia in n:
	            cl.sendText(manusia, (bctxt) + "\n\n[" + datetime.today().strftime('%Y/%m/%d  %H:%M:%S.%f') + "]")
		
            elif msg.text in ["/bye","/Bye"]:
			cl.sendText(msg.to,"作者:戦神 Made In Taiwan\nhttps://line.me/R/ti/p/%40cld3625n")
			cl.leaveGroup(msg.to)
		
            elif "名字:" in msg.text:
              if msg.from_ in admin:
                string = msg.text.replace("名字:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = cl.getProfile()
                    profile.displayName = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"成功:" + string + "" + "\n\n[" + datetime.today().strftime('%Y/%m/%d  %H:%M:%S.%f') + "]")
		else:
			pass
		
            elif "BGbyeall" in msg.text:
              if msg.from_ in admin:
                gid = cl.getGroupIdsJoined()
                for i in gid:
		    cl.sendText(i,"一鍵退群功能啟用,若需要此機器,請重新邀請\n作者:戦神\nhttps://line.me/R/ti/p/%40cld3625n" + "\n\n[" + datetime.today().strftime('%Y/%m/%d  %H:%M:%S.%f') + "]")
                    cl.leaveGroup(i)
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"已退出所有群組" + "\n\n[" + datetime.today().strftime('%Y/%m/%d  %H:%M:%S.%f') + "]")
                else:
                    cl.sendText(msg.to,"已退出所有群組" + "\n\n[" + datetime.today().strftime('%Y/%m/%d  %H:%M:%S.%f') + "]")

         #-------------Fungsi Change Clock Finish-----------------#


#--------------------#

            elif msg.text in ["/Groupcreator","/群長","/Gc","/gc","/groupcreator","群長"]:
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
		 cl.sendMessage(msg)
		 cl.sendText(msg.to,"[群長]\n->" + gCreator + "\n\n[" + datetime.today().strftime('%Y/%m/%d  %H:%M:%S.%f') + "]")
              else:
		pass



#-------------------#


#--------------------------------------------------------            
#--------------------------------------------------------
#--------------------------------------------------------

                	
#----------------------------------------------------------
#-----------------------------------------------


         #-------------Fungsi Jam Update Finish-------------------#
            elif msg.text in ["/set","/Set"]:
		 if msg.toType == 2:
		    cl.sendText(msg.to, "已讀點設置完成" + "\n\n[" + datetime.today().strftime('%Y/%m/%d  %H:%M:%S.%f') + "]")
		    try:
			del wait2['readPoint'][msg.to]
			del wait2['readMember'][msg.to]
		    except:
			pass
 		    wait2['readPoint'][msg.to] = msg.id
 		    wait2['readMember'][msg.to] = ""
 		    wait2['setTime'][msg.to] = datetime.today().strftime('%Y/%m/%d %H:%M:%S.%f')
 		    wait2['ROM'][msg.to] = {}


            elif msg.text in ["/read","/Read"]:
 		 if msg.toType == 2:
  		    if msg.to in wait2['readPoint']:
 			if wait2["ROM"][msg.to].items() == []:
 			    chiya = ""
 			else:
			    chiya = ""
			    for rom in wait2["ROM"][msg.to].items():
				chiya += rom[1] + "\n"
 			cl.sendText(msg.to, "已讀者:\n%s\n\n\n已讀點設置時間:\n[%s]" % (wait2['readMember'][msg.to],setTime[msg.to]))
		    else:
			cl.sendText(msg.to, "請先打[/set]設置已讀點" + "\n\n[" + datetime.today().strftime('%Y/%m/%d  %H:%M:%S.%f') + "]")



#-----------------------------------------------





	if op.type == 55:
	    try:
		if op.param1 in wait2['readPoint']:
		    Name = cl.getContact(op.param2).displayName
		    if Name in wait2['readMember'][op.param1]:
			pass
		    else:
			wait2['readMember'][op.param1] += "\n・ " + Name + "\n  " + datetime.today().strftime(' [%m/%d - %H:%M:%S]')
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
		fid =  cl.getAllContactIds()
		gid =  cl.getGroupIdsJoined()
		profile.statusMessage = "台湾戦神☆style\nFriend: " + str(len(fid)) + "\nGroups: " + str(len(gid)) + "\n\nMade in Taiwan"
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
