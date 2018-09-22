from concurrent.futures import ThreadPoolExecutor
from threading import local, get_ident

ctx = local()
ctx.counter = 0

def inc(_):
   try:
       ctx.counter += 1
   except AttributeError:
       ctx.counter = 0
   print(get_ident(), ctx.counter)

with ThreadPoolExecutor(max_workers=3) as executor:
   list(executor.map(inc, list(range(100))))
print(get_ident(), ctx.counter)
