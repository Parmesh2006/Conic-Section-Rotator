#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
from fractions import Fraction
import time
from sympy import *

################################################################### ORIGINAL CLASS {START} ####################################################################
# BOLD CLASS (to bold text) #
class color:
    BOLD = '\033[1m'
    END = '\033[0m'

# Inverse Cotangent Function. Necessary for finding the angle of rotation for a conic section #
def cotInv(x: int or float) -> int or float:
    # cotInv x = pi/2 - tan^-1(x)
    cotInverse: float = ((math.pi) / 2) - math.atan(x)
    return cotInverse

# Class Definition #

class Conics:
    def __init__(self) -> None:
        self.ConicParts = self.ConicParts()
        self.ConicClassifier = self.ConicClassifier()
        self.ConicAngleRotation = self.ConicAngleRotation()
        self.ConicRotator = self.ConicRotator()
        self.ConicStatistics = self.ConicStatistics()

    #################################################### FUNCTION SPLIT ####################################################
    def ConicParts(conicEquations: str) -> dict:
        if ("=" in conicEquations):
            conicEquation: str = conicEquations.split("=")[0]
            equals: str = conicEquations.split("=")[1]

            if (int(equals) == 0):
                if ((" " and "-") in conicEquation):
                    conicEquation: str = "+-".join(("".join(conicEquation.split(" "))).split("-"))
                elif (" " in conicEquation):
                    conicEquation: str = "".join(conicEquation.split(" "))
                else:
                    pass

                PlusSplit: list = conicEquation.split("+")
            else:
                if ((" " and "-") in conicEquation):
                    conicEquation: str = "+-".join(("".join(conicEquation.split(" "))).split("-"))
                elif (" " in conicEquation):
                    conicEquation: str = "".join(conicEquation.split(" "))
                else:
                    pass

                PlusSplit: list = conicEquation.split("+")
                if equals != "0":
                    if float(equals) > 0:
                        PlusSplit.append(f"-{float(equals)}".replace(" ", ""))
                    else:
                        PlusSplit.append(f"{-float(equals)}")
            
            # Naming the values A, B, C, D, E, F according to the base equation given above #
            abcdef: dict = dict() # The dictionary that holds the value of A, B, C, D, E, and F #
            
            # Adding the values of A, B, C, D, E, F to abcdef #
            for i in PlusSplit:
                if ("x^2" in i):
                    if ("*" not in i):
                        abcdef["A"] = 1.0
                    else:
                        i = i.replace("*x^2", "")
                        abcdef["A"] = float(i)
                elif ("x*y" in i):
                    if ("x" == i[0]):
                        abcdef["B"] = 1.0
                    else:
                        i = i.replace("*x*y", "")
                        abcdef["B"] = float(i)
                elif ("y^2" in i):
                    if ("*" not in i):
                        abcdef["C"] = 1.0
                    else:
                        i = i.replace("*y^2", "")
                        abcdef["C"] = float(i)
                elif ("x" in i):
                    if ("*" not in i):
                        abcdef["D"] = 1.0
                    else:
                        i = i.replace("*x", "")
                        abcdef["D"] = float(i)
                elif ("y" in i):
                    if ("*" not in i):
                        abcdef["E"] = 1.0
                    else:
                        i = i.replace("*y", "")
                        abcdef["E"] = float(i)
                else:
                    abcdef["F"] = float(i)

            sortedAbcdef: dict = sorted(abcdef.keys())
            newDict: dict = dict()

            # Setting Other Values to Zero to Prevent Error #
            if ("A" not in newDict.keys()):
                newDict["A"] = 0
            if ("B" not in newDict.keys()):
                newDict["B"] = 0
            if ("C" not in newDict.keys()):
                newDict["C"] = 0
            if ("D" not in newDict.keys()):
                newDict["D"] = 0
            if ("E" not in newDict.keys()):
                newDict["E"] = 0
            if ("F" not in newDict.keys()):
                newDict["F"] = 0

            for i in range(0, len(sortedAbcdef)):
                newDict[sortedAbcdef[i]] = abcdef[sortedAbcdef[i]]
            
            return newDict
    def ConicClassifier(conicEquations: str) -> str:
        ################################################ PREPROCESSING START ################################################
        if ("=" in conicEquations):
            conicEquation: str = conicEquations.split("=")[0]
            equals: str = conicEquations.split("=")[1]

            if (int(equals) == 0):
                if ((" " and "-") in conicEquation):
                    conicEquation: str = "+-".join(("".join(conicEquation.split(" "))).split("-"))
                elif (" " in conicEquation):
                    conicEquation: str = "".join(conicEquation.split(" "))
                else:
                    pass

                PlusSplit: list = conicEquation.split("+")
            else:
                if ((" " and "-") in conicEquation):
                    conicEquation: str = "+-".join(("".join(conicEquation.split(" "))).split("-"))
                elif (" " in conicEquation):
                    conicEquation: str = "".join(conicEquation.split(" "))
                else:
                    pass

                PlusSplit: list = conicEquation.split("+")
                if equals != "0":
                    if float(equals) > 0:
                        PlusSplit.append(f"-{float(equals)}".replace(" ", ""))
                    else:
                        PlusSplit.append(f"{-float(equals)}")
            
            # Naming the values A, B, C, D, E, F according to the base equation given above #
            abcdef: dict = dict() # The dictionary that holds the value of A, B, C, D, E, and F #
            
            # Adding the values of A, B, C, D, E, F to abcdef #
            for i in PlusSplit:
                if ("x^2" in i):
                    if ("*" not in i):
                        abcdef["A"] = 1.0
                    else:
                        i = i.replace("*x^2", "")
                        abcdef["A"] = float(i)
                elif ("x*y" in i):
                    if ("x" == i[0]):
                        abcdef["B"] = 1.0
                    else:
                        i = i.replace("*x*y", "")
                        abcdef["B"] = float(i)
                elif ("y^2" in i):
                    if ("*" not in i):
                        abcdef["C"] = 1.0
                    else:
                        i = i.replace("*y^2", "")
                        abcdef["C"] = float(i)
                elif ("x" in i):
                    if ("*" not in i):
                        abcdef["D"] = 1.0
                    else:
                        i = i.replace("*x", "")
                        abcdef["D"] = float(i)
                elif ("y" in i):
                    if ("*" not in i):
                        abcdef["E"] = 1.0
                    else:
                        i = i.replace("*y", "")
                        abcdef["E"] = float(i)
                else:
                    abcdef["F"] = float(i)

            sortedAbcdef: dict = sorted(abcdef.keys())
            newDict: dict = dict()

            for i in range(0, len(sortedAbcdef)):
                newDict[sortedAbcdef[i]] = abcdef[sortedAbcdef[i]]

            # Setting Other Values to Zero to Prevent Error #
            if ("A" not in newDict.keys()):
                newDict["A"] = 0
            if ("B" not in newDict.keys()):
                newDict["B"] = 0
            if ("C" not in newDict.keys()):
                newDict["C"] = 0
            if ("D" not in newDict.keys()):
                newDict["D"] = 0
            if ("E" not in newDict.keys()):
                newDict["E"] = 0
            if ("F" not in newDict.keys()):
                newDict["F"] = 0
            ################################################ PREPROCESSING END ################################################

            ################################################ CLASSIFYING START ################################################
            # Ax^2 + Bxy + Cy^2 + Dx + Ey + F = 0 #
            # if A == C: circle #
            # if (x^2 present and y^2 not present) or (x^2 not present and y^2 present): parabola #
            # if (coef(x^2) != coef(y^2)) and ((coef(x^2) and coef(y^2)) is positive): ellipse #
            # if (coef(x^2) != coef(y^2)) and (((coef(x^2) is positive) and (coef(y^2) is negative))): hyperbola #

            if (newDict["A"] == newDict["C"]):
                return ("\tCIRCLE")
            elif ((("A" in newDict.keys()) and ("C" not in newDict.keys())) or (("A" not in newDict.keys()) and ("C" not in newDict.keys()))):
                return ("\tPARABOLA")
            elif ((newDict["A"] != newDict["C"]) and ((newDict["A"] > 0) and (newDict["C"] > 0))):
                return ("\tELLIPSE")
            elif ((newDict["A"] != newDict["C"]) and (((newDict["A"] > 0) and (newDict["C"] < 0)) or ((newDict["A"] < 0) and (newDict["C"] > 0)))):
                return ("\tHYPERBOLA")
            else:
                # Most likely never going to happen... #
                return ("\tInvalid Equation\n")
            ################################################ CLASSIFYING END ##################################################
        else:
            return ("\tNo `=` in equation or `= 0` in equation.\n")

    #################################################### FUNCTION SPLIT ####################################################
    def ConicAngleRotation(conicEquations: str) -> str:
        if ("=" in conicEquations):
            conicEquation: str = (conicEquations.split("="))[0]
            equals: str = (conicEquations.split("="))[1]

            if (int(equals) == 0):
                if ((" " and "-") in conicEquation):
                    conicEquation: str = "+-".join(("".join(conicEquation.split(" "))).split("-"))
                elif (" " in conicEquation):
                    conicEquation: str = "".join(conicEquation.split(" "))
                else:
                    pass

                PlusSplit: list = conicEquation.split("+")
            else:
                if ((" " and "-") in conicEquation):
                    conicEquation: str = "+-".join(("".join(conicEquation.split(" "))).split("-"))
                elif (" " in conicEquation):
                    conicEquation: str = "".join(conicEquation.split(" "))
                else:
                    pass

                PlusSplit: list = conicEquation.split("+")
                if equals != "0":
                    if float(equals) > 0:
                        PlusSplit.append(f"-{float(equals)}".replace(" ", ""))
                    else:
                        PlusSplit.append(f"{-float(equals)}")
            
            # Naming the values A, B, C, D, E, F according to the base equation given above #
            abcdef: dict = dict() # The dictionary that holds the value of A, B, C, D, E, and F #
            
            # Adding the values of A, B, C, D, E, F to abcdef #
            for i in PlusSplit:
                if ("x^2" in i):
                    if ("*" not in i):
                        abcdef["A"] = 1.0
                    else:
                        i = i.replace("*x^2", "")
                        abcdef["A"] = float(i)
                elif ("x*y" in i):
                    if ("x" == i[0]):
                        abcdef["B"] = 1.0
                    else:
                        i = i.replace("*x*y", "")
                        abcdef["B"] = float(i)
                elif ("y^2" in i):
                    if ("*" not in i):
                        abcdef["C"] = 1.0
                    else:
                        i = i.replace("*y^2", "")
                        abcdef["C"] = float(i)
                elif ("x" in i):
                    if ("*" not in i):
                        abcdef["D"] = 1.0
                    else:
                        i = i.replace("*x", "")
                        abcdef["D"] = float(i)
                elif ("y" in i):
                    if ("*" not in i):
                        abcdef["E"] = 1.0
                    else:
                        i = i.replace("*y", "")
                        abcdef["E"] = float(i)
                else:
                    abcdef["F"] = float(i)

            sortedAbcdef: dict = sorted(abcdef.keys())
            newDict: dict = dict()

            for i in range(0, len(sortedAbcdef)):
                newDict[sortedAbcdef[i]] = abcdef[sortedAbcdef[i]]

            # Setting Other Values to Zero to Prevent Error #
            if ("A" not in newDict.keys()):
                newDict["A"] = 0
            if ("B" not in newDict.keys()):
                newDict["B"] = 0
            if ("C" not in newDict.keys()):
                newDict["C"] = 0
            if ("D" not in newDict.keys()):
                newDict["D"] = 0
            if ("E" not in newDict.keys()):
                newDict["E"] = 0
            if ("F" not in newDict.keys()):
                newDict["F"] = 0

            angleOfRotation: float = (cotInv((newDict["A"] - newDict["C"]) / newDict["B"]) / 2) / math.pi
            newAngleRot: str = str(nsimplify(math.sin(angleOfRotation), rational=False))

            return f"Angle Of Rotation: ({newAngleRot})π"
    def ConicRotator(conicEquations: str) -> str:
        if ("=" in conicEquations):
            ################################################ PREPROCESSING START ################################################
            conicEquation: str = conicEquations.split("=")[0]
            equals: str = conicEquations.split("=")[1]

            if (int(equals) == 0):
                if ((" " and "-") in conicEquation):
                    conicEquation: str = "+-".join(("".join(conicEquation.split(" "))).split("-"))
                elif (" " in conicEquation):
                    conicEquation: str = "".join(conicEquation.split(" "))
                else:
                    pass

                PlusSplit: list = conicEquation.split("+")
            else:
                if ((" " and "-") in conicEquation):
                    conicEquation: str = "+-".join(("".join(conicEquation.split(" "))).split("-"))
                elif (" " in conicEquation):
                    conicEquation: str = "".join(conicEquation.split(" "))
                else:
                    pass

                PlusSplit: list = conicEquation.split("+")
                if equals != "0":
                    if float(equals) > 0:
                        PlusSplit.append(f"-{float(equals)}".replace(" ", ""))
                    else:
                        PlusSplit.append(f"{-float(equals)}")
            
            # Naming the values A, B, C, D, E, F according to the base equation given above #
            abcdef: dict = dict() # The dictionary that holds the value of A, B, C, D, E, and F #
            
            # Adding the values of A, B, C, D, E, F to abcdef #
            for i in PlusSplit:
                if ("x^2" in i):
                    if ("*" not in i):
                        abcdef["A"] = 1.0
                    else:
                        i = i.replace("*x^2", "")
                        abcdef["A"] = float(i)
                elif ("x*y" in i):
                    if ("x" == i[0]):
                        abcdef["B"] = 1.0
                    else:
                        i = i.replace("*x*y", "")
                        abcdef["B"] = float(i)
                elif ("y^2" in i):
                    if ("*" not in i):
                        abcdef["C"] = 1.0
                    else:
                        i = i.replace("*y^2", "")
                        abcdef["C"] = float(i)
                elif ("x" in i):
                    if ("*" not in i):
                        abcdef["D"] = 1.0
                    else:
                        i = i.replace("*x", "")
                        abcdef["D"] = float(i)
                elif ("y" in i):
                    if ("*" not in i):
                        abcdef["E"] = 1.0
                    else:
                        i = i.replace("*y", "")
                        abcdef["E"] = float(i)
                else:
                    abcdef["F"] = float(i)

            sortedAbcdef: dict = sorted(abcdef.keys())
            newDict: dict = dict()

            for i in range(0, len(sortedAbcdef)):
                newDict[sortedAbcdef[i]] = abcdef[sortedAbcdef[i]]

            # Setting Other Values to Zero to Prevent Error #
            if ("A" not in newDict.keys()):
                newDict["A"] = 0
            if ("B" not in newDict.keys()):
                newDict["B"] = 0
            if ("C" not in newDict.keys()):
                newDict["C"] = 0
            if ("D" not in newDict.keys()):
                newDict["D"] = 0
            if ("E" not in newDict.keys()):
                newDict["E"] = 0
            if ("F" not in newDict.keys()):
                newDict["F"] = 0
            ################################################ PREPROCESSING END ################################################

            ################################################# MECHANICS START #################################################
            # Getting Angle of Rotation using newDict's values of A, B, C, D, E, and F in radians #
            angleOfRotation: str = (cotInv((newDict["A"] - newDict["C"]) / newDict["B"]) / 2)

            FracSinAngle: str = str(nsimplify(math.sin(angleOfRotation), rational=False))
            FracCosAngle: str = str(nsimplify(math.cos(angleOfRotation), rational=False))
            FracSinTimesFracCos: str = str(nsimplify(math.cos(angleOfRotation) * nsimplify(math.sin(angleOfRotation)), rational=False))
            FracSinAngleSquared: str = str(nsimplify(math.sin(angleOfRotation) ** 2, rational=False))
            FracCosAngleSquared: str = str(nsimplify(math.cos(angleOfRotation) ** 2, rational=False))


            xPart: str = f"[({FracCosAngle})(x')-({FracSinAngle})(y')]"
            yPart: str = f"[({FracSinAngle})(x')+({FracCosAngle})(y')]"

            rotatedConicEquation: str = ""
            for char in conicEquations.replace(" ", ""):
                if (char == "x"):
                    rotatedConicEquation += xPart
                elif (char == "y"):
                    rotatedConicEquation += yPart
                elif (char == "*"):
                    pass
                else:
                    rotatedConicEquation += char
            
            if (f"{xPart}{yPart}" in rotatedConicEquation):
                rotatedConicEquation: str = rotatedConicEquation.replace(f"{xPart}{yPart}", f"[((x')^2)({FracSinTimesFracCos}) + (x')(y')({FracCosAngleSquared}) - (x')(y')({FracSinAngleSquared})]")

                newRotatedConicEquation: str = ""

                for i in rotatedConicEquation:
                    if (i == "+"):
                        newRotatedConicEquation += " + "
                    elif (i == "-"):
                        newRotatedConicEquation += " - "
                    elif (i == "*"):
                        newRotatedConicEquation += " * "
                    elif (i == "="):
                        newRotatedConicEquation += " = "
                    else:
                        newRotatedConicEquation += i
            else:
                newRotatedConicEquation: str = ""
                

                for i in rotatedConicEquation:
                    if (i == "+"):
                        newRotatedConicEquation += " + "
                    elif (i == "-"):
                        newRotatedConicEquation += " - "
                    elif (i == "*"):
                        newRotatedConicEquation += " * "
                    elif (i == "="):
                        newRotatedConicEquation += " = "
                    else:
                        newRotatedConicEquation += i

            if ("sqrt" in newRotatedConicEquation):
                newRotatedConicEquation: str = "√".join(newRotatedConicEquation.split("sqrt"))
            else:
                pass
            ################################################# MECHANICS END #################################################

            ################################################# OUTPUT START #################################################
            # Whew! Print out final result after rotation #
            return (f"{f'{newRotatedConicEquation}'}")
            ################################################# OUTPUT END #################################################
        else:
            return ("No `=` in equation or `= 0` in equation.")
    #################################################### FUNCTION SPLIT ####################################################
    def ConicStatistics(conicEquations: str) -> str:
        def Quadratic(expr: str, var: str) -> str:
            newExprSplit: list = expr.split("+")
            ABCdict: dict = dict()

            for i in newExprSplit:
                if ("^2" in i):
                    if "*" in i:
                        ABCdict["A"] = float(i.replace(f"*{var}^2", ""))
                    else:
                        ABCdict["A"] = 1
                else:
                    ABCdict["A"] = 0.0
                
                if ((var in i) and ("^2" not in i)):
                    if "*" in i:
                        ABCdict["B"] = float(i.replace(f"*{var}", ""))
                    else:
                        ABCdict["B"] = 1
                else:
                    ABCdict["B"] = 0.0

                if (var not in i) and (i != ''):
                    ABCdict["C"] = float(i)
                else:
                    ABCdict["C"] = 0.0

            firstZero: float = (-1 * ABCdict["B"]) + ((ABCdict["B"] ** 2 - 4 * ABCdict["A"] * ABCdict["C"]) ** 0.5)
            secondZero: float = (-1 * ABCdict["B"]) - ((ABCdict["B"] ** 2 - 4 * ABCdict["A"] * ABCdict["C"]) ** 0.5)

            return (f"\n\n\tFirst Zero: {firstZero}\n\tSecond Zero: {secondZero}")
        def Zeros(conic: str) -> None: # X-INTERCEPTS #  # MAKE SURE CONIC IS SET EQUAL TO ZERO #
            if " " in conic:
                conic: str = "".join(conic.split(" "))
            if "-" in conic:
                conic: str = "+-".join(conic.split("-"))

            # If Zeros, x is a value and Y IS 0 #
            conicList: list = conic.split("+")
            newPart: list = []

            for i in conicList:
                if ("y" in i):
                    pass
                else:
                    newPart.append(i)

            newQuadratic: str = ("".join(("+".join(newPart)).split("-"))).replace("=0", "")
            ans: str = "x-intercept".join(Quadratic(newQuadratic, "x").split("Zero"))

            return (f"{f'{ans}'} -> Can be not real. Can be imaginary (meaning not visible on graph)")
        def yIntercept(conic: str) -> None: # Y-INTERCEPTS # # MAKE SURE CONIC IS SET EQUAL TO ZERO #
            if " " in conic:
                conic: str = "".join(conic.split(" "))
            if "-" in conic:
                conic: str = "+-".join(conic.split("-"))

            # If Zeros, x is a value and Y IS 0 #
            conicList: list = conic.split("+")
            newPart: list = []

            for i in conicList:
                if ("x" in i):
                    pass
                else:
                    newPart.append(i)

            newQuadratic: str = ("".join(("+".join(newPart)).split("-"))).replace("=0", "")
            ans: str = "y-intercept".join(Quadratic(newQuadratic, "y").split("Zero"))

            return (f"\n\t{f'{ans}'} -> Can be not real. Can be imaginary (meaning not visible on graph)")
        def Center(conic: str) -> None:
            if " " in conic:
                conic: str = "".join(conic.split(" "))
            if "-" in conic:
                conic: str = "+-".join(conic.split("-"))

            conicList: list = conic.split("+")
            ABCdict: dict = dict()

            for i in conicList: # Ax^2 + Bxy + Cy^2 + Dx + Ey + F = 0 # -> ax^2 + 2bxy + cy^2 + 2dx + 2ey + f = 0
                if ("x^2" in i):
                    i: str = i.replace("x^2", "")
                    if (i == ""):
                        ABCdict["a"] = 1
                    else:
                        ABCdict["a"] = float(i.replace("*", ""))
                elif ("x*y" in i):
                    i: str = i.replace("x*y", "")
                    if (i == ""):
                        ABCdict["b"] = 0.5
                    else:
                        ABCdict["b"] = float(i.replace("*", "")) / 2
                elif ("y^2" in i):
                    i: str = i.replace("y^2", "")
                    if (i == ""):
                        ABCdict["c"] = 1
                    else:
                        ABCdict["c"] = float(i.replace("*", "").replace("=0", ""))
                elif ("x" in i):
                    i: str = i.replace("x", "")
                    if (i == ""):
                        ABCdict["d"] = 0.5
                    else:
                        ABCdict["d"] = float(i.replace("*", "")) / 2
                elif ("y" in i):
                    i: str = i.replace("y", "").replace("=0", "")
                    if (i == ""):
                        ABCdict["e"] = 0.5
                    else:
                        ABCdict["e"] = float(i.replace("*", "")) / 2
                else:
                    ABCdict["f"] = float(i.replace("=0", ""))

            letterList: list = ["a", "b", "c", "d", "e", "f"]
            for i in letterList:
                if (i not in ABCdict.keys()):
                    ABCdict[i] = 0
                else:
                    pass

            δ: str = ABCdict["a"] * ABCdict["c"] - (ABCdict["b"] ** 2) # delta (determinant) #

            xCenter: float = (ABCdict["b"] * ABCdict["e"] - ABCdict["c"] * ABCdict["d"]) / δ
            yCenter: float = (ABCdict["b"] * ABCdict["d"] - ABCdict["a"] * ABCdict["e"]) / δ

            return (f"\nCenter: ({f'{xCenter}'},{f'{yCenter}'}) -> Can be not real. Can be imaginary (meaning not visible on graph)")

        zeros: str = Zeros(conicEquations)
        yIntercepts: str = yIntercept(conicEquations)
        centerPoint: str = Center(conicEquations)
        return zeros, yIntercepts, centerPoint


# LEARNING OPTION #
class ConicRotatorLearn:
    def __init__(self) -> None:
        # Identify the parts of the conic #
        self.Step1_IdentifyThePartsOfTheConic = self.Step1_IdentifyThePartsOfTheConic()

        # How to find the angle of rotation step-by-step #
        self.Step2_FindTheAngleOfRotation_PartOne = self.Step2_FindTheAngleOfRotation_PartOne()
        self.Step2_FindTheAngleOfRotation_PartTwo = self.Step2_FindTheAngleOfRotation_PartTwo()
        self.Step2_FindTheAngleOfRotation_PartThree = self.Step2_FindTheAngleOfRotation_PartThree()
        self.Step2_FindTheAngleOfRotation_PartFour = self.Step2_FindTheAngleOfRotation_PartFour()
        self.Step2_FindTheAngleOfRotation_PartFive = self.Step2_FindTheAngleOfRotation_PartFive()
        self.Step2_FindTheAngleOfRotation_PartFinal = self.Step2_FindTheAngleOfRotation_PartFinal()

        # Calculate Sine and Cosine Of Angle #
        self.Step3_FindTheSineAngle = self.Step3_FindTheSineAngle()
        self.Step4_FindTheCosineAngle = self.Step4_FindTheCosineAngle()

        # Find New x's and y's #
        self.Step5_FindNewX_Part1 = self.Step5_FindNewX_Part1()
        self.Step5_FindNewX_PartFinal = self.Step5_FindNewX_PartFinal()

        self.Step6_FindNewY_Part1 = self.Step6_FindNewY_Part1()
        self.Step6_FindNewY_PartFinal = self.Step6_FindNewY_PartFinal()

        # Substitute New x's and y's #
        self.Step7_SubstituteFinal = self.Step7_SubstituteFinal()

        # Simplify #
        self.Step8_Simplify = self.Step8_Simplify()

    # Identify the parts of the conic #
    def Step1_IdentifyThePartsOfTheConic(ConicEquation: str) -> dict:
        return Conics.ConicParts(ConicEquation)

    # How to find the angle of rotation step-by-step #
    def Step2_FindTheAngleOfRotation_PartOne() -> str:
        return "cot(2Θ) = (A - C) / B"
    
    def Step2_FindTheAngleOfRotation_PartTwo(ConicEquation: str) -> str:
        parts: dict = Conics.ConicParts(ConicEquation)
        return f"cot(2Θ) = ({parts['A']} - {parts['C']}) / {parts['B']}"

    def Step2_FindTheAngleOfRotation_PartThree(ConicEquation: str) -> str:
        parts: dict = Conics.ConicParts(ConicEquation)
        return f"2Θ = cot⁻¹(({parts['A'] - parts['C']}) / {parts['B']}) r"
    
    def Step2_FindTheAngleOfRotation_PartFour(ConicEquation: str) -> str:
        parts: dict = Conics.ConicParts(ConicEquation)
        return f"2Θ = cot⁻¹({(parts['A'] - parts['C']) / parts['B']}) r"
    
    def Step2_FindTheAngleOfRotation_PartFive(ConicEquation: str) -> str:
        parts: dict = Conics.ConicParts(ConicEquation)
        return f"Θ = [cot⁻¹({(parts['A'] - parts['C']) / parts['B']}) / 2] r"
    
    def Step2_FindTheAngleOfRotation_PartFinal(ConicEquation: str) -> str:
        parts: dict = Conics.ConicParts(ConicEquation)
        return f"Θ = ({str(nsimplify(nsimplify(cotInv(((parts['A'] - parts['C']) / (parts['B']))) / 2, rational=False) / math.pi, rational=False))})π r"

    # Calculate Sine and Cosine Of Angle #
    def Step3_FindTheSineAngle(ConicEquation: str) -> str:
        parts: dict = Conics.ConicParts(ConicEquation)
        if str(nsimplify(math.sin(cotInv(((parts['A'] - parts['C']) / (parts['B']))) / 2), rational=False)) == '6.12323399573677e-17':
            return f"sin(Θ) = 0"
        return f"sin(Θ) = {str(nsimplify(math.sin(cotInv(((parts['A'] - parts['C']) / (parts['B']))) / 2), rational=False))}"
    
    def Step4_FindTheCosineAngle(ConicEquation: str) -> str:
        parts: dict = Conics.ConicParts(ConicEquation)
        if str(nsimplify(math.cos(cotInv(((parts['A'] - parts['C']) / (parts['B']))) / 2), rational=False)) == '6.12323399573677e-17':
            return f"cos(Θ) = 0"
        return f"cos(Θ) = {str(nsimplify(math.sin(cotInv(((parts['A'] - parts['C']) / (parts['B']))) / 2), rational=False))}"

    # Find New x's and y's #
    def Step5_FindNewX_Part1() -> str:
        return f"x = x'cos(Θ) - y'sin(Θ)"

    def Step5_FindNewX_PartFinal(ConicEquation: str) -> str:
        def Step3_FindTheSineAngle(ConicEquation: str) -> str:
            parts: dict = Conics.ConicParts(ConicEquation)
            if str(nsimplify(math.sin(cotInv(((parts['A'] - parts['C']) / (parts['B']))) / 2), rational=False)) == '6.12323399573677e-17':
                return f"sin(Θ) = 0"
            return f"sin(Θ) = {str(nsimplify(math.sin(cotInv(((parts['A'] - parts['C']) / (parts['B']))) / 2), rational=False))}"
        def Step4_FindTheCosineAngle(ConicEquation: str) -> str:
            parts: dict = Conics.ConicParts(ConicEquation)
            if str(nsimplify(math.cos(cotInv(((parts['A'] - parts['C']) / (parts['B']))) / 2), rational=False)) == '6.12323399573677e-17':
                return f"cos(Θ) = 0"
            return f"cos(Θ) = {str(nsimplify(math.sin(cotInv(((parts['A'] - parts['C']) / (parts['B']))) / 2), rational=False))}"

        sine: str = Step3_FindTheSineAngle(ConicEquation).replace("sin(Θ) = ", "")
        cosine: str = Step4_FindTheCosineAngle(ConicEquation).replace("cos(Θ) = ", "")

        return f"x = [({cosine})(x') - ({sine})(y')]"

    def Step6_FindNewY_Part1() -> str:
        return f"y = x'sin(Θ) + y'cos(Θ)"

    def Step6_FindNewY_PartFinal(ConicEquation: str) -> str:
        def Step3_FindTheSineAngle(ConicEquation: str) -> str:
            parts: dict = Conics.ConicParts(ConicEquation)
            if str(nsimplify(math.sin(cotInv(((parts['A'] - parts['C']) / (parts['B']))) / 2), rational=False)) == '6.12323399573677e-17':
                return f"sin(Θ) = 0"
            return f"sin(Θ) = {str(nsimplify(math.sin(cotInv(((parts['A'] - parts['C']) / (parts['B']))) / 2), rational=False))}"
        def Step4_FindTheCosineAngle(ConicEquation: str) -> str:
            parts: dict = Conics.ConicParts(ConicEquation)
            if str(nsimplify(math.cos(cotInv(((parts['A'] - parts['C']) / (parts['B']))) / 2), rational=False)) == '6.12323399573677e-17':
                return f"cos(Θ) = 0"
            return f"cos(Θ) = {str(nsimplify(math.sin(cotInv(((parts['A'] - parts['C']) / (parts['B']))) / 2), rational=False))}"
        
        sine: str = Step3_FindTheSineAngle(ConicEquation).replace("sin(Θ) = ", "")
        cosine: str = Step4_FindTheCosineAngle(ConicEquation).replace("cos(Θ) = ", "")

        return f"y = [({sine})(x') + ({cosine})(y')]"

    # Substitute New x's and y's #
    def Step7_SubstituteFinal(ConicEquation: str) -> str:
        def Step5_FindNewX_PartFinal(ConicEquation: str) -> str:
            def Step3_FindTheSineAngle(ConicEquation: str) -> str:
                parts: dict = Conics.ConicParts(ConicEquation)
                if str(nsimplify(math.sin(cotInv(((parts['A'] - parts['C']) / (parts['B']))) / 2), rational=False)) == '6.12323399573677e-17':
                    return f"sin(Θ) = 0"
                return f"sin(Θ) = {str(nsimplify(math.sin(cotInv(((parts['A'] - parts['C']) / (parts['B']))) / 2), rational=False))}"
            def Step4_FindTheCosineAngle(ConicEquation: str) -> str:
                parts: dict = Conics.ConicParts(ConicEquation)
                if str(nsimplify(math.cos(cotInv(((parts['A'] - parts['C']) / (parts['B']))) / 2), rational=False)) == '6.12323399573677e-17':
                    return f"cos(Θ) = 0"
                return f"cos(Θ) = {str(nsimplify(math.sin(cotInv(((parts['A'] - parts['C']) / (parts['B']))) / 2), rational=False))}"

            sine: str = Step3_FindTheSineAngle(ConicEquation).replace("sin(Θ) = ", "")
            cosine: str = Step4_FindTheCosineAngle(ConicEquation).replace("cos(Θ) = ", "")

            return f"[({cosine})(x') - ({sine})(y')]"
        def Step6_FindNewY_PartFinal(ConicEquation: str) -> str:
            def Step3_FindTheSineAngle(ConicEquation: str) -> str:
                parts: dict = Conics.ConicParts(ConicEquation)
                if str(nsimplify(math.sin(cotInv(((parts['A'] - parts['C']) / (parts['B']))) / 2), rational=False)) == '6.12323399573677e-17':
                    return f"sin(Θ) = 0"
                return f"sin(Θ) = {str(nsimplify(math.sin(cotInv(((parts['A'] - parts['C']) / (parts['B']))) / 2), rational=False))}"
            def Step4_FindTheCosineAngle(ConicEquation: str) -> str:
                parts: dict = Conics.ConicParts(ConicEquation)
                if str(nsimplify(math.cos(cotInv(((parts['A'] - parts['C']) / (parts['B']))) / 2), rational=False)) == '6.12323399573677e-17':
                    return f"cos(Θ) = 0"
                return f"cos(Θ) = {str(nsimplify(math.sin(cotInv(((parts['A'] - parts['C']) / (parts['B']))) / 2), rational=False))}"

            sine: str = Step3_FindTheSineAngle(ConicEquation).replace("sin(Θ) = ", "")
            cosine: str = Step4_FindTheCosineAngle(ConicEquation).replace("cos(Θ) = ", "")

            return f"[({sine})(x') + ({cosine})(y')]"
        
        PartX: str = (Step5_FindNewX_PartFinal(ConicEquation))
        PartY: str = (Step6_FindNewY_PartFinal(ConicEquation))

        NewConicEquation: str = ""

        for char in ConicEquation:
            if (char == "x"):
                NewConicEquation += PartX
            elif (char == "y"):
                NewConicEquation += PartY
            else:
                NewConicEquation += char
        
        return f"{NewConicEquation}"

    # Simplify #
    def Step8_Simplify(ConicEquation: str) -> str:
        def Step7_SubstituteFinal(ConicEquation: str) -> str:
            def Step5_FindNewX_PartFinal(ConicEquation: str) -> str:
                def Step3_FindTheSineAngle(ConicEquation: str) -> str:
                    parts: dict = Conics.ConicParts(ConicEquation)
                    if str(nsimplify(math.sin(cotInv(((parts['A'] - parts['C']) / (parts['B']))) / 2), rational=False)) == '6.12323399573677e-17':
                        return f"sin(Θ) = 0"
                    return f"sin(Θ) = {str(nsimplify(math.sin(cotInv(((parts['A'] - parts['C']) / (parts['B']))) / 2), rational=False))}"
                def Step4_FindTheCosineAngle(ConicEquation: str) -> str:
                    parts: dict = Conics.ConicParts(ConicEquation)
                    if str(nsimplify(math.cos(cotInv(((parts['A'] - parts['C']) / (parts['B']))) / 2), rational=False)) == '6.12323399573677e-17':
                        return f"cos(Θ) = 0"
                    return f"cos(Θ) = {str(nsimplify(math.sin(cotInv(((parts['A'] - parts['C']) / (parts['B']))) / 2), rational=False))}"

                sine: str = Step3_FindTheSineAngle(ConicEquation).replace("sin(Θ) = ", "")
                cosine: str = Step4_FindTheCosineAngle(ConicEquation).replace("cos(Θ) = ", "")

                return f"[({cosine})(x') - ({sine})(y')]"
            def Step6_FindNewY_PartFinal(ConicEquation: str) -> str:
                def Step3_FindTheSineAngle(ConicEquation: str) -> str:
                    parts: dict = Conics.ConicParts(ConicEquation)
                    if str(nsimplify(math.sin(cotInv(((parts['A'] - parts['C']) / (parts['B']))) / 2), rational=False)) == '6.12323399573677e-17':
                        return f"sin(Θ) = 0"
                    return f"sin(Θ) = {str(nsimplify(math.sin(cotInv(((parts['A'] - parts['C']) / (parts['B']))) / 2), rational=False))}"
                def Step4_FindTheCosineAngle(ConicEquation: str) -> str:
                    parts: dict = Conics.ConicParts(ConicEquation)
                    if str(nsimplify(math.cos(cotInv(((parts['A'] - parts['C']) / (parts['B']))) / 2), rational=False)) == '6.12323399573677e-17':
                        return f"cos(Θ) = 0"
                    return f"cos(Θ) = {str(nsimplify(math.sin(cotInv(((parts['A'] - parts['C']) / (parts['B']))) / 2), rational=False))}"

                sine: str = Step3_FindTheSineAngle(ConicEquation).replace("sin(Θ) = ", "")
                cosine: str = Step4_FindTheCosineAngle(ConicEquation).replace("cos(Θ) = ", "")

                return f"[({sine})(x') + ({cosine})(y')]"
            
            PartX: str = (Step5_FindNewX_PartFinal(ConicEquation))
            PartY: str = (Step6_FindNewY_PartFinal(ConicEquation))

            NewConicEquation: str = ""

            for char in ConicEquation:
                if (char == "x"):
                    NewConicEquation += PartX
                elif (char == "y"):
                    NewConicEquation += PartY
                else:
                    NewConicEquation += char
            
            return f"{NewConicEquation}"
        
        return Step7_SubstituteFinal(ConicEquation)
        

################################################################### ORIGINAL CLASS {END} ####################################################################
##################################################################################################################################################################################################################################################################
######################################################################## APP {START} ########################################################################
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash.dependencies as ddc
from dash.dependencies import Input, Output, State
from dash_html_components.Br import Br
from dash_html_components.P import P
from dash_html_components.Img import Img
from dash_core_components.Tab import Tab
from dash_core_components.RadioItems import RadioItems
from dash_core_components.Checklist import Checklist
from dash_html_components.Button import Button
import random

app = dash.Dash()
colors = {
    'background': '#073b4c',
    'backgroundNext': '#118ab2',
    'text': '#06d6a0',
    'text2': '#ef476f',
    'bodyBackground': '#ffd166',
    'white':'#ffffff',
    'lightBlue':'#3792cb'
}


app.layout = html.Div(style={'backgroundColor': colors['background'], "padding": "0", "margin": "0", "border": f"2px solid {colors['text2']}"}, children=[
    dcc.Tabs(id="AllTabsHolder", value="ConicHomeTab", children=[
        dcc.Tab(label="Home Page", id="HomeTab", value="ConicHomeTab", style={'font-weight': 'bold', 'backgroundColor':colors['backgroundNext'], 'color':colors['white']}, children=[
            html.H1(
                children='Home',
                style={
                    'textAlign': 'center',
                    'color': colors['text']
                }
            ),
            html.Div(style={'backgroundColor': colors['backgroundNext'], 'textAlign': 'center', 'color': colors['background'], 'font-weight': 'bold'}, 
                children='Dash: A web application framework for Python.'
            ),
            html.Div(style={'backgroundColor': colors['text2'], 'textAlign': 'center', 'color': colors['background'], 'font-weight': 'bold'}, 
                children='By: Parmeshvar Prakash'
            ),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Label('What Is A Conic?', style={'backgroundColor': colors['bodyBackground'], 'font-size': '200%', 'margin-left': '5%'}),
            html.Div(style={'font-size':'125%', 'margin-left': '0.5%'}, children=[
                html.P(
                    'The conic sections are the nondegenerate curves generated by the intersections of a plane with one or two nappes (one of the two cones set point to point) of a cone.',
                    style={'margin-left': '0.5%', 'color':colors['text']}
                ),
                html.Img(
                    src='https://www.shelovesmath.com/wp-content/uploads/2018/10/Conics-in-Cones.gif',
                    style={'margin-left': '0.5%'}
                ),
            ]),
            html.Br(),
            html.Br(),
            html.Label('What Are The Four Types Of Conics?', style={'backgroundColor': colors['bodyBackground'], 'font-size': '200%', 'margin-left': '5%'}),
            html.Div(style={'font-size':'125%', 'margin-left':'0.5%'}, children=[
                html.P(
                    "• Circle",
                    style={'margin-left':'8%', 'color': colors['text2']}
                ),
                html.Img(
                    src='https://uploads.desmos.com/activitybuilder/4ce9d06ab379b66bb5ca7c92f72c9e01',
                    style={'margin-left':'8%', 'color': colors['text2']}
                ),
                html.P(
                    "• Ellipse",
                    style={'margin-left':'8%', 'color': colors['text2']}
                ),
                html.Img(
                    src='https://www.softschools.com/math/calculus/images/graphing_ellipses_img22.png',
                    style={'margin-left':'8%', 'color': colors['text2']}
                ),
                html.P(
                    "• Parabola",
                    style={'margin-left':'8%', 'color': colors['text2']}
                ),
                html.Img(
                    src='https://useruploads.socratic.org/5ptsdt6SVmzgiF5QPfeS_2016-01-11_203936.jpg',
                    style={'margin-left':'8%', 'color': colors['text2']}
                ),
                html.P(
                    "• Hyperbola",
                    style={'margin-left':'8%', 'color': colors['text2']}
                ),
                html.Img(
                    src='http://cochranmath.pbworks.com/f/desmos-graph.png',
                    style={'margin-left':'8%', 'color': colors['text2'], 'width':'25%', 'height':'25%'}
                )
            ])
        ]),
        dcc.Tab(label="Conic Rotator Step-By-Step (Reccommended For Learning)", id="StepStepTab", value="StepStepTab", style={'font-weight': 'bold', 'backgroundColor':colors['backgroundNext'], 'color':colors['white']}, children=[
            html.H1(
                children='Conic Rotator Step-By-Step',
                style={
                    'textAlign': 'center',
                    'color': colors['text']
                }
            ),
            html.Div(style={'backgroundColor': colors['backgroundNext'], 'textAlign': 'center', 'color': colors['background'], 'font-weight': 'bold'}, 
                children='Dash: A web application framework for Python.'
            ),
            html.Div(style={'backgroundColor': colors['text2'], 'textAlign': 'center', 'color': colors['background'], 'font-weight': 'bold'}, 
                children='By: Parmeshvar Prakash'
            ),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Label('Enter Conic Equation Below (Simplify Radicals And Round To Nearest Millionth in Input): ', style={'backgroundColor': colors['bodyBackground'], 'font-size': '200%', 'margin-left': '5%'}),
            html.P(
                'Simplify Equation As Much As You Can Before Input (Combine Like Terms, etc.). Make sure final equation is in the form Ax^2 + Bxy + Cy^2 + Dx + Ey + F = 0. If any of A, B, C, D, E, or F equals 0, then leave it out.',
                style={'backgroundColor': colors['background'], 'color':colors['lightBlue'], 'font-size': '150%', 'padding': '1%', 'height':'auto', 'font-weight':'bold'}
            ),
            html.Br(),
            html.Div(children=[
                dcc.Input(value="Enter Equation Here", type="text", style={'font-size': '125%', 'margin-left': '0.5%', "padding": "12px 20px", 'backgroundColor': colors['text'], 'color': 'black', 'width': '50%'}, id="inputEq2"),
                html.Br(),
                html.Br(),
                dcc.Dropdown(
                    id="optionsForChoose",
                    options=[
                        {'label': 'Done', 'value': 'D'},
                        {'label': 'Not Done', 'value': 'N'}
                    ],
                    value='N',
                    style={'font-size': '110%', 'margin-left': '0.5%', "padding": "12px 20px", 'backgroundColor': colors['text'], 'color': 'black', 'width': '50%'}
                ),
                html.Br(),
                html.P(
                    'Output will be displayed below on the light blue colored box (text in white). Make sure there is an equal sign (=) in your equation.',
                    style={'backgroundColor': colors['background'], 'color':colors['white'], 'font-size': '150%', 'padding': '5%', 'height':'auto', 'font-weight':'bold'}
                )
            ]),
            html.Div(
                id="hiddenDiv",
                style={'display': 'none'}
            ),
            html.Div(
                id="tabsContent",
                style={'backgroundColor': colors['backgroundNext'], 'color':colors['text2'], 'font-size': '100%', 'padding': '5%', 'height':'auto', 'font-weight':'bold'}
            ),
            html.Br(),
            html.Br(),
            html.Div(
                children = [
                    html.P(
                        'Do not worry about rounding radicals to the nearest millionth as instructed. This calculator can ensure that it will give the right answer EVEN after approximating radicals while inputting your equation. And substitute your real radical back into the output and simplify.'
                    ),
                    html.P(
                        'The different information that can be provided by this calculator are (Some tips included too...):'
                    ),
                    #html.Br(),
                    html.P(
                        '1. The Parts Of A Conic Section Equation',
                        style={"margin-left": "8px"}
                    ),
                    #html.Br(),
                    html.P(
                        '\u2022 A Conic Equations Parts are classified by the general equation -> Ax^2 + Bxy + Cy^2 + Dx + Ey + F = 0',
                        style={"margin-left": "20px"}
                    ),
                    #html.Br(),
                    html.P(
                        '2. Type Of Conic',
                        style={"margin-left": "8px"}
                    ),
                    #html.Br(),
                    html.P(
                        '\u2022 Referring to Conic Equation Parts',
                        style={"margin-left": "20px"}
                    ),
                    #html.Br(),
                    html.P(
                        '\u25E6 If A equals C, then the equation can be identified as a CIRCLE',
                        style={"margin-left": "32px"}
                    ),
                    #html.Br(),
                    html.P(
                        '\u25E6 If x^2 is there and y^2 is not there, or if x^2 is not there and y^2 is there, then the equation can be identified as a PARABOLA',
                        style={"margin-left": "32px"}
                    ),
                    #html.Br(),
                    html.P(
                        '\u25E6 If A does NOT equal C, and both A and C are positive, then the equation can be identified as a(n) ELLIPSE',
                        style={"margin-left": "32px"}
                    ),
                    #html.Br(),
                    html.P(
                        '\u25E6 If A does NOT equal C, and either A or C is negative, then the equation can be identified as a(n) HYPERBOLA',
                        style={"margin-left": "32px"}
                    ),
                ],
                style={'backgroundColor': colors['text2'], 'color':colors['background'], 'font-size': '100%', 'padding': '5%', 'height':'auto', 'font-weight':'bold'}
            )
        ])
    ])
])


# Learn Page Section #
LearnEquation: dict = dict()

@app.callback(ddc.Output('hiddenDiv', 'children'), [ddc.Input('inputEq2', 'value')])
def update_equation(value):
    LearnEquation["Equation"] = value

    return None

@app.callback(ddc.Output('tabsContent', 'children'), [ddc.Input('optionsForChoose', 'value')]) 
def update_steps(value):
    if value == 'D':
        equation = LearnEquation["Equation"]

        return html.Div(children=[
            html.Div(children=[
                html.P(
                    "Some tips: "
                ),
                html.P(
                    "\u2022 'sqrt' in the equation means \u221A (square root symbol).",
                    style={'padding-left':'5%', 'padding-top':'2px'}
                ),
                html.P(
                    "\u2022 'Θ' (greek letter 'theta') is the angle of rotation.",
                    style={'padding-left':'5%', 'padding-top':'2px'}
                ),
                html.P(
                    "\u2022 These are all steps that are listed on finding the rotated equation of a conic section.",
                    style={'padding-left':'5%', 'padding-top':'2px'}
                )],
                style={'backgroundColor': colors['background'], 'color':colors['text2'], 'font-size': '200%', 'padding': '5%', 'height':'auto', 'font-weight':'bold'}
            ),
            html.Br(),
            html.Div(
                f"Your equation is \u27A0 [{equation}] and it is a {Conics.ConicClassifier(equation)}",
                id="EquationIs",
                style={'backgroundColor': colors['background'], 'color':colors['bodyBackground'], 'font-size': '200%', 'padding': '5%', 'height':'auto', 'font-weight':'bold'}
            ),
            html.Br(),
            html.Br(),
            html.Div(
                f"Step 1, Identify the parts of the conic equation \u27AA {ConicRotatorLearn.Step1_IdentifyThePartsOfTheConic(equation)}",
                id="Step1",
                style={'backgroundColor': colors['background'], 'color':colors['white'], 'font-size': '150%', 'padding': '5%', 'height':'auto', 'font-weight':'bold'}
            ),
            html.Div(
                f"Step 2.1, Find the Angle Of Rotation (Using the parts we figured out, you find the angle using this formula) \u27AA {ConicRotatorLearn.Step2_FindTheAngleOfRotation_PartOne()}",
                id="Step2Part1",
                style={'backgroundColor': colors['background'], 'color':colors['white'], 'font-size': '150%', 'padding': '5%', 'height':'auto', 'font-weight':'bold'}
            ),
            html.Div(
                f"Step 2.2, Find the Angle Of Rotation (continued) \u27AA {ConicRotatorLearn.Step2_FindTheAngleOfRotation_PartTwo(equation)}",
                id="Step2Part2",
                style={'backgroundColor': colors['background'], 'color':colors['white'], 'font-size': '150%', 'padding': '5%', 'height':'auto', 'font-weight':'bold'}
            ),
            html.Div(
                f"Step 2.3, Find the Angle Of Rotation (continued) \u27AA {ConicRotatorLearn.Step2_FindTheAngleOfRotation_PartThree(equation)}",
                id="Step2Part3",
                style={'backgroundColor': colors['background'], 'color':colors['white'], 'font-size': '150%', 'padding': '5%', 'height':'auto', 'font-weight':'bold'}
            ),
            html.Div(
                f"Step 2.4, Find the Angle Of Rotation (continued) \u27AA {ConicRotatorLearn.Step2_FindTheAngleOfRotation_PartFour(equation)}",
                id="Step2Part4",
                style={'backgroundColor': colors['background'], 'color':colors['white'], 'font-size': '150%', 'padding': '5%', 'height':'auto', 'font-weight':'bold'}
            ),
            html.Div(
                f"Step 2.5, Find the Angle Of Rotation (continued) \u27AA {ConicRotatorLearn.Step2_FindTheAngleOfRotation_PartFive(equation)}",
                id="Step2Part5",
                style={'backgroundColor': colors['background'], 'color':colors['white'], 'font-size': '150%', 'padding': '5%', 'height':'auto', 'font-weight':'bold'}
            ),
            html.Div(
                f"Step 2.6, Find the Angle Of Rotation (continued, final) \u27AA {ConicRotatorLearn.Step2_FindTheAngleOfRotation_PartFinal(equation)}",
                style={'backgroundColor': colors['background'], 'color':colors['white'], 'font-size': '150%', 'padding': '5%', 'height':'auto', 'font-weight':'bold'}
            ),
            html.Div(
                f"Step 3, Find the Sine Of the Angle of Rotation \u27AA {ConicRotatorLearn.Step3_FindTheSineAngle(equation)}",
                id="Step3",
                style={'backgroundColor': colors['background'], 'color':colors['white'], 'font-size': '150%', 'padding': '5%', 'height':'auto', 'font-weight':'bold'}
            ),
            html.Div(
                f"Step 4, Find the Cosine Of the Angle of Rotation \u27AA {ConicRotatorLearn.Step4_FindTheCosineAngle(equation)}",
                id="Step4",
                style={'backgroundColor': colors['background'], 'color':colors['white'], 'font-size': '150%', 'padding': '5%', 'height':'auto', 'font-weight':'bold'}
            ),
            html.Div(
                f"Step 5.1, Find out what is going to be substituted for x in the equation (The new x's will be defined by this equation) \u27AA {ConicRotatorLearn.Step5_FindNewX_Part1()}",
                id="Step5Part1",
                style={'backgroundColor': colors['background'], 'color':colors['white'], 'font-size': '150%', 'padding': '5%', 'height':'auto', 'font-weight':'bold'}
            ),
            html.Div(
                f"Step 5.2, what is the new x? \u27AA {ConicRotatorLearn.Step5_FindNewX_PartFinal(equation)}",
                id="Step5PartFinal",
                style={'backgroundColor': colors['background'], 'color':colors['white'], 'font-size': '150%', 'padding': '5%', 'height':'auto', 'font-weight':'bold'}
            ),
            html.Div(
                f"Step 6.1, Find out what is going to be substituted for y in the equation (The new y's will be defined by this equation) \u27AA {ConicRotatorLearn.Step6_FindNewY_Part1()}",
                id="Step6Part1",
                style={'backgroundColor': colors['background'], 'color':colors['white'], 'font-size': '150%', 'padding': '5%', 'height':'auto', 'font-weight':'bold'}
            ),
            html.Div(
                f"Step 6.2, what is the new y? \u27AA {ConicRotatorLearn.Step6_FindNewY_PartFinal(equation)}",
                id="Step6PartFinal",
                style={'backgroundColor': colors['background'], 'color':colors['white'], 'font-size': '150%', 'padding': '5%', 'height':'auto', 'font-weight':'bold'}
            ),
            html.Div(
                f"Step 7, Substitute the new x's and y's into the original equation \u27AA {ConicRotatorLearn.Step7_SubstituteFinal(equation)}",
                id="Step7",
                style={'backgroundColor': colors['background'], 'color':colors['white'], 'font-size': '150%', 'padding': '5%', 'height':'auto', 'font-weight':'bold'}
            ),
            html.Div(
                f"Step 8, Simplify \u27AA {ConicRotatorLearn.Step8_Simplify(equation)}",
                id="Step8",
                style={'backgroundColor': colors['background'], 'color':colors['white'], 'font-size': '150%', 'padding': '5%', 'height':'auto', 'font-weight':'bold'}
            )
        ])


# Main Server Run #
if __name__ == '__main__':
   app.run_server(port=8050)