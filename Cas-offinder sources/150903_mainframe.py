# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 15:47:04 2015

@author: Sunghyun Kim(chizksh@gmail.com)
"""

import wx
import wx.xrc
import re
import time
import paramiko as prm
from string import maketrans
t = maketrans("ATGC", "TACG")

'''
mismatch_num_0 = 1
mismatch_num_1 = 1
mismatch_num_2 = 1
mismatch_num_3_0 = 0.561
mismatch_num_3_1 = 0.435
mismatch_num_3_2 = 0.119
mismatch_num_3_3 = 0.002
mismatch_num_4_0 = 0.215
mismatch_num_4_1 = 0.0618
mismatch_num_4_2 = 0.01
mismatch_num_4_3 = 0.00126
mismatch_num_4_4 = 0
mismatch_num_5_0 = 0.0101
mismatch_num_5_1 = 0.01
mismatch_num_5_2 = 0.00145
mismatch_num_5_3 = 0.000252
mismatch_num_5_4 = 0
mismatch_num_5_5 = 0
mismatch_num_6_0 = 0.0067
mismatch_num_6_1 = 0.00171
mismatch_num_6_2 = 0.0000397
mismatch_num_6_3 = 0.0000542
mismatch_num_6_4 = 0
mismatch_num_6_5 = 0
mismatch_num_6_6 = 0
'''
mismatch_num_list = [1.0,1.0,1.0,0.561,0.435,0.119,0.002,0.215,0.0618,0.01,0.00126,0,0.0101,0.01,0.00145,0.000252,0,0,0.0067,0.00171,0.0000397,0.0000542,0,0,0]
'''
Indel_mismatch_num_0=0
Indel_mismatch_num_1=0.15
Indel_mismatch_num_2=0.15
Indel_mismatch_num_3_0=0.11883102
Indel_mismatch_num_3_1=0.0235683
Indel_mismatch_num_3_2=0.001426096
Indel_mismatch_num_3_3=0
Indel_mismatch_num_4_0=0.4424012
Indel_mismatch_num_4_1=0.0177207792
Indel_mismatch_num_4_2=0.001007285
Indel_mismatch_num_4_3=0.0000879984
Indel_mismatch_num_4_4=0
Indel_mismatch_num_5_0=0.0009230592
Indel_mismatch_num_5_1=0.00452928
Indel_mismatch_num_5_2=0.0008652672
Indel_mismatch_num_5_3=0.000088228224
Indel_mismatch_num_5_4=0
Indel_mismatch_num_5_5=0
Indel_mismatch_num_6_0=0.0007449462
Indel_mismatch_num_6_1=0.00117870471
Indel_mismatch_num_6_2=0.0000587819241
Indel_mismatch_num_6_3=0.0000700802748
Indel_mismatch_num_6_4=0
Indel_mismatch_num_6_5=0
Indel_mismatch_num_6_6=0
'''
Indel_mismatch_num_list = [0.0,0.15,0.15,0.03026,0.00774,0.002996,0.0001,0.03026,0.003928,0.0008759,0.004365,0,0.000672,0.000672,0.000672,0.000672,0,0,0.000261,0.000261,0.000261,0.000261,0,0,0]



def n_lower_chars(string):
    return sum(1 for c in string if c.islower())
     
def prm_init(_id, _pass,_server,_port):
    ssh=prm.SSHClient()
    ssh.set_missing_host_key_policy(prm.AutoAddPolicy())
    ssh.connect(_server,port=_port,username=_id,password=_pass)
    
    transport = prm.Transport((_server,_port))
    transport.connect(username=_id,password=_pass)
    
    sftp = prm.SFTPClient.from_transport(transport)
    return ssh, sftp
    
def result_ana(gene_name,dlocalpath):

    
    fi = open(dlocalpath, 'r')
    fo = open("./"+gene_name+"_final_result.txt", 'w')
    
    mismatch_dic = {}    
    mismatch_score_dic = {}
    indel_score_dic = {}
    for line in fi.xreadlines():
            units = line.split()
            if not mismatch_dic.has_key(units[0]):
                mismatch_dic[units[0]] = []
                mismatch_score_dic[units[0]] = 0.0
                indel_score_dic[units[0]] = 0.0
            
            seed_seq = units[3][10:20]
            
            mismatch_num_seed=n_lower_chars(seed_seq)
            mismatch_dic[units[0]]+=[(int(units[5]),mismatch_num_seed)]
            
           
        #print mismatch_dic
    fi.close()
    #print len(mismatch_dic.keys())
    for each_key in mismatch_dic.keys():
        c0 = mismatch_dic[each_key].count((0,0))
        
        c1_0 = mismatch_dic[each_key].count((1,0))
        c1_1 = mismatch_dic[each_key].count((1,1))
        c1 = c1_0 + c1_1
        
        c2_0 = mismatch_dic[each_key].count((2,0))
        c2_1 = mismatch_dic[each_key].count((2,1))
        c2_2 = mismatch_dic[each_key].count((2,2))
        c2 = c2_0 + c2_1 + c2_2
        
        c3_0 = mismatch_dic[each_key].count((3,0))
        c3_1 = mismatch_dic[each_key].count((3,1))
        c3_2 = mismatch_dic[each_key].count((3,2))
        c3_3 = mismatch_dic[each_key].count((3,3))
        c3 = c3_0 + c3_1 + c3_2 + c3_3
        
        c4_0 = mismatch_dic[each_key].count((4,0)) 
        c4_1 = mismatch_dic[each_key].count((4,1))
        c4_2 = mismatch_dic[each_key].count((4,2))
        c4_3 = mismatch_dic[each_key].count((4,3))
        c4_4 = mismatch_dic[each_key].count((4,4))
        c4 = c4_0 + c4_1 + c4_2 + c4_3 +c4_4

        c5_0 = mismatch_dic[each_key].count((5,0))
        c5_1 = mismatch_dic[each_key].count((5,1))
        c5_2 = mismatch_dic[each_key].count((5,2))
        c5_3 = mismatch_dic[each_key].count((5,3))
        c5_4 = mismatch_dic[each_key].count((5,4))
        c5_5 = mismatch_dic[each_key].count((5,5))
        c5 = c5_0 + c5_1 + c5_2 + c5_3 + c5_4 + c5_5

        c6_0 = mismatch_dic[each_key].count((6,0))
        c6_1 = mismatch_dic[each_key].count((6,1))
        c6_2 = mismatch_dic[each_key].count((6,2))
        c6_3 = mismatch_dic[each_key].count((6,3))
        c6_4 = mismatch_dic[each_key].count((6,4))
        c6_5 = mismatch_dic[each_key].count((6,5))
        c6_6 = mismatch_dic[each_key].count((6,6))
        c6 = c6_0 + c6_1 + c6_2 + c6_3 + c6_4 + c6_5 + c6_6
        count_list = [c0,c1,c2,c3_0,c3_1,c3_2,c3_3,c4_0,c4_1,c4_2,c4_3,c4_4,c5_0,c5_1,c5_2,c5_3,c5_4,c5_5,c6_0,c6_1,c6_2,c6_3,c6_4,c6_5,c6_6]

        print c0,c1,c2,c3,c4,c5,c6
        
        count = len(mismatch_dic[each_key])
        for i in range(len(count_list)):
            mismatch_score_dic[each_key] += mismatch_num_list[i] * count_list[i]
            indel_score_dic[each_key] += mismatch_num_list[i] * count_list[i] * Indel_mismatch_num_list[i]
        
        fo.write("%s\t%d\t%d\t%d\t%d\t"%(each_key,c0,c1,c2,count))
        if (c0==1 and c1==0 and c2==0) and (count < 13000):
            fo.write('O\t%f\t%f\n'%(mismatch_score_dic[each_key],indel_score_dic[each_key]))
        else:
            fo.write('X\t%f\t%f\n'%(mismatch_score_dic[each_key],indel_score_dic[each_key]))
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
                print 'CC'+seq[each_pos+2:each_pos+23]
                print seq[each_pos+3:each_pos+23].translate(t)[::-1]
                ccns_revcomp.append(seq[each_pos+3:each_pos+23].translate(t)[::-1])
            except IndexError:
                pass;
    #print len(set(nggs+ccns_revcomp))
    return set(nggs+ccns_revcomp)

def make_inputfile(gene_name,nggs):
    f = open('./'+gene_name+'_NGG.txt','w')
    f.write('/data/analysis/Hg19'+'\n')
    f.write('N'*20+'NGG'+'\n')
    for each in nggs:
        f.write(each+'NGG'+'\t'+'6'+'\n')
    f.close()


class MainFrame ( wx.Frame ):
    
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"cas-offinder", pos = wx.Point( -1,-1 ), size = wx.Size( 597,360 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        
        MainSizer = wx.FlexGridSizer( 1, 2, 0, 10 )
        MainSizer.AddGrowableCol( 1 )
        MainSizer.SetFlexibleDirection( wx.BOTH )
        MainSizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
        
        LeftSizer = wx.FlexGridSizer( 2, 1, 10, 10 )
        LeftSizer.SetFlexibleDirection( wx.BOTH )
        LeftSizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
        
        SettingSizer = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Setting" ), wx.VERTICAL )
        
        SettingSizer.SetMinSize( wx.Size( 200,250 ) ) 
        setting = wx.FlexGridSizer( 3, 1, 0, 0 )
        setting.SetFlexibleDirection( wx.BOTH )
        setting.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
        
        server_ip_port = wx.FlexGridSizer( 1, 2, 0, 0 )
        server_ip_port.SetFlexibleDirection( wx.BOTH )
        server_ip_port.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
        
        server_ip = wx.BoxSizer( wx.VERTICAL )
        
        self.server_ip_text = wx.StaticText( SettingSizer.GetStaticBox(), wx.ID_ANY, u"Server IP", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.server_ip_text.Wrap( -1 )
        server_ip.Add( self.server_ip_text, 0, wx.ALL, 5 )
        
        self.server_ip_ctrl = wx.TextCtrl( SettingSizer.GetStaticBox(), wx.ID_ANY, u"203.247.183.92", wx.DefaultPosition, wx.DefaultSize, 0 )
        server_ip.Add( self.server_ip_ctrl, 0, wx.ALL, 5 )
        
        
        server_ip_port.Add( server_ip, 1, wx.EXPAND, 5 )
        
        port = wx.BoxSizer( wx.VERTICAL )
        
        self.port_text = wx.StaticText( SettingSizer.GetStaticBox(), wx.ID_ANY, u"Port", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.port_text.Wrap( -1 )
        port.Add( self.port_text, 0, wx.ALL, 5 )
        
        self.port_ctrl = wx.TextCtrl( SettingSizer.GetStaticBox(), wx.ID_ANY, u"5130", wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
        port.Add( self.port_ctrl, 0, wx.ALL, 5 )
        
        
        server_ip_port.Add( port, 1, wx.EXPAND, 5 )
        
        
        setting.Add( server_ip_port, 1, wx.EXPAND, 5 )
        
        id_pass = wx.BoxSizer( wx.VERTICAL )
        
        self.id_text = wx.StaticText( SettingSizer.GetStaticBox(), wx.ID_ANY, u"Id", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.id_text.Wrap( -1 )
        id_pass.Add( self.id_text, 0, wx.ALL, 5 )
        
        self.id_ctrl = wx.TextCtrl( SettingSizer.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        id_pass.Add( self.id_ctrl, 0, wx.ALL, 5 )
        
        self.pass_text = wx.StaticText( SettingSizer.GetStaticBox(), wx.ID_ANY, u"Password", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.pass_text.Wrap( -1 )
        id_pass.Add( self.pass_text, 0, wx.ALL, 5 )
        
        self.pass_ctrl = wx.TextCtrl( SettingSizer.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD )
        id_pass.Add( self.pass_ctrl, 0, wx.ALL, 5 )
        
        
        setting.Add( id_pass, 1, wx.EXPAND, 5 )
        
        file_select = wx.BoxSizer( wx.VERTICAL )
        
        self.input_file_text = wx.StaticText( SettingSizer.GetStaticBox(), wx.ID_ANY, u"Input file", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.input_file_text.Wrap( -1 )
        file_select.Add( self.input_file_text, 0, wx.ALL, 5 )
        
        self.input_picker = wx.FilePickerCtrl( SettingSizer.GetStaticBox(), wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.txt", wx.DefaultPosition, wx.DefaultSize, wx.FLP_CHANGE_DIR|wx.FLP_DEFAULT_STYLE|wx.FLP_FILE_MUST_EXIST|wx.FLP_OPEN|wx.FLP_SMALL )
        file_select.Add( self.input_picker, 0, wx.ALL, 5 )
        
        
        setting.Add( file_select, 1, wx.EXPAND, 5 )
        
        
        SettingSizer.Add( setting, 1, wx.EXPAND, 5 )
        
        
        LeftSizer.Add( SettingSizer, 1, wx.EXPAND, 10 )
        
        self.run = wx.Button( self, 1, u"Run", wx.DefaultPosition, wx.DefaultSize, 0 )
        LeftSizer.Add( self.run, 0, wx.ALIGN_CENTER|wx.ALL|wx.EXPAND, 5 )
        
        
        MainSizer.Add( LeftSizer, 1, wx.EXPAND|wx.TOP|wx.BOTTOM|wx.LEFT, 5 )
        
        RightSizer = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Message" ), wx.VERTICAL )
        
        self.Bind(wx.EVT_BUTTON, self.runClick, id=1)
        
        self.message = wx.TextCtrl( RightSizer.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.TE_MULTILINE|wx.TE_READONLY )
        
        
        RightSizer.Add( self.message, 1, wx.ALL|wx.EXPAND, 5 )
        
        
        MainSizer.Add( RightSizer, 1, wx.EXPAND|wx.TOP|wx.BOTTOM|wx.RIGHT, 5 )
        
        
        self.SetSizer( MainSizer )
        self.Layout()
        
        self.Centre( wx.BOTH );self.Show()
    
    def __del__( self ):
        pass
    
    def runClick(self, event):
        server = self.server_ip_ctrl.GetValue()
        port = int(self.port_ctrl.GetValue())
        _id = self.id_ctrl.GetValue()
        _pass= self.pass_ctrl.GetValue()
        file_path = self.input_picker.GetPath()
        _message=''
        t1 = time.time()
        f=open(file_path,'r')
    
        for line in f.xreadlines():
            gene_name, seq = line.strip('\n').split('\t')
            _message+=(gene_name+'\n')
            self.message.SetValue(_message)
            print gene_name
            ssh, sftp = prm_init(_id,_pass,server,port)
                
            nggs=find_NGG_CCN(seq)
            _message+=('total NGG: '+str(len(nggs))+'\n')
            self.message.SetValue(_message)
            print 'total NGG: '+str(len(nggs))
            
            make_inputfile(gene_name,nggs)
            _message+=('input file created.'+'\n')
            self.message.SetValue(_message)
            print 'input file created.'
            
            #upload
            uremotepath = '/home/'+_id+'/'+gene_name+'_NGG.txt'
            ulocalpath = './'+gene_name+'_NGG.txt'
            sftp.put(ulocalpath,uremotepath)
            _message+=('input file uploaded.'+'\n')
            self.message.SetValue(_message)
            print 'input file uploaded.'
            
            #processing
            stdin, stdout, stderr = ssh.exec_command('cd '+'/home/'+_id)
            command = 'cas-offinder '+gene_name+'_NGG.txt G '+gene_name+'_output.txt'
            stdin, stdout, stderr = ssh.exec_command(command)
            
            #confirm finished    
            _message+=("cas-offinder processing...")
            self.message.SetValue(_message)
            wx.Yield()
            print "cas-offinder processing...",
            '''            
            stdout.channel.recv_exit_status()
            '''
            wait_time = 0.0
            while not stdout.channel.exit_status_ready():
                time.sleep(0.5)
                wait_time+=0.5
                self.message.SetValue(_message+" "+str(int(wait_time))+" seconds elasped.")
                wx.Yield()
            s = stdout.readlines()[-1].strip('\n')
            _message+=(s+'\n')
            self.message.SetValue(_message)
            print s
            _message+=('done.'+'\n')
            self.message.SetValue(_message)
            print 'done'
            stdout.channel.close()
        
            #download
            dremotepath = '/home/'+_id+'/'+gene_name+'_output.txt'
            dlocalpath = './'+gene_name+'_output.txt'
            sftp.get(dremotepath,dlocalpath)
            _message+=('output file downloaded.'+'\n')
            self.message.SetValue(_message)
            print 'output file downloaded'
            ssh.close()
            sftp.close()    
            
            #result_ana
            result_ana(gene_name,dlocalpath)
            _message+=('result file created.'+'\n')
            self.message.SetValue(_message)
            print 'result file created.'
        f.close()
        t2= time.time()
        _message+=('total elasped time: %d seconds'%(t2-t1))
        self.message.SetValue(_message)

    
if __name__ == '__main__':
  
    app = wx.App()
    MainFrame(None)
    app.MainLoop()
