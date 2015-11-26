# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 10:46:05 2015

@author: Sunghyun Kim(chizksh@gmail.com)
"""

import wx
import wx.xrc
import math

mismatch_num_1 = 1
mismatch_num_2 = 1
mismatch_num_5 = 0.0042
mismatch_num_6 = 0.00045
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




def n_lower_chars(string):
    return sum(1 for c in string if c.islower())
          

class casoffinder_analysis ( wx.Frame ):
    
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"cas-offinder analysis (server version)", pos = wx.DefaultPosition, size = wx.Size( 616,455 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        
        fgSizer6 = wx.FlexGridSizer( 2, 1, 0, 0 )
        fgSizer6.AddGrowableRow( 1 )
        fgSizer6.SetFlexibleDirection( wx.BOTH )
        fgSizer6.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
        
        fgSizer7 = wx.FlexGridSizer( 0, 2, 0, 0 )
        fgSizer7.SetFlexibleDirection( wx.BOTH )
        fgSizer7.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
        
        self.file_path = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.txt", wx.DefaultPosition, wx.Size( 500,-1 ), wx.FLP_DEFAULT_STYLE|wx.FLP_FILE_MUST_EXIST )
        fgSizer7.Add( self.file_path, 0, wx.ALL, 5 )
        
        self.run_btn = wx.Button( self, 1, u"Run", wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer7.Add( self.run_btn, 0, wx.ALL, 5 )
        
        
        fgSizer6.Add( fgSizer7, 1, wx.EXPAND, 5 )
        
        sbSizer4 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Result" ), wx.VERTICAL )
        
        sbSizer4.SetMinSize( wx.Size( 700,-1 ) ) 
        self.result_ctrl = wx.TextCtrl( sbSizer4.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,400 ), wx.TE_MULTILINE )
        sbSizer4.Add( self.result_ctrl, 0, wx.ALL|wx.EXPAND, 5 )
        
        
        fgSizer6.Add( sbSizer4, 1, wx.EXPAND, 5 )
        
        
        self.SetSizer( fgSizer6 )
        self.Layout()
        
        self.Centre( wx.BOTH );self.Show()
        self.Bind(wx.EVT_BUTTON, self.mismatch_analysis, id=1)
        font1 = wx.Font(10, wx.MODERN, wx.NORMAL, wx.NORMAL, False, u'Consolas')
        self.result_ctrl.SetFont(font1)
    def __del__( self ):
        pass
    def mismatch_analysis(self, event):
        
        _file = self.file_path.GetPath()
        
        
        fi = open(_file, 'r')
        fo = open(_file[:-4]+"_result.txt", 'w')
        
        mismatch_dic = {}    
        mismatch_score_dic = {}
        for line in fi.xreadlines():
            units = line.split()
            if not mismatch_dic.has_key(units[0]):
                mismatch_dic[units[0]] = []
                mismatch_score_dic[units[0]] = 0.0
            mismatch_dic[units[0]]+=[int(units[5])]
            
            
            mismatch_num=int(units[5])
            seed_seq = units[3][10:20]
            
            
            
            mismatch_num_seed=n_lower_chars(seed_seq)
            #print mismatch_num,seed_seq, mismatch_num_seed
            if mismatch_num == 6:
                if mismatch_score_dic[units[0]] == 0:
                    mismatch_score_dic[units[0]]+=mismatch_num_6_0
                elif mismatch_score_dic[units[0]] == 1:
                    mismatch_score_dic[units[0]]+=mismatch_num_6_1
                elif mismatch_score_dic[units[0]] == 2:
                    mismatch_score_dic[units[0]]+=mismatch_num_6_2
                elif mismatch_score_dic[units[0]] == 3:
                    mismatch_score_dic[units[0]]+=mismatch_num_6_3
                elif mismatch_score_dic[units[0]] == 4:
                    mismatch_score_dic[units[0]]+=mismatch_num_6_4  
                elif mismatch_score_dic[units[0]] == 5:
                    mismatch_score_dic[units[0]]+=mismatch_num_6_5
                elif mismatch_score_dic[units[0]] == 6:
                    mismatch_score_dic[units[0]]+=mismatch_num_6_6
                #print(mismatch_score_dic[units[0]])
            elif mismatch_num == 5:
                if mismatch_score_dic[units[0]] == 0:
                    mismatch_score_dic[units[0]]+=mismatch_num_5_0
                elif mismatch_score_dic[units[0]] == 1:
                    mismatch_score_dic[units[0]]+=mismatch_num_5_1
                elif mismatch_score_dic[units[0]] == 2:
                    mismatch_score_dic[units[0]]+=mismatch_num_5_2
                elif mismatch_score_dic[units[0]] == 3:
                    mismatch_score_dic[units[0]]+=mismatch_num_5_3
                elif mismatch_score_dic[units[0]] == 4:
                    mismatch_score_dic[units[0]]+=mismatch_num_5_4  
                elif mismatch_score_dic[units[0]] == 5:
                    mismatch_score_dic[units[0]]+=mismatch_num_5_5
                #print(mismatch_score_dic[units[0]])
            elif mismatch_num == 4:
                if mismatch_num_seed == 0:
                    mismatch_score_dic[units[0]]+=mismatch_num_4_0
                elif mismatch_num_seed == 1:
                    mismatch_score_dic[units[0]]+=mismatch_num_4_1
                elif mismatch_num_seed == 2:
                    mismatch_score_dic[units[0]]+=mismatch_num_4_2
                elif mismatch_num_seed == 3:
                    mismatch_score_dic[units[0]]+=mismatch_num_4_3
                elif mismatch_num_seed == 4:
                    mismatch_score_dic[units[0]]+=mismatch_num_4_4
                #print(mismatch_score_dic[units[0]])
            elif mismatch_num == 3:
                if mismatch_num_seed == 0:
                    mismatch_score_dic[units[0]]+=mismatch_num_3_0
                elif mismatch_num_seed == 1:
                    mismatch_score_dic[units[0]]+=mismatch_num_3_1
                elif mismatch_num_seed == 2:
                    mismatch_score_dic[units[0]]+=mismatch_num_3_2
                elif mismatch_num_seed == 3:
                    mismatch_score_dic[units[0]]+=mismatch_num_3_3
                #print(mismatch_score_dic[units[0]])
            elif mismatch_num == 2:
                mismatch_score_dic[units[0]]+=mismatch_num_1
            elif mismatch_num == 1 :
                mismatch_score_dic[units[0]]+=mismatch_num_2
                
            else:
                pass
            
        fi.close()
        #print len(mismatch_dic.keys())
        for each_key in mismatch_dic.keys():
            c0 = mismatch_dic[each_key].count(0)
            c1 = mismatch_dic[each_key].count(1)
            c2 = mismatch_dic[each_key].count(2)
            count = len(mismatch_dic[each_key])
            
            fo.write("%s\t%d\t%d\t%d\t%d\t"%(each_key,c0,c1,c2,count))
            if (c0==1 and c1==0 and c2==0) and (count < 13000):
                fo.write('O\t%f\n'%(math.sqrt(mismatch_score_dic[each_key])))
            else:
                fo.write('X\t%f\n'%(math.sqrt(mismatch_score_dic[each_key])))
        fo.close()
        fm = open(_file[:-4]+"_result.txt", 'r')
        message = fm.read()
        
        self.result_ctrl.SetValue(message)
        fm.close()


        
if __name__ == '__main__':
  
    app = wx.App()
    casoffinder_analysis(None)
    app.MainLoop()
