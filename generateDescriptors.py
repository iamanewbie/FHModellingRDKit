from rdkit import Chem
import os, webbrowser
from utilities import *
import pandas as pd
from rdkit.Chem import Descriptors
from rdkit.ML.Descriptors.MoleculeDescriptors import MolecularDescriptorCalculator as MDC
from multiprocessing import Pool
import utilities


# activeMolecules = Chem.SDMolSupplier("/home/knzk574/Desktop/Data/set3_actives.sdf")
# inactiveMolecules = Chem.SDMolSupplier("/home/knzk574/Desktop/Data/set3_inactives.sdf")

with open("smallActiveSet", "r") as f:
    activeMolecules = pickle.load(f)
with open("smallInactiveSet", "r") as f:
    inactiveMolecules= pickle.load(f)


def makeDescriptorTable(tableobj, outcome):
    descriptorTable = pd.DataFrame(tableobj)
    print len(descriptorTable.columns)
    descriptorTable.columns = descriptorList

    descriptorTable['Outcome'] = outcome
    print len(descriptorTable.columns)
    return descriptorTable


descriptorList = [desc[0] for desc in Descriptors.descList]

calc = MDC(descriptorList)

activesdesc = []

LOG_EVERY_N = 100



# def CalcDescriptorsErrorCheck(mol):
#     if mol.GetNumHeavyAtoms() > 0:
#         print MDC.CalcDescriptors(calc, mol)
#         return MDC.CalcDescriptors(calc, mol)


# pool1 = Pool(4)
# pool2 = Pool(4)
# activesdesc = pool1.map(CalcDescriptorsErrorCheck, smallActiveSet)
# pool1.close()
# inactivedesc = pool2.map(CalcDescriptorsErrorCheck, smallInactiveSet)
# pool2.close()


for i, mol in enumerate(activeMolecules):
        try:
            if mol.GetNumHeavyAtoms() > 0:
                activesdesc.append(MDC.CalcDescriptors(calc, mol))
                if (i % LOG_EVERY_N) == 0:
                    print str(i)+" molecules processed"
        except:
            print "Error while processing "

inactivedesc = []
for i, mol in enumerate(inactiveMolecules):
        try:
            if mol.GetNumHeavyAtoms() > 0:
                inactivedesc.append(MDC.CalcDescriptors(calc, mol))
                if (i%LOG_EVERY_N) == 0:
                    print str(i)+" molecules processed"
        except:
            print "Error while processing "



descDfActive = makeDescriptorTable(activesdesc, 1)
print len(descDfActive.columns)
descDfInactive = makeDescriptorTable(inactivedesc, 0)
print len(descDfActive.columns)

descDfAll = pd.concat([descDfActive, descDfInactive], ignore_index=True)
print len(descDfActive.columns)

descDfAll.to_csv("descDFSmallSet.csv")

print "Descriptors are ready. Moving on to prep the data"
utilities.viewTable(pd.DataFrame(activesdesc))

#pickledump(descDfAll, "descdfAll")

