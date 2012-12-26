## Using minimalmodbus library, this attempts to create a python driver to interface with the XW Inverters that are being 
## currently set up in Steinman Hall. 
## Created by Irving Derin


## Minimalmodbus library has been edited, and uploaded to google code. the chan ge in code allowes for reading of 
## 32 bit registers via modbus. 

import minimalmodbus

######################################### INITIALIZATION OF CLASS HERE!!!! #####################################
################################################################################################################
## This class is a sub class of the minimal modbus instrument class. 
 
class XW_Inverter(minimalmodbus.Instrument):
    """ Instrument class driver for the XW Inverters that are currently being used by the Energy Institute. 
    
    Communications are completed by using the RTU protocol to connect the Xantrax gateway, and from there 
    individual Inverters are proxied and addressed on their own.


    Default address for the Communications gateway: 0xc9
    Default addresses for proxied Inverters: 0x65 + 
    Each new proxied Inverter has an address that is a single increment from the previous address. 

    Arguments: 
        * port(str/int): Serial Port name
            The port name HAS to be a string for unix systems, on windows, this can be an interger which is n-1, where n is the COM number
            i.e  COM8 = 7
            This has to be set only once on a computer. From then on, the port number DOES NOT CHANGE

        * Address(int): Address of the device you want to contact. DO NOT USE THIS CLASS FOR THE GATEWAY!!!!! It will not function properly
            Future Implentation - A check to make sure that gateway was not the connected class. 

    """


############# Initialization and setup functions ##############

    def __init__(self, portname, slaveaddress):
        minimalmodbus.Instrument.__init__(self, portname, slaveaddress)
	self.serial.timeout = 0.06
        print("Current Timeout")
        print(self.serial.timeout)
    def setTimeout(self,time):
        """ Set the timeout for the serial port. use a number greater than 0.25 seconds, or else you will get communication errors
         Arguments:
             time(int) : The amount of time to wait before returning a timeout error. In seconds
        """

        self.serial.timeout = time
           
############# Active Registers ####################################
    
    def getActiveFaults(self):
	""" This is still currently not implemented, due to really weird Xantrax settings for this. Will do in the future"""
	pass

    def getActiveWarnings(self):
        """ This is still currently not implemented, due to really weird Xantrax settings for this. Will do in the future"""
        pass

    def getState(self):
        """ Gets the current state of the inverter """
        return self.read_registers(207)


############ Battery DC Input Status #############################

    def getDCInVolt(self):
        """ Reads the Input DC Voltage to the inverters. Units: VDC/x100 """
        return self.read_registers(0x0201,2,2)

    def getDCInCurr(self):
        """ Reads the Input DC Current to the inverters. Units: ADC/x100 """
        return self.read_registers(0x0203,2,2)

    def getDCInPower(self):
        """ Reads the Input DC Power to the inverters. Units: W/x1 """
        return self.read_registers(0x0205,2) 

############ Battery Misc Functions #############################

    def getBatSOC(self):
        """ Reads the current State of Charge on the battery """
        return self.read_registers(0x0302) 

############ Battery DC Output Status ###########################

    def getDCOutVolt(self):
        """ Reads the DC Output Voltage of the inverter. Units: VDC/x100 """
        return self.read_registers(0x0401,2,2)  

    def getDCOutCurr(self):
        """ Reads the DC Output Current of the Inverter. Units: ADC/x100 """
        return self.read_registers(0x0403,2,2)

    def getDCOutPower(self):
        """ Reads the DC Output Power of the Inverter. Units: W/x1 """
        return self.read_registers(0x0405,2)

    def getDCOutPercent(self):
        """ Reads the DC Output % of the maximum """
        return self.read_registers(0x0407)         

############ AC Input Status 1 ###################################

    def getACInVolt1(self):
        """ Reads the Input AC Voltage for the Inverter. Units: Vrms:x100 """
        return self.read_registers(0x0501,2,2)

    def getACInCurr1(self):
        """ Reads the Input AC Current for the Inverters. Units: Arms/x100 """
        return self.read_registers(0x0503,2,2)

    def getACInFreq1(self):
        """ Reads the Input AC Frequency for the Inverters. Units: Hz/x10 """
        return self.read_registers(0x0505,1,1)

    def getACInPowe1(self):
        """ Reads the Input AC REAL!!! Power for the Inverters. Units: Watts/x1 """
        return self.read_registers(0x0506,2)

############ AC Input Status 2 ###################################

    def getACInVolt2(self):
        """ Reads the Input AC Voltage for the Inverter. Units: Vrms:x100 """
        return self.read_registers(0x0511,2,2)

    def getACInCurr2(self):
        """ Reads the Input AC Current for the Inverters. Units: Arms/x100 """
        return self.read_registers(0x0513,2,2)

    def getACInFreq2(self):
        """ Reads the Input AC Frequency for the Inverters. Units: Hz/x10 """
        return self.read_registers(0x0515,1,1)

    def getACInPowe2(self):
        """ Reads the Input AC REAL!!! Power for the Inverters. Units: Watts/x1 """
        return self.read_registers(0x0516,2)

########### AC Output Status   ##################################
    
    def getACOutVolt(self):
        """ Reads the voltage of the AC Output. Units: Vrms/X100 """
        return self.read_registers(0x0701,2,2)

    def getACOutCurr(self):
        """ Reads the current of the AC Output. Units: Arms/X100 """
        return self.read_registers(0x0703,2,2)

    def getACOutFreq(self):
        """ Reads the current of the AC Output. Units are in Hz/X10 """
        return self.read_registers(0x0705)

    def getACOutPower(self):
        """ Reads the current REAL POWER of the AC Output. Units are in Watts """
        return self.read_registers(0x0706,2)

########### AC Source Status 1 ##################################

    def getACQualLvl1(self):
        """ Reads the AC Level Qualificiation of the Inverter
        0 - Not Qualified
        1 - Qualifying
	2 - Missing
	3 - Too Low
	4 - Too High
	5 - Good
        """
        return self.read_registers(0x0601)

    def getACQualFreq1(self):
        """ Reads the AC Level Qualificiation of the Inverter
        0 - Not Qualified
        1 - Qualifying
	2 - Missing
	3 - Too Low
	4 - Too High
	5 - Good
        """
        return self.read_registers(0x0602)

    def getACQualTime1(self):
        """ Reads the amount of time that has elapsed that the source has been qualified """
        return self.read_registers(0x0603,2)


########### AC Source Status 2 ##################################

    def getACQualLvl2(self):
        """ Reads the AC Level Qualificiation of the Inverter
        0 - Not Qualified
        1 - Qualifying
	2 - Missing
	3 - Too Low
	4 - Too High
	5 - Good
        """
        return self.read_registers(0x0611)

    def getACQualFreq2(self):
        """ Reads the AC Level Qualificiation of the Inverter
        0 - Not Qualified
        1 - Qualifying
	2 - Missing
	3 - Too Low
	4 - Too High
	5 - Good
        """
        return self.read_registers(0x0612)

    def getACQualTime2(self):
        """ Reads the amount of time that has elapsed that the source has been qualified """
        return self.read_registers(0x0613,2)

########## Temperture Readings ###################################

    def getBatTemp(self):
        """Reads the temperture reading from the Battery Temp. Sensor. Units: C/x10 """
        return self.read_registers(0x0301,1,1)

    def getTransTemp(self):
        """ Reads the temperture reading from the internal Transformer. Units: C/x10 """
        return self.read_registers(0x0900,1,1)

    def getFETTemp1(self):
        """ Reads the FET 1 Temperture from the inverter. Units: C/x10 """
        return self.read_registers(0x0910,1,1)

    def getFETTemp2(self):
        """ Reads the FET 2 Temperture from the inverter. Units: C/x10 """
        return self.read_registers(0x0920,1,1)

    def getCapTemp(self):
        """ Reads the Capacitor Temperture from the inverter. Units: C/x10 """
        return self.read_registers(0x0930,1,1)

############# Changeable Statuses #########################################

## Charger Reads

    def getChargeState(self):
        """ Reads to see if the charger is enabled or disabled (0 - Disabled || 1 - enabled) """
        return self.read_registers(0xF101)

    def getChargerEqualize(self):
        """ Reads to se if the charger is set to equalize  (0 - Disabled || 1 - enabled)"""
        return self.read_registers(0xF102)

## Inverter Reads

    def getInvertState(self):
        """ Reads to see if the inverters are running (0 - Disabled || 1 - enabled) """
        return self.read_registers(0xF201)

    def getSearchMode(self):
        """ Reads to get the state of the Search Mode (0 - Disabled || 1 - enabled) """
        return self.read_registers(0xF202)

    def getGridTie(self):
        """ Reads to get the status of the Grid-Tie (0 - Disabled || 1 - enabled)"""
        return self.read_registers(0xF203)

    def getSellMode(self):
        """ Reads to get the status of the sell to grid mode (0 - Disabled || 1 - enabled) """
        return self.read_registers(0xF204)

    def getForSellMode(self):
        """ Reads to get the forced sell status (0 - Disabled || 1 - enabled) """
        return self.read_registers(0xF205)

## Charger Configs

    def getMaxChargeRate(self):
        """ """
        return self.read_registers(0x8302)
## Inverter Configs

    def getMaxSellAmps(self):
        """ """
        return self.read_registers(0x8411)

    def getGridAmpsAC(self):
        """ """
        return self.read_registers(0x8412)

    def getSellDuration(self):
        """ """
        return self.read_registers(0x8413)

  
 
###########################################################################
###########################################################################
############################ WRITE ########################################
###########################################################################
###########################################################################

# Write in exceptions for states that are greater than 1

########################## Inverters #######################################

    def setInvertState(self,state):
        """  This function sets the inverters state.  
             returns the new value for the registers that was changed value
        """
        self.write_register(0xf201,state)
        return self.read_registers(0xf201)

    def setSearchMode(self,state):
        
        """ """
        self.write_register(0xf202,state)
        return self.read_registers(0xf202)


    def setGridTie(self,state):
        
        """ """
        self.write_register(0xF203,state)
        return self.read_registers(0xf203)


    def setSellMode(self,state):
        
        """ """
        self.write_register(0xf204,state)
        return self.read_registers(0xf204)


    def setForSellMode(self,state):
        
        """ """
        self.write_register(0xF205,state)
        return self.read_registers(0xf205)

	
########################## Charger ########################################

    def setChargeState(self,state):
        
        """ """
        self.write_register(0xF101,state)
        return self.read_registers(0xF101)

    def setForceCharge(self, state):
	
	    """ 1 - Bulk
	        2 - float
	        3 - No Float
	    """
	    self.write_register(0xF103,state)


    def setEqualizeActive(self,state):
    
        """ """
        self.write_register(0xF102,state)
        return self.read_registers(0xF102)

######################### Charger Configuration ##########################
    def setMaxChargeRate(self, rate):

        """ """
        self.write_register(0x8302, rate)
        return self.read_registers(0x8302)

######################## Inverter Configureations ########################

    def setMaxSellAmp(self,rate):
    
        """ """
        self.write_register(0x8411,rate)
        return self.read_registers(0x8411)

    def setGridAmpsAC(self, amps):
        
        """ """
        self.write_register(0x8412,amps)
        return self.read_registers(0x8412)

    def setSellDuration(self,minutes):
        
        """ """
        self.write_register(0x8413,minutes)
        return self.read_registers(0x8413)

####################### User Configuration ################################

    def setUserCommand(self):
	    self.write_register(0x8300,00)
	    self.write_register(0x8400,00)
	    
