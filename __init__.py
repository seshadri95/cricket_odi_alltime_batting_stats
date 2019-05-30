import pandas as pd
import scraping.scaper as sc


class generate_csv:
    def __init__(self,path):
        obj = sc.scrapering_result()
        a = obj.get_total_dataset()
        header = ['Year','Mat','Inns','NO','100s','50s','0s','HS','Runs','Avg','S/R','Ca','St','player_name']
        df = pd.DataFrame(columns=header)
        it = -1

        for i,j in a.items():
            for k in j:
                it = it+1
                k['player_name'] = i

                # Website has data like overall(1),overall(2) mentioning total years data available inside bracket --> so just having overall for convineance of analysis

                if 'overall' in k['Year'].lower():
                    k['Year'] = 'Overall'

                df2 = pd.DataFrame.from_records([k],index = [it])
                df = pd.concat([df,df2])

        df.to_csv(path, sep=',', encoding='utf-8')
        print('check the below path for output file'+'\n'+path)
        print('!!!!!!!!!!!!!!!!!!Completed!!!!!!!!!!!!!!!!!')


if __name__ == '__main__':
    generate_csv('S:\op.csv')