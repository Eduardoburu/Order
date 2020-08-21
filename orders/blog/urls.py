from django.urls import path
from .views import Article_1_View, Article_2_View, Article_3_View, Article_4_View, Article_5_View, Article_6_View, Article_7_View, Article_8_View, Article_9_View, Article_10_View, Article_11_View, Article_12_View, Article_13_View, Article_14_View, Article_15_View, Article_16_View, Article_17_View, Article_18_View, Article_19_View, Article_20_View, Article_21_View, Article_22_View, Article_23_View, Article_24_View, Article_25_View, Article_26_View




urlpatterns = [
    path('Similarities_and_Differences_between_the_Arizona_and_US_Constitution_1', Article_1_View.as_view(), name='Article_1'),
    path('Transfer_Pricing_2', Article_2_View.as_view(), name='Article_2'),
    path('The_2007-2008_Financial_Crisis_3', Article_3_View.as_view(), name='Article_3'),
    path('Reducing_Road_Accidents_by_Banning_the_Use_of_Cellphone_while_Driving_4', Article_4_View.as_view(), name='Article_4'),
    path('Internal_and_External_Analysis_of_the_NFLs_New_York_Giants_5', Article_5_View.as_view(), name='Article_5'),
    path('Directional_Process_Analysis_for_Complaining_Effectively_6', Article_6_View.as_view(), name='Article_6'),
    path('Warren_Buffet_On_Business_7', Article_7_View.as_view(), name='Article_7'),
    path('Effects_of_Poverty_on_a_Culture_8', Article_8_View.as_view(), name='Article_8'),
    path('Multilateral_projections_of_an_Asia-Pacific_Free_Trade_Agreement_9', Article_9_View.as_view(), name='Article_9'),
    path('Wells_Fargo_Fake_Accounts_Scandal_10', Article_10_View.as_view(), name='Article_10'),
    path('The_Role_and_Importance_of_Organizational_Behavior_11', Article_11_View.as_view(), name='Article_11'),
    path('Accounting_for_Financial_Instruments_with_both_Debt_and_Equity_Features_12', Article_12_View.as_view(), name='Article_12'),
    path('Role_and_Importance_of_Ethnic_Cuisines_13', Article_13_View.as_view(), name='Article_13'),
    
    
]