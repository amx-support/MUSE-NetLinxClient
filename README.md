# MUSEとNetLinxマスターの相互制御の実装

### 機能
MUSEからNetLinxマスターに接続し、相互制御を行います。

### 使用方法

プログラムフォルダに **ele_libフォルダ** をコピーし、メインプログラムから **import** します。
- netlinx_client.py

##### オブジェクト生成

`netlinx = netlinx_client.NetLinxClient(ip,device,user,password)`<br/><br/>
**ip**は接続先NetLinxマスターのIPアドレスを指定<br/>
**device**はNetLinxシステムでのデバイス番号を指定<br/>
**user**はNetLinxマスター接続時のユーザー名を指定<br/>
**password**はNetLinxマスター接続時のパスワードを指定<br/>

##### 接続

`netlinx.connect()`<br/><br/>

指定したデバイス番号でNetLinxマスターへ接続します。<br/><br/>

##### 切断

`netlinx.disconnect()`<br/><br/>

NetLinxマスターから切断します。<br/><br/>

##### 送信

`netlinx.send_string(data)`<br/><br/>

NetLinxマスターへ指定したデバイス経由でSEND_STRINGを行います。<br/>
NetLinxシステム側では指定したデバイスの**DATA_EVENT - STRING:**でデータ取得します。<br/>
**data**は送信するデータを指定<br/><br/>

##### 受信

`netlinx.listen(func)`<br/><br/>

データ受信時のコールバック関数を指定します。<br/>
**func**はデータ受信時に行う処理が記述されている関数を指定

