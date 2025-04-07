# -----------------------------------------------------------------------------
# Godlike Fuser Refreshrate Switcher
# Copyright (c) 2025 Sorted1 (github.com/Sorted1)
# This software is open-sourced under the GNU General Public License (GPL).
# See the LICENSE file for more information.
# ---------------------------------------------------------------------------

import ctypes
import fade
import os

CDS_UPDATEREGISTRY = 0x01
CDS_TEST = 0x02
DISP_CHANGE_SUCCESSFUL = 0
CURRENT_SETS = -1

class DEVMODE(ctypes.Structure):
    _fields_ = [
        ("dmDeviceName", ctypes.c_wchar * 32),
        ("dmSpecVersion", ctypes.c_ushort),
        ("dmDriverVersion", ctypes.c_ushort),
        ("dmSize", ctypes.c_ushort),
        ("dmDriverExtra", ctypes.c_ushort),
        ("dmFields", ctypes.c_uint),
        ("dmOrientation", ctypes.c_short),
        ("dmPaperSize", ctypes.c_short),
        ("dmPaperLength", ctypes.c_short),
        ("dmPaperWidth", ctypes.c_short),
        ("dmScale", ctypes.c_short),
        ("dmCopies", ctypes.c_short),
        ("dmDefaultSource", ctypes.c_short),
        ("dmPrintQuality", ctypes.c_short),
        ("dmColor", ctypes.c_short),
        ("dmDuplex", ctypes.c_short),
        ("dmYResolution", ctypes.c_short),
        ("dmTTOption", ctypes.c_short),
        ("dmCollate", ctypes.c_short),
        ("dmFormName", ctypes.c_wchar * 32),
        ("dmLogPixels", ctypes.c_ushort),
        ("dmBitsPerPel", ctypes.c_uint),
        ("dmPelsWidth", ctypes.c_uint),
        ("dmPelsHeight", ctypes.c_uint),
        ("dmDisplayFlags", ctypes.c_uint),
        ("dmDisplayFrequency", ctypes.c_uint),
        ("dmICMMethod", ctypes.c_uint),
        ("dmICMIntent", ctypes.c_uint),
        ("dmMediaType", ctypes.c_uint),
        ("dmDitherType", ctypes.c_uint),
        ("dmReserved1", ctypes.c_uint),
        ("dmReserved2", ctypes.c_uint),
        ("dmPanningWidth", ctypes.c_uint),
        ("dmPanningHeight", ctypes.c_uint),
    ]

devmode = DEVMODE()
devmode.dmSize = ctypes.sizeof(DEVMODE)

BANNER_TEXT = """
                    ███████╗ ██████╗ ██████╗ ████████╗███████╗██████╗ 
                    ██╔════╝██╔═══██╗██╔══██╗╚══██╔══╝██╔════╝██╔══██╗
                    ███████╗██║   ██║██████╔╝   ██║   █████╗  ██║  ██║
                    ╚════██║██║   ██║██╔══██╗   ██║   ██╔══╝  ██║  ██║
                    ███████║╚██████╔╝██║  ██║   ██║   ███████╗██████╔╝
                    ╚══════╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═════╝ 
                            Godlike Fuser Refresh Rate Switcher
                                    github.com/Sorted1
───────────────────────────────────────────────────────────────────────────────────────────────
"""


def main():
    os.system('mode con: cols=96 lines=33')
    os.system("title github.com/Sorted1 ｜ Godlike Fuser Refreshrate Switcher ｜ github.com/Sorted1")
    os.system("cls")
    print(fade.purplepink(BANNER_TEXT))
    input("\nHit Enter To Continue")
    os.system("cls")
    print(fade.purplepink(BANNER_TEXT))
    if ctypes.windll.user32.EnumDisplaySettingsW(None, CURRENT_SETS, ctypes.byref(devmode)):
        print(f"Current refresh rate: {devmode.dmDisplayFrequency} Hz")
        
        try:
            choice = int(input("Enter the desired refresh rate (e.g., 60, 75, 120): "))
            devmode.dmDisplayFrequency = choice
            devmode.dmFields = 0x400000 

            result = ctypes.windll.user32.ChangeDisplaySettingsW(ctypes.byref(devmode), 0)

            if result == DISP_CHANGE_SUCCESSFUL:
                print(f"Refresh rate changed to {choice}Hz successfully.")
                input("Click Enter To Exit")
            else:
                print(f"Failed to change refresh rate. Error code: {result}")
                input("Click Enter To Exit")
        except ValueError:
            print("Invalid input. Please enter a numeric value for the refresh rate.")
            input("Click Enter To Exit")
    else:
        print("Could not retrieve display settings.")
        input("Click Enter To Exit")

main()