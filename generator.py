# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 15:11:52 2019

@author: PSSung
"""

import os

def xml_generator(file):
    char_count = 0 #cahracteristics
    meas_count = 0 #measurement
    with open(file, 'r+') as a2l:
        for line in a2l:            
            if line.find('/begin CHARACTERISTIC')>=0:
                char_count += 1
                char_name = next(a2l, '').strip()
                char_name = char_name.strip('/* Name                   */      ')
                print(char_name)
                generated = open('myXML.txt','a+')
                for i in range(4):
                    char_type = next(a2l, '').strip()
                    if 'FLOAT32' in char_type:
                        generated_out = '${block:Engineering-AllValues-Value-text \'%s\' \'%s\'}' % (char_name,char_name)
                        generated.write(str(generated_out)+'\n') 
                    elif 'Scalar_BOOLEAN' in char_type:
                        if 'Val' in char_name:
                            generated_out = '${block:Engineering-AllValues-Value-bool-HL \'%s\' \'%s\'}' % (char_name,char_name)
                            generated.write(str(generated_out)+'\n')
                        elif 'Enb' in char_name:
                            generated_out = '${block:Engineering-AllValues-Value-bool-err \'%s\' \'%s\'}' % (char_name,char_name)
                            generated.write(str(generated_out)+'\n')

# =============================================================================
#             if line.find('/begin MEASUREMENT')>=0:
#                 meas_count += 1
#                 char_name = next(a2l, '').strip()
#                 print(char_name)
# =============================================================================
                
    print('characteristics: ',char_count,' measurements: ',meas_count)
    
# =============================================================================
#     generated = open('myXML.txt','a+')
#     generated.write(str(char_name)+'\n')
#     generated.close
# =============================================================================

path = r'C:/Users/pssung/Documents/mylab/a2l'
dirs = os.listdir( path )
for file in sorted(dirs):
   #print(file)
   #if file==""
   try:
     xml_generator(file)
   except:
     print('not found')