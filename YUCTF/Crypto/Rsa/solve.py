from gmpy2 import iroot
from Crypto.Util.number import long_to_bytes
e =  3
n =  11910341044374384302617379125490379433072854311514764671764868526316271997199062374128741274979567756258494212115620278335928666244949885255928701245618950371093059139082840313198571300576963443412145945060033239703477401624163988255003007679907850521411559440308457234027146940778940578836881225393551070354653902645485097706123469337766212646923690667591437108866701400105366105056377247386400007988701665598871409068323455846065036365555316190325967934384709149428803289248886143601635030608497203874139820670298679036497605734966385115897949735002187865785110691650594647615433755231847654653821946691344441293689
c =  46670325452385885230608208904001991637776544836470366751916269800253997729013324828891618446813465657537433617045180174813860677812482319113164505950109708460570405815782594375026288479449701214971204970038679979223184987929457438615668389574757



for i in range(100000):
    rot , itrue = iroot((n*i)+c  , e )
    if itrue :
        print(long_to_bytes(rot))
