import os
import subprocess


maxX = 40
maxY = 40
enbP = [[20, 20], [40, 20], [10,37.3205], [10,2.67949]]

# create possition
for x in range (1):
        for y in range (200,201):
                pos_x = x
                pos_y = y
                fileName = str(x)+'_'+str(pos_y)+'losfalse.txt'
                cmd_string_sub = 'Test_Performance --uepx='+str(pos_x) + ' --uepy='+str(pos_y) + ' --fileName=trace4000/'+fileName
                cmd_string = "./waf --run " +'"'+cmd_string_sub+'"'
                
                subprocess.Popen(cmd_string, shell=True).wait()
