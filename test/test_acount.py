from acount import Acount


acount_luz_1   = Acount('LUZ')
acount_luz_2 = Acount('LUZ_2')

assert acount_luz_1.name_acount() == 'LUZ'
assert acount_luz_2.name_acount() == 'LUZ_2'

assert acount_luz_1 != acount_luz_2





 