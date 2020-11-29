####### Milestone 2 Python Script
import pandas as pd
import scipy.stats as st
from snhu_MAT243 import prop_1samp_ztest
from snhu_MAT243 import means_1samp_ttest
from statsmodels.stats.proportion import proportions_ztest


##Step 1: Import your data set
##-----------------------------------------------------------------------------
production = pd.read_csv('Rice_Production.csv')

#######Step 2: Perform hypothesis test for the difference of two population proportions
##-------------------------------------------------------------------------------------------------
print ('Hypothesis test for the difference of two population proportions - Step 2')
n1 = production.loc[production['Month'] == 3]['Company1'].count()
n2 = production.loc[production['Month'] == 10]['Company1'].count()
x1 = (production.loc[production['Month'] == 3]['Company1'] > 307200.0).values.sum()
x2 = (production.loc[production['Month'] == 10]['Company1'] > 307200.0).values.sum()
counts = [x1, x2]
n = [n1, n2]
print (proportions_ztest(counts, n))
print ('')

####### Step 3: Perform hypothesis test for the difference of two population proportions
##-------------------------------------------------------------------------------------------------
print ('Hypothesis test for the difference of two population proportions - Step 3')
n1 = production.loc[production['Month'] == 3]['Company2'].count()
n2 = production.loc[production['Month'] == 10]['Company2'].count()
x1 = (production.loc[production['Month'] == 3]['Company2'] > 209500.0).values.sum()
x2 = (production.loc[production['Month'] == 10]['Company2'] > 209500.0).values.sum()
counts = [x1, x2]
n = [n1, n2]
print (proportions_ztest(counts, n))
print ('')

####### Step 4: Perform hypothesis test for the difference of two population means
##----------------------------------------------------------------------------------
print ('Hypothesis test for the difference of two population means - Step 4')
jul_data = production.loc[production['Month'] == 7]['Company1']
aug_data = production.loc[production['Month'] == 8]['Company1']
print (st.ttest_ind(jul_data, aug_data, equal_var=False))
print ('')


####### Step 5: Perform hypothesis test for the difference of two population means
##----------------------------------------------------------------------------------
print ('Hypothesis test for the difference of two population means - Step 5')
feb_data = production.loc[production['Month'] == 2]['Company2']
aug_data = production.loc[production['Month'] == 8]['Company2']
print (st.ttest_ind(feb_data, aug_data, equal_var=False))
print ('')
