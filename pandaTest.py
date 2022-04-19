import pandas as pd

sal = pd.read_csv('Salaries.csv')


sal.head()
sal.head(2)

sal.info()

sal['Basepay'].mean()

sal['OvertimePay'].max()

sal['JobTitle']

sal[sal['EmployeeName'] == 'Joseph Driscoll']['JobTitle']

sal[sal['EmployeeName'] == 'Joseph Driscoll']['TotalPayBenefits']

sal[sal['TotalPayBenefits'] == sal['TotalPayBenefits'].max()]['EmployeeName']

sal.loc[sal['TotalPayBenefits'].idxmax()]

sal.iloc[sal['TotalPayBenefits'].argmax()]

sal.iloc[sal['TotalPayBenefits'].argmin()]

sal[sal['TotalPayBenefits'] == sal['TotalPayBenefits'].min()]['EmployeeName']

sal.groupby('Year').mean()['BasePay']

sal['JobTitle'].unique()

sal['JobTitle'].nnunique()
len(sal['JobTitle'].unique())

#top 5 most common job
sal['JobTitle'].value_counts().head(5)

sum(sal[sal['Year'] == 2013]['JobTitle'].value_counts() == 1)

def chief_string(title):
    if 'chief' in title.lower().split():
        return True
    else:
        return False

sum(sal['JobTile'].apply(lambda x: chief_string(x)))

sal['title_len'] = sal['JobTitle'].apply(len)

sal[['TotalPayBenefits', 'title_len']].corr()

############

ecom = pd.read_csv('Ecommerce Purchases')

ecom.head()

len(ecom.columns)
len(ecom.index)
len.info()

ecom['Purchase Price'].mean()

ecom['Purchase Price'].max()
ecom['Purchase Price'].min()

ecom[ecom['Language'] == 'en'].head()
ecom[ecom['Language'] == 'en'].count()
ecom[ecom['Language'] == 'en']['Language'].count()

ecom['AM or PM'].value_counts()

ecom['Job'].value_counts().head(5)

ecom[(ecom['CC Provider'] == 'American Express') & (ecom['Purchase Price'] > 95)]
ecom[(ecom['CC Provider'] == 'American Express') & (ecom['Purchase Price'] > 95)].count()

sum(ecom['CC Exp Date'].apply(lambda exp: exp[3:] == '25'))
ecom[ecom['CC Exp Date'].apply(lambda exp: exp[3:] == '25')].count()








