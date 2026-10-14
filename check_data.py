import json
with open ("tickets.json") as f:
     tickets = json.load(f)
print("Distinct priority values:")
for value in {t.get("priority") for t in tickets}:
   print(f" {value!r}")

print("\nDistinct status values:")
for value in {t.get("status") for t in tickets}:
    print(f" {value!r}")
