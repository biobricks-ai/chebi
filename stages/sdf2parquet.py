import pandas as pd
import sys
import fastparquet as fastparquet
from rdkit import Chem

from IPython.display import display

def convertSDFtoDF(p_sdf):
    print(p_sdf)

    #Loading SDF(Read all parameter names the first time)
    sdf_sup = Chem.SDMolSupplier(p_sdf)
    
    # 1. load properties from sdf format
    l_props = []
    
    for mol in sdf_sup:
        try: l_prop_bychem = mol.GetPropNames() # case of last block empty
        except: continue
        for prop_by_chem in l_prop_bychem:
            if not prop_by_chem in l_props:
                l_props.append(prop_by_chem)

    d_out = {}
    for prop in l_props:d_out[prop] = [] 
    # 2. need to load a second time to populate a dictionnary 
    for mol in sdf_sup:
        if mol == None: continue
        for prop in l_props:
            if mol.HasProp(prop):
                d_out[prop].append(mol.GetProp(prop).replace("\n", ";;")) # replace \n with two ;; for a better reading
            else:
                d_out[prop].append(None)

    #Convert at once with pandas
    df = pd.DataFrame(data=d_out)
    
    ### for testing
    #df.to_csv('./test.csv')
    #display(df)
    return df


InFileName = sys.argv[1]
OutFileName = sys.argv[2]

print(f"sdf2parquet: Converting file {InFileName}")

# 1. convert sdf in table format
df = convertSDFtoDF(InFileName)

# 2. convert in parquet
df.to_parquet(OutFileName)
