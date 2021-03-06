
### converting date in lower letter.
### If two names are present in a single cell then convert into two rows
### Filtering the data based on poltician vs politician, poltician vs party and party vs party

import pandas as pd
import numpy as np


df = pd.read_csv("farmbill.csv",encoding = "ISO-8859-1")


df.assign(mentions=df['mentions'].str.split(',')).explode('mentions')

df['mentions'] = df['mentions'].str.split(',')
df = df.explode('mentions').reset_index(drop=True)
cols = list(df.columns)
cols.append(cols.pop(cols.index('author_screen_name')))
df = df[cols]

tags = ['AITCofficial', 'BSP4Bharat', 'BJP4Indiacpimspeak', 'INCInsdia', 'nppmeghalaya', 'NCPspeaks', 'AamAadmiParty', 'AAPGoa', 'AAPUttarPradesh', 'AAPUttarakhand', 'AAPRajasthan', 'AAP4Jharkhand', 'AAPPunjab', 'AAPHaryana', 'AAPPunjab', 'AAPBihar', 'AAPGujarat', 'AAPMPOfficial', 'AAPBangalore', 'AAPMumbai', 'AIADMKOfficial', 'aimim_national', 'AIUDFOfficial', 'ajsupartyjh', 'agpofficial_', 'bjd_odisha', 'BJP4Maharashtra', 'BJP4Telangana', 'BJP4UK', 'BJP4Nagaland', 'BJP4Punjab', 'BJP4Jharkhand', 'BJP4Rajasthan', 'BJPMahilaMorcha', 'BJP4Himachal', 'BJP4Puducherry', 'BJP4Meghalaya', 'BJP4Chandigarh', 'bpfront', 'cpimspeak', 'CPIM_WESTBENGAL', 'CPIMKerala', 'pycpim', 'biharcpim', 'tncpim', 'mahacpimspeak', 'INCRajasthan', 'INCMumbai', 'INCPunjab', 'INCUttarakhand', 'INCHaryana', 'INCGoa', 'INCHimachal', 'INCWestBengal', 'INCChhattisgarh', 'INCAssam', 'IYC_UPEast', 'IYCWestBengal', 'INCUPEast', 'IYCBihar', 'IYCGujarat', 'IYCChhattisgarh', 'TN_PYC', 'INCTelangana', 'IYCUttarakhand', 'IYCJharkhand', 'IYCPunjab', 'IYC_UPWest', 'IYCOdisha', 'IYCMaha', 'Haryana_YC', 'DelhiPYC', 'IYCAssam', 'SevadalPB', 'TN_PYC', 'INCTamilNadu', 'TNCCMinority', 'TamilNaduPMC', 'IYCWestBengal', 'dmdkparty2005', 'arivalayam', 'Goaforwardparty', 'OfficialINLD', 'Iumlofficial', 'JKNC_', 'jkpdp', 'jdsindia', 'Jduonline', 'JJPofficial', 'JmmJharkhand', 'LJP4India', 'MNF_mizoram', 'NagalandNPF', 'MumbaiNCP', 'ThePMKOfficial ', 'RJDforIndia', 'RLDparty', 'rlspofficial', 'RLPINDIAorg', 'samajwadiparty', 'Akali_Dal_ ', 'ShivSena ', 'KrantiSikkim', 'JaiTDP ', 'trspartyonline', 'YSRCParty ']
tags_p = ['DrTanweerHassan',
 'ItsYourDev',
 'nrkbjp',
 'omarabdullah',
 'p_sahibsingh',
 'IndraHangSubba1',
 'visrane',
 'mohanAdmk24',
 'loveyvirk',
 'NeerajZimba',
 'durgadasskamat',
 'iamchsekar',
 'ManishTewari',
 'JVSinghINC',
 'vishvendrabtp',
 'dilipkpandey',
 'smritiirani',
 'uddhavthackeray',
 'attorneybharti',
 'tovihoto',
 'SuVe4Madurai',
 'Vaibhav_AAP',
 'sanjuydv',
 'PonnamLoksabha',
 'ChDadaPatil',
 'JamesSangma1',
 'guptar',
 'gauravbh',
 'SunilAmbekarM',
 'salimdotcomrade',
 'dpradhanbjp',
 'mepratap',
 'CTRavi_BJP',
 'asaravanan21',
 'GVLNRAO',
 'PCMohanMP',
 'jitupatwari',
 'Amitjanhit',
 'blsanthosh',
 'SuPriyoBabul',
 'PandaJay',
 'RNGhoshOfficial',
 'SpurdhaOfficial',
 'UttamTPCC',
 'somuveerraju',
 'ChBirenderSingh',
 'iamsunnydeol',
 'loismarandi',
 'ahir_hansraj',
 'dasraghubar',
 'harishrawatcmuk',
 'BMSandeepAICC',
 'JitendraTMC',
 'PonnalaLaksmiah',
 'SidharthNSingh',
 'SAustinMLA',
 'rakeshreddybjp',
 'BjpAchary',
 'KPGBJP',
 'priyankagandhi',
 'MukulWasnik',
 'ParimalSuklaba1',
 'SucharitaYSRCP',
 'AtishiAAP',
 'MP_Meerut',
 'mrhasanmushrif',
 'VipinWankhede_',
 'VelmuruganTVK',
 'yourBabulal',
 'VijaiSardesai',
 'SATAVRAJEEV',
 'SitaramYechury',
 'Aap_Praveen',
 'KailashOnline',
 'me_locket',
 'JM_Scindia',
 'VTankha',
 'OfficeOfKNath',
 'BhupenKBorah',
 'CMPuducherry',
 'TCGEHLOT',
 'sureshkpujari',
 'apjithender',
 'KhanAmanatullah',
 'SukhpalKhaira',
 'HemantSorenJMM',
 'princerajpaswan',
 'LNSharmaSikkim',
 'ChhaganCBhujbal',
 'PrinceAAP',
 'HardikPatel_',
 'rsprasad',
 'nsitharamanoffc',
 'SharadYadavMP',
 'evvelu',
 'S_AravindRamesh',
 'AroraAmanSunam',
 'SarojPandeyBJP',
 'KunalSarangi',
 'ManoMLA',
 'rakhibirla',
 'UrmilaMatondkar',
 'MitaliRoyMLA',
 'PitchandiK',
 'kolhe_amol',
 'Tanwar_Indian',
 'myogioffice',
 'ajaymaken',
 'nkishoreyadav',
 'ChhattisgarhCMO',
 'aifbspeaks',
 'AnubhavMohanty_',
 'OfficeOfRSP',
 'SampathKumarINC',
 'NayakRagini',
 'IPSinghSp',
 'imtiaz_jaleel',
 'Neiphiu_Rio',
 'dprakashbjp',
 'bhupeshbaghel',
 'GautamGambhir',
 'aradhanam7000',
 'RRPSpeaks',
 'AbrahamRoyMani',
 'CMOGuj',
 'ssrajputINC',
 'rbsharmabjp',
 'AmbaPrasadINC',
 'Jayant_R_Patil',
 'PrasannaTamilan',
 'iVijayakant',
 'jayantsinha',
 'DrHVoffice',
 'nithya_shre',
 'saidulkhan',
 'RSBharathiDMK',
 'MKumaramangalam',
 'digambarkamat',
 'VijayWadettiwar',
 'DsaikiaOfficial',
 'DrAjaySChautala',
 'KS_Alagiri',
 'PashupatiParas',
 'SurajKrBauddh',
 'duttabhishek',
 'KPonmudiMLA',
 'SunilTatkare',
 'digvijaya_28',
 'KN_NEHRU',
 'NANA_PATOLE',
 'VipulGoelBJP',
 'NNatarajanoffl',
 'yvsubbareddymp',
 'brijmohan_ag',
 'TRBRajaa',
 'kirenrijiju',
 'SangmaConrad',
 'hmksrahmani',
 'shaktisinhgohil',
 'Rajendra4BJP',
 'iManishankarP',
 'amitshah',
 'kakoligdastidar',
 'IrfanAnsariMLA',
 'DrKirodilalBJP',
 'Narayanan3',
 'arun_ud',
 'SmtJMOfficial',
 'Hemaram_INC',
 'dharam_kaushik',
 'robertroyte',
 'ManoharanVMC',
 'PrakashJavdekar',
 'BYRBJP',
 'NeelkanthAd',
 'HMOIndia',
 'Subramanian_ma',
 'dgurjarofficial',
 'DrJitendraSingh',
 'nsitharaman',
 'anilvijminister',
 'PiyushGoyalOffc',
 'RamaAIADMK',
 'sanjayraiupbjp',
 'Rakesh_Sachan_',
 'CMOfficeUP',
 'Md_MajidHussain',
 'AmitShahOffice',
 'Rathinghoshtmc',
 'kamala_kalita',
 'BasheerEt',
 'BYVijayendra',
 'tarun_gogoiF',
 'JAslamBasha',
 'AapkiBandana',
 'arjunrammeghwal',
 'vijaysamplabjp',
 'GulabMatiala',
 'DipikaPS',
 'ptshrikant',
 'aitcsudip',
 'rajazzmantra',
 'SubhashiniAli',
 'seethakkaMLA',
 'ramkripalmp',
 'CaptAbhimanyu',
 'doley_naba',
 'Naveen_Odisha',
 'tsrawatbjp',
 'NitinTyagiAAP',
 'mieknathshinde',
 'VinitThind',
 'shivpalsinghyad',
 'ApnaDalOfficial',
 'JharkhandCMO',
 'satyenaiadmk',
 'prajaktdada',
 'AjayLalluINC',
 'KartiPC',
 'aloor_ShaNavas',
 'RajeevRai',
 'RKSinhaBJP',
 'R_Gandhi_MLA',
 'Saurabh_MLAgk',
 'NitinRaut_INC',
 'devender_babli',
 'srivatsayb',
 'KunalChoudhary_',
 'hd_kumaraswamy',
 'kishanreddybjp',
 'VijayGoelBJP',
 'ruby_manoharan',
 'raghav_chadha',
 'siddharthanbjp',
 'sanjayjaiswalMP',
 'ncbn',
 'shyamalsantra13',
 'HagramaOnline',
 'CMOTamilNadu',
 'jothims',
 'swamy39',
 'RaoKavitha',
 'upadhyaysbjp',
 'CMOPb',
 'DilipSaikia4Bjp',
 'SupriyaShrinate',
 'SalmanSoz',
 'OfficeofminRK',
 'ptrmadurai',
 'jay_majumdar',
 'sachin_inc',
 'TheUpenYadav',
 'TRZeliang',
 'drsanjeevbalyan',
 'DrJayakumarMP',
 'juhiesingh',
 'GolayPs',
 'NARENDER1970',
 'BodkheShilpa',
 'PKSekarbabu',
 'spshahibjp',
 'yuva_rajad',
 'jigneshmevani80',
 'sureshpprabhu',
 'MahuaMoitra',
 'vbwalia',
 'ChetanDudiINC',
 'dr_maheshsharma',
 'JanataDal_S',
 'MahipalMahla',
 'CMOMaharashtra',
 'PurandeswariBJP',
 'ShuklaRajiv',
 'Deepakkhatri812',
 'drlaxmanbjp',
 'ErKKSakthivel',
 'jayantrld',
 'RTforINDIA',
 'MausamNoor',
 'djohninc',
 'DhirendraGBN',
 'thirumaofficial',
 'pallablochandas',
 'vivekvenkatswam',
 'sanjaynirupam',
 'drramansingh',
 'Ahmad_Shakeel',
 'Amar4Odisha',
 'CNAnnaduraiMP',
 'rohanrgupta',
 'JTNBJP',
 'AlongImna',
 'sasmitpatra',
 'cmpatowary',
 'OPDhankar',
 'bsmajithia',
 'dr_satyapal',
 'DVSadanandGowda',
 'iamVisheshravi',
 'CMO_Odisha',
 'drdwivedisatish',
 'Oommen_Chandy',
 'bjpdrmahendra',
 'digvijaysinghd9',
 'NakulKNath',
 'ParmilaTokas',
 'ravikishann',
 'SitaSorenMLA',
 'JagadishShettar',
 'nawabmalikncp',
 'DrPramodPSawant',
 'asadowaisi',
 'KM_Gopi',
 'officeofssbadal',
 'CosmoSubbu',
 'khehrajaswinder',
 'ashokgehlot51',
 'FinMinIndia',
 'official_sdf',
 'KanimozhiDMK',
 'PChidambaram_IN',
 'salman7khurshid',
 'jualoram',
 'Ra_THORe',
 'chmallareddyMLA',
 'SalemRRajendran',
 'DefenceMinIndia',
 'SachinPilot',
 'Mpsantoshtrs',
 'Sharmistha_GK',
 'AsiriyarKV',
 'santoshgangwar',
 'myogiadityanath',
 'vijayrupanibjp',
 'HarsimratBadal_',
 'pratibhaiyc1',
 'SChopraINC',
 'MmhonlumoKikon',
 'PreetiSMenon',
 'plpunia',
 'AdvRajendraPal',
 'shivprakashbjp',
 'nimmasuresh',
 'IVeenaDevi',
 'TrinankurWBTMCP',
 'MLA_NareshYadav',
 'capt_amarinder',
 'JaiveerShergill',
 'AmanDubey_',
 'KomatireddyKVR',
 'lurinjtgogoi',
 'JansamparkMP',
 'manojsinha_',
 'MisaBharti',
 'manojkjhadu',
 'jellasudhakar',
 'iumlofficial',
 'SudhinBhadoria',
 'chkanwarpal',
 'DwivediSurbhi',
 'Dayanidhi_Maran',
 'TelanganaCMO',
 'KosalramT',
 'GopalJi_Tandon',
 'syedasimwaqar',
 'VPSecretariat',
 'Arvindharmapuri',
 'basusayan',
 'JoshiPralhad',
 'RohanKhaunte',
 'officialYAD',
 'PawarSpeaks',
 'CHOTIWALA',
 'Ashokkatariya9',
 'ErRakeshraushan',
 'HarpalCheemaMLA',
 'RajBabbarMP',
 'manthriji',
 'nalinkateel',
 'LaxmanSavadi',
 'mlaruparam',
 'shindespeaks',
 'CMOfficeAssam',
 'DineshMohaniya',
 'kewekhapetherie',
 'ghulamnazad',
 'ARROffice',
 'saraditoo7',
 'drashwathcn',
 'aruna_dk',
 'rssurjewala',
 'VamsiChandReddy',
 'Abhilash4BJP',
 'MadhavBJP',
 'v_shrivsatish',
 'karkalasunil',
 'DeepakSinghINC',
 'adeshguptabjp',
 'BashisthaNarain',
 'RajaBrar_INC',
 'maji_mahua',
 'saddam_jmm',
 'GovindDotasra',
 'nagma_morarji',
 'VidadalaRajini',
 'RajuBistaBJP',
 'GouravVallabh',
 'amolmitkari22',
 'goacm',
 'ChitraKWagh',
 'SandhyaTudu',
 'OfficialArupRoy',
 'ShashiTharoor',
 'supriya_sule',
 'MBPatil',
 'RajibBaitc',
 'sarbanandsonwal',
 'OPRavindranath',
 'mansukhmandviya',
 'katchannaidu',
 'Vijayabaskarofl',
 'CMofKarnataka',
 'AbhaySChautala',
 'yadavakhilesh',
 'ManojTiwariMP',
 'SamujjalBhatta',
 'MohinderAAP',
 'AmitChavdaINC',
 'ashwinityagibjp',
 'ImranHussaain',
 'kashikirai',
 'n_sureshrajan',
 'aditya_golay',
 'ianuragthakur',
 'KaushikSiddarth',
 'JitinPrasada',
 'uttampadmavathi',
 'RanjeetkrDass',
 'MPRakeshSingh',
 'AKYOnline',
 'ShahnawazBJP',
 'TarunTewatia14',
 'pasupathy_senth',
 'jacob_zhimomi',
 'SabhajeetAAP',
 'arulpethiah1',
 'AnupriyaSPatel',
 'SudhanshuTrived',
 'SmitaBakshi5',
 'NitishKumar',
 'SwatiJaiHind',
 'RubyAap',
 'VyshRam',
 'Mayawati',
 'nusratchirps',
 'DilipGhoshBJP',
 'YogendraYadav',
 'JPNadda',
 'vishwajeetkadam',
 'Sanjeev_aap',
 'Pawankhera',
 'mimichakraborty',
 'himantabiswa',
 'nitin_gadkari',
 'TokhehoYepthomi',
 'deepakmishra979',
 'ArunSinghbjp',
 'satyakumar_y',
 'aaprajeshrishi',
 'Chiranjeev_INC',
 'OfficeofminMRV',
 'mohdmoazamkhan',
 'pemakhandubjp',
 'RakeshSinha01',
 'nikhilmandalJDU',
 'roysaryu',
 'BjpBiplab',
 'Gen_VKSingh',
 'DrRameshwarOra1',
 'SanjaySDutt',
 'SeemanOfficial',
 'DalitOnLine',
 'madanmitraoff',
 'PiyushGoyal',
 'bandisanjay_bjp',
 'gssjodhpur',
 'jairamthakurbjp',
 'Neerajkundan',
 'NvssprabhakarM',
 'vinod_palyekar',
 'crchaudharymos',
 'ArvinderLovely',
 'BannaGupta76',
 'siddaramaiah',
 'MPRBJP',
 'thamoanbarasan',
 'NSawaikar',
 'mpriteshpandey',
 'priyankac19',
 'VijayaRahatkar',
 'dimpleyadav',
 'mishra_surjya',
 'pranavINC',
 'Arunrjd',
 'BJPShanthikumar',
 'Nisith_Malik',
 'MSinghBJP',
 'AAPAjeshYadav',
 'ShayarImran',
 'RamvicharNetam',
 'ZoramthangaCM',
 'MotilalVora',
 'msisodia',
 'satyajeettambe',
 'pcsharmainc',
 'cpmkanagaraj',
 'yadavtejashwi',
 'SushilModi',
 'SadhviNiranjan',
 'prithvrj',
 'Kavitajainbjp',
 'Bvinubalan',
 'VSReddy_MP',
 'MayorofS',
 'hrishikeshgosw3',
 'CMOKerala',
 'MYaskhi',
 'PradeepYadavMLA',
 'OfficeofSSC',
 'suranjanbjp',
 'temjentoy',
 'KedarKashyapBJP',
 'RaoMlc',
 'ChitraSarwara',
 'mla_sudhakar',
 'avinashpandeinc',
 'MPDharmendraYdv',
 'DVJChautala',
 'drrpnishank',
 'nbirensingh',
 'JyotipriyaMLA',
 'Hkhehoviy',
 'cmohry',
 'GORANTLA_BC',
 'SanjayJhaBihar',
 'Chandrakbose',
 'ysjagan',
 'narendramodi',
 'MhathungYantha2',
 'dbchauhanbjp',
 'nadeeminc',
 'RCP_Singh',
 'Jaffarhusainmla',
 'kpmaurya1',
 'revanth_anumula',
 'sitaramlamba',
 'WamanCMeshram',
 'drdineshbjp',
 'Anbil_Mahesh',
 'Badal_Patralekh',
 'gauthamponmudy',
 'laluprasadrjd',
 'keshavyadaviyc',
 'ArjunsinghWB',
 'Kikseshwarappa',
 'INCSandesh',
 'M_Lekhi',
 'CMODelhi',
 'jdhankhar1',
 'YepthomiBen',
 'DrShashiPanja',
 'JitendraBaghel_',
 'EzhilarasanCvmp',
 'NupurSharmaBJP',
 'dhananjay_munde',
 'vijayanpinarayi',
 'meet_hayer',
 'TendulkarBJP',
 'pramodtiwari700',
 'satpalsattibjp',
 'FirhadHakim',
 'prahladspatel',
 'Sujan_Speak',
 'SunilAstay',
 'iChiragPaswan',
 'BhimArmyChief',
 'pankhuripathak',
 'sravandasoju',
 'HimatoZ',
 'GingeeMla',
 'Chandrakar_Ajay',
 'GauravGogoiAsm',
 'sirivellaprasad',
 'drharshvardhan',
 'jayanta_malla',
 'rashtrapatibhvn',
 'NandiGuptaBJP',
 'JebiMather',
 'kuljeetschahal',
 'sushmitadevinc',
 'YanthungoPatton',
 'AUThackeray',
 'ThiruArasarINC',
 'TThenarasu',
 'KalrajMishra',
 'VSrinivasGoud',
 'rajeshgupta',
 'harjotbains',
 'anil100y',
 'SRParthibanMP',
 'BrajeshYadavSP',
 'adarshshastri',
 'MS4BJP',
 'KNavaskani',
 'bb_thorat',
 'AjayDutt48',
 'RitaBJoshi',
 'rajeshtope11',
 'KapilSibal',
 'Dr_Uditraj',
 'ThamizhachiTh',
 'rckhuntia',
 'GhulamRabbani_',
 'ChouhanShivraj',
 'nirahua1',
 'Keerthireddybjp',
 'Pijush_hazarika',
 'V_Senthilbalaji',
 'PMuralidharRao',
 'byadavbjp',
 'srinivasathilak',
 'Sunil_Deodhar',
 'drrajdeeproy',
 'raosahebdanve',
 'AkshayMarathe',
 'aishe_ghosh',
 'ShobhaBJP',
 'AnupamaRawatUK',
 'gkzhimomi',
 'americai',
 'EPeddiReddy',
 'KrSanjayKrishna',
 'AnandSharmaINC',
 'ChetanChauhanCr',
 'sanghaviharsh',
 'mlabecharam',
 'abumetha',
 'PMOIndia',
 'Shalupcrf',
 'SPK_TNCC',
 'keshab_mahanta',
 'yschowdary',
 'Ch_RanjitSingh',
 'AnkitLal',
 'pratulshahdeo',
 'swatantrabjp',
 'BadruddinAjmal',
 'LjpSaraf',
 'Uday_Bhanu9',
 'Suba_Vee',
 'riyasdyfi',
 'drjgeetareddy',
 'KotasBJP',
 'bjpsanjaybhatia',
 'Gupta_vijender',
 'AkhileshPSingh',
 'AnoopDhanak',
 'RuchiraC',
 'MPArunYadav',
 'sureshbhattbjp',
 'devendrayadvinc',
 'girirajsinghbjp',
 'kumari_selja',
 'SunilYadavBJP',
 'subhashbrala',
 'dreamgirlhema',
 'Ch_AnilKumarINC',
 'ATULBORA2',
 'drcpjoshi',
 'ReginaldoGoa',
 'mlkhattar',
 'TTVDhinakaran',
 'hanumanbeniwal',
 'DeependerSHooda',
 'BhagwantMann',
 'JhaSanjay',
 'thayagamkavi',
 'ShatruganSinha',
 'BikashDahalBJP',
 'Rao_InderjitS',
 'charulata_tokas',
 'VaigaiPravin',
 'Buntyshelke_inc',
 'rajnathsingh',
 'OfficeOfOPS',
 'ShashiPanja',
 'rautsanjay61',
 'VipinINC',
 'arvindkejriwal',
 'SPVelumanicbe',
 'PresidentGFP',
 'mdr_saravanan',
 'Nawalk7',
 'nanglucky',
 'NirmalGhoshMla',
 'MithileshJMM',
 'rammadhavbjp',
 'BSYBJP',
 'klnbjp',
 'GauravPandhi',
 'praful_patel',
 'MamataOfficial',
 'SureshKKhanna',
 'rameshbidhuri',
 'HasibaAmin',
 'rahulgandhi',
 'pangnyu',
 'sunilbansalbjp',
 'Dev_Fadnavis',
 'PradeepraoBJP',
 'RajeshMunat',
 'nstomar',
 'JPNYadav',
 'r_khing',
 'Radhika_Khera',
 'imAkbarOwaisi',
 'BhupinderSHooda',
 'Dchautala',
 'NareshUttamSP',
 'GTDevegowda',
 'DevineniUma',
 'LaliteshPati',
 'INCMohitJain',
 'shripadynaik',
 'vijaypathakbjp',
 'SudeshMahtoAJSU',
 'ppchaudharybjp',
 'DebasreeBJP',
 'ArvindLBJP',
 'RajCMO',
 'RAshokaBJP',
 'RojaSelvamaniRK',
 'HibiEden',
 'SatyendarJain',
 'SanjayAzadSln',
 'shalabhmani',
 'Pankajamunde',
 'mrkpanneerselva',
 'satejp',
 'AnilDeshmukhNCP',
 'JSTomarAAP',
 'brajeshpathakup',
 'HRajaBJP',
 'Junaid_Mattu',
 'RadhamohanBJP',
 'b_kodiyeri',
 'PWilsonDMK',
 'SureshRanaBJP',
 'PSDhindsa1',
 'UmmedaRamBaytu',
 'BanglarGorboMB',
 'AshokChavanINC',
 'chennithala',
 'CMMadhyaPradesh',
 'BJPMadhukarAP',
 'AapKaGopalRai',
 'KiritSomaiya',
 'tejasvi_surya',
 'SaralPatel',
 'hansrajhansHRH',
 'AshwiniKChoubey',
 'MayuraSJ',
 'bhatia_niraj23',
 'VasundharaBJP',
 'RahulSinhaBJP',
 'AndhraPradeshCM',
 'girishgoa',
 'naqvimukhtar',
 'ripunbora',
 'JDSpresident',
 'Chandramohanbjp',
 'MP_SiddharthBSP',
 'UpendraRLSP',
 'AerpulaVenkata',
 'HariManjhi',
 'PSBrarOfficial',
 'MukulR_Official',
 'DrMNPandeyMP',
 'ASPJhanserane',
 'poonam_mahajan',
 'PankajSinghBJP',
 'DrAMSinghvi',
 'Chandrimaaitc',
 'PomiBaruah',
 'JAGANTRS',
 'ImranNDar',
 'mkstalin',
 'mangalpandeybjp',
 'kcvenugopalmp',
 'sajjanvermaINC',
 'virenderrathor',
 'RameshwarDudi',
 'nainachautala',
 'vikaskyogi',
 'VNarayanasami',
 'sujitboseaitc',
 'draramadoss',
 'bhttachrya',
 'MenonArvindBJP',
 'UttamKu73639199',
 'BabuKavlekar',
 'JarnailSinghAAP',
 'ToponKumarGogo1',
 'Jayeshvsal',
 'Sandhwan']


filt = df['author_screen_name'].str.contains('|'.join(tags), na=False)


ds = df.loc[filt]
filt = ds['mentions'].str.contains('|'.join(tags), na=False)


ds1 = ds.loc[filt]

ds1 = ds1[['author_screen_name','mentions','sentiment','type']]
ds1.to_csv('farmbill_mentions_partyVparty.csv',index=False)
tagsr = ['retweet']

filt = ds1['type'].str.contains('|'.join(tagsr), na=False)


ds1 = ds1.loc[filt]

df1 = ds1[['author_screen_name','mentions','sentiment']]


df1.to_csv('farmbill_retweet_partyVparty.csv', index=False)

df2.to_csv('node_farm_mention_with_partyVparty.csv', index=False)

df2 = ds1[['author_screen_name']]
df2.to_csv('node_farm_retweet_with_polvpol.csv', index=False)

