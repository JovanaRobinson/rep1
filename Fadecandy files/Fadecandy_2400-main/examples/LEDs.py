

import opc
import time
from time import sleep

leds = [(20,20,20)]*360

client = opc.Client('localhost:7890')
client.put_pixels(leds)
client.put_pixels(leds)
            


black = [ (0,0,0) ] * 360 #used in right and wrong animations


def white():
    for led in range(0,360):
        leds[led] = (20,20,20)
        client.put_pixels(leds)

#all functions below are for the hello animation
        
def first():
    leds[59] = (0,255,255)
    leds[119] = (0,255,255)
    leds[179] = (0,255,255)
    leds[239] = (0,255,255)
    leds[299] = (0,255,255)
    leds[359] = (0,255,255)
    client.put_pixels(leds)


def second():
    leds[58] = (0,255,255)
    leds[118] = (0,255,255)
    leds[178] = (0,255,255)
    leds[238] = (0,255,255)
    leds[298] = (0,255,255)
    leds[358] = (0,255,255)
    leds[239] = (0,255,255)
    client.put_pixels(leds)
    
def third():
    leds[57] = (0,255,255)
    leds[117] = (0,255,255)
    leds[177] = (0,255,255)
    leds[237] = (0,255,255)
    leds[297] = (0,255,255)
    leds[357] = (0,255,255)
    leds[238] = (0,255,255)
    leds[239] = (0,255,255)
    client.put_pixels(leds)

def fourth():
    leds[56] = (0,255,255)
    leds[116] = (0,255,255)
    leds[176] = (0,255,255)
    leds[236] = (0,255,255)
    leds[296] = (0,255,255)
    leds[356] = (0,255,255)
    leds[237] = (0,255,255)
    leds[238] = (0,255,255)
    leds[239] = (0,255,255)
    client.put_pixels(leds)

def fifth():
    leds[55] = (0,255,255)
    leds[115] = (0,255,255)
    leds[175] = (0,255,255)
    leds[235] = (0,255,255)
    leds[295] = (0,255,255)
    leds[355] = (0,255,255)
    leds[236] = (0,255,255)
    leds[237] = (0,255,255)
    leds[238] = (0,255,255)
    leds[239] = (0,255,255)
    client.put_pixels(leds)

def sixth():
    leds[54] = (0,255,255)
    leds[114] = (0,255,255)
    leds[174] = (0,255,255)
    leds[234] = (0,255,255)
    leds[294] = (0,255,255)
    leds[354] = (0,255,255)
    leds[235] = (0,255,255)
    leds[236] = (0,255,255)
    leds[237] = (0,255,255)
    leds[238] = (0,255,255)
    leds[59] = (0,255,255)
    leds[119] = (0,255,255)
    leds[179] = (0,255,255)
    leds[239] = (0,255,255)
    leds[299] = (0,255,255)
    leds[359] = (0,255,255)
    client.put_pixels(leds)

def seventh():
    leds[53] = (0,255,255)
    leds[113] = (0,255,255)
    leds[173] = (0,255,255)
    leds[233] = (0,255,255)
    leds[293] = (0,255,255)
    leds[353] = (0,255,255)
    leds[234] = (0,255,255)
    leds[235] = (0,255,255)
    leds[236] = (0,255,255)
    leds[237] = (0,255,255)
    leds[238] = (0,255,255)
    leds[58] = (0,255,255)
    leds[118] = (0,255,255)
    leds[178] = (0,255,255)
    leds[238] = (0,255,255)
    leds[298] = (0,255,255)
    leds[358] = (0,255,255)
    client.put_pixels(leds)

def eighth(): #maybe change to another colour from here
    leds[52] = (0,255,0)
    leds[112] = (0,255,0)
    leds[172] = (0,255,0)
    leds[232] = (0,255,0)
    leds[292] = (0,255,0)
    leds[352] = (0,255,0)
    leds[233] = (0,255,0)
    leds[234] = (0,255,0)
    leds[235] = (0,255,0)
    leds[236] = (0,255,0)
    leds[237] = (0,255,0)
    leds[57] = (0,255,0)
    leds[117] = (0,255,0)
    leds[177] = (0,255,0)
    leds[237] = (0,255,0)
    leds[297] = (0,255,0)
    leds[357] = (0,255,0)
    leds[59] = (0,255,0)
    leds[119] = (0,255,0)
    leds[179] = (0,255,0)
    leds[239] = (0,255,0)
    leds[299] = (0,255,0)
    leds[359] = (0,255,0)
    client.put_pixels(leds)

def ninth():
    leds[51] = (0,255,0)
    leds[111] = (0,255,0)
    leds[171] = (0,255,0)
    leds[231] = (0,255,0)
    leds[291] = (0,255,0)
    leds[351] = (0,255,0)
    leds[232] = (0,255,0)
    leds[233] = (0,255,0)
    leds[234] = (0,255,0)
    leds[235] = (0,255,0)
    leds[236] = (0,255,0)
    leds[56] = (0,255,0)
    leds[116] = (0,255,0)
    leds[176] = (0,255,0)
    leds[236] = (0,255,0)
    leds[296] = (0,255,0)
    leds[356] = (0,255,0)
    leds[58] = (0,255,0)
    leds[118] = (0,255,0)
    leds[178] = (0,255,0)
    leds[238] = (0,255,0)
    leds[298] = (0,255,0)
    leds[358] = (0,255,0)
    leds[239] = (0,255,0)
    leds[59] = (0,255,0)
    leds[359] = (0,255,0)
    client.put_pixels(leds)

def tenth():
    leds[50] = (0,255,0)
    leds[110] = (0,255,0)
    leds[170] = (0,255,0)
    leds[230] = (0,255,0)
    leds[290] = (0,255,0)
    leds[350] = (0,255,0)
    leds[231] = (0,255,0)
    leds[232] = (0,255,0)
    leds[233] = (0,255,0)
    leds[234] = (0,255,0)
    leds[235] = (0,255,0)
    leds[55] = (0,255,0)
    leds[115] = (0,255,0)
    leds[175] = (0,255,0)
    leds[235] = (0,255,0)
    leds[295] = (0,255,0)
    leds[355] = (0,255,0)
    leds[57] = (0,255,0)
    leds[117] = (0,255,0)
    leds[177] = (0,255,0)
    leds[237] = (0,255,0)
    leds[297] = (0,255,0)
    leds[357] = (0,255,0)
    leds[238] = (0,255,0)
    leds[58] = (0,255,0)
    leds[358] = (0,255,0)
    leds[239] = (0,255,0)
    leds[59] = (0,255,0)
    leds[359] = (0,255,0)
    client.put_pixels(leds)

def eleven():
    leds[49] = (0,255,0)
    leds[109] = (0,255,0)
    leds[169] = (0,255,0)
    leds[229] = (0,255,0)
    leds[289] = (0,255,0)
    leds[349] = (0,255,0)
    leds[230] = (0,255,0)
    leds[231] = (0,255,0)
    leds[232] = (0,255,0)
    leds[233] = (0,255,0)
    leds[234] = (0,255,0)
    leds[54] = (0,255,0)
    leds[114] = (0,255,0)
    leds[174] = (0,255,0)
    leds[234] = (0,255,0)
    leds[294] = (0,255,0)
    leds[354] = (0,255,0)
    leds[56] = (0,255,0)
    leds[116] = (0,255,0)
    leds[176] = (0,255,0)
    leds[236] = (0,255,0)
    leds[296] = (0,255,0)
    leds[356] = (0,255,0)
    leds[237] = (0,255,0)
    leds[57] = (0,255,0)
    leds[357] = (0,255,0)
    leds[238] = (0,255,0)
    leds[58] = (0,255,0)
    leds[358] = (0,255,0)
    leds[239] = (0,255,0)
    leds[59] = (0,255,0)
    leds[359] = (0,255,0)
    client.put_pixels(leds)

def twelve():
    leds[48] = (0,255,0)
    leds[108] = (0,255,0)
    leds[168] = (0,255,0)
    leds[228] = (0,255,0)
    leds[288] = (0,255,0)
    leds[348] = (0,255,0)
    leds[229] = (0,255,0)
    leds[230] = (0,255,0)
    leds[231] = (0,255,0)
    leds[232] = (0,255,0)
    leds[233] = (0,255,0)
    leds[53] = (0,255,0)
    leds[113] = (0,255,0)
    leds[173] = (0,255,0)
    leds[233] = (0,255,0)
    leds[293] = (0,255,0)
    leds[353] = (0,255,0)
    leds[55] = (0,255,0)
    leds[115] = (0,255,0)
    leds[175] = (0,255,0)
    leds[235] = (0,255,0)
    leds[295] = (0,255,0)
    leds[355] = (0,255,0)
    leds[236] = (0,255,0)
    leds[56] = (0,255,0)
    leds[356] = (0,255,0)
    leds[237] = (0,255,0)
    leds[57] = (0,255,0)
    leds[357] = (0,255,0)
    leds[238] = (0,255,0)
    leds[58] = (0,255,0)
    leds[358] = (0,255,0)
    leds[239] =(0,255,0)
    leds[59] = (0,255,0)
    leds[359] = (0,255,0)
    client.put_pixels(leds)

def thirteen():
    leds[47] = (0,255,0)
    leds[107] = (0,255,0)
    leds[167] = (0,255,0)
    leds[227] = (0,255,0)
    leds[287] = (0,255,0)
    leds[347] = (0,255,0)
    leds[228] = (0,255,0)
    leds[229] = (0,255,0)
    leds[230] = (0,255,0)
    leds[231] = (0,255,0)
    leds[232] = (0,255,0)
    leds[52] = (0,255,0)
    leds[112] = (0,255,0)
    leds[172] = (0,255,0)
    leds[232] = (0,255,0)
    leds[292] = (0,255,0)
    leds[352] = (0,255,0)
    leds[54] = (0,255,0)
    leds[114] = (0,255,0)
    leds[174] = (0,255,0)
    leds[234] = (0,255,0)
    leds[294] = (0,255,0)
    leds[354] = (0,255,0)
    leds[235] = (0,255,0)
    leds[55] = (0,255,0)
    leds[355] = (0,255,0)
    leds[236] = (0,255,0)
    leds[56] = (0,255,0)
    leds[356] = (0,255,0)
    leds[237] = (0,255,0)
    leds[57] = (0,255,0)
    leds[357] = (0,255,0)
    leds[238] = (0,255,0)
    leds[58] = (0,255,0)
    leds[358] = (0,255,0)
    client.put_pixels(leds)

def fourteen():
    leds[46] = (255,0,0)
    leds[106] = (255,0,0)
    leds[166] = (255,0,0)
    leds[226] = (255,0,0)
    leds[286] = (255,0,0)
    leds[346] = (255,0,0)
    leds[227] = (255,0,0)
    leds[228] = (255,0,0)
    leds[229] = (255,0,0)
    leds[230] = (255,0,0)
    leds[231] = (255,0,0)
    leds[51] = (255,0,0)
    leds[111] = (255,0,0)
    leds[171] = (255,0,0)
    leds[231] = (255,0,0)
    leds[291] = (255,0,0)
    leds[351] = (255,0,0)
    leds[53] = (255,0,0)
    leds[113] = (255,0,0)
    leds[173] = (255,0,0)
    leds[233] = (255,0,0)
    leds[293] = (255,0,0)
    leds[353] = (255,0,0)
    leds[234] = (255,0,0)
    leds[54] = (255,0,0)
    leds[354] = (255,0,0)
    leds[235] = (255,0,0)
    leds[55] = (255,0,0)
    leds[355] = (255,0,0)
    leds[236] = (255,0,0)
    leds[56] = (255,0,0)
    leds[356] = (255,0,0)
    leds[237] = (255,0,0)
    leds[57] = (255,0,0)
    leds[357] = (255,0,0)
    leds[59] = (255,0,0)
    leds[119] = (255,0,0)
    leds[179] = (255,0,0)
    leds[239] = (255,0,0)
    leds[299] = (255,0,0)
    leds[359] = (255,0,0)
    client.put_pixels(leds)

def fifteen():
    leds[45] = (255,0,0)
    leds[105] = (255,0,0)
    leds[165] = (255,0,0)
    leds[225] = (255,0,0)
    leds[285] = (255,0,0)
    leds[345] = (255,0,0)
    leds[226] = (255,0,0)
    leds[227] = (255,0,0)
    leds[228] = (255,0,0)
    leds[229] = (255,0,0)
    leds[230] = (255,0,0)
    leds[50] = (255,0,0)
    leds[110] = (255,0,0)
    leds[170] = (255,0,0)
    leds[230] = (255,0,0)
    leds[290] = (255,0,0)
    leds[350] = (255,0,0)
    leds[52] = (255,0,0)
    leds[112] = (255,0,0)
    leds[172] = (255,0,0)
    leds[232] = (255,0,0)
    leds[292] = (255,0,0)
    leds[352] = (255,0,0)
    leds[233] = (255,0,0)
    leds[53] = (255,0,0)
    leds[353] = (255,0,0)
    leds[234] = (255,0,0)
    leds[54] = (255,0,0)
    leds[354] = (255,0,0)
    leds[235] = (255,0,0)
    leds[55] = (255,0,0)
    leds[355] = (255,0,0)
    leds[236] = (255,0,0)
    leds[56] = (255,0,0)
    leds[356] = (255,0,0)
    leds[58] = (255,0,0)
    leds[118] = (255,0,0)
    leds[178] = (255,0,0)
    leds[238] = (255,0,0)
    leds[298] = (255,0,0)
    leds[358] = (255,0,0)
    leds[359] = (255,0,0)
    client.put_pixels(leds)

def sixteen():
    leds[44] = (255,0,0)
    leds[104] = (255,0,0)
    leds[164] = (255,0,0)
    leds[224] = (255,0,0)
    leds[284] = (255,0,0)
    leds[344] = (255,0,0)
    leds[225] = (255,0,0)
    leds[226] = (255,0,0)
    leds[227] = (255,0,0)
    leds[228] = (255,0,0)
    leds[229] = (255,0,0)
    leds[49] = (255,0,0)
    leds[109] = (255,0,0)
    leds[169] = (255,0,0)
    leds[229] = (255,0,0)
    leds[289] = (255,0,0)
    leds[349] = (255,0,0)
    leds[51] = (255,0,0)
    leds[111] = (255,0,0)
    leds[171] = (255,0,0)
    leds[231] = (255,0,0)
    leds[291] = (255,0,0)
    leds[351] = (255,0,0)
    leds[232] = (255,0,0)
    leds[52] = (255,0,0)
    leds[352] = (255,0,0)
    leds[233] = (255,0,0)
    leds[53] = (255,0,0)
    leds[353] = (255,0,0)
    leds[234] = (255,0,0)
    leds[54] = (255,0,0)
    leds[354] = (255,0,0)
    leds[235] = (255,0,0)
    leds[55] = (255,0,0)
    leds[355] = (255,0,0)
    leds[57] = (255,0,0)
    leds[117] = (255,0,0)
    leds[177] = (255,0,0)
    leds[237] = (255,0,0)
    leds[297] = (255,0,0)
    leds[357] = (255,0,0)
    leds[358] = (255,0,0)
    leds[359] = (255,0,0)
    client.put_pixels(leds)

def seventeen():
    leds[43] = (255,0,0)
    leds[103] = (255,0,0)
    leds[163] = (255,0,0)
    leds[223] = (255,0,0)
    leds[283] = (255,0,0)
    leds[343] = (255,0,0)
    leds[224] = (255,0,0)
    leds[225] = (255,0,0)
    leds[226] = (255,0,0)
    leds[227] = (255,0,0)
    leds[228] = (255,0,0)
    leds[48] = (255,0,0)
    leds[108] = (255,0,0)
    leds[168] = (255,0,0)
    leds[228] = (255,0,0)
    leds[288] = (255,0,0)
    leds[348] = (255,0,0)
    leds[50] = (255,0,0)
    leds[110] = (255,0,0)
    leds[170] = (255,0,0)
    leds[230] = (255,0,0)
    leds[290] = (255,0,0)
    leds[350] = (255,0,0)
    leds[231] = (255,0,0)
    leds[51] = (255,0,0)
    leds[351] = (255,0,0)
    leds[232] = (255,0,0)
    leds[52] = (255,0,0)
    leds[352] = (255,0,0)
    leds[233] = (255,0,0)
    leds[53] = (255,0,0)
    leds[353] = (255,0,0)
    leds[234] = (255,0,0)
    leds[54] = (255,0,0)
    leds[354] = (255,0,0)
    leds[56] = (255,0,0)
    leds[116] = (255,0,0)
    leds[176] = (255,0,0)
    leds[236] = (255,0,0)
    leds[296] = (255,0,0)
    leds[356] = (255,0,0)
    leds[357] = (255,0,0)
    leds[358] = (255,0,0)
    leds[359] = (255,0,0)
    client.put_pixels(leds)

def eighteen():
    leds[42] = (255,0,0)
    leds[102] = (255,0,0)
    leds[162] = (255,0,0)
    leds[222] = (255,0,0)
    leds[282] = (255,0,0)
    leds[342] = (255,0,0)
    leds[223] = (255,0,0)
    leds[224] = (255,0,0)
    leds[225] = (255,0,0)
    leds[226] = (255,0,0)
    leds[227] = (255,0,0)
    leds[47] = (255,0,0)
    leds[107] = (255,0,0)
    leds[167] = (255,0,0)
    leds[227] = (255,0,0)
    leds[287] = (255,0,0)
    leds[347] = (255,0,0)
    leds[49] = (255,0,0)
    leds[109] = (255,0,0)
    leds[169] = (255,0,0)
    leds[229] = (255,0,0)
    leds[289] = (255,0,0)
    leds[349] = (255,0,0)
    leds[230] = (255,0,0)
    leds[50] = (255,0,0)
    leds[350] = (255,0,0)
    leds[231] = (255,0,0)
    leds[51] = (255,0,0)
    leds[351] = (255,0,0)
    leds[232] = (255,0,0)
    leds[52] = (255,0,0)
    leds[352] = (255,0,0)
    leds[233] = (255,0,0)
    leds[53] = (255,0,0)
    leds[353] = (255,0,0)
    leds[55] = (255,0,0)
    leds[115] = (255,0,0)
    leds[175] = (255,0,0)
    leds[235] = (255,0,0)
    leds[295] = (255,0,0)
    leds[355] = (255,0,0)
    leds[356] = (255,0,0)
    leds[357] = (255,0,0)
    leds[358] = (255,0,0)
    leds[359] = (255,0,0)
    client.put_pixels(leds)

def nineteen(): #Where first L ends
    leds[41] = (255,0,0)
    leds[101] = (255,0,0)
    leds[161] = (255,0,0)
    leds[221] = (255,0,0)
    leds[281] = (255,0,0)
    leds[341] = (255,0,0)
    leds[222] = (255,0,0)
    leds[223] = (255,0,0)
    leds[224] = (255,0,0)
    leds[225] = (255,0,0)
    leds[226] = (255,0,0)
    leds[46] = (255,0,0)
    leds[106] = (255,0,0)
    leds[166] = (255,0,0)
    leds[226] = (255,0,0)
    leds[286] = (255,0,0)
    leds[346] = (255,0,0)
    leds[48] = (255,0,0)
    leds[108] = (255,0,0)
    leds[168] = (255,0,0)
    leds[228] = (255,0,0)
    leds[288] = (255,0,0)
    leds[348] = (255,0,0)
    leds[229] = (255,0,0)
    leds[49] = (255,0,0)
    leds[349] = (255,0,0)
    leds[230] = (255,0,0)
    leds[50] = (255,0,0)
    leds[350] = (255,0,0)
    leds[231] = (255,0,0)
    leds[51] = (255,0,0)
    leds[351] = (255,0,0)
    leds[232] = (255,0,0)
    leds[52] = (255,0,0)
    leds[352] = (255,0,0)
    leds[54] = (255,0,0)
    leds[114] = (255,0,0)
    leds[174] = (255,0,0)
    leds[234] = (255,0,0)
    leds[294] = (255,0,0)
    leds[354] = (255,0,0)
    leds[355] = (255,0,0)
    leds[356] = (255,0,0)
    leds[357] = (255,0,0)
    leds[358] = (255,0,0)
    
    client.put_pixels(leds)

def twenty():
    leds[40] = (255,0,255)
    leds[100] = (255,0,255)
    leds[160] = (255,0,255)
    leds[220] = (255,0,255)
    leds[280] = (255,0,255)
    leds[340] = (255,0,255)
    leds[221] = (255,0,255)
    leds[222] = (255,0,255)
    leds[223] = (255,0,255)
    leds[224] = (255,0,255)
    leds[225] = (255,0,255)
    leds[45] = (255,0,255)
    leds[105] = (255,0,255)
    leds[165] = (255,0,255)
    leds[225] = (255,0,255)
    leds[285] = (255,0,255)
    leds[345] = (255,0,255)
    leds[47] = (255,0,255)
    leds[107] = (255,0,255)
    leds[167] = (255,0,255)
    leds[227] = (255,0,255)
    leds[287] = (255,0,255)
    leds[347] = (255,0,255)
    leds[228] = (255,0,255)
    leds[48] = (255,0,255)
    leds[348] = (255,0,255)
    leds[229] = (255,0,255)
    leds[49] = (255,0,255)
    leds[349] = (255,0,255)
    leds[230] = (255,0,255)
    leds[50] = (255,0,255)
    leds[350] = (255,0,255)
    leds[231] = (255,0,255)
    leds[51] = (255,0,255)
    leds[351] = (255,0,255)
    leds[53] = (255,0,255)
    leds[113] = (255,0,255)
    leds[173] = (255,0,255)
    leds[233] = (255,0,255)
    leds[293] = (255,0,255)
    leds[353] = (255,0,255)
    leds[354] = (255,0,255)
    leds[355] = (255,0,255)
    leds[356] = (255,0,255)
    leds[357] = (255,0,255)
    leds[59] = (255,0,255)
    leds[119] = (255,0,255)
    leds[179] = (255,0,255)
    leds[239] = (255,0,255)
    leds[299] = (255,0,255)
    leds[359] = (255,0,255)
    client.put_pixels(leds)

def twentyOne():
    leds[39] = (255,0,255)
    leds[99] = (255,0,255)
    leds[159] = (255,0,255)
    leds[219] = (255,0,255)
    leds[279] = (255,0,255)
    leds[339] = (255,0,255)
    leds[220] = (255,0,255)
    leds[221] = (255,0,255)
    leds[222] = (255,0,255)
    leds[223] = (255,0,255)
    leds[224] = (255,0,255)
    leds[44] = (255,0,255)
    leds[104] = (255,0,255)
    leds[164] = (255,0,255)
    leds[224] = (255,0,255)
    leds[284] = (255,0,255)
    leds[344] = (255,0,255)
    leds[46] = (255,0,255)
    leds[106] = (255,0,255)
    leds[166] = (255,0,255)
    leds[226] = (255,0,255)
    leds[286] = (255,0,255)
    leds[346] = (255,0,255)
    leds[227] = (255,0,255)
    leds[47] = (255,0,255)
    leds[347] = (255,0,255)
    leds[228] = (255,0,255)
    leds[48] = (255,0,255)
    leds[348] = (255,0,255)
    leds[229] = (255,0,255)
    leds[49] = (255,0,255)
    leds[349] = (255,0,255)
    leds[230] = (255,0,255)
    leds[50] = (255,0,255)
    leds[350] = (255,0,255)
    leds[52] = (255,0,255)
    leds[112] = (255,0,255)
    leds[172] = (255,0,255)
    leds[232] = (255,0,255)
    leds[292] = (255,0,255)
    leds[352] = (255,0,255)
    leds[353] = (255,0,255)
    leds[354] = (255,0,255)
    leds[355] = (255,0,255)
    leds[356] = (255,0,255)
    leds[58] = (255,0,255)
    leds[118] = (255,0,255)
    leds[178] = (255,0,255)
    leds[238] = (255,0,255)
    leds[298] = (255,0,255)
    leds[358] = (255,0,255)
    leds[359] = (255,0,255)
    client.put_pixels(leds)

def twentyTwo():
    leds[38] = (255,0,255)
    leds[98] = (255,0,255)
    leds[158] = (255,0,255)
    leds[218] = (255,0,255)
    leds[278] = (255,0,255)
    leds[338] = (255,0,255)
    leds[219] = (255,0,255)
    leds[220] = (255,0,255)
    leds[221] = (255,0,255)
    leds[222] = (255,0,255)
    leds[223] = (255,0,255)
    leds[43] = (255,0,255)
    leds[103] = (255,0,255)
    leds[163] = (255,0,255)
    leds[223] = (255,0,255)
    leds[283] = (255,0,255)
    leds[343] = (255,0,255)
    leds[45] = (255,0,255)
    leds[105] = (255,0,255)
    leds[165] = (255,0,255)
    leds[225] = (255,0,255)
    leds[285] = (255,0,255)
    leds[345] = (255,0,255)
    leds[226] = (255,0,255)
    leds[46] = (255,0,255)
    leds[346] = (255,0,255)
    leds[227] = (255,0,255)
    leds[47] = (255,0,255)
    leds[347] = (255,0,255)
    leds[228] = (255,0,255)
    leds[48] = (255,0,255)
    leds[348] = (255,0,255)
    leds[229] = (255,0,255)
    leds[49] = (255,0,255)
    leds[349] = (255,0,255)
    leds[51] = (255,0,255)
    leds[111] = (255,0,255)
    leds[171] = (255,0,255)
    leds[231] = (255,0,255)
    leds[291] = (255,0,255)
    leds[351] = (255,0,255)
    leds[352] = (255,0,255)
    leds[353] = (255,0,255)
    leds[354] = (255,0,255)
    leds[355] = (255,0,255)
    leds[57] = (255,0,255)
    leds[117] = (255,0,255)
    leds[177] = (255,0,255)
    leds[237] = (255,0,255)
    leds[297] = (255,0,255)
    leds[357] = (255,0,255)
    leds[358] = (255,0,255)
    leds[359] = (255,0,255)
    client.put_pixels(leds)

def twentyThree():
    leds[37] = (255,0,255)
    leds[97] = (255,0,255)
    leds[157] = (255,0,255)
    leds[217] = (255,0,255)
    leds[277] = (255,0,255)
    leds[337] = (255,0,255)
    leds[218] = (255,0,255)
    leds[219] = (255,0,255)
    leds[220] = (255,0,255)
    leds[221] = (255,0,255)
    leds[222] = (255,0,255)
    leds[42] = (255,0,255)
    leds[102] = (255,0,255)
    leds[162] = (255,0,255)
    leds[222] = (255,0,255)
    leds[282] = (255,0,255)
    leds[342] = (255,0,255)
    leds[44] = (255,0,255)
    leds[104] = (255,0,255)
    leds[164] = (255,0,255)
    leds[224] = (255,0,255)
    leds[284] = (255,0,255)
    leds[344] = (255,0,255)
    leds[225] = (255,0,255)
    leds[45] = (255,0,255)
    leds[345] = (255,0,255)
    leds[226] = (255,0,255)
    leds[46] = (255,0,255)
    leds[346] = (255,0,255)
    leds[227] = (255,0,255)
    leds[47] = (255,0,255)
    leds[347] = (255,0,255)
    leds[228] = (255,0,255)
    leds[48] = (255,0,255)
    leds[348] = (255,0,255)
    leds[50] = (255,0,255)
    leds[110] = (255,0,255)
    leds[170] = (255,0,255)
    leds[230] = (255,0,255)
    leds[290] = (255,0,255)
    leds[350] = (255,0,255)
    leds[351] = (255,0,255)
    leds[352] = (255,0,255)
    leds[353] = (255,0,255)
    leds[354] = (255,0,255)
    leds[56] = (255,0,255)
    leds[116] = (255,0,255)
    leds[176] = (255,0,255)
    leds[236] = (255,0,255)
    leds[296] = (255,0,255)
    leds[356] = (255,0,255)
    leds[357] = (255,0,255)
    leds[358] = (255,0,255)
    leds[359] = (255,0,255)
    client.put_pixels(leds)

def twentyFour():
    leds[36] = (255,0,255)
    leds[96] = (255,0,255)
    leds[156] = (255,0,255)
    leds[216] = (255,0,255)
    leds[276] = (255,0,255)
    leds[336] = (255,0,255)
    leds[217] = (255,0,255)
    leds[218] = (255,0,255)
    leds[219] = (255,0,255)
    leds[220] = (255,0,255)
    leds[221] = (255,0,255)
    leds[41] = (255,0,255)
    leds[101] = (255,0,255)
    leds[161] = (255,0,255)
    leds[221] = (255,0,255)
    leds[281] = (255,0,255)
    leds[341] = (255,0,255)
    leds[43] = (255,0,255)
    leds[103] = (255,0,255)
    leds[163] = (255,0,255)
    leds[223] = (255,0,255)
    leds[283] = (255,0,255)
    leds[343] = (255,0,255)
    leds[224] = (255,0,255)
    leds[44] = (255,0,255)
    leds[344] = (255,0,255)
    leds[225] = (255,0,255)
    leds[45] = (255,0,255)
    leds[345] = (255,0,255)
    leds[226] = (255,0,255)
    leds[46] = (255,0,255)
    leds[346] = (255,0,255)
    leds[227] = (255,0,255)
    leds[47] = (255,0,255)
    leds[347] = (255,0,255)
    leds[49] = (255,0,255)
    leds[109] = (255,0,255)
    leds[169] = (255,0,255)
    leds[229] = (255,0,255)
    leds[289] = (255,0,255)
    leds[349] = (255,0,255)
    leds[350] = (255,0,255)
    leds[351] = (255,0,255)
    leds[352] = (255,0,255)
    leds[353] = (255,0,255)
    leds[55] = (255,0,255)
    leds[115] = (255,0,255)
    leds[175] = (255,0,255)
    leds[235] = (255,0,255)
    leds[295] = (255,0,255)
    leds[355] = (255,0,255)
    leds[356] = (255,0,255)
    leds[357] = (255,0,255)
    leds[358] = (255,0,255)
    leds[359] = (255,0,255)
    client.put_pixels(leds)

def twentyFive(): #Where 2nd L ends
    leds[35] = (255,0,255)
    leds[95] = (255,0,255)
    leds[155] = (255,0,255)
    leds[215] = (255,0,255)
    leds[275] = (255,0,255)
    leds[335] = (255,0,255)
    leds[216] = (255,0,255)
    leds[217] = (255,0,255)
    leds[218] = (255,0,255)
    leds[219] = (255,0,255)
    leds[220] = (255,0,255)
    leds[40] = (255,0,255)
    leds[100] = (255,0,255)
    leds[160] = (255,0,255)
    leds[220] = (255,0,255)
    leds[280] = (255,0,255)
    leds[340] = (255,0,255)
    leds[42] = (255,0,255)
    leds[102] = (255,0,255)
    leds[162] = (255,0,255)
    leds[222] = (255,0,255)
    leds[282] = (255,0,255)
    leds[342] = (255,0,255)
    leds[223] = (255,0,255)
    leds[43] = (255,0,255)
    leds[343] = (255,0,255)
    leds[224] = (255,0,255)
    leds[44] = (255,0,255)
    leds[344] = (255,0,255)
    leds[225] = (255,0,255)
    leds[45] = (255,0,255)
    leds[345] = (255,0,255)
    leds[226] = (255,0,255)
    leds[46] = (255,0,255)
    leds[346] = (255,0,255)
    leds[48] = (255,0,255)
    leds[108] = (255,0,255)
    leds[168] = (255,0,255)
    leds[228] = (255,0,255)
    leds[288] = (255,0,255)
    leds[348] = (255,0,255)
    leds[349] = (255,0,255)
    leds[350] = (255,0,255)
    leds[351] = (255,0,255)
    leds[352] = (255,0,255)
    leds[54] = (255,0,255)
    leds[114] = (255,0,255)
    leds[174] = (255,0,255)
    leds[234] = (255,0,255)
    leds[294] = (255,0,255)
    leds[354] = (255,0,255)
    leds[355] = (255,0,255)
    leds[356] = (255,0,255)
    leds[357] = (255,0,255)
    leds[358] = (255,0,255)
    client.put_pixels(leds)

def twentySix():
    leds[34] = (255,204,153)
    leds[94] = (255,204,153)
    leds[154] = (255,204,153)
    leds[214] = (255,204,153)
    leds[274] = (255,204,153)
    leds[334] = (255,204,153)
    leds[215] = (255,204,153)
    leds[216] = (255,204,153)
    leds[217] = (255,204,153)
    leds[218] = (255,204,153)
    leds[219] = (255,204,153)
    leds[39] = (255,204,153)
    leds[99] = (255,204,153)
    leds[159] = (255,204,153)
    leds[219] = (255,204,153)
    leds[279] = (255,204,153)
    leds[339] = (255,204,153)
    leds[41] = (255,204,153)
    leds[101] = (255,204,153)
    leds[161] = (255,204,153)
    leds[221] = (255,204,153)
    leds[281] = (255,204,153)
    leds[341] = (255,204,153)
    leds[222] = (255,204,153)
    leds[42] = (255,204,153)
    leds[342] = (255,204,153)
    leds[223] = (255,204,153)
    leds[43] = (255,204,153)
    leds[343] = (255,204,153)
    leds[224] = (255,204,153)
    leds[44] = (255,204,153)
    leds[344] = (255,204,153)
    leds[225] = (255,204,153)
    leds[45] = (255,204,153)
    leds[345] = (255,204,153)
    leds[47] = (255,204,153)
    leds[107] = (255,204,153)
    leds[167] = (255,204,153)
    leds[227] = (255,204,153)
    leds[287] = (255,204,153)
    leds[347] = (255,204,153)
    leds[348] = (255,204,153)
    leds[349] = (255,204,153)
    leds[350] = (255,204,153)
    leds[351] = (255,204,153)
    leds[53] = (255,204,153)
    leds[113] = (255,204,153)
    leds[173] = (255,204,153)
    leds[233] = (255,204,153)
    leds[293] = (255,204,153)
    leds[353] = (255,204,153)
    leds[354] = (255,204,153)
    leds[355] = (255,204,153)
    leds[356] = (255,204,153)
    leds[357] = (255,204,153)
    leds[59] = (255,204,153)
    leds[119] = (255,204,153)
    leds[179] = (255,204,153)
    leds[239] = (255,204,153)
    leds[299] = (255,204,153)
    leds[359] = (255,204,153)
    client.put_pixels(leds)

def twentySeven():
    leds[33] = (255,204,153)
    leds[93] = (255,204,153)
    leds[153] = (255,204,153)
    leds[213] = (255,204,153)
    leds[273] = (255,204,153)
    leds[333] = (255,204,153)
    leds[214] = (255,204,153)
    leds[215] = (255,204,153)
    leds[216] = (255,204,153)
    leds[217] = (255,204,153)
    leds[218] = (255,204,153)
    leds[38] = (255,204,153)
    leds[98] = (255,204,153)
    leds[158] = (255,204,153)
    leds[218] = (255,204,153)
    leds[278] = (255,204,153)
    leds[338] = (255,204,153)
    leds[40] = (255,204,153)
    leds[100] = (255,204,153)
    leds[160] = (255,204,153)
    leds[220] = (255,204,153)
    leds[280] = (255,204,153)
    leds[340] = (255,204,153)
    leds[221] = (255,204,153)
    leds[41] = (255,204,153)
    leds[341] = (255,204,153)
    leds[222] = (255,204,153)
    leds[42] = (255,204,153)
    leds[342] = (255,204,153)
    leds[223] = (255,204,153)
    leds[43] = (255,204,153)
    leds[343] = (255,204,153)
    leds[224] = (255,204,153)
    leds[44] = (255,204,153)
    leds[344] = (255,204,153)
    leds[46] = (255,204,153)
    leds[106] = (255,204,153)
    leds[166] = (255,204,153)
    leds[226] = (255,204,153)
    leds[286] = (255,204,153)
    leds[346] = (255,204,153)
    leds[347] = (255,204,153)
    leds[348] = (255,204,153)
    leds[349] = (255,204,153)
    leds[350] = (255,204,153)
    leds[52] = (255,204,153)
    leds[112] = (255,204,153)
    leds[172] = (255,204,153)
    leds[232] = (255,204,153)
    leds[292] = (255,204,153)
    leds[352] = (255,204,153)
    leds[353] = (255,204,153)
    leds[354] = (255,204,153)
    leds[355] = (255,204,153)
    leds[356] = (255,204,153)
    leds[58] = (255,204,153)
    leds[118] = (255,204,153)
    leds[178] = (255,204,153)
    leds[238] = (255,204,153)
    leds[298] = (255,204,153)
    leds[358] = (255,204,153)
    leds[59] = (255,204,153)
    leds[359] = (255,204,153)
    client.put_pixels(leds)

def twentyEight():
    leds[32] = (255,204,153)
    leds[92] = (255,204,153)
    leds[152] = (255,204,153)
    leds[212] = (255,204,153)
    leds[272] = (255,204,153)
    leds[332] = (255,204,153)
    leds[213] = (255,204,153)
    leds[214] = (255,204,153)
    leds[215] = (255,204,153)
    leds[216] = (255,204,153)
    leds[217] = (255,204,153)
    leds[37] = (255,204,153)
    leds[97] = (255,204,153)
    leds[157] = (255,204,153)
    leds[217] = (255,204,153)
    leds[277] = (255,204,153)
    leds[337] = (255,204,153)
    leds[39] = (255,204,153)
    leds[99] = (255,204,153)
    leds[159] = (255,204,153)
    leds[219] = (255,204,153)
    leds[279] = (255,204,153)
    leds[339] = (255,204,153)
    leds[220] = (255,204,153)
    leds[40] = (255,204,153)
    leds[340] = (255,204,153)
    leds[221] = (255,204,153)
    leds[41] = (255,204,153)
    leds[341] = (255,204,153)
    leds[222] = (255,204,153)
    leds[42] = (255,204,153)
    leds[342] = (255,204,153)
    leds[223] = (255,204,153)
    leds[43] = (255,204,153)
    leds[343] = (255,204,153)
    leds[45] = (255,204,153)
    leds[105] = (255,204,153)
    leds[165] = (255,204,153)
    leds[225] = (255,204,153)
    leds[285] = (255,204,153)
    leds[345] = (255,204,153)
    leds[346] = (255,204,153)
    leds[347] = (255,204,153)
    leds[348] = (255,204,153)
    leds[349] = (255,204,153)
    leds[51] = (255,204,153)
    leds[111] = (255,204,153)
    leds[171] = (255,204,153)
    leds[231] = (255,204,153)
    leds[291] = (255,204,153)
    leds[351] = (255,204,153)
    leds[352] = (255,204,153)
    leds[353] = (255,204,153)
    leds[354] = (255,204,153)
    leds[355] = (255,204,153)
    leds[57] = (255,204,153)
    leds[117] = (255,204,153)
    leds[177] = (255,204,153)
    leds[237] = (255,204,153)
    leds[297] =(255,204,153)
    leds[357] = (255,204,153)
    leds[58] = (255,204,153)
    leds[358] = (255,204,153)
    leds[59] = (255,204,153)
    leds[359] = (255,204,153)
    client.put_pixels(leds)

def twentyNine():
    leds[31] = (255,204,153)
    leds[91] = (255,204,153)
    leds[151] = (255,204,153)
    leds[211] = (255,204,153)
    leds[271] = (255,204,153)
    leds[331] = (255,204,153)
    leds[212] = (255,204,153)
    leds[213] = (255,204,153)
    leds[214] = (255,204,153)
    leds[215] = (255,204,153)
    leds[216] = (255,204,153)
    leds[36] = (255,204,153)
    leds[96] = (255,204,153)
    leds[156] = (255,204,153)
    leds[216] = (255,204,153)
    leds[276] = (255,204,153)
    leds[336] = (255,204,153)
    leds[38] = (255,204,153)
    leds[98] = (255,204,153)
    leds[158] = (255,204,153)
    leds[218] = (255,204,153)
    leds[278] = (255,204,153)
    leds[338] = (255,204,153)
    leds[219] = (255,204,153)
    leds[39] = (255,204,153)
    leds[339] = (255,204,153)
    leds[220] = (255,204,153)
    leds[40] = (255,204,153)
    leds[340] = (255,204,153)
    leds[221] = (255,204,153)
    leds[41] = (255,204,153)
    leds[341] = (255,204,153)
    leds[222] = (255,204,153)
    leds[42] = (255,204,153)
    leds[342] = (255,204,153)
    leds[44] = (255,204,153)
    leds[104] = (255,204,153)
    leds[164] = (255,204,153)
    leds[224] = (255,204,153)
    leds[284] = (255,204,153)
    leds[344] = (255,204,153)
    leds[345] = (255,204,153)
    leds[346] = (255,204,153)
    leds[347] = (255,204,153)
    leds[348] = (255,204,153)
    leds[50] = (255,204,153)
    leds[110] = (255,204,153)
    leds[170] = (255,204,153)
    leds[230] = (255,204,153)
    leds[290] = (255,204,153)
    leds[350] = (255,204,153)
    leds[351] = (255,204,153)
    leds[352] = (255,204,153)
    leds[353] = (255,204,153)
    leds[354] = (255,204,153)
    leds[56] = (255,204,153)
    leds[116] = (255,204,153)
    leds[176] = (255,204,153)
    leds[236] = (255,204,153)
    leds[296] = (255,204,153)
    leds[356] = (255,204,153)
    leds[57] = (255,204,153)
    leds[357] = (255,204,153)
    leds[58] = (255,204,153)
    leds[358] = (255,204,153)
    leds[59] = (255,204,153)
    leds[359] = (255,204,153)
    client.put_pixels(leds)

def thirty():
    leds[30] = (255,204,153)
    leds[90] = (255,204,153)
    leds[150] = (255,204,153)
    leds[210] = (255,204,153)
    leds[270] = (255,204,153)
    leds[330] = (255,204,153)
    leds[211] = (255,204,153)
    leds[212] = (255,204,153)
    leds[213] = (255,204,153)
    leds[214] = (255,204,153)
    leds[215] = (255,204,153)
    leds[35] = (255,204,153)
    leds[95] = (255,204,153)
    leds[155] = (255,204,153)
    leds[215] = (255,204,153)
    leds[275] = (255,204,153)
    leds[335] = (255,204,153)
    leds[37] = (255,204,153)
    leds[97] = (255,204,153)
    leds[157] = (255,204,153)
    leds[217] = (255,204,153)
    leds[277] = (255,204,153)
    leds[337] = (255,204,153)
    leds[218] = (255,204,153)
    leds[38] = (255,204,153)
    leds[338] = (255,204,153)
    leds[219] = (255,204,153)
    leds[39] = (255,204,153)
    leds[339] = (255,204,153)
    leds[220] = (255,204,153)
    leds[40] = (255,204,153)
    leds[340] = (255,204,153)
    leds[221] = (255,204,153)
    leds[41] = (255,204,153)
    leds[341] = (255,204,153)
    leds[43] = (255,204,153)
    leds[103] = (255,204,153)
    leds[163] = (255,204,153)
    leds[223] = (255,204,153)
    leds[283] = (255,204,153)
    leds[343] = (255,204,153)
    leds[344] = (255,204,153)
    leds[345] = (255,204,153)
    leds[346] = (255,204,153)
    leds[347] = (255,204,153)
    leds[49] = (255,204,153)
    leds[109] = (255,204,153)
    leds[169] = (255,204,153)
    leds[229] = (255,204,153)
    leds[289] = (255,204,153)
    leds[349] = (255,204,153)
    leds[350] = (255,204,153)
    leds[351] = (255,204,153)
    leds[352] = (255,204,153)
    leds[353] = (255,204,153)
    leds[55] = (255,204,153)
    leds[115] = (255,204,153)
    leds[175] = (255,204,153)
    leds[235] = (255,204,153)
    leds[295] = (255,204,153)
    leds[355] = (255,204,153)
    leds[56] = (255,204,153)
    leds[356] = (255,204,153)
    leds[57] = (255,204,153)
    leds[357] = (255,204,153)
    leds[58] = (255,204,153)
    leds[358] = (255,204,153)
    leds[59] = (255,204,153)
    leds[359] = (255,204,153)
    client.put_pixels(leds)

def thirtyOne():
    leds[29] = (255,204,153)
    leds[89] = (255,204,153)
    leds[149] = (255,204,153)
    leds[209] = (255,204,153)
    leds[269] = (255,204,153)
    leds[329] = (255,204,153)
    leds[210] = (255,204,153)
    leds[211] = (255,204,153)
    leds[212] = (255,204,153)
    leds[213] = (255,204,153)
    leds[214] = (255,204,153)
    leds[34] = (255,204,153)
    leds[94] = (255,204,153)
    leds[154] = (255,204,153)
    leds[214] = (255,204,153)
    leds[274] = (255,204,153)
    leds[334] = (255,204,153)
    leds[36] = (255,204,153)
    leds[96] = (255,204,153)
    leds[156] = (255,204,153)
    leds[216] = (255,204,153)
    leds[276] = (255,204,153)
    leds[336] = (255,204,153)
    leds[217] = (255,204,153)
    leds[37] = (255,204,153)
    leds[337] = (255,204,153)
    leds[218] = (255,204,153)
    leds[38] = (255,204,153)
    leds[338] = (255,204,153)
    leds[219] = (255,204,153)
    leds[39] = (255,204,153)
    leds[339] = (255,204,153)
    leds[220] = (255,204,153)
    leds[40] = (255,204,153)
    leds[340] = (255,204,153)
    leds[42] = (255,204,153)
    leds[102] = (255,204,153)
    leds[162] = (255,204,153)
    leds[222] = (255,204,153)
    leds[282] = (255,204,153)
    leds[342] = (255,204,153)
    leds[343] = (255,204,153)
    leds[344] = (255,204,153)
    leds[345] = (255,204,153)
    leds[346] = (255,204,153)
    leds[48] = (255,204,153)
    leds[108] = (255,204,153)
    leds[168] = (255,204,153)
    leds[228] = (255,204,153)
    leds[288] = (255,204,153)
    leds[348] = (255,204,153)
    leds[349] = (255,204,153)
    leds[350] = (255,204,153)
    leds[351] = (255,204,153)
    leds[352] = (255,204,153)
    leds[54] = (255,204,153)
    leds[114] = (255,204,153)
    leds[174] = (255,204,153)
    leds[234] = (255,204,153)
    leds[294] = (255,204,153)
    leds[354] = (255,204,153)
    leds[55] = (255,204,153)
    leds[355] = (255,204,153)
    leds[56] = (255,204,153)
    leds[356] = (255,204,153)
    leds[57] = (255,204,153)
    leds[357] = (255,204,153)
    leds[58] = (255,204,153)
    leds[358] = (255,204,153)
    leds[59] = (255,204,153)
    leds[119] = (255,204,153)
    leds[179] = (255,204,153)
    leds[239] = (255,204,153)
    leds[299] = (255,204,153)
    leds[359] = (255,204,153)
    client.put_pixels(leds)


    
for i in range(2):
    first()
    sleep(.05)
    leds = [(20,20,20)]*360
    sleep(.05)
    second()
    sleep(.05)
    leds = [(20,20,20)]*360
    sleep(.05)
    third()
    sleep(.05)
    leds = [(20,20,20)]*360
    sleep(.05)
    fourth()
    sleep(.05)
    leds = [(20,20,20)]*360
    sleep(.05)
    fifth()
    sleep(.05)
    leds = [(20,20,20)]*360
    sleep(.05)
    sixth()
    sleep(.05)
    leds = [(20,20,20)]*360
    sleep(.05)
    seventh()
    sleep(.05)
    leds = [(20,20,20)]*360
    sleep(.05)
    eighth()
    sleep(.05)
    leds = [(20,20,20)]*360
    sleep(.05)
    ninth()
    sleep(.05)
    leds = [(20,20,20)]*360
    sleep(.05)
    tenth()
    sleep(.05)
    leds = [(20,20,20)]*360
    sleep(.05)
    eleven()
    sleep(.05)
    leds = [(20,20,20)]*360
    sleep(.05)
    twelve()
    sleep(.05)
    leds = [(20,20,20)]*360
    sleep(.05)
    thirteen()
    sleep(.05)
    leds = [(20,20,20)]*360
    sleep(.05)
    fourteen()
    sleep(.05)
    leds = [(20,20,20)]*360
    sleep(.05)
    fifteen()
    sleep(.05)
    leds = [(20,20,20)]*360
    sleep(.05)
    sixteen()
    sleep(.05)
    leds = [(20,20,20)]*360
    sleep(.05)
    seventeen()
    sleep(.05)
    leds = [(20,20,20)]*360
    sleep(.05)
    eighteen()
    sleep(.05)
    leds = [(20,20,20)]*360
    sleep(.05)
    nineteen()
    sleep(.05)
    leds = [(20,20,20)]*360
    sleep(.05)
    twenty()
    sleep(.05)
    leds = [(20,20,20)]*360
    sleep(.05)
    twentyOne()
    sleep(.05)
    leds = [(20,20,20)]*360
    sleep(.05)
    twentyTwo()
    sleep(.05)
    leds = [(20,20,20)]*360
    sleep(.05)
    twentyThree()
    sleep(.05)
    leds = [(20,20,20)]*360
    sleep(.05)
    twentyFour()
    sleep(.05)
    leds = [(20,20,20)]*360
    sleep(.05)
    twentyFive()
    sleep(.05)
    leds = [(20,20,20)]*360
    sleep(.05)
    twentySix()
    sleep(.05)
    leds = [(20,20,20)]*360
    sleep(.05)
    twentySeven()
    sleep(.05)
    leds = [(20,20,20)]*360
    sleep(.05)
    twentyEight()
    sleep(.05)
    leds = [(20,20,20)]*360
    sleep(.05)
    twentyNine()
    sleep(.05)
    leds = [(20,20,20)]*360
    sleep(.05)
    thirty()
    sleep(.05)
    leds = [(20,20,20)]*360
    sleep(.05)
    thirtyOne()
    sleep(.05)
    leds = [(20,20,20)]*360
    sleep(.05)
white()




    

    

    
