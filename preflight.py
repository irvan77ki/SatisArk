import json,glob
S={f[:-5]:json.load(open(f)) for f in glob.glob("*.json")}
ids={n:{r["id"] for r in rows} for n,rows in S.items()}
allids=set().union(*ids.values())
issues=[]
for n,rows in S.items():
  for r in rows:
    for k,v in r.items():
      if v in ("UNVERIFIED","",None): issues.append(f"{n}/{r['id']}.{k} unfilled")
      if k in("tameItem","boostSource","target","needs") and v not in allids: issues.append(f"{n}/{r['id']}.{k} -> '{v}' does not resolve")
      if k=="allowedMachines":
        for m in v:
          if m not in allids: issues.append(f"{n}/{r['id']}.{k} -> '{m}' does not resolve")
print("\n".join(issues) or "clean")
