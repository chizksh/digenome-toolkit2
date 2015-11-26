# -*- coding: utf-8 -*-
"""
Created on Fri Aug 07 11:07:33 2015

@author: Sunghyun Kim(chizksh@gmail.com)
"""

import re
import time
import paramiko as prm
from string import maketrans
t = maketrans("ATGC", "TACG")


     
def prm_init(_id, _pass):
    ssh=prm.SSHClient()
    ssh.set_missing_host_key_policy(prm.AutoAddPolicy())
    ssh.connect('203.247.183.92',port=5130,username=_id,password=_pass)
    
    transport = prm.Transport(('203.247.183.92',5130))
    transport.connect(username=_id,password=_pass)
    
    sftp = prm.SFTPClient.from_transport(transport)
    return ssh, sftp
    
def result_ana(gene_name,dlocalpath):
    
    fi = open(dlocalpath, 'r')
    fo = open("./"+gene_name+"_final_result.txt", 'w')
    
    mismatch_dic = {}    
    for line in fi.xreadlines():
        units = line.split()
        if not mismatch_dic.has_key(units[0]):
            mismatch_dic[units[0]] = []
        mismatch_dic[units[0]]+=[int(units[5])]
    fi.close()
    #print len(mismatch_dic.keys())
    for each_key in mismatch_dic.keys():
        c0 = mismatch_dic[each_key].count(0)
        c1 = mismatch_dic[each_key].count(1)
        c2 = mismatch_dic[each_key].count(2)
        s = len(mismatch_dic[each_key])
        fo.write("%s\t%d\t%d\t%d\t%d\t"%(each_key,c0,c1,c2,s))
        if (c0==1 and c1==0 and c2==0) and (s < 13000):
            fo.write('O\n')
        else:
            fo.write('X\n')
    fo.close()             


def find_NGG_CCN(seq):
    #seq should be upper case
    seq=seq.upper()

    #find NGG
    nggs=[]    
    pos = [m.start() for m in re.finditer('(?=GG)', seq)]
    
    for each_pos in pos:
        if each_pos>=21:
            try:        
                nggs.append(seq[each_pos-21:each_pos-1])
            except IndexError:
                pass;
    
    #find CCN
    ccns_revcomp=[]
    pos = [m.start() for m in re.finditer('(?=CC)', seq)]
    
    for each_pos in pos:
        if each_pos+23<=len(seq):
            try:
                ccns_revcomp.append(seq[each_pos+3:each_pos+23].translate(t)[::-1])
            except IndexError:
                pass;
    #print len(set(nggs+ccns_revcomp))
    return set(nggs+ccns_revcomp)

def make_inputfile(nggs):
    f = open('./NGG.txt','w')
    f.write('/data/analysis/Hg19'+'\n')
    f.write('N'*20+'NNG'+'\n')
    for each in nggs:
        f.write(each+'NGG'+'\t'+'6'+'\n')
    f.close()
    
def main():
    f=open("./exons.txt",'r')
    
    for line in f.xreadlines():
        gene_name, seq = line.strip('\n').split('\t')
        print gene_name
        _id = 'shkim'
        _pass = 'tjdgus8965'
        
        ssh, sftp = prm_init(_id,_pass)
            
        nggs=find_NGG_CCN(seq)
        print 'total NGG:'+str(len(nggs))
        
        make_inputfile(nggs)
        print 'input file created.'
    
        #upload
        uremotepath = '/home/'+_id+'/NGG.txt'
        ulocalpath = './NGG.txt'
        sftp.put(ulocalpath,uremotepath)
        print 'input file uploaded.'
        
        #processing
        stdin, stdout, stderr = ssh.exec_command('cd '+'/home/'+_id)
        stdin, stdout, stderr = ssh.exec_command('cas-offinder NGG.txt G output.txt')
        
        #confirm finished    
        print "cas-offinder processing...",
        stdout.channel.recv_exit_status()
        print stdout.readlines()[-1].strip('\n')
        print 'done'
        stdout.channel.close()
    
        #download
        dremotepath = '/home/'+_id+'/output.txt'
        dlocalpath = './output.txt'
        sftp.get(dremotepath,dlocalpath)
        print 'output file downloaded'
        ssh.close()
        sftp.close()    
        
        #result_ana
        result_ana(gene_name,dlocalpath)
        print 'result file created.'
    f.close()
main()











'''webdriver methods
def webdriver_init():
        
    #Firefox profile    
    fp = wd.FirefoxProfile()
    fp.set_preference("browser.download.folderList",2)
    fp.set_preference("browser.download.manager.showWhenStarting",False)
    fp.set_preference("browser.helperApps.alwaysAsk.force", False)
    fp.set_preference("browser.helperApps.neverAsk.saveToDisk","application/xml,text/plain,text/xml,image/jpeg,text/csv")
    fp.set_preference("browser.download.manager.showWhenStarting",False)
 
    #webdriver option setting   
    driver = wd.Firefox(firefox_profile=fp)
    return driver
  
def get_casfinder(driver, seq):
        
    
    driver.get('http://www.rgenome.net/cas-offinder/')
        
    hg19_radio = driver.find_element_by_xpath('//input[@type="radio" and @value="2"]')    
    hg19_radio.click()    
    
    text_area = driver.find_element_by_id('query_seq')
    text_area.send_keys(seq)
    
    mismatch_span = driver.find_element_by_xpath("//select[@name='mismatch']/option[text()='6']")
    mismatch_span.click()
    
    submit_btn = driver.find_element_by_xpath('//input[@type="submit" and @value="Submit"]')
    submit_btn.click()
    
    #driver.implicitly_wait(30)
    try:
        WebDriverWait(driver, 100).until(EC.text_to_be_present_in_element((By.ID,'table_res'), 'Finished!'))
        down_link = driver.find_element_by_link_text('Download result')
        down_link.click()
        print 'result.txt - downloaded'
    finally:
        #driver.save_screenshot('out.png')
        #driver.quit()
        pass;
''' 