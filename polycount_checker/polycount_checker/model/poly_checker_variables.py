"""Constants"""

GHR = 'GHR'
G0 = 'G0'
G1 = 'G1'
G2 = 'G2'
ENGINE = 'Engine'
WIPERS = 'Wipers'
STOCK = 'Stock'
RACER = 'Racer'
BODY = 'Body'
INTERIOR = 'Interior'
RIMS = 'Rim'
RIM_2 = '2 rims'
RIM_4 = '4 rims'
TIRE = 'Tire'
INVALID = 'Invalid'

BODY_TYPE = 0
RACER_TYPE = 1
INTERIOR_TYPE = 2
RIM_TYPE = 3

"""UI Variables"""
UI_NAME = 'Polycount Checker'

LIGHT_GREEN = 'LIGHT GREEN'
RED = 'RED'
YELLOW = 'YELLOW'
WHITE = 'WHITE'
ITEM_COLOR =  {0:LIGHT_GREEN, 1:RED, 2:YELLOW,3:WHITE}

"""UTIL Variables"""
BUFFER = 20

AVAILABLE_LOD = [GHR, G0, G1, G2]

STATUS = {0:'OK', 1:'Exceeds the buffer by: '}
POLYCOUNT = {
    BODY: {
        STOCK: {GHR: 60000,
                G0 : 30000,
                G1 : 5000,
                G2 : 1500
                },
        RACER: {GHR: 60000,
                   G0: 35000,
                   G1 : 7000,
                   G2 : 1500
                }
    },
    WIPERS: {
        GHR : 2500,
        G0 : 1000,
        G1 : 250,
        G2: 0
    },
    ENGINE:{
        GHR : 0,
        G0 : 3000,
        G1 : 1500,
        G2 : 0
    },
    INTERIOR:{
        GHR : 50000,
        G0 : 5000,
        G1 : 1000,
        G2 : 0
    },
    RIMS:{
        GHR : 20000,
        G0 : 5000,
        G1 : 1700,
        G2 : 700
    },
    RIM_2:{
        GHR : 16000,
        G0 : 4000,
        G1 : 1500,
        G2 : 700
    },
    RIM_4:{
        GHR : 5000,
        G0 : 5000,
        G1 : 1500,
        G2 : 700
    }
}
EXCLUDE = {
    WIPERS: ['Wiper', 'WiperArm', 'WiperBlade'],
    ENGINE: ['Engine'],
    RIMS: ['Rim','Tire']
}
