import csv
import mo_legislators.download

mo_legislators_list = mo_legislators.download.get_state_legislators('MO')

list_vars = ['last_name','suffixes','first_name','middle_name','party','chamber','district','email','url','photo_url','leg_id','updated_at']

def get_val(var, val):
        var = p.get(val, '')
        return var

with open('data/mo.csv', 'w+') as f:
    fieldnames = ['last_name','suffixes','first_name','middle_name','party','chamber','district','email','url','photo_url','leg_id','updated_at']
    w = csv.writer(f)
    w.writerow(fieldnames)
    for p in mo_legislators_list:
        row = []
        if p['active'] == True:
            for var in fieldnames:
                 row.append(get_val(var,var))
        w.writerow(row)

mo_fed_legislators = mo_legislators.get_fed_legislators('MO')

def get_val(var, val):
        var = p.get(val, '')
        return var

with open('data/mo-fed.csv', 'w+') as f:
    fieldnames = ['last_name', 'name_suffix', 'first_name', 'middle_name','party','title','district','website','twitter_id','youtube_id','facebook_id','bioguide_id']
    w = csv.writer(f)
    w.writerow(fieldnames)
    for p in mo_fed_legislators:
        row = []
        if p['in_office'] == True:
            for var in fieldnames:
                 row.append(get_val(var,var))
        w.writerow(row)
