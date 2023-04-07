#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re
import requests

url = "https://www.google.com/search?q=site:instagram.com+%22instagram.com%22+%22indian%22+%22influencers%22++%22%40gmail.com%22&rlz=1C1RXQR_enIN1028IN1028&sxsrf=APwXEdezi43XOlx-W8RnehMjxKBKnTqkNQ:1680747518040&ei=_isuZN6KAuTC4-EPwL2k0Ak&ved=0ahUKEwjegZS2mJT-AhVk4TgGHcAeCZoQ4dUDCA8&uact=5&oq=site:instagram.com+%22instagram.com%22+%22indian%22+%22influencers%22++%22%40gmail.com%22&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQA0oECEEYAVD7KFj7KGC1MWgBcAB4AIABhQGIAYUBkgEDMC4xmAEAoAEBwAEB&sclient=gws-wiz-serp"

e_regex = r"[\w\.-]+@[\w\.-]+"

r = requests.get(url)

for i in re.findall(e_regex, r.text):
    print(i)


# In[ ]:




