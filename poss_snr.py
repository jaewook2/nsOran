import os
import subprocess
# 5초작성
maxX = 400
maxY = 400
enbP = [[20, 20], [40, 20], [10,37.3205], [10,2.67949]]
rootName = 'trace/'
i_num = 1000
# Do iteration
for i in range (i_num):
        basePathName = rootName+str(i)
        # create random possition within (max_X, max_Y)
        pos_x_list = 
        pos_y_list = 
        #poss.txt file 작성 (basePathName)
        for bs1 in range (2):
                for bs2 in range (2):
                        for bs3 in range (2):
                                for bs4 in range (2):
                                        if bs1+bs2+bs3+bs3 !=0:
                                                folderName = str(bs1)+str(bs2)+str(bs3)+str(bs4)
                                                os.mkdir(folderName)  # 폴더 생성
                                                pathName = basePathName+'/'+folderName+'/'
                                                cmd_string_sub = '0513_scenario-zero  --TracePath='+pathName +' --bs1='+str(bs1)+' --bs2='+str(bs2)+' --bs3='+str(bs3)+' --bs4='+str(bs4) + '--poss_file='+basePathName+'/poss.txt'
                                                # NS-3 상에서 possition file을 읽고 작성
                                                cmd_string = "./waf --run " +'"'+cmd_string_sub+'"'
                                                subprocess.Popen(cmd_string, shell=True).wait()

