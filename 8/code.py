from collections import Counter
import itertools
sample = """
be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce
"""

real = """
dg debg edgfc afbgcd efdbgc gdc bfdceag bfdec febcad gfaec | dcg bdaegfc egbd dcgfe
ebafgc feadcb deagf gdacf gae edbg ge bcefagd dgbefa ebfda | eg bgfaed fgdaecb agcdbfe
gfcbe bfg fg efbca bcdgea dfge gdcfba dfbgcae ebcgd cgbedf | fg cegabdf cebdg cgebdf
bdafg gbdfea ge fegacd gabcdf eadbg egd cgafdbe acdbe gfbe | cebda bfgda bfdgace adcbefg
fdb fdbce cbade fcdagb fcgdbe cgbfea fd dgfe afbdecg fgecb | fedg cdebf fd dafcbg
dcgefa fcgbde bdecg cde edfb cfdeagb feagbc de efbgc bdcga | ed febgc fabgec cegadf
fbcaeg cfgdae egc edgcf fdcag ebdcf dgae bagcfd eg eagfcbd | gdcfeab adge cbgfad cedfb
edagf bfg dbcfge cgeab aebfg dcgeaf fb daebfg eafcbdg bfad | ebafg gfedac bfg ecagb
bafgce agcdb gaefc agcfed defbag cbgfa afb fb ecfdgba cebf | bf bf dacbg cfgab
egcdbaf begdaf acgfdb fcba cfbdg cbd gdabf fcdge bc ecgdba | dcb dgefc dcbgf ebcfgad
cgbef faedc acfbgd fcebdg ebfcag febdacg ba gaeb ebcfa abf | cefagb ba dceaf bfa
gbaed cbafeg ebc bcgedf gbcaedf becga geafc cfba adgfec bc | gaedb aegbcf cb abfc
dgbec fd acgdfbe bfaced efad cagbef dcgabf bcfed cafbe bdf | dgcbefa ecdgafb fdb fbd
dcagfeb daf decgf fa dcfag gdacfe dbgcef cbdga aedcbf fega | gafcd fad afd fdaceb
bcga gfcad cgdbf caf dbcfage ca cbdafe efdga egdcfb dbcagf | fdecbga bfdcg fca efabdc
eafd adfgecb cgfdeb egfab ea cgfba gea dfgeb debacg eafbgd | ae efda fdae fade
dce acdfg gbdace ecbgdf gadbe eacb dfgceab agedc gbafed ec | fgedacb dec bdgfcae ced
ebfda fabcde adgcfe fdc cedb eagbfcd bfacd gedfba cd cbfga | bgdfcea dcf afcgb ebfacd
cebadf ecdag gadb bcage deabcg eda fbaecg fdceg fagebdc da | edbcag badg ad gbad
dbafegc fgdaec acegd aedfbg fcdba bdg bgacde cdbag ebcg bg | gecb bg bdagc cedag
gb bgf bagfce geacf acdgef fbecgd bacg geabf cdfageb defba | cbgfae egbfdc afebgc fbdea
da fda bedcaf cbfde egbaf ecgdbf aefdb adbc afgdce dcegafb | gafeb gadbfce ad ad
cedf bdagf dc ebafc dca dfbac cadfgbe bcfaeg acdgeb bcfead | ebdgfca bcdfa adc dabgf
dcbga daf efga dgcbfe fgdca af efbdac fgbdeac efdcg dgfeac | fbdegac fdagc bdeagcf agfe
abg gb ecfdab afegcb afbed dgfab cadfg gdeb dagfeb degafcb | bg egbd bdafg deafb
bge ecadg fgecdab dgfecb egdcba egdba dcfaeg gbdaf bcae eb | be aecb be ecdag
cgade dbgec debgcf cdbeag ea gafcd fgabedc edba cae befgac | eac ea daeb eac
bca cb acfgde gbdea adcbe acgbef cebgafd fdcb fcade ebcadf | acgfde dabfceg cb bagedcf
cdfgeab acd cbdfg dfcga gedbac fdcgba gdefa gfdecb ac fbca | ac afgecdb gcefbd ac
aec afcdegb gceafd fbdagc ea aebd agebc adcbg gcebad gbcef | cdgbfa aec fecgb adfbgc
efcda cgefa cag dceafb acdfgb gc agefcdb adcfge agbef edcg | cg cdaef agc gca
dgbeaf bdg eabd cadegf edbfg cgfbe cabfdg dgefbca daefg db | gbd edbgcaf eagfdcb edab
gdbca fdgecb fabceg geadbfc cdafbg ga gca cdfbg bdace fgad | fdcbg ag fdga agc
cdfgaeb ca dcbfe cabg eca befga cdfega bcgaef ebacf gbefad | aec bcga cea eabfgd
efgd deagc aegcdf dgcaf gdacefb ecafbg gfa ebacgd cfabd gf | dagbfec bcfad fag fag
dcbage beagcf dgfaeb eac bcaf ebfcadg cfegd ac beafg gfcae | eca cae acegf abfc
cfeag agbdfc bc fdagb cbdf cab faebgdc fdbega bcdage abfcg | cbfgda cgbaed gbafd fcbag
facgbd begda bf fecb adefc bfdecag fbeadc fab afdbe egafdc | dfcgea edbacfg fb bcef
dbf dfac cebfa egdcb bfecd df afbdeg fedcba fcebga aecdgfb | ceafbd cbegd gacdebf bdf
dgfae agfbedc badgfc cagb ca fdgca dca dbcgfe cfgbd dacebf | cad ac gdbaecf gacb
fcgad dbgac ebcfdag fcagde feda gcaef fdc cdfgbe df gbacef | cgaebf cfd fgecda gdecfa
cadfbe gbcaed geac ecb begcd dbega gdbcf ec acbdegf agbfde | cdbgea ecb fdabegc efdgba
adgfb afdegb dbgcfae cgdbef aedg bedafc dab ad gbfac ebfgd | bad da adb geda
dcgbe aecd gcfadb ad dag gabed efcbagd bafeg ecbdag bcdgef | bdecg abgde gbfceda ad
dcfgbe fedcgab cba gcfaeb abcgd dgfac ab dgecab aebd ebcdg | fcgeab deab baed cab
acbef gbfca fg bfge ecdagfb fadbec fgc ecabfg fgacde dacgb | fegb cgf adfgceb efbg
eaf fbde dcabgfe cdgea ef gfbdac bcafd facbde ecadf cbaegf | fbde fe fbed fegabc
cdbfe gfcd edbfga cgdfaeb dfb gbfcae df ebdac gfbedc cbgef | bcedf dbf eagbfc cgdf
edf bade ecgfdb gacfeb fegbda eagfb daegf gacdf egdbafc ed | fedgba deab dbaegf agfdc
bdef aed dgeab de ecabgdf agefb afebdg fecdga gfecba bagcd | aed fbed bedf dfgaeb
dgcefa gfdecb ae aec dagcfeb ecabf cebfg cfbeag afdbc beag | gabe ace dgeafc cgbef
dcfeb eadfbg ecad ed afbdec bcfda acfdgb ecfbgad dfe cegbf | adec acedbf ed ed
abd bfcd adceg bgefad dfceba db decba ecabf efagcb cdfbega | egdbfa deagc cdbf befdacg
dbacfeg bcdfa defbg aedfb gaed eba gacefb ae cedbfg dfaebg | abe ae deag cbeafdg
acbfdg abcdef gcdb gedfab dcagf dfg gcbdfea dabfc eacgf dg | dgcb afceg cbgd bdgc
dgbace bgaed dbgacf fb bfea fgdcaeb gbf dcefg dgefb gbeadf | bcgfead dgafbc fabe dbfge
egdf fbagdc gbd dg ecbfga egbfdc gcbef bcged egbdfca adbce | dg gecfdb adcfgeb efdbcag
gcfdb gacbd fc ceabgd gacbef egbdf acbdgf adcgbfe dcaf fbc | dcaf fdcgb bgcafe cdaf
edbacf dgfaec feb feadc bcfed cdefbga bdegc cfba dfaebg bf | ecbfd ecbafgd adgbcfe fcedb
ba cgafeb fdbecg dbag dfcae ebdgf bgedacf abfde fdgeab afb | ebgadf bcdgafe egbdfa abf
defbag dcgf acbdgf edcba gecfba fdgba cg gac adcgb ecadfgb | gbacd cgfd gfcdba gc
fbd dfecag dacgbf dcebgf bd cbfae cdgfa dbag dbcfa cgbfead | dbga bfd gadcef cgfaed
daceg ecfdgb ab gab bcdgf cdafegb cgadbf bdaefg gdbac afbc | ba bfac gbdcf cbdegaf
ef gbfcd caebg cdfe gafdbc bcgfe feg fcdgeab efdgcb dgfbae | gfe begfdc bgefc cefgadb
eafc fecdab fcebd bdegcf dfeacbg cab bdegac ac gadbf bfacd | bcedf bcdega dfbac fbdcgea
bef aecbd edgbcf ebcadf adefg dbecfga bf eadbf cfab gabecd | fb cabf cafb efb
agef fecda cdfbga cgefda efcbad fg gdf cdbge ecgdabf cdgef | cadegfb ecfdg dfgabce gf
ebcf gcbed fcgbdea gef gecdbf baecgd ef fabdg egdbf gdfcea | gfedac cgdfeab fe ef
adebf fecg gedbc fg bgfdeca dfg fagdbc dgefb gbdcea cfdbge | dfg dfg gdf ebgfadc
gacb dfabg abfdc gfa fadgcb ag gdefac ebcdaf bfdcega gfbed | ceabdf fadcb bfdca bfegd
ecbagf bdfae gfbd adebcf gdfae agf ebadfg abdcgef fg egdac | gdbf afg gf gdefa
bfde cbafdge agced dbfacg gcbfd bfdgce ef gdcef feagbc feg | dgcfe gefcdb aecdg cegad
dc cead fdc adgcf dgfae dfgaec cfgab gbdeaf gebdcf edgfabc | bafcg cdf cfdegb dace
bf cbedg fgeca fgeacb bcafdeg fgdaec badfgc gcbef fbc baef | fb fbea bf fbc
db dcfbe cgfeb daefc efdgcb edabfg bed cgbd facbdeg eacfbg | baefcg fabgec gfbced egbafc
baedcf cadeb beg cgeadfb cbdage edfag eabgd bg cabg cebdgf | cgab fcbegd gb bg
egbfd ecdafg gfbdec eda ad fabd acbge becfgad adgbe dabegf | ebfgd da gbdfce cfgeadb
caegf dafbcg cbef dfgae bdegca fc cebagf gfc cbage cafgbed | cf abcedg cf cf
gcaebdf bc adcfe cbaefd bcd gfdace decab cbfa bdcgef adegb | ecgfdba abdge cb bcd
egcbfda gfda efacbg edfgca cdeab cgfdbe dg ceagd cgfae cgd | dg bacde geacd dafg
baf efbagd bgaecdf gadcf ecbf baegcd afdecb cedab fb adbcf | bafecd fbcda fagedb bf
efadbc ebdac dca dbefa bdfgae gfabdc agbfedc cefa cgedb ac | cafe dgebfa cefabdg bdeac
cegabd ebdfc dbcefa cgdfba fc cebda efac fbegd gebcfda dfc | bdfge ebacd becgadf fdc
gcbea bd febgac fdbeca ceadgb fcgde ebd cedgb gdeabfc abdg | gafbedc gcfde bed gdbce
dac cbgd cbdea ceafdg gadbe dcbaeg fbcae cd gadbef gdafceb | adc cbfaged ecgfad dc
dfgeac dfage gdfc gc febgad dbgcae gce fcbae cbdafeg cfaeg | dbfegca gec gce afdceg
fdbaceg cadfge gbedc edfgb agecb dc dcaebg dcg acdb bafcge | gafbdec gbcae fgdebac cegbfad
fcabed gbaefc dgeb dgfaecb bcfde bcfged gefdc adgfc ge gce | gbde ecfdb cge gebd
gdebc cdab decag ecb fgebd ebcfagd cgbade gceadf abcfge bc | ecb dbac cdab ecb
dgcbfa caebd gcbfdae dgbfc efdbgc ecg dfeagc eg bfeg gbced | cgfdeb eg ebgfcd gbdce
ba cdfgae bdcafge dagecb cegfb dcbfae gabd eba gaecb cegad | gadb ab feadcb efadbgc
bed dcbage dgce de bgdfca ebdca bcefa agcdb gacfdeb abdegf | fdcgaeb ceafdgb cdge cagdbef
beacgfd dgebaf agefbc fagbc fgcdeb cabgd cfg fc gebaf eacf | afce fgc fc gebafc
gfcadeb deg fbdec egafb dg fdegb aefcdb edacbg fgdc dcbfge | deg dbeagcf deg afdecbg
egacf aeg fbcag ea gcfdae ecda bagdef baegdfc edfcg fcedbg | dace dgbefc ae ae
degbf fbgdae bdcfae decgbfa fgcd dbc bgdefc bdgce gabce dc | cd dbc dc abgdfe
fda df bafceg cfgeadb abgefd fdgb gdaef eagbf cgaed abedcf | cfadbge bcdefa fad cgead
acd gfebca agdfbc debcf agcef bagedfc fdecga aedg da dcfae | gbcdfa gaed feadc agfce
adbfgce dfgeab cd ecdb dcgbfa fcgae fdegb egcdf fgdcbe gcd | cfdbeg efdabg caefg cafgdbe
fb dbgcf cfbe gdbce eabfcdg gadefb dgcebf bfd gdcfa cedbga | bcef aedgfbc cfbe gfadc
cdgefa gcdaf baedfgc fag dgef edafc adbgc abfegc fg bcdeaf | fdcbae facedb fg bacgd
cebfg fd fdecag gdbcef gbead def fdcb fcaebg fedbg gafecdb | dgbcfe fdbeg gdfcbe cfegba
deabgf cdaf dabfg fgbca deagcb bac fbdcga ac cgefb caefdbg | degbca ac egbadc cdfa
bafcge dfec bacdgf ecbgd bgfedc dcbgeaf eagdb dfgcb ce ecb | bdgacfe aefbcdg bce dfgcb
edcbgf agfedc ebafgd cgfad fdcba cega febcgad gc fcg dgfea | cg gcea fcg bgefda
efgab gced gc gfc abedcf bdcefg febcg bgafcd acbdfge befdc | gcf fgc bedfc becfd
ceagbd adbf gfdec eadcf fabce agdbcef abcfge dac bfcdae da | bfegacd fcead dabegc dac
af fga gcbea dcgeaf cgdef fbgdce fdea febgcda fbgdca faegc | fcebgd fdegcb gfecbad eagfc
fegcad decg daegf badecgf cdbafe fgacd dbegaf dc gcbaf adc | gdaebf dgfea acd dcefag
decfb eg dbfcag egd adbcefg gefbda bdgef cdfeag geab dbgaf | fdgba gdcefab eg fabdg
gfbaced adcbg ecbdga gfceda cbgfe acgbdf ced edab de ebdcg | gaebfcd adcgbf ebacgd ced
ba eacgfd beadcg dfgac dbgcaf fdgeb bcaf bga fecgdba dfbga | dacgf acedgb agbdf dbfegca
cdbgfa dfgbe gdabf bdfage ef gedbc fde bcafed bcagdef gafe | efd edf fe ebcdg
befdg bagced dcb fgaecb fbced cfda dcbfea cfagebd cfeba cd | cd cd fdgbe fdac
cfead cafb gcdaeb ca adfecbg degaf fecbd ecabdf aec bgdefc | cbedfa bacfedg eac ceafd
dgacbe dfcbgea decbgf cagdf daceg cde adeb de fcbgae cbgea | bdae ed gbdcae cfbaeg
fbedc fgceabd eg cge adcbg baeg dgecb fdcgea badceg gbcadf | dabgec gbae cbdfga aebg
fbgd aedcfgb baf abgecf fcabd fb dcbae afgcde dcfag adgcbf | gafbdc fab fb dgbf
dgbacfe bafgd ceda gfabec cd fdc cfebgd acfbe fcbad cedbfa | cdaefb fbecga fceab cd
dfceba aefg ebagc cfbgad afdgcbe bafegc gcedb ea aeb acfbg | gfaecb eabfdc bagcf geaf
dfcb bfedg agedf defgcb db fgcbdea dbe fgceb gefacb dgcabe | fcdb db db acdbge
fgbcad dabce fdbe dfaec dcb cafdbe db gecba efcdag bgeafcd | cegdfba faebcd cgeadf fabgdc
baegcf dgcb ecgafdb bgdeca cd fegad caegb cedafb cde egdca | efgad cbegfa egbdfca aefbdc
bcdaf cgb bafge afcbeg fgcebda bfacg dgfebc cg eabgfd geac | cbg bcfdgea gbc fcdab
fg dbegcaf decabf gfd gdaebf decga cfbg cdgef ebgfcd fbdce | gfd fegbda cdage dfceg
fdeca cb gbedac gecfab bac edacfbg agfbe efadgb cbgf fcabe | acb dfgaeb cfdae bfgeac
befcag cdgfa acg befcda fbagd cg cfead bgdafec edcg dgfaec | cag dcefabg gca gecd
decab cga acgefb agbef adcgefb cg faegbd cfbg acbge fdcega | abgdcef cg cg cbdae
abc fcbge cdafbe aegc gbefcd ca gbface bdfga cbafg acdebfg | gcbfde cgafbed geca fgbeac
afbegdc edacb dabeg edcfa cebfad bc ceb dbfc cegafd gbeafc | efbgca becda bce adbeg
aedcgbf ab ecadg gdeba fgab dba abgdfe fcebda fecbgd dgefb | decga bda cgafedb afcdbe
dg degbc aebcdf cegfb gbcafd daceb dcg cegdab adeg egcabdf | gd bcged gcbdafe cegbd
cbgd acbefg db dbaecg dab afecdbg dfage cfebda aegbd agceb | dcbg ecdgba db dbcg
fedgc agf ga fcagbe dfgcae dega fdbceg fbcda dacfg efcdbga | ag fga ga ga
ca fdgbac bcedf afgdeb adfgecb cdbfa cefagd afc bgfad cgba | gacb ac bcgdfae cdagef
acdbfe abdge gca gc gcfdba aebcg faebc bgefdca cefg cfbeag | bcdagf dgeba gfec ecfg
fdbga afd dbgaefc abfc af fgbcda ebcadg dcgaef fgdbe cdgab | fdgab gefbacd af ebdgf
gcafdbe efd ef cdeba abdfcg gdfaeb egcf bedcfg gfbcd cfdbe | dceab gdcabf ef fe
bdca cdfgeb begfa bdf bafgdc db fcgade ecadfgb dbfag gcfad | fbd fbd bgdaf gafdc
efbacg bgedc abcdge bgd dcba db agbce gcfde cgbdeaf eafdbg | bfcega cgdbe bd bdg
fbe fcgbeda fb cebfa ebgac egacdb gebadf ebgcaf adcfe cbfg | bdcafge afgbdec bdegcaf fb
bdcgae fcdbag cdeafg defa fcgea af gbfce cegad bcefdga acf | acf cgdeab dafbcg aefd
ebcag eda ecfabd fedcgb cgfed eagcdf da acedg gcdfbea agfd | dgace agfecd egcbfda cbdeaf
dbgec gebfdc cba bdgfaec acebd ac acdbeg agcd afbed bgaefc | cegdab eadcgb feabd acb
afcg cgadb bedcga efgdb fab gafcbed dabgf afcdbg dcfbae af | baf fbegacd abf fab
ae ebagcd gacdebf gdfeac afdge febgd faec ade dgacfb cadgf | gfdea ae eda bgfde
gbdacfe faedbg be cbgfa ebac cbafgd efb gbfce fecbag dgcfe | fcegb acgfb bafedg ecab
dbefac fdegbca ec ced cdafb cdeab dgface abegd fcadbg cefb | baegd dce edc gdbea
gadecb dcge fcabd ec afegbc gdbae bcdfeag aecbd fbgdea ace | eac geabdf cae bacedgf
efabd ga ebadcf cgdfeba adfceg fadbge degbc baged bfag eag | abgf bfga aeg aeg
eafdbc acgdbe dfae deb gfcbe fdbcag ed fbced cfabd fadegcb | cfgeb ed ebd eadf
egd caedgf de gbcea edafbg eadgb fadgbec bedf bgfda dgabcf | de efdb aecgb gadbf
ceg cade dgfbac cfdeg agcfd fgdeb ce gaecfb fcdageb defacg | fdabgc aced edfgb cdae
fadebc fa fade dbgfca ecfbg ebdcfga dbeac egcadb afb ceafb | fa daef cegfadb dfae
eadgbc fbaecg gdb db fcebdg cdgfa gbcad egbca abde gefcabd | gbd db cbdga acgbe
cab dabgef defbcga ca aecgfb aecf dcegab bfaeg bacfg gfbcd | gfdcb bfaedg ca egabf
bace egbafd fceabg beafg afc ca bafecgd afegcd dgcbf bgfac | bdcefag dfbcg cebgfad fagdebc
afc gcadf dacbfe ca gdbacf befcagd gcba cbdgfe cfbdg fdage | agfcedb febgcd ca bcga
cdgbfa gbdac bda gdebc fcebagd cbeagf gfda efbdca ad fagbc | cbfga gafd fgad gadbc
eb edfagb agecdfb agdfbc gebc cagbfe edfac efb acfbg acfbe | febdag egcb bdgfca eb
cadgebf dgbf bf baf gdbea gbdace gdbefa bagfec ebdfa cafde | ebdfa ebdafgc gfdbea gfdbae
fca cafdg bdacfe bgfa cbdga dcbage af gfcde bfgcda bcegfad | caf caf bafg afc
ecdfa fegda cedgfb ge gcdfae deg efcdab fgdab cgafdeb cgae | fdgeacb gabfcde afgdecb dfgceb
fcegda bcegda fgabcd geba bcafedg cdbge gceda bgd cebfd gb | bfgcda egba geba dgbceaf
fagdeb bgf cdefgba dbgea agfe fg dgaecb bfcda abgfd cdebgf | agfbd agcebdf fbg fbg
afdeb fb ebafgd cafbge gdfb egdba fab dbcaeg bcdegaf eacfd | bf dbacfeg fb baf
fcdae gacbed bcfgead agbd cfegbd acb edbgc cabgef ab edcba | adbg acb abfgec ba
ceda ecfab beadcf eba bcedf ae adcbegf bgafde cbfag gedcbf | gacdebf ceda cefba abe
edgc dfcbge dfbga bcgeaf bgfcd bfcde aedfcgb dcbafe gfc cg | dgec gfc cegd gacefb
dfe dcbe efdbag fcdgb fgcadb ecdgf efcga cgfbde gfdecab ed | eacfgbd dceb cfgdbe de
ecbdg daefb edgbac ac fcdeag cae cgba dfebgc dgefcab dbaec | cgadfe abdef ac aec
cdgbef debacf gafcb ea abde bedcf efacb efadgcb fea eacfdg | ecbfa ea ea fcbde
bacd eadcg gecfa edbgca edc gfcbde dgeba gfbcade cd bdafeg | aedbfg dc fabcegd cde
edfgb agebdf gc gbdafc adfebcg dfceg bcge cgebdf eafdc dgc | cdg dbefcga cg egcfd
befd gaedbf decgab badgf gcebfa bgeda dcgaebf bf bfg afgcd | bf fb edbacg febd
abcdgef egba bfcdga ecabfg dcfae ab fab fecba cfebg dfebgc | afb egab abge aebg
debgac ad afcbeg adg cfgad gdecfa daef gcaef cgbdf cebgdfa | cgfda cgfad ad da
gcbade dagcb gefba agebc bdec fagedc ce daebfgc fabgdc cea | decb bfgea ce ecbd
ecdfbga dcabfe efdagc bdcae ga dfbcg gcbda agd egab eagbcd | cdebfag ecabd fbgaecd ag
acgfebd dacb acfeg bagec ebfagd cdegb bga cgadeb bfcedg ab | cgbade agecb adcb ab
edfac fdcb fdeabc fbe cfabe acdegf gbcae efgbda bf cgdefab | bgefad dcfeabg bef bfcd
gdaceb fac gafcdb cefdab fc cgabd gfbc fcdag agecfbd daegf | dagbfec dfcagb dgacf gdabcef
bgfdac db cbd fbdg cgfaedb cgafd acbef dcbfa gfceda bgaedc | agcefd cbd cdb cdabf
adcgfeb cdafbe agecbf egdcb gbaf dgfcea egf baecf fg fbgec | fcdabeg agbf bgdec efcdab
adbfec abfge cgdfea fgbaced gecfba edgbf fceba age cagb ag | age ga age gbecaf
ebfdg ecfdb fcd bfaegcd cdbg fdcgeb afbged ceabf edafgc dc | egbadf cbfgde febac gbedaf
gfacd cefagb bcegdfa ad adbf gfdcba adc bgecad gcdfe bgfac | da gebcfa fdgac gcfab
feacbg ca bgcfd gdacb dabge bgeadcf gca fdca fcdbag cdfgbe | badfgec adcf dbfegc cfdabge
acb gcbf acbefg fcade bfaeg gebadfc bc aecbdg bgeadf bface | gfcb gbcf dfegabc cab
gcfadb cdf eabdfgc df cdefga gbacd gdbfc eagcdb dabf fgecb | bcgfe cgfbe bdagce gbdfcae
gecab bgecfad defcg dae caegd ebfagc da cbaged fdecba bdag | gadb agbd eadgc ad
fabce bafdegc abfegc dabecf dbgeca gbdaf gbe eg bfega cfge | bdafg eafbg febcgad gcedab
eafdgc dabgcfe dafceb efa fbde acebf acbde ef bcgaf cgeadb | aef ef edfb cgbaf
gfdacb gfedac cefbd cgea egfdc gcd bgedfa eagfd cg fcagebd | cg fgdcae cg cg
ebfga dgbcef gbc cdbef agdfbec cfdg cabegd dcfeba gcfeb cg | afbeg cg bgcdfe gefba
cfgdb efbgdca gde gafcbe gacbed acbeg ed dcgeb fagdec adbe | ecgdb deg gbeafc gaecbdf
gdefbc egfb fcbeda gabecd fcdbg bg bgc dfgac dfbec bfgadce | afbdce bdcefa bg acfdbeg
ed gbcedaf gbde defcab efbdga adfbg adegf ecfga dae dcgfba | cafgbd bdeg bcfdga gefbcad
gfeabd ceafd gca agdcfbe badge agbecf dcgeab gcbd gcade gc | daecf dbeag agc gc
cgbaf dbagf da gdcfbae febdg gbfeca bdca cdegaf gfdacb fad | cgafbd bcafg fbdga badc
"""

SEVEN_SEGMENTS = [
    ' aaaa ',
    'b    c',
    'b    c',
    ' dddd ',
    'e    f',
    'e    f',
    ' gggg '
]
DIGITS = ['abcefg', 'cf', 'acdeg', 'acdfg', 'bcdf', 'abdfg', 'abdefg', 'acf', 'abcdefg', 'abcdfg']
LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
assert len(DIGITS)== 10

def parse(text):
    return [ [x.split() for x in line.split('|')] for line in text.split('\n') if line.strip()]
        
data = parse(sample)
assert len(data) == 10
assert len(data[0]) == 2
assert data[0][0][0] == 'be'

def part1(data):
    n = 0
    for row in data:
        output = row[1]
        n += len([x for x in output if len(x) in [2, 3, 4, 7]])
    return n

assert part1(data) == 26

realdata = parse(real)
easy = part1(realdata)
assert easy == 473

def find_unique_length(n, combos):
    out = [x for x in combos if len(x) == n]
    assert len(out) == 1
    return set([c for c in out[0]])

def singlev(x):
    elem = list(x)
    assert len(elem) == 1
    return elem[0]

def render_print(digits, mapping):
    output = [list() for x in range(len(SEVEN_SEGMENTS))]
    for digit in digits:
        for i, line in enumerate(SEVEN_SEGMENTS):
            text = line
            for ch in 'abcdefg':
                text = text.replace(ch, '#' if mapping[ch] in digit else ' ')                
            output[i] += text + '  '
    for line in output:
        print(''.join(line))

def signals_to_number(signals, inv_mapping):
    out = ''
    for digit in signals:
        ch_mapped = ''.join(sorted([inv_mapping[c] for c in digit]))
        digit = DIGITS.index(ch_mapped)
        out += str(digit)
    return int(out, 10)

def deduce(s10):
    one = find_unique_length(2, s10)
    four = find_unique_length(4, s10)
    seven = find_unique_length(3, s10)
    eight = find_unique_length(7, s10)
    mapping = {}
    mapping['a'] = singlev(seven - one)
    print(mapping)
    bd = four - one
    aeg = eight - four
    print('bd=', bd, 'aeg=', aeg)
    abdeg = eight - one # not useful?
    assert bd.union(aeg) == abdeg # just for sanity, not deductive
    print('abdeg=', abdeg, 'sum=', bd.union(aeg))        

    # a occurs in 8 digits
    # b occurs in 6 digits
    # c occurs in 8 digits
    # d occurs in 7 digits
    # e occurs in 4 digits
    # f occurs in 9 digits
    # g occurs in 7 digits

    occurrences = Counter()
    for digit in s10:
        for elem in digit:
            occurrences[elem] += 1
    print(occurrences)
    inv_occurrences = {}
    for k, v in occurrences.items():
        inv_occurrences[v] = inv_occurrences.get(v, []) + [k]
    print(inv_occurrences)
    assert len(inv_occurrences[9]) == 1
    mapping['f'] = inv_occurrences[9][0]
    assert len(inv_occurrences[6]) == 1        
    mapping['b'] = inv_occurrences[6][0]
    assert len(inv_occurrences[4]) == 1        
    mapping['e'] = inv_occurrences[4][0]

    # the one digit pattern, is known, and consists of c and f. Since f is known we can deduce c.
    mapping['c'] = list(one - set([mapping['f']]))[0]

    # check: c can also be deduced because it has 8 occurrences, as does a, and we know a at this point
    c2 = singlev(list(set(inv_occurrences[8]) - set([mapping['a']])))
    assert mapping['c'] == c2

    mapping['d'] = singlev(bd - set([mapping['b']]))

    dg = set(inv_occurrences[7])         # 7 occurrences is d and g 
    mapping['g'] = singlev(dg - set([mapping['d']]))

    # confirm we had no ambiguity
    seq = mapping.values()
    for ix, x in enumerate(seq):
        for iy, y in enumerate(seq):
            if ix != iy:
                assert x!=y
    return mapping

def part2(data):
    result =[]
    for row in data:
        s10 = row[0]
        payload = row[1]
        mapping = deduce(s10)
        print(mapping)
        bmapping = brute(s10)
        print('potential mappings', bmapping)
        assert mapping == bmapping[0]
        inv_mapping = {v: k for k, v in mapping.items()}
        print('inverse', inv_mapping)
        # render text
        render_print(s10, mapping)
        print(signals_to_number(s10, inv_mapping))
        render_print(payload, mapping)
        x = signals_to_number(payload, inv_mapping)
        print(x)
        result.append(x)
    return result
        
def brute(digits):
    """Find all mappings which successfully decode the given digits, by brute force"""
    out = []
    for mapping_permutation in itertools.permutations(''.join(LETTERS)):
        mpl = list(mapping_permutation)
        mapping = { LETTERS[i]: mapping_permutation[i] for i in range(len(mapping_permutation)) }
        inv_mapping = {v: k for k, v in mapping.items()}

        try: 
            x = signals_to_number(digits, inv_mapping)
            out.append(mapping)
        except ValueError:
            pass
    return out            

res = part2(data)
assert sum(res) == 61229
realres = part2(realdata)
print(sum(realres))
