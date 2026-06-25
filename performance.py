import time
clinics = [{"name": f"Clinic_{i}"} for i in range(500)]
clinic_dict = {c["name"]: c for c in clinics}

start = time.time()
for c in clinics:
    if c["name"] == "Clinic_499": break
print(f"Slow: {time.time()-start:.6f}s")

start = time.time()
clinic_dict.get("Clinic_499")
print(f"Fast: {time.time()-start:.6f}s")