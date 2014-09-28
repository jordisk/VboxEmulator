
'''
Author: Jordi Vazquez Aira
Email: jordi@jordivazquez.com
'''

import _winreg as wreg
import os
import urllib
import shutil

#Variables
sysdrive = os.getenv("SystemDrive")
sysfolder = (sysdrive + "\\windows\\system32")
storeguest = (sysfolder + "\\DRVSTORE\\VBoxGuest_ED40339D75DAC80DECCD6CCCDB8E202724F5321D")
storevideo = (sysfolder + "\\DRVSTORE\\VBOXVideo_5C9060E472F2B1E3E9D5353B27AF6B8DABF99D47")
ProgramFiles = os.getenv("ProgramFiles")
pfilesvm = (ProgramFiles + "\\Oracle\\VirtualBox Guest Additions")
cwd = os.path.dirname(os.path.abspath(__file__))

#PrintVars
version = "[+]----- Version: 0.5 -----[+]"
versionDate = "[+]--- Date: 2014-09-28 ---[+]"


#Main print
for mainprint in ["", "[+]------ VBEmulator ------[+]", "[+]- Virtual Box emulator -[+]",
                  version, versionDate, "", "", "Please, press enter to start"  ] :
    print(mainprint)

raw_input()

print("")
print("Creating Registry keys...")

key = wreg.CreateKey(wreg.HKEY_LOCAL_MACHINE, "Software\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\Oracle VM VirtualBox Guest Additions")
Hkey = ["DisplayName", "UninstallString", "DisplayVersion", "URLInfoAbout", "Publisher"]
Hval = ["Oracle VM VirtualBox Guest Additions 4.2.16", ProgramFiles + '\\Oracle\\VirtualBox VM Guest Additions\\unist.exe', "4.2.16.0", "http://www.virtualbox.org", "Oracle Corporation"]
for keys, vals in zip(Hkey, Hval):
	wreg.SetValueEx(key, keys, 0, wreg.REG_SZ, vals)

key = wreg.CreateKey(wreg.HKEY_LOCAL_MACHINE, "Software\\Microsoft\\Windows\\CurrentVersion\\DIFx\\DriverStore\\VBoxGuest_3D1C46450F98FCC27B9B5245C5D9D88736B7CD6F")
Hkey = ["INF", "ProductName", "ManufacturerName", "DisplayName"]
Hval = ["VBoxVideo.inf", "VirtualBox Guest Additions", "Oracle Corporation", "VirtualBox Guest Additions Install Helper"]
for keys, vals in zip(Hkey, Hval):
	wreg.SetValueEx(key, keys, 0, wreg.REG_SZ, vals)
wreg.SetValueEx(key, 'DependentInstaller', 0, wreg.REG_MULTI_SZ, ['{7d2c708d-c202-40ab-b3e8-de21da1dc629}'])	
wreg.SetValueEx(key, 'DependentInstallerName', 0, wreg.REG_MULTI_SZ, ['VirtualBox Guest Additions Install Helper'])
wreg.SetValueEx(key, 'Services', 0, wreg.REG_MULTI_SZ, ['VBoxGuest'])
wreg.SetValueEx(key, 'type', 0, wreg.REG_DWORD, 6)
key = wreg.CreateKey(wreg.HKEY_LOCAL_MACHINE, "Software\\Microsoft\\Windows\\CurrentVersion\\DIFx\\DriverStore\\VBoxVideo_6520996AB99D2C6DF7C2AD5A2414F1F27AA75DF0")
Hval = ["VBoxGuest.inf", "VirtualBox Guest Additions", "Oracle Corporation", "VirtualBox Guest Additions Install Helper"]
for keys, vals in zip(Hkey, Hval):
	wreg.SetValueEx(key, keys, 0, wreg.REG_SZ, vals)
wreg.SetValueEx(key, 'DependentInstaller', 0, wreg.REG_MULTI_SZ, ['{7d2c708d-c202-40ab-b3e8-de21da1dc629}'])	
wreg.SetValueEx(key, 'DependentInstallerName', 0, wreg.REG_MULTI_SZ, ['VirtualBox Guest Additions Install Helper'])
wreg.SetValueEx(key, 'Services', 0, wreg.REG_MULTI_SZ, ['VBoxVideo'])
wreg.SetValueEx(key, 'type', 0, wreg.REG_DWORD, 6)	

key = wreg.CreateKey(wreg.HKEY_LOCAL_MACHINE, "Software\\Microsoft\\Windows NT\\CurrentVersion\\OpenGLDrivers\\VBoxOGL")
wreg.SetValueEx(key, 'Dll', 0, wreg.REG_SZ, "VBoxOGL.dll")
wreg.SetValueEx(key, 'DriverVersion', 0, wreg.REG_DWORD, 1)
wreg.SetValueEx(key, 'Flags', 0, wreg.REG_DWORD, 1)
wreg.SetValueEx(key, 'Version', 0, wreg.REG_DWORD, 2)


key = wreg.CreateKey(wreg.HKEY_LOCAL_MACHINE, "Software\\Oracle")
wreg.SetValue(key, 'VirtualBox Guest Additions', wreg.REG_SZ, '')
key = wreg.CreateKey(wreg.HKEY_LOCAL_MACHINE, "Software\\Oracle\\VirtualBox Guest Additions")
wreg.SetValueEx(key, 'InstallDir', 0, wreg.REG_SZ, pfilesvm)
wreg.SetValueEx(key, 'Revision', 0, wreg.REG_SZ, '84104')
wreg.SetValueEx(key, 'Version', 0, wreg.REG_SZ, '4.2.16')
wreg.SetValueEx(key, 'VersionExt', 0, wreg.REG_SZ, '4.2.16')


key = wreg.OpenKey(wreg.HKEY_LOCAL_MACHINE, "Hardware\\DEVICEMAP\\Scsi\\Scsi Port 0\\ScSi Bus 0\\Target Id 0\\Logical Unit Id 0", 0, wreg.KEY_ALL_ACCESS)
wreg.SetValueEx(key, 'Identifier', 0, wreg.REG_SZ, 'VBOX HARDDISK')

key = wreg.OpenKey(wreg.HKEY_LOCAL_MACHINE, "Hardware\\DESCRIPTION\\System", 0, wreg.KEY_ALL_ACCESS)
wreg.SetValueEx(key, 'SystemBiosVersion', 0, wreg.REG_MULTI_SZ, ['VBOX   -1 '])
wreg.SetValueEx(key, 'VideoBiosVersion', 0, wreg.REG_MULTI_SZ, ['Oracle VM VirtualBox Version 4.2.16 VGA Bios'])

key = wreg.CreateKey(wreg.HKEY_LOCAL_MACHINE, "Hardware\\Acpi\\DSDT\\VBOX__\\VBOXBIOS\\00000002")
wreg.SetValueEx(key, '00000000', 0, wreg.REG_BINARY, 'DSDT......VBOX  VBOXBIOS....INTL')

key = wreg.OpenKey(wreg.HKEY_LOCAL_MACHINE, "System\\ControlSet001\\Services\\Disk\\Enum", 0, wreg.KEY_ALL_ACCESS)
wreg.SetValueEx(key, '0', 0, wreg.REG_SZ, 'IDE\DiskVBOX_HARDDISK___________________________1.0_____\42566264366366323661362d3265623939632031')
key = wreg.OpenKey(wreg.HKEY_LOCAL_MACHINE, "System\\CurrentControlSet\\Services\\Disk\\Enum", 0, wreg.KEY_ALL_ACCESS)
wreg.SetValueEx(key, '0', 0, wreg.REG_SZ, 'IDE\DiskVBOX_HARDDISK___________________________1.0_____\42566264366366323661362d3265623939632031')

key = wreg.CreateKey(wreg.HKEY_LOCAL_MACHINE, "System\\CurrentControlSet\\Enum\\IDE\\DiskVBOX_HARDDISK\\425663643663663")
wreg.SetValueEx(key, 'FriendlyName', 0, wreg.REG_SZ, 'VBOX HARDDISK')

key = wreg.CreateKey(wreg.HKEY_LOCAL_MACHINE, "System\\CurrentControlSet\\Enum\\IDE\\CdRomVBOX_CD-ROM\\925663643663663")
wreg.SetValueEx(key, 'FriendlyName', 0, wreg.REG_SZ, 'VBOX CD-ROM')

for regfolder in ["ControlSet001", "Controlset002", "CurrentControlSet"]:
    key = wreg.CreateKey(wreg.HKEY_LOCAL_MACHINE, "System\\" + regfolder + "\\Services")
    wreg.SetValue(key, 'VBoxGuest', wreg.REG_SZ, '')
    key = wreg.CreateKey(wreg.HKEY_LOCAL_MACHINE, "System\\" + regfolder + "\\Services\\VBoxGuest")
    wreg.SetValueEx(key, 'DisplayName', 0, wreg.REG_SZ, 'VirtualBox Guest Driver')
    wreg.SetValueEx(key, 'ImagePath', 0, wreg.REG_EXPAND_SZ, 'system32\DRIVERS\VBoxGuest.sys')

    wreg.SetValue(key, 'Enum', wreg.REG_SZ, '')
    key = wreg.CreateKey(wreg.HKEY_LOCAL_MACHINE, "System\\" + regfolder + "\\Services\\VBoxGuest\\Enum")
    wreg.SetValueEx(key, '0', 0, wreg.REG_SZ, 'PCI\VEN_80EE&DEV_CAFE&SUBSYS_00000000&REV_00\3&267a616a&0&20')
    
    key = wreg.CreateKey(wreg.HKEY_LOCAL_MACHINE, "System\\" + regfolder + "\\Services")
    wreg.SetValue(key, 'VBoxMouse', wreg.REG_SZ, '')
    key = wreg.CreateKey(wreg.HKEY_LOCAL_MACHINE, "System\\" + regfolder + "\\Services\\VBoxMouse")
    wreg.SetValueEx(key, 'DisplayName', 0, wreg.REG_SZ, 'VirtualBox Guest Mouse Service')
    wreg.SetValueEx(key, 'ImagePath', 0, wreg.REG_EXPAND_SZ, 'system32\DRIVERS\VBoxMouse.sys')
    
    wreg.SetValue(key, 'Enum', wreg.REG_SZ, '')
    key = wreg.CreateKey(wreg.HKEY_LOCAL_MACHINE, "System\\" + regfolder + "\\Services\\VBoxMouse\\Enum")
    wreg.SetValueEx(key, '0', 0, wreg.REG_SZ, 'ACPI\PNP0F03\4&1d401fb5&0')
    
    key = wreg.CreateKey(wreg.HKEY_LOCAL_MACHINE, "System\\" + regfolder + "\\Services")
    wreg.SetValue(key, 'VBoxService', wreg.REG_SZ, '')
    key = wreg.CreateKey(wreg.HKEY_LOCAL_MACHINE, "System\\" + regfolder + "\\Services\\VBoxService")
    wreg.SetValueEx(key, 'DisplayName', 0, wreg.REG_SZ, 'VirtualBox Guest Aditions Service')
    wreg.SetValueEx(key, 'ImagePath', 0, wreg.REG_EXPAND_SZ, 'system32\VBoxService.exe')
    wreg.SetValueEx(key, 'Description', 0, wreg.REG_SZ, 'Manages VM runtime information and utilities for guest operating systems.')
    wreg.SetValueEx(key, 'ObjectName', 0, wreg.REG_SZ, 'LocalSystem')
    
    wreg.SetValue(key, 'Enum', wreg.REG_SZ, '')
    key = wreg.CreateKey(wreg.HKEY_LOCAL_MACHINE, "System\\" + regfolder + "\\Services\\VBoxService\\Enum")
    wreg.SetValueEx(key, '0', 0, wreg.REG_SZ, 'Root\LEGACY_VBOXSERVICE\0000')
    
    key = wreg.CreateKey(wreg.HKEY_LOCAL_MACHINE, "System\\" + regfolder + "\\Services")
    wreg.SetValue(key, 'VBoxSF', wreg.REG_SZ, '')
    key = wreg.CreateKey(wreg.HKEY_LOCAL_MACHINE, "System\\" + regfolder + "\\Services\\VBoxSF")
    wreg.SetValueEx(key, 'DisplayName', 0, wreg.REG_SZ, 'VirtualBox Shared Folders')
    wreg.SetValueEx(key, 'ImagePath', 0, wreg.REG_EXPAND_SZ, 'system32\DRIVERS\VBoxSF.sys')
    
    wreg.SetValue(key, 'Enum', wreg.REG_SZ, '')
    key = wreg.CreateKey(wreg.HKEY_LOCAL_MACHINE, "System\\" + regfolder + "\\Services\\VBoxSF\\Enum")
    wreg.SetValueEx(key, '0', 0, wreg.REG_SZ, 'Root\LEGACY_VBOXSF\0000')
    
    key = wreg.CreateKey(wreg.HKEY_LOCAL_MACHINE, "System\\" + regfolder + "\\Services\\VBoxSF")
    wreg.SetValue(key, 'NetworkProvider', wreg.REG_SZ, '')
    key = wreg.CreateKey(wreg.HKEY_LOCAL_MACHINE, "System\\" + regfolder + "\\Services\\VBoxSF\\NetworkProvider")
    wreg.SetValueEx(key, 'DeviceName', 0, wreg.REG_SZ, '\Device\VboxMinRdr')
    wreg.SetValueEx(key, 'Name', 0, wreg.REG_SZ, 'VirtualBox Shared Folder')
    wreg.SetValueEx(key, 'ProviderPath', 0, wreg.REG_SZ, sysfolder + '\VBoxMRXNP.dll')
    
    key = wreg.CreateKey(wreg.HKEY_LOCAL_MACHINE, "System\\" + regfolder + "\\Services")
    wreg.SetValue(key, 'VBoxVideo', wreg.REG_SZ, '')
    key = wreg.CreateKey(wreg.HKEY_LOCAL_MACHINE, "System\\" + regfolder + "\\Services\\VBoxVideo")
    wreg.SetValueEx(key, 'ImagePath', 0, wreg.REG_EXPAND_SZ, 'system32\DRIVERS\VBoxVideo.sys')
    
    wreg.SetValue(key, 'Enum', wreg.REG_SZ, '')
    key = wreg.CreateKey(wreg.HKEY_LOCAL_MACHINE, "System\\" + regfolder + "\\Services\\VBoxVideo\\Enum")
    wreg.SetValueEx(key, '0', 0, wreg.REG_SZ, 'PCI\VEN_80EE&DEV_BEEF&SUBSYS_00000000&REV_00\3&267a616a&0&10')
    
    key = wreg.CreateKey(wreg.HKEY_LOCAL_MACHINE, "System\\" + regfolder + "\\Services\\VBoxVideo")
    wreg.SetValue(key, 'Device0', wreg.REG_SZ, '')
    key = wreg.CreateKey(wreg.HKEY_LOCAL_MACHINE, "System\\" + regfolder + "\\Services\\VBoxVideo\\Device0")
    wreg.SetValueEx(key, 'Device Description', 0, wreg.REG_SZ, 'VirtualBox Graphics Adapter')
    wreg.SetValueEx(key, 'InstalledDisplayDrivers', 0, wreg.REG_MULTI_SZ, ['VBoxDisp'])
    
    key = wreg.CreateKey(wreg.HKEY_LOCAL_MACHINE, "System\\" + regfolder + "\\Services\\VBoxVideo")
    wreg.SetValue(key, 'Video', wreg.REG_SZ, '')
    key = wreg.CreateKey(wreg.HKEY_LOCAL_MACHINE, "System\\" + regfolder + "\\Services\\VBoxVideo\\Video")
    wreg.SetValueEx(key, 'Service', 0, wreg.REG_SZ, 'VBox Video')

key.Close()


print("Creating Files...")

for driverfiles in ["\\VBoxMouse.sys", "\\VBoxGuest.sys", "\\VBoxSF.sys", "\\VBoxVideo.sys",
                  "\\VBoxOGL.dll", "\\VBoxOGLarrayspu.dll", "\\VBoxOGLcrutil.dll", "\\VBoxOGLerrorspu.dll",
                  "\\VBoxOGLfeedbackspu.dll", "\\VBoxOGLfeedbackspu.dll", "\\VBoxOGLpackspu.dll", "\\VBoxOGLpassthroughspu.dll",
                  "\\VBoxService.exe", "\\VBoxControl.exe","\\VBoxTray.exe"] :
    f = open(sysfolder + driverfiles, "w")
f.close()


for file in ["VBoxHook.dll", "VBoxMRXNP.dll"]:
    try:
        with open(sysfolder + "\\" + file):
            pass
    except IOError:
        shutil.copyfile(cwd + "\\dll\\" + file, sysfolder + "\\" + file)


if not os.path.exists(pfilesvm):
    os.makedirs(pfilesvm)

for guestfiles in ["\\VBoxDisp.dll", "\\VBoxDrvInst.exe", "\\VBoxVideo.inf", "\\VBoxVideo.sys",
                  "\\DIFxAPI.dll", "\\iexplore.ico", "\\install_drivers.log", "\\uninst.exe",
                  "\\VBoxControl.exe", "\\VboxGuest.cat", "\\VboxGuest.inf", "\\VboxGuest.sys",
                  "\\VboxMouse.cat", "\\VboxMouse.inf", "\\VboxMouse.sys","\\VBoxTray.exe",
                  "\\VBoxWHQLFake.exe"] :
    f = open(pfilesvm + guestfiles, "w")
f.close()


if not os.path.exists(storeguest):
    os.makedirs(storeguest)
if not os.path.exists(storevideo):
    os.makedirs(storevideo)
for driverstorefiles in ["\\VBoxControl.exe","\\VBoxGuest.cat","\\VBoxGuest.inf", "\\VBoxGuest.sys", "\\VBoxTray.exe", 
                        "\\VBoxDisp.dll", "\\VBoxVideo.cat", "\\VBoxVideo.inf", "\\VBoxVideo.sys"] :
                        f = open(storeguest + driverstorefiles, "w")
f.close()

print ("Starting processes...")
print ("Done!")

for proc in ["VBoxService.exe", "wiresharck.exe", "regshot.exe", "procmon.exe", "filemon.exe", 
            "regmon.exe", "procdump.exe", "cports.exe", "procexp.exe", "squid.exe", "dumpcat.exe"]:
    os.system(cwd + "\\process\\" + proc)

