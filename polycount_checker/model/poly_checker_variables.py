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
INVALID = 'Invalid'



"""UI Variables"""
UINAME = 'Polycount Checker'

LIGHTGREEN = 'LIGHT GREEN'
RED = 'RED'
YELLOW = 'YELLOW'
WHITE = 'WHITE'
ITEMCOLOR =  {0:LIGHTGREEN, 1:RED, 2:YELLOW,3:WHITE}

"""UTIL Variables"""
BUFFER = 20

AVAILABLELOD = [GHR, G0, G1, G2]

OBJECTDICT = {
            BODY: {
                GHR:[],
                G0:[],
                G1:[],
                G2:[]
            },
            INTERIOR:{
                GHR:[],
                G0:[],
                G1:[],
                G2:[]
            },
            WIPERS:{
                GHR:[],
                G0:[],
                G1:[],
                G2:[]
            },
            ENGINE:{
                GHR:[],
                G0:[],
                G1:[],
                G2:[]
            },
            RIMS:{
                GHR:[],
                G0:[],
                G1:[],
                G2:[]
            }
}

POLYDICT = {
            BODY:{
                GHR:0,
                G0:0,
                G1:0,
                G2:0
            },
            INTERIOR:{
                GHR:0,
                G0:0,
                G1:0,
                G2:0
            },
            WIPERS:{
                GHR:0,
                G0:0,
                G1:0,
                G2:0
            },
            ENGINE:{
                GHR:0,
                G0:0,
                G1:0,
                G2:0
            },
            RIMS:{
                GHR:0,
                G0:0,
                G1:0,
                G2:0
            }
}
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
        GHR : 3000,
        G0 : 1500,
        G1 : 0,
        G2 : 0
    },
    INTERIOR:{
        GHR : 50000,
        G0 : 5000,
        G1 : 1000,
        G2 : 0
    },
    RIMS:{
        GHR : 50000,
        G0 : 5000,
        G1 : 1000,
        G2 : 0
    }
}
EXCLUDE = {
    WIPERS: ['Wiper', 'WiperArm', 'WiperBlade'],
    ENGINE: ['Engine'],
    RIMS: ['Rim','Tire']
}
