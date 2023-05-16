from gattaranuse.tasklist import *
from time import sleep

f = open(r'api_keys.txt')
llaves = f.read()
if(llaves[43:45] == 'MX'):
    ticketId = llaves[97:142]
    wsgsigId = llaves[-138:]
else:
    ticketId = llaves[90:135]
    wsgsigId = llaves[-138:]
f.close()

countries = ['MX','PE','CL','DO','CR','CO']

while True:

    for countryId in countries:
        df = getRewardsPending(ticketId,wsgsigId,countryId)

        if df is not None and isinstance(df, pd.DataFrame) and not(df.empty):
            print("Se detectaron rewards creados por user: raulcorrea")
            errorsTotal = 0
            rewardsTotal = 0
            for key,row in df.iterrows():
                result = approveReward(ticketId,wsgsigId,countryId,row['taskId'])
                if result != 0:
                    errorsTotal += 1
                else:
                    rewardsTotal += 1

            print("Para",countryId,"se aprobaron",rewardsTotal," con ",errorsTotal,"errores")

        else:
            print("Sin rewards por aprobar")

        df = None
    sleep(60)

