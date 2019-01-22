import pickle
website = {'title' : 'Techbeamers', 'site_link' : '/','site_type': 'technology blog','owner':'Python Serialization tutorial','established_date':'Sep2015'}

with open ('website.pickle','wb') as f:
    pickle.dump(website,f)

with open ('website.pickle', 'rb') as f:
    data = pickle.load(f)
    print (data)