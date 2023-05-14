import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt


number1 = [0,1,2,3,4,5,6,7,8,9]
number2 = [10,11,12,13,14,15,16,17,18,19,20,21,22,99]

for i in number1:
    atname = 'Attackerlist0' + str(i)+'.csv'
    impactname = 'Impactlist0' + str(i)+'.csv'
    vulname = 'Vullist0' + str(i)+'.csv'
    locals()['dfat0'+str(i)]= pd.read_csv(atname)
    locals()['dfim0'+str(i)]= pd.read_csv(impactname)
    locals()['dfvu0'+str(i)]= pd.read_csv(vulname)

for i in number2:
    atname = 'Attackerlist' + str(i)+'.csv'
    impactname = 'Impactlist' + str(i)+'.csv'
    vulname = 'Vullist' + str(i)+'.csv'
    locals()['dfat'+str(i)]= pd.read_csv(atname)
    locals()['dfim'+str(i)]= pd.read_csv(impactname)
    locals()['dfvu'+str(i)]= pd.read_csv(vulname)

totat = pd.read_csv('Attacker99-22.csv')
totim = pd.read_csv('Impact99-22.csv')
totvul = pd.read_csv('Vul99-22.csv')

print("There are {} attacker observations from 1999 to 2022. \n".format(totat.shape[0]))
print("There are {} impact observations from 1999 to 2022. \n".format(totim.shape[0]))
print("There are {} vulnerabilities observations from 1999 to 2022. \n".format(totvul.shape[0]))

print("There are {} vulnerabilities observations in 2000. \n".format(dfvu00.shape[0]))

print("There are {} types of vulnerabilities in this dataset such as {}... \n".format(len(dfvu00.Vul.unique()),
                                                                           ", ".join(dfvu00.Vul.unique()[0:5])))

print("There are {} vulnerabilities observations in 2010. \n".format(dfvu10.shape[0]))

print("There are {} types of vulnerabilities in this dataset such as {}... \n".format(len(dfvu10.Vul.unique()),
                                                                           ", ".join(dfvu10.Vul.unique()[0:5])))

print("There are {} vulnerabilities observations in 2020. \n".format(dfvu20.shape[0]))

print("There are {} types of vulnerabilities in this dataset such as {}... \n".format(len(dfvu20.Vul.unique()),
                                                                           ", ".join(dfvu20.Vul.unique()[0:5])))


print(totvul)
print(totim)
print(totat)
# Start with one review:
print(totvul.Vul)
print(totim.Impact)
print(totat.Attacker)
vul = ' '.join(totvul["Vul"].astype(str).value_counts().to_dict())
im = ' '.join(totim["Impact"].astype(str).value_counts().to_dict())
at = ' '.join(totat["Attacker"])

# Display the generated image:
#wordcloud = WordCloud(max_font_size=50, max_words=100, background_color="white").generate(at)
#plt.figure()
#plt.imshow(wordcloud, interpolation="bilinear")
#plt.axis("off")
#plt.show()

#wordcloud = WordCloud(max_font_size=50, max_words=100, background_color="white").generate(im)
#plt.figure()
#plt.imshow(wordcloud, interpolation="bilinear")
#plt.axis("off")
#plt.show()

#wordcloud = WordCloud(max_font_size=50, max_words=100, background_color="white").generate(vul)
#plt.figure()
#plt.imshow(wordcloud, interpolation="bilinear")
#plt.axis("off")
#plt.show()

#plt.figure(figsize=(20,6))
#totat.groupby(['Attacker']).size().sort_values(ascending=False).head(10).plot.bar()
#plt.xticks(rotation=30)
#plt.xlabel("Attacker types")
#plt.ylabel("Number of Attacker types")
#plt.show()

print(totat.groupby(['Attacker']).size().sort_values(ascending=False).head(10))
print(totim.groupby(['Impact']).size().sort_values(ascending=False).head(10))
print(totvul.groupby(['Vul']).size().sort_values(ascending=False).head(10))

dfvu0307 = pd.read_csv('0307.csv')
dfvu0812 = pd.read_csv('0812.csv')
dfvu1317 = pd.read_csv('1317.csv')
dfvu1822 = pd.read_csv('1822.csv')
dfvu0307=dfvu0307[dfvu0307["Vul"].str.contains("XSS")==False]
dfvu0812=dfvu0812[dfvu0812["Vul"].str.contains("XSS")==False]
dfvu1317=dfvu1317[dfvu1317["Vul"].str.contains("XSS")==False]
dfvu1822=dfvu1822[dfvu1822["Vul"].str.contains("XSS")==False]

vul03_07=dfvu0307.groupby("Vul")
vul08_12=dfvu0812.groupby("Vul")
vul13_17=dfvu1317.groupby("Vul")
vul18_22=dfvu1822.groupby("Vul")

im00=dfim00.groupby("Impact")
im10=dfim10.groupby("Impact")
im20=dfim20.groupby("Impact")

at00=dfat00.groupby("Attacker")
at10=dfat10.groupby("Attacker")
at20=dfat20.groupby("Attacker")

print('Most vultypes found 2003-2007:')
print(vul03_07.size().sort_values(ascending=False).head(10))
print('Total found vultypes 2003-2007: {}'.format(dfvu0307.shape[0]))
print('Most vultypes found 2008-2012:')
print(vul08_12.size().sort_values(ascending=False).head(10))
print('Total found vultypes 2008-2012: {}'.format(dfvu0812.shape[0]))
print('Most vultypes found 2013-2017:')
print(vul13_17.size().sort_values(ascending=False).head(10))
print('Total found vultypes 2013-2017: {}'.format(dfvu1317.shape[0]))
print('Most vultypes found 2018-2022:')
print(vul18_22.size().sort_values(ascending=False).head(10))
print('Total found vultypes 2018-2022: {}'.format(dfvu1822.shape[0]))


#print('Most Impact types found in 2000:')
#print(im00.size().sort_values(ascending=False).head(10))
#print('Total found Impact types in 2000: {}'.format(dfim00.shape[0]))
#print('Most Impact types found in 2010:')
#print(im10.size().sort_values(ascending=False).head(10))
#print('Total found Impact types in 2010: {}'.format(dfim10.shape[0]))
#print('Most Impact types found in 2020:')
#print(im20.size().sort_values(ascending=False).head(10))
#print('Total found Impact types in 2020: {}'.format(dfim20.shape[0]))

#print('Most attacker types found in 2000:')
#print(at00.size().sort_values(ascending=False).head(10))
#print('Total found attacker types in 2000: {}'.format(dfat00.shape[0]))
#print('Most attacker types found in 2010:')
#print(at10.size().sort_values(ascending=False).head(10))
#print('Total found attacker types in 2010: {}'.format(dfat10.shape[0]))
#print('Most attacker types found in 2020:')
#print(at20.size().sort_values(ascending=False).head(10))
#print('Total found attacker types in 2020: {}'.format(dfat20.shape[0]))


