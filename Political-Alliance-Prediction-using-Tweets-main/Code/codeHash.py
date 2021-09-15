
###### Filtering the data based on hashtag #########################

import pandas as pd


df = pd.read_csv("topic_tweets.csv",encoding = "ISO-8859-1")

#tags_farm = ['FarmBills', 'FarmBill', 'ModiWithFarmers', 'FarmersProtest', 'AgriculturalReforms', 'FarmersEmpowermentAndProtectiOnAgreementOnPriceAssuranceAndFarmServicesBil', 'EssentialCommoditiesAmendmentBill', 'ProduceTradeAndCommerceBill', 'EmpowermentAndProtectionAgreement ', 'TRSAgainstFarmers', '3FarmOrdinancesBillPassed', 'FarmersProduceTradeAndCommerce ', 'BillsInLoksabha ', 'farmerbill', 'farmersbill2020 ', 'supportfarmers', 'kissanmovement', 'farmerbill2020 ', 'kissanmajdoorektazindabadh', 'kissanmajdoorektazindabad ', 'kissanunionzindabaad', 'Isupportfarmersprotest', 'FarmLaws2020', 'IstandWithIndianFarmers', 'istandfarmerprotest ', 'IstandWithFarmers', 'Farmersday2020 ', 'supportfarmers', 'FarmerBill2020 ', 'iagainstfarmerbill ', 'FarmersNotOnSale', 'ModiStopIgnoringFarmers ', 'FreedomOfFarmers', 'KisanWithPMModi', 'JaiKisan', 'EssentialCommoditiesAct', 'FarmLaws ', 'agriculturalreforms', 'KisanMuktiMarch', 'FarmingFriendlyPolicies ', 'FarmersProtestDelhi', 'kisanandolan', 'FarmersDyingModiEnjoying', 'FarmerBill ', 'FarmersWithPMModi', 'pmwithfarmer', 'ModiHatesFarmers', 'PMGraminGrihaPravesh', 'BycottAmbaniAdani ', 'FarmActsAreUnconstitutional ', 'KisanEktaMorcha', 'NoFarmersNoFood', 'FarmerLivesMatters', 'standwithfarmerschallenge', 'किसान_आंदोलन ', 'किसान_एकता_जिंदाबाद  ', 'FarmActsDeathWarrant ', 'TakeBackFarmBills  ', 'TakeBackFarmLaws ', 'TakeBackFarmBills2020 ', 'Standwithfarmerschallenge ', 'GodiMediaAgainstFarmers', 'मर_रहा_किसान_जागो_प्रधान', 'SupremeCourtStand4Farmers', 'KisanEktaZindabad', 'ModiRepealFarmActs', 'AatmaNirbharKrishi', 'PMModiWithKisan']
tags_covid = ['Covid19', 'कोरोना', 'COVID19', 'COVIDIOT', 'coronavirus', 'Coronavirus', 'CoronavirusStrain', 'Covid', 'IndiaFightsCorona', 'Unite2FightCorona', 'IndiaWillWin', 'covid19inindia', 'ukstrain', 'Corona19Out', 'CoronaPandemic', 'Corona19Out', 'Covid_19', 'COVID19India', 'StayHomeSaveLives', 'DoGajKiDooriMaskHaiZaruri', 'CombatCovid  ', 'OxfordVaccine', 'CovidVaccine', 'coronavaccin ', 'astrazenecavaccine', 'CoronaVaccine', 'Coviran', 'Pfizervaccine', 'COVID19Vaccine', 'PfizerCovidVaccine', 'ReadyToVaccinate', 'Covaxin', 'Covidshield', 'lockdown', 'nightcurfew', 'CoronavirusLockdown', '21daysLockdown', 'LockdowninIndia ', 'Lockdown', 'Lockdownextention', 'JanataCurfew', 'Corona', 'IndiaFightsCOVID19', 'CoronavirusLockdown', 'SocialDistancing', 'CoronavirusOutbreak']
#tags_Ind_china = ['IndiaChina' , 'IndiaChinaStandOff' , 'ChinaIndia ' , 'IndiaChina70' , 'IndiaChinaBorderTension' , 'ChinaIndiaFaceoff' , 'IndiaChinaFaceOff' , 'IndoChina' , 'BoycottChina' , 'ModiSpeakUpOnChina' , 'IndiaChinaBorder' , 'indiachinaFaceoff' , 'indiachinastandoff' , 'indiachinaborder' , 'ChineseAppsBanned' , 'ChineseApps' , 'Ladakhwarriors' , 'LadakhStandoff' , 'LADAKHSTANDOFF' , 'LadakhTension' , 'Standoff' , 'LACStandoff ' , 'LAC' , 'LineofActualControl ' , 'Sinoindoborder' , 'galwanvalleyclash' , 'GalwanBloodshed' , 'GalwanValley']

filt = df['hashtag_list'].str.contains('|'.join(tags_covid), na=False)


ds = df.loc[filt]
#print(ds)
ds.to_csv('covid_1.csv',index=False)

