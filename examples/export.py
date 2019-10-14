import xenarix as xen
import xenarix.sample as xen_s
import xenarix.results as xen_r

# default repository : [your_working_directory]\repository
# xen.set_repository('c:\repository')

# scenario set
set_name = 'set1'
scenSet = xen.ScenarioSet(set_name=set_name)

# scenario
scen_id = 'scen1'
result_id = 'res1'
scen1 = xen.Scenario(scen_id=scen_id, result_id=result_id)

# generation setting
scen1.general.scenario_num = 100
scen1.general.maxyear = 10

# model add
scen1.add_model(xen_s.gbm('kospi200'))
scen1.add_model(xen_s.gbmconst('kospi'))
scen1.add_model(xen_s.hw1f('irskrw'))

scenSet.add_scenario(scen1)
# scenSet.generate()

# get result from current repository
res = xen_r.ResultObj(set_name, scen_id, result_id)

for model in res.res_models.values():
    print(model.name)

# export csv
# for i, model in enumerate(scen1.models):
#     filename = model + '_' + str(i) + '.csv'
#     res.get_resultModel_by_index(i).export_csv(filename)

res.export_npz(scenSet.set_name + '.npz')

#print(res.result_data_info)

import numpy as np
import pandas as pd

arr = res.result_data_info.to_numpy()

np.savez('test.npz', test=arr)
test_d = np.load('test.npz')
dd = test_d['test']

for f in test_d:
    print(f)



#print('dtype : ' + str(arr.dtype))

# for k in res.result_data_info:
#     print(k)



d = np.load(scenSet.set_name + '.npz')

for k in d.keys():
    print(k)

