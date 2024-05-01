#--------------------------------------------------------------------------------------------------
#
# netlinxClient service 簡易操作用モジュール v1.0
# 
# Program: KEI
#
#--------------------------------------------------------------------------------------------------

from mojo import context

# netlinxClient service用クラス -----------------------------------------------------------------------
class NetLinxClient:
    # 初期化
    def __init__(self,ip,dev,user,password):
        self.ip = ip
        self.dev = dev
        self.user = user
        self.password = password
        self.online = False
        self.dvNetlinx = context.services.get("netlinxClient")
        self.dvNetlinx.online.listen(self.Online)
        self.dvNetlinx.offline.listen(self.Offline)

    # NetLinxへ接続
    def connect(self):
        self.dvNetlinx.connect(self.ip,self.dev,self.user,self.password)
    
    # NetLinxから切断
    def disconnect(self):
        self.dvNetlinx.disconnect()
    
    # SEND_STRINGを送信
    def send_string(self,string):
        if self.online:
            self.dvNetlinx.send_string(string)
    
    # Onlineイベント取得用コールバック関数
    def Online(self,e):
        self.online = True
    
    # Offlineイベント取得用のコールバック関数
    def Offline(self,e):
        self.online = False
    
    # データ受信検知用のコールバック関数
    def listen(self,callback):
        self.dvNetlinx.string.listen(callback)