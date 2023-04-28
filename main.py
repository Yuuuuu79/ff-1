from time import sleep
for bb in range(1000001):
  try:
    import h.py
  except:
    print("B")
    sleep(60)