import csv
import mo_legislators

mo_legislators = mo_legislators.read.get_state_legislators('MO')

list_vars = ['last_name','suffixes','first_name','middle_name','party','chamber','district','email','url','photo_url','leg_id','updated_at']

def get_val(var, val):
        var = p.get(val, '')
        return var            

with open('data/mo.csv', 'w+') as f:
    fieldnames = ['last_name', 'suffix', 'first_name', 'middle_name','party','chamber','district','email','url','photo','id','updated']
    w = csv.writer(f)
    w.writerow(fieldnames)
    for p in mo_legislators:
        row = []
        if p['active'] == True:
            for var in list_vars:
                 row.append(get_val(var,var))
        w.writerow(row)