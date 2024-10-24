import pandas as pd

std_details=pd.DataFrame({'usn': [1,2,3,4,5,6,7,8,9,10], 'Name': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', '1']})

fee_status=pd.DataFrame (('usn': [1,2,3,4,5], 'pending': [100, 1000, 200, 50,150]})

print("Printing raw data\n")

print(std_details)

print(fee_status)

print("Merging\n")

merged_df=pd.merge(std_details, fee_status,on='usn")

print(merged_df)

print("Concatinating\n")

concat_df=pd.concat([std_details, fee_status])

print(concat_df)

print("Non duplicated\n")

non_duplicate=fee_status [~fee_status.duplicated()]

print(non_duplicate)

print("Filtering")

filtered1=fee_status.query('usn>2')

print(filtered1)

filtered2=fee_status.query('pending>150')

print(filtered2)
