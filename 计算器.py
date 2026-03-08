import wx
import math
class JisuanqiFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None,title='计算器',size=(500,700))#初始化框架
        panel=wx.Panel(self)
        main_sizer=wx.BoxSizer(wx.VERTICAL)
        self.screen=wx.TextCtrl(panel,style=wx.TE_RIGHT|wx.TE_READONLY)
        self.screen.SetFont(wx.Font(20,wx.FONTFAMILY_DEFAULT,wx.FONTSTYLE_NORMAL,wx.FONTWEIGHT_BOLD))#20后面的是字体设置
        self.screen.SetValue('0')
        main_sizer.Add(self.screen,proportion=1,flag=wx.EXPAND|wx.ALL,border=5)#弄这个的布局和位置
        button_sizer=wx.GridBagSizer(5,5)#(垂直间距,水平间距)
        self.is_degree=True
        buttons=[
            ((0,0),'角度制','sanjiao'),#第二个是名字，第三个是能力标识用来调用函数的作用
            ((0,1),'复制','copy'),
            ((0,2),'历史','history'),
            ((0,3),'退位','tui'),
            ((0,4),'清除','clear'),
            ((1,0),'sin','sanjiao'),
            ((1,1),'tan','sanjiao'),
            ((1,2),'asin','sanjiao'),
            ((1,3),'余数','yushu'),
            ((1,4),'ln','duishu'),
            ((2,0),'cos','sanjiao'),
            ((2,1),'atan','sanjiao'),
            ((2,2),'acos','sanjiao'),
            ((2,3),'相反数','fan'),
            ((2,4),'lg','duishu'),
            ((3,0),'π','number'),
            ((3,1),'7','number'),
            ((3,2),'8','number'),
            ((3,3),'9','number'),
            ((3,4),'/','yunsuan'),
            ((4,0),'e','number'),
            ((4,1),'4','number'),
            ((4,2),'5','number'),
            ((4,3),'6','number'),
            ((4,4),'*','yunsuan'),
            ((5,0),'%','precent'),
            ((5,1),'1','number'),
            ((5,2),'2','number'),
            ((5,3),'3','number'),
            ((5,4),'-','yunsuan'),
            ((6,0),'1/x','daoshu'),
            ((6,1),'0','number'),
            ((6,2),'.','yunsuan'),
            ((6,3),'=','yunsuan'),
            ((6,4),'+','yunsuan'),
            ((7,0),'(','yunsuan'),
            ((7,1),')','yunsuan'),
        ]
        for pos,label,btntype in buttons:
            if label:
                btn=wx.Button(panel,label=label,size=(60,50))
                btn.SetFont(wx.Font(14, wx.FONTFAMILY_DEFAULT,wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
                if btntype=='yunsuan':
                    btn.SetBackgroundColour(wx.Colour(255,149,0))
                    btn.SetForegroundColour(wx.BLACK)
                elif btntype=='number':
                    btn.SetBackgroundColour(wx.Colour(51,51,51))
                    btn.SetForegroundColour(wx.WHITE)
                else:
                    btn.SetBackgroundColour(wx.Colour(255,130,171))
                    btn.SetForegroundColour(wx.BLACK)
                btn.Bind(wx.EVT_BUTTON,lambda event,l=label,t=btntype:self.buttonclick(l,t))
                button_sizer.Add(btn,pos=pos,flag=wx.EXPAND|wx.ALL,border=5)
        self.currentinput='0'
        self.previousinput=''
        main_sizer.Add(button_sizer,proportion=1,flag=wx.EXPAND|wx.ALL,border=5)
        panel.SetSizer(main_sizer)
            

    def buttonclick(self,label,btntype):
                if btntype=='number':
                    self.handnumber(label)
                elif btntype=='yunsuan':
                    self.handyunsuan(label)
                elif btntype=='sanjiao':
                    self.handsanjiao(label)
                elif btntype=='duishu':
                    self.handduishu(label)
                elif btntype=='yuan':
                    self.handyuan(label)
                elif btntype=='zimu':
                    self.handzimu(label)
                elif btntype=='fan':
                    self.handfan(label)
                elif btntype=='copy':
                    self.handcopy(label)
                elif btntype=='history':
                    self.handhistory(label)
                elif btntype=='tui':
                    self.handtui(label)
                elif btntype=='clear':
                    self.handclear(label)
                elif btntype=='yushu':
                    self.handyushu(label)
                elif btntype=='daoshu':
                    self.handdaoshu(label)
                elif btntype=='precent':
                    self.handprecent(label)
    def handnumber(self,label):
                if label == 'π':
                       label= str(math.pi)
                elif label == 'e':
                        label= str(math.e)
                else:
                        value = label
                if self.currentinput=='0':
                    self.currentinput=label
                else:
                    self.currentinput+=label
                self.screen.SetValue(self.currentinput)
    def handyunsuan(self,label):
                if label=='=':
                    result=eval(self.currentinput)
                    self.screen.SetValue(str(result))
                    self.previousinput=self.currentinput
                    self.currentinput=str(result)
                else:
                    self.currentinput+=label
                    self.screen.SetValue(self.currentinput)
    def handsanjiao(self,label):
                if label=='sin':
                    result=math.sin(math.radians(float(self.currentinput)))
                elif label=='cos':
                    result=math.cos(math.radians(float(self.currentinput)))
                elif label=='tan':
                    result=math.tan(math.radians(float(self.currentinput)))
                elif label=='asin':
                    result=math.degrees(math.asin(float(self.currentinput)))
                elif label=='acos':
                    result=math.degrees(math.acos(float(self.currentinput)))
                elif label=='atan':
                    result=math.degrees(math.atan(float(self.currentinput)))
                elif label=='角度制':
                    result=math.degrees(float(self.currentinput))
                self.screen.SetValue(str(result))
                self.previousinput=self.currentinput
                self.currentinput=str(result)
    def handduishu(self,label):
                if label=='ln':
                    result=math.log(float(self.currentinput))
                elif label=='lg':
                    result=math.log10(float(self.currentinput))
                self.screen.SetValue(str(result))
                self.previousinput=self.currentinput
                self.currentinput=str(result)
    def handfan(self,label):
                if label=='相反数':
                    result=-float(self.currentinput)
                self.screen.SetValue(str(result))
                self.previousinput=self.currentinput
                self.currentinput=str(result)
    def handhistory(self,label):
                pass
    def handyushu(self,label):
                if label=='余数':
                    a=float(self.previousinput)
                    b=float(self.currentinput)
                    result=a%b
                self.screen.SetValue(str(result))
                self.previousinput=self.currentinput
                self.currentinput=str(result)
    def handdaoshu(self,label):
                if label=='1/x':
                    result=1/float(self.currentinput)
                self.screen.SetValue(str(result))
                self.previousinput=self.currentinput
                self.currentinput=str(result)
    def handtui(self,label):
                pass
    def handclear(self,label):
            self.currentinput='0'
            self.previousinput='0'
            self.screen.SetValue(self.currentinput)
    def handcopy(self,label):
                pass
    def handprecent(self,label):
                if label=='%':
                    a=float(self.previousinput)
                    b=float(self.currentinput)
                    result=a*b/100  
                self.screen.SetValue(str(result))
                self.previousinput=self.currentinput
                self.currentinput=str(result)
class JisuanqiApp(wx.App):
    def OnInit(self):
        return True
if __name__=='__main__':
    app=JisuanqiApp()
    frame=JisuanqiFrame()
    frame.Show()
    app.MainLoop()