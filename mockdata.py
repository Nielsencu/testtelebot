from models import *

data = [
    (FoodSet(settype="selfservice", breakfastbool=True),"selfservice",True),
    (FoodSet(settype="western", breakfastbool=True),"western",True),
    (FoodSet(settype="noodle", breakfastbool=True),"noodle",True),
    (FoodSet(settype="asian", breakfastbool=True),"asian",True),
    (FoodSet(settype="asianveg", breakfastbool=True),"asianveg",True),
    (FoodSet(settype="malay", breakfastbool=True),"malay",True),
    (FoodSet(settype="halalveg", breakfastbool=True),"halalveg",True),
    (FoodSet(settype="grabngo", breakfastbool=True),"grabngo",True),

    (FoodSet(settype="selfservice", breakfastbool=False),"selfservice",False),
    (FoodSet(settype="western", breakfastbool=False),"western",False),
    (FoodSet(settype="noodle", breakfastbool=False),"noodle",False),
    (FoodSet(settype="asian", breakfastbool=False),"asian",False),
    (FoodSet(settype="veg", breakfastbool=False),"veg",False),
    (FoodSet(settype="malay", breakfastbool=False),"malay",False),
    (FoodSet(settype="indian", breakfastbool=False),"asian",False),
]