'''
@Author: Guo Yingwei
@Date: 2020-06-28 10:54:11
@E-mail: willgyw@126.com
@Description:  
@LastEditors: gyw
@LastEditTime: 2020-06-28 11:31:57
'''
import sys,logging,os

logging.basicConfig(filename='{0}.log'.format(os.path.basename(__file__).replace('.py','')),
                    format='%(asctime)s: %(name)s: %(levelname)s: %(message)s',level=logging.DEBUG,filemode='a')
logging.info(f"The command line is:\n\tpython3 {' '.join(sys.argv)}")


region_d = {}
with open(sys.argv[1], 'r') as region_f:
    for line in region_f:
        lines = line.strip().split()
        if ((int(lines[2]) - int(lines[1])) // int(50000)) + 1 < 5:
            num = ((int(lines[2]) - int(lines[1])) // int(50000)) + 1
        else:
            num = 5 
        #print(num)
        region_d['-'.join(lines)] = num
        
for region in region_d:
    try:
        with open('tagSNP/' + region + '.tagSNP') as tag_f:
            tag_lst = tag_f.read().strip().split('\n')
            #print(tag_lst)
            head_tag = tag_lst[:region_d.get(region) + 1]
            #print(head_tag)
            fo = open('head_tagSNP/' + region + '.tagSNP.head', 'w')
            fo.write('\n'.join(head_tag) + '\n')
            #print('\n'.join(head_tag) + '\n')
    except:
        print('File Not Found :' + region + '.tagSNP')

fo.close()
            

