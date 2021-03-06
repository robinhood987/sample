from linepy import *
import json, time, random

client = LineClient()
#client = LineClient(authToken='AUTH TOKEN')
client.log("Auth Token : " + str(client.authToken))

channel = LineChannel(client)
client.log("Channel Access Token : " + str(channel.channelAccessToken))

poll = LinePoll(client)

cctv={
    "cyduk":{},
    "point":{},
    "sidermem":{}
}

while True:
            try:
                    if msg.contentType == 0:
                        if msg.toType == 2:
                            client.sendChatChecked(receiver, msg_id)
                            contact = client.getContact(sender)
                            if text.lower() == 'me':
                                client.sendMessage(receiver, None, contentMetadata={'mid': sender}, contentType=13)
                            elif text.lower() == 'speed':
                                start = time.time()
                                client.sendText(receiver, "TestSpeed")
                                elapsed_time = time.time() - start
                                client.sendText(receiver, "%sdetik" % (elapsed_time))
                            elif 'pfp' in text.lower():
                                try:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    u = key["MENTIONEES"][0]["M"]
                                    a = client.getContact(u).pictureStatus
                                    client.sendImageWithURL(receiver, 'http://dl.profile.line.naver.jp/'+a)
                                except Exception as e:
                                    client.sendText(receiver, str(e))
                            elif 'coverpic' in text.lower():
                                try:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    u = key["MENTIONEES"][0]["M"]
                                    a = channel.getProfileCoverURL(mid=u)
                                    client.sendImageWithURL(receiver, a)
                                except Exception as e:
                                    client.sendText(receiver, str(e))
                            elif text.lower() == 'tagall':
                                group = client.getGroup(msg.to)
                                nama = [contact.mid for contact in group.members]
                                nm1, nm2, nm3, nm4, nm5, jml = [], [], [], [], [], len(nama)
                                if jml <= 100:
                                    client.mention(msg.to, nama)
                                if jml > 100 and jml < 200:
                                    for i in range(0, 100):
                                        nm1 += [nama[i]]
                                    client.mention(msg.to, nm1)
                                    for j in range(101, len(nama)):
                                        nm2 += [nama[j]]
                                    client.mention(msg.to, nm2)
                                if jml > 200 and jml < 300:
                                    for i in range(0, 100):
                                        nm1 += [nama[i]]
                                    client.mention(msg.to, nm1)
                                    for j in range(101, 200):
                                        nm2 += [nama[j]]
                                    client.mention(msg.to, nm2)
                                    for k in range(201, len(nama)):
                                        nm3 += [nama[k]]
                                    client.mention(msg.to, nm3)
                                if jml > 300 and jml < 400:
                                    for i in range(0, 100):
                                        nm1 += [nama[i]]
                                    client.mention(msg.to, nm1)
                                    for j in range(101, 200):
                                        nm2 += [nama[j]]
                                    client.mention(msg.to, nm2)
                                    for k in range(201, len(nama)):
                                        nm3 += [nama[k]]
                                    client.mention(msg.to, nm3)
                                    for l in range(301, len(nama)):
                                        nm4 += [nama[l]]
                                    client.mention(msg.to, nm4)
                                if jml > 400 and jml < 501:
                                    for i in range(0, 100):
                                        nm1 += [nama[i]]
                                    client.mention(msg.to, nm1)
                                    for j in range(101, 200):
                                        nm2 += [nama[j]]
                                    client.mention(msg.to, nm2)
                                    for k in range(201, len(nama)):
                                        nm3 += [nama[k]]
                                    client.mention(msg.to, nm3)
                                    for l in range(301, len(nama)):
                                        nm4 += [nama[l]]
                                    client.mention(msg.to, nm4)
                                    for m in range(401, len(nama)):
                                        nm5 += [nama[m]]
                                    client.mention(msg.to, nm5)             
                                client.sendText(receiver, "Members :"+str(jml))
                        
            # Don't remove this line, if you wan't get error soon!
            
            
    except Exception as e:
        client.log("[SINGLE_TRACE] ERROR : " + str(e))
