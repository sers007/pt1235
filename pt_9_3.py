import requests

res_psrs_list=[]
resp = requests.get("https://coinmarketcap.com/")
resp_test = resp.text
parse = resp_test.split("<span>")
for pars_elem1 in parse:
    if pars_elem1.startswith("$"):
       for pars_elem2 in pars_elem1.split("</span>"):
           if pars_elem2.startswith("$") and pars_elem2[1].isdigit():
              res_psrs_list.append(pars_elem2)

bitcoin = res_psrs_list[0]
dogecoin = res_psrs_list[7]

print(bitcoin, dogecoin)

