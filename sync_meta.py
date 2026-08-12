import json

from generate_lol_data import ITEMS, RUNES, SPELLS
from make_master_data import CHAMPIONS_LIST, build_champion_object
from update_custom_meta import SPECIFIC_BUILDS
from make_full_dataset import generate_skill_order

print("🚀 Building DuckLoL 169 Champion Master Database...")

final_db = {
    "version": "16.16.1",
    "patch": "16.16.1",
    "updatedAt": "2026-08-12",
    "items": ITEMS,
    "runes": RUNES,
    "spells": SPELLS,
    "champions": {}
}

# 1. Build all 169 champions
for champ_data in CHAMPIONS_LIST:
    c_obj = build_champion_object(champ_data)
    final_db["champions"][c_obj["id"]] = c_obj

# 2. Add MonkeyKing (Wukong)
mk_data = ("MonkeyKing", "Wukong", "the Monkey King", ["Fighter", "Tank"], [("TOP", 65), ("JUNGLE", 35)], "bruiser_ad", ["Q", "E", "W"], ("Stone Skin", "Crushing Blow", "Warrior Trickster", "Nimbus Strike", "Cyclone"))
c_obj = build_champion_object(mk_data)
final_db["champions"][c_obj["id"]] = c_obj

# 3. Apply tailored high-elo builds
for cid, sbuild in SPECIFIC_BUILDS.items():
    if cid in final_db["champions"]:
        c = final_db["champions"][cid]
        prole = c["primaryRole"]
        if prole in c["builds"]:
            b = c["builds"][prole]
            b["starter"] = sbuild["starter"]
            b["boots"] = sbuild["boots"]
            b["coreItems"] = sbuild["core"]
            b["situationalItems"] = sbuild["sit"]
            b["buildPath"] = [sbuild["starter"], sbuild["boots"]] + sbuild["core"] + [sbuild["sit"][0]]
            b["runes"]["primary"] = sbuild["pri"]
            b["runes"]["keystone"] = sbuild["keystone"]
            b["runes"]["primaryRunes"] = sbuild["pri_runes"]
            b["runes"]["secondary"] = sbuild["sec"]
            b["runes"]["secondaryRunes"] = sbuild["sec_runes"]
            b["runes"]["stats"] = sbuild["stats"]
            b["skillMaxOrder"] = sbuild["max"]
            b["skillOrder"] = generate_skill_order(sbuild["max"])
            b["summonerSpells"] = sbuild["spells"]
            b["altSpells"] = sbuild["altSpells"]
            b["winRate"] = sbuild["wr"]
            b["pickRate"] = sbuild["pr"]
            b["banRate"] = sbuild["br"]
            b["tier"] = "S+" if sbuild["wr"] >= 51.8 else ("S" if sbuild["wr"] >= 51.0 else "A")
            c["build"] = b
            c["counters"] = b["counters"]

# 4. Save to data.json
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(final_db, f, indent=2, ensure_ascii=False)

print(f"✅ Successfully compiled {len(final_db['champions'])} official champions into data.json!")
