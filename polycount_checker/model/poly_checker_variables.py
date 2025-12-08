"""Constants"""
GHR = 'GHR'
G0 = 'G0'
G1 = 'G1'
G2 = 'G2'
INVALID = 'Invalid'
ENGINE = 'Engine'
WIPERS = 'Wipers'
STOCK = 'Stock'
RACER = 'Racer'
BODY = 'Body'
INTERIOR = 'Interior'
RIM = 'Rim'



"""UI Variables"""
UINAME = 'Polycount Checker'
ITEMCOLOR =  {0:'LIGHT GREEN', 1:'RED', 2:'YELLOW'}

"""UTIL Variables"""
AVAILABLELOD = [GHR, G0 , G1 , G2, INVALID]
STATUS = {0:'OK', 1:'Exceeds the limit by: ', 2:'Within the buffer: ',4:'Exist objects that do not in a LOD'}
POLYCOUNT = {
    BODY: {
        STOCK: {GHR:0,
                  G0 : 30000,
                  G1 : 5000,
                  G2 : 1500
                  },
        RACER: {GHR:0,
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
        }
}
EXCLUDE = {
    WIPERS: ['Wiper', 'WiperArm', 'WiperBlade'],
    ENGINE: ['Engine'],
    RIM: ['Rim','Tire']
}
BUFFER = 20