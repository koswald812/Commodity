import requests
import pandas as pd

#insert location of Excel file on your system below
df = pd.read_excel (r'All_Product_Codes.xlsx')
#Ensure column number below alligns with correct collumn number of product codes in Excel file (preset as column C)
product_code = df.iloc[:,2];
#Once all above values are updated script is ready to run
#
code_count = {}
for word in product_code:
    code_count[word] = ""
ind=0
for num in product_code:
    requested_url = 'https://api.fda.gov/device/registrationlisting.json?search=products.product_code:' + str(num) + '&limit=1&api_key=lRpQPBNqJQdhH5ftVdMsURt9a96IHLeYNPG5cwFt'
    name = product_code[ind]
    try:
        res = requests.get(requested_url)
        data = res.json()
        pcode_count =  data['meta']['results']['total']
        code_count[name] = pcode_count
    except:
        pass
    ind=ind+1

final = pd.DataFrame([code_count])
final2 = final.transpose()
final2.to_excel("Establishment_PCODE_COUNT.xlsx")
# Check working folder for new excel sheet containing data on specified product code
