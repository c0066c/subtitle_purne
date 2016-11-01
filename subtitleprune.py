#print len("00:00:31,916 --> 00:00:34,751") #29
def subtitle_prune(instr, outstr, sec):
    f = open(instr, 'r')
    w = open(outstr, 'w')
    for line in f:
        if(line.find(':') == 2): #those timeline
            tmp = line.split(":")        
            #tmp will be a list ['00', '00', '31,916 --> 00', '00', '34,751\n']
            tmp2 = tmp[2].split("-->")
            #split the middle part from '31,916 --> 00' to '31,916 ', ' 00']
            
            #here is the started second, e.g., 31,916
            tmp3 = tmp2[0].split(",")        
    #        print tmp3
            if(int(tmp3[0])-sec >= 0): 
                if(int(tmp3[0])-sec < 10): 
                    tmp3[0] = '0'+str(int(tmp3[0])-sec)
                else:
                    tmp3[0] = str(int(tmp3[0])-sec)
            else:
                tmp3[0] = str(int(tmp3[0])+60-sec)
                tmp[1] = str(int(tmp[1])-1)
            #here is the ended second, e.g., 34,751
            tmp4 =tmp[4].split(",")
    #        print tmp4
            if(int(tmp4[0])-sec >= 0): 
                if(int(tmp4[0])-sec < 10):
                    tmp4[0] = '0'+str(int(tmp4[0])-sec)
                else:
                    tmp4[0] = str(int(tmp4[0])-sec)
            else:
                tmp4[0] = str(int(tmp4[0])+60-sec)
                tmp[3] = str(int(tmp[3])-1)
            w.write(tmp[0]+":"+tmp[1]+":"+tmp3[0]+ "," + tmp3[1] + "-->" + tmp2[1] + ":" + tmp[3] + ":" + tmp4[0] + ","+tmp4[1])
            
        else:
            w.write(line)
    w.close()
#subtitle_prune("test.srt", "pruned.srt", 2)