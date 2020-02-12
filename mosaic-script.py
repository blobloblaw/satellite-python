
# ADVANDED DIGITAL IMAGE PROCESSING
# RS 6023
# CENTRE OF GEOGRAPHIC SCIENCES, LAWRENCETOWN, NOVA SCOTIA
# ASSINGMENT 2
#
# CREATED BY ROB MCEWAN, JANUARY 20 2020
#
# LANDSAT 8 PREPROCESSING AND MOSAICING
#
# FOR EDUCATIONAL PURPOSES ONLY
#
# BE SURE TO CHANGE FILE PATHS
# -----------------------------------------------------------------------------



import os
import shutil
from pci.hazerem import hazerem
from pci.atcor import atcor
from pci.automos import automos
from pci.mosprep import mosprep


j = os.path.join


# direct to images
scene1 = r"E:\AdvDigImageProc-6023\Asn2\Landsat\scene1\LC08_L1TP_001073_20191216_20191226_01_T1_MTL.txt-MS"
scene2 = r"E:\AdvDigImageProc-6023\Asn2\Landsat\scene2\LC08_L1TP_233073_20200126_20200126_01_RT_MTL.txt-MS"
scene3 = r"E:\AdvDigImageProc-6023\Asn2\Landsat\scene3\LC08_L1TP_233074_20200126_20200126_01_RT_MTL.txt-MS"
scene4 = r"E:\AdvDigImageProc-6023\Asn2\Landsat\scene4\LC08_L1TP_001074_20191216_20191226_01_T1_MTL.txt-MS"
scene5 = r"E:\AdvDigImageProc-6023\Asn2\Landsat\scene5\LC08_L1TP_233075_20200126_20200126_01_RT_MTL.txt-MS"
scene6 = r"E:\AdvDigImageProc-6023\Asn2\Landsat\scene6\LC08_L1TP_232074_20191218_20191226_01_T1_MTL.txt-MS"
scene7 = r"E:\AdvDigImageProc-6023\Asn2\Landsat\scene7\LC08_L1TP_002074_20200124_20200128_01_T1_MTL.txt-MS"
scene8 = r"E:\AdvDigImageProc-6023\Asn2\Landsat\scene8\LC08_L1TP_002073_20200124_20200128_01_T1_MTL.txt-MS"

scenes = [scene1, scene2, scene3, scene4, scene5, scene6, scene7, scene8]



# create function for reproducability
def folder_generator(algorithm):
    if os.path.exists(r"E:\AdvDigImageProc-6023\Asn2\{}".format(algorithm)):
        print("[INFO] {} folder exists, removing...".format(algorithm))
        shutil.rmtree(r"E:\AdvDigImageProc-6023\Asn2\{}".format(algorithm))
        print("[INFO] {} folder created".format(algorithm))
    if not os.path.exists(r"E:\AdvDigImageProc-6023\Asn2\{}".format(algorithm)):
        os.mkdir(r"E:\AdvDigImageProc-6023\Asn2\{}".format(algorithm))
        print("[INFO] {} folder created".format(algorithm))


# HAZE REMOVAL
# ----------------------------------------------------------------------

 apply folder creation function
folder_generator("HAZEREM")
# create variable for output path
hazeout = r"E:\AdvDigImageProc-6023\Asn2\HAZEREM"
print("[INFO] initializing haze removal")

# remove haze from multispec input images
# scene 3 commented out, haze removed causing strange artifacts

hazerem(fili=scene1, hazecov=[10], filo=j(hazeout,"hazefree1_ms.pix"))
print("[INFO] Haze removal applied, hazecov=20")

hazerem(fili=scene2, hazecov=[10], filo=os.path.join(hazeout,"hazefree2_ms.pix"))
print("[INFO] Haze removal applied, hazecov=10")

hazerem(fili=scene3, hazecov=[10], filo=os.path.join(hazeout,"hazefree3_ms.pix"))
print("[INFO] Haze removal applied, hazecov=5")

hazerem(fili=scene4, hazecov=[10], filo=os.path.join(hazeout,"hazefree4_ms.pix"))
print("[INFO] Haze removal applied, hazecov=10")

hazerem(fili=scene5, hazecov=[10], filo=os.path.join(hazeout,"hazefree5_ms.pix"))
print("[INFO] Haze removal applied, hazecov=5")

hazerem(fili=scene6, hazecov=[10], filo=os.path.join(hazeout,"hazefree6_ms.pix"))
print("[INFO] Haze removal applied, hazecov=10")

def hazeremove(scenes):
    for index, values in enumerate(scenes, start=1):
        print("[INFO] (",index,"/",len(scenes),")Haze removal initializing")
        hazerem(fili=values, hazecov=[10], filo=j(hazeout,"hazefree{}.pix".format(index)))
        print("[INFO] (",index,"/",len(scenes),") Haze removal applied, hazecov=10")

hazeremove(scenes)
    


# ATMOSPHERIC CORRECTION
# --------------------------------------------------------------------------

# create folder, point to input and output directories
folder_generator("ATCOR")
atin = hazeout
atout = r"E:\AdvDigImageProc-6023\Asn2\ATCOR"
print("[INFO] initializing atmospheric correction")

# apply correction

atcor(fili=j(atin, "hazefree1_ms.pix"), filo=j(atout, "atcor1.pix"),
      atmdef="Rural", atmcond="Tropical", outunits="scaled_reflectance[10]",
      sazangl=[31.085217,92.990616], meanelev=[3827.50])
print("[INFO] (1/6) atmospheric correction applied, atmdef=rural, atmcond=tropical, adjacen=ON, outunits=10, sazangle=[31.085217,92.990616], meanelev=3827.50")

atcor(fili=j(atin, "hazefree2_ms.pix"), filo=j(atout, "atcor2.pix"),
      atmdef="Rural", atmcond="Tropical", outunits="scaled_reflectance[10]",
      sazangl=[31.085217,92.990616], meanelev=[3827.50])
print("[INFO] (2/6) atmospheric correction applied, atmdef=rural, atmcond=tropical, adjacen=ON, outunits=10, sazangle=[31.085217,92.990616], meanelev=3827.50")

atcor(fili=j(atin, "hazefree3_ms.pix"), filo=j(atout, "atcor3.pix"),
      atmdef="Rural", atmcond="Tropical", outunits="scaled_reflectance[10]",
      sazangl=[31.085217,92.990616], meanelev=[3827.50])
print("[INFO] (3/6) atmospheric correction applied, atmdef=rural, atmcond=tropical, adjacen=ON, outunits=10, sazangle=[31.085217,92.990616], meanelev=3827.50")

atcor(fili=j(atin, "hazefree4_ms.pix"), filo=j(atout, "atcor4.pix"),
      atmdef="Rural", atmcond="Tropical", outunits="scaled_reflectance[10]",
      sazangl=[31.085217,92.990616], meanelev=[3827.50])
print("[INFO] (4/6) atmospheric correction applied, atmdef=rural, atmcond=tropical, adjacen=ON, outunits=10, sazangle=[31.085217,92.990616], meanelev=3827.50")

atcor(fili=j(atin, "hazefree5_ms.pix"), filo=j(atout, "atcor5.pix"),
      atmdef="Rural", atmcond="Tropical", outunits="scaled_reflectance[10]",
      sazangl=[31.085217,92.990616], meanelev=[3827.50])
print("[INFO] (5/6) atmospheric correction applied, atmdef=rural, atmcond=tropical, adjacen=ON, outunits=10, sazangle=[31.085217,92.990616], meanelev=3827.50")

atcor(fili=j(atin, "hazefree6_ms.pix"), filo=j(atout, "atcor6.pix"),
      atmdef="Rural", atmcond="Tropical", outunits="scaled_reflectance[10]",
      sazangl=[31.085217,92.990616], meanelev=[3827.50])
print("[INFO] (6/6) atmospheric correction applied, atmdef=rural, atmcond=tropical, adjacen=ON, outunits=10, sazangle=[31.085217,92.990616], meanelev=3827.50")




def atcorrect():
    hazefiles = os.listdir("E:\AdvDigImageProc-6023\Asn2\HAZEREM")
    for index, values in enumerate(hazefiles, start=1):
        print("[INFO] (",index,"/",len(hazefiles),") Initializing atmospheric correction")
        atcor(fili=j(hazeout,values), filo=j(atout, "atcor{}.pix".format(index)),
              atmdef="Rural", atmcond="Tropical", outunits="scaled_reflectance[10]",
              sazangl=[31.085217,92.990616], meanelev=[3827.50])
        print("[INFO] (",index,"/",len(hazefiles),") Atmospheric correction applied, atmdef=rural, atmcond=tropical, adjacen=ON, outunits=10, sazangle=[31.085217,92.990616], meanelev=3827.50")
        
    
atcorrect() 



# AUTOMOS
# --------------------------------------------------------------------------

# create folder, point to input and output directories
folder_generator("AUTOMOS")
autom_in = atout
autom_out = r"E:\AdvDigImageProc-6023\Asn2\AUTOMOS"
print("[INFO] Initializing automosaic module")

automos(mfile=autom_in, mostype="full", filo=j(autom_out, "automosaic3.pix"),
        startimg="atcor1.pix", radiocor="adaptive", balmthd="overlap",
        dbiclist="7,3,2", cutmthd="mindiff")
print("[INFO] automosaic complete, mostype=full, startingimg=atcor1.pix, radiocor=adaptive, \nbalmthd=overlap, cutmthd=mindiff, all other parameters set to default")




 
                                    










