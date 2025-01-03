import os
import subprocess
import numpy as np
import shutil

# 5초작성

i_sim = 0
def createPoss(nUes, maxX, maxY, path_file = None):
  possList = np.zeros((nUes,2)) # (x,y point)
  possIndList = np.random.choice (range(0,(maxX+1)*(maxY+1)), nUes, replace = False)
  
  if path_file != None:
    f = open(path_file,'w')
  
  for i in range (nUes):
    possList[i,0], possList[i,1] = possIndList[i]%maxY, possIndList[i]//maxY
    if path_file != None:
    	f.write("%d %d\n"% (possList[i,0], possList[i,1]))

  if path_file != None:
    f.close()
    
  return possList

def createFolder(path_folder):
  if os.path.isdir (path_folder):
    shutil.rmtree(path_folder)
    
  os.mkdir(path_folder) 
    

#0812
maxX = 400
maxY = maxX
#enbP = [[20, 20], [40, 20], [10,37.3205], [10,2.67949]]
rootName = 'trace/'
i_num = 10 # 10 unit

nUes = 12
# Do iteration
for i in range (0, i_num):
  basePathName = rootName+str(i_sim)+'_'+str(i)
  # create_folder
  createFolder(basePathName) 
  # create random possition within (max_X, max_Y) and save ue poss to file
  possList = createPoss(nUes, maxX, maxY, path_file = basePathName+'/ues_poss.txt')
  
  for bs1 in range (1,2):
    for bs2 in range (1,2):
      for bs3 in range (1,2):
        for bs4 in range (1,2):
          if bs1+bs2+bs3+bs4 !=0:
            folderName = str(bs1)+str(bs2)+str(bs3)+str(bs4)
            pathName = basePathName+'/'+folderName
            createFolder(pathName) # 폴더 생성
            cmd_string_sub = '0513_scenario-zero --TracePath='+pathName+'/' \
            + ' --bs1=' + str(1) + ' --bs2=' + str(1)+ ' --bs3='+str(1)+ ' --bs4='+str(1) \
            + ' --poss_file='+basePathName+'/ues_poss.txt' + ' --maxXAxis='+str(maxX) \
            + ' --nUeNodes='+str(nUes)

            # NS-3 상에서 possition file을 읽고 작성
            cmd_string = "./waf --run " +'"'+cmd_string_sub+'"'
            subprocess.Popen(cmd_string, shell=True).wait()



