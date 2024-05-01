from mojo import context
from ele_lib import netlinx_client

# デバイス定義 ------------------------------------------------------------------------------------------
# MU-3300
dvMUSE = context.devices.get("idevice")
dvREL = dvMUSE.relay

# VARIA-100
dvVARIA = context.devices.get("AMX-10001")
dvTP = dvVARIA.port[1]

# NetlinxClient
dvNetlinx = netlinx_client.NetLinxClient("192.168.52.101",6001,"administrator","password")


# イベント定義 ------------------------------------------------------------------------------------------

def ButtonEvent(e):
    ch = int(e.id)

    print("CH: %s" %(ch))

    dvTP.channel[ch] = e.value

    if e.value:
        if ch == 1:
            dvNetlinx.connect()
        elif ch == 2:
            dvNetlinx.disconnect()
        elif ch == 3:
            dvNetlinx.send_string("[REL1 ON]")
        elif ch == 4:
            dvNetlinx.send_string("[REL1 OFF]")

def DataEvent(e):
    datatext = e.arguments["data"].decode("utf-8")

    dvTP.send_command("^TXT-1,0,%s" %datatext)

    if "[REL1 ON]" in datatext:
        dvREL[0].state = True
    elif "[REL1 OFF]" in datatext:
        dvREL[0].state = False


# イベント取得 ------------------------------------------------------------------------------------------
for ch in range(1,5):
    dvTP.button[ch].watch(ButtonEvent)

dvNetlinx.listen(DataEvent)

context.run(globals())
