import pandas as pd
import re

#file = '/home/mon/Documents/code/wrepit/IC-Accounts-Payable-Ledger-Template-Updated-8552.xlsx'
#df = pd.read_excel(file, header=None) 
file = '/home/mon/Documents/code/wrepit/new_input_csv.csv'
#file = '/home/mon/Documents/code/wrepit/table_csv.csv'
df = pd.read_csv(file, header=None)

# Dictionary of regex patterns and their corresponding data type.
pattern_dict = {r'^(0?[1-9]|1[012])[- /.](0?[1-9]|[12][0-9]|3[01])[- /.](19|20)?[0-9]{2}$': 'date',   #MM/DD/YY(YY)
                r'^(0?[1-9]|[12][0-9]|3[01])[- /.](0?[1-9]|1[012])[- /.](19|20)?[0-9]{2}$': 'date',   #DD/MM/YY(YY)
                r'^(19|20)?[0-9]{2}[- /.](0?[1-9]|1[012])[- /.](0?[1-9]|[12][0-9]|3[01])$': 'date',   #YY(YY)/MM/DD
                r'^-?[0-9]+$': 'integer',
                #r'^-?[0-9]*\.?[0-9]+$': 'float',
                r'^-?([0-9]+|[0-9]{1,3}([,\ ][0-9]{3})+)((\.|,)[0-9]+)?$': 'float',
                r'^\ *\$\ *[-+]?[0-9]*\.?[0-9]+\ *$': 'currency',
                r'^\ *\$\ *-?([0-9]+|[0-9]{1,3}([,\ ]?[0-9]{3})+)((\.|,)[0-9]+)?\ *$': 'currency'
                }

def get_content_type(cell):
    if pd.isna(cell) or cell==' ':
        return ''
    #print(cell)
    #print('read as:',type(cell))
    content = str(cell)

    for pattern, dtype in pattern_dict.items():
        if re.search(pattern, content):
            print('typed: ',dtype)
            return(dtype)
    
    return 'string'


type_df = df.applymap(get_content_type)

type_df.to_excel('type_output_new.xlsx', header=False, index=False)