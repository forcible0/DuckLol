import json
from make_full_dataset import generate_skill_order

SPECIFIC_BUILDS = {
    "Yasuo": {
        "starter": "1055", "boots": "3006", "core": ["3153", "3031", "6673"], "sit": ["6333", "3156", "3026", "3072", "3036"],
        "pri": "Precision", "keystone": 8008, "pri_runes": [8009, 9104, 8299], "sec": "Resolve", "sec_runes": [8444, 8451], "stats": [5005, 5008, 5001],
        "max": ["Q", "E", "W"], "spells": ["Flash", "Teleport"], "altSpells": ["Flash", "Ignite"], "wr": 50.8, "pr": 12.4, "br": 18.2
    },
    "Yone": {
        "starter": "1055", "boots": "3006", "core": ["3153", "3031", "6673"], "sit": ["6333", "3156", "3026", "3072", "3036"],
        "pri": "Precision", "keystone": 8008, "pri_runes": [8009, 9104, 8299], "sec": "Resolve", "sec_runes": [8444, 8451], "stats": [5005, 5008, 5001],
        "max": ["Q", "E", "W"], "spells": ["Flash", "Teleport"], "altSpells": ["Flash", "Ignite"], "wr": 50.4, "pr": 11.8, "br": 16.5
    },
    "Zed": {
        "starter": "1055", "boots": "3158", "core": ["6692", "6699", "6694"], "sit": ["6701", "3814", "6696", "3156", "3026"],
        "pri": "Precision", "keystone": 8010, "pri_runes": [9111, 9105, 8299], "sec": "Domination", "sec_runes": [8143, 8106], "stats": [5008, 5008, 5001],
        "max": ["Q", "E", "W"], "spells": ["Flash", "Ignite"], "altSpells": ["Flash", "Teleport"], "wr": 51.2, "pr": 8.9, "br": 22.4
    },
    "Ahri": {
        "starter": "1056", "boots": "3020", "core": ["3118", "3100", "3157"], "sit": ["4645", "3089", "3135", "2508", "4629"],
        "pri": "Domination", "keystone": 8112, "pri_runes": [8139, 8138, 8106], "sec": "Sorcery", "sec_runes": [8226, 8210], "stats": [5008, 5008, 5001],
        "max": ["Q", "W", "E"], "spells": ["Flash", "Teleport"], "altSpells": ["Flash", "Ignite"], "wr": 51.6, "pr": 9.2, "br": 5.4
    },
    "Kaisa": {
        "starter": "1055", "boots": "3006", "core": ["6672", "3302", "6675"], "sit": ["3157", "3089", "3036", "3072", "3153"],
        "pri": "Precision", "keystone": 8005, "pri_runes": [9111, 9104, 8017], "sec": "Inspiration", "sec_runes": [8304, 8345], "stats": [5005, 5008, 5001],
        "max": ["Q", "E", "W"], "spells": ["Flash", "Cleanse"], "altSpells": ["Flash", "Heal"], "wr": 51.2, "pr": 18.5, "br": 8.6
    },
    "Jinx": {
        "starter": "1055", "boots": "3006", "core": ["6672", "3085", "3031"], "sit": ["3036", "3072", "6673", "3026", "3094"],
        "pri": "Precision", "keystone": 8008, "pri_runes": [9101, 9104, 8014], "sec": "Inspiration", "sec_runes": [8304, 8345], "stats": [5005, 5008, 5001],
        "max": ["Q", "W", "E"], "spells": ["Flash", "Cleanse"], "altSpells": ["Flash", "Ghost"], "wr": 51.8, "pr": 15.2, "br": 4.1
    },
    "Caitlyn": {
        "starter": "1055", "boots": "3006", "core": ["6676", "3031", "3036"], "sit": ["3094", "3072", "6701", "3814", "3026"],
        "pri": "Inspiration", "keystone": 8369, "pri_runes": [8304, 8321, 8347], "sec": "Sorcery", "sec_runes": [8233, 8236], "stats": [5008, 5008, 5001],
        "max": ["Q", "W", "E"], "spells": ["Flash", "Heal"], "altSpells": ["Flash", "Barrier"], "wr": 50.9, "pr": 14.1, "br": 11.2
    },
    "Jhin": {
        "starter": "1055", "boots": "3009", "core": ["6676", "3031", "3094"], "sit": ["3036", "3072", "6701", "3814", "3026"],
        "pri": "Precision", "keystone": 8021, "pri_runes": [9111, 9103, 8014], "sec": "Sorcery", "sec_runes": [8234, 8236], "stats": [5008, 5008, 5001],
        "max": ["Q", "W", "E"], "spells": ["Flash", "Heal"], "altSpells": ["Flash", "Ghost"], "wr": 51.5, "pr": 16.8, "br": 5.8
    },
    "Ezreal": {
        "starter": "1055", "boots": "3158", "core": ["3078", "3003", "3161"], "sit": ["6694", "3153", "3156", "3026", "3036"],
        "pri": "Precision", "keystone": 8010, "pri_runes": [8009, 9103, 8017], "sec": "Inspiration", "sec_runes": [8304, 8345], "stats": [5005, 5008, 5001],
        "max": ["Q", "E", "W"], "spells": ["Flash", "Teleport"], "altSpells": ["Flash", "Heal"], "wr": 50.7, "pr": 17.5, "br": 6.2
    },
    "LeeSin": {
        "starter": "1103", "boots": "3047", "core": ["6692", "6610", "3071"], "sit": ["3053", "6333", "3156", "3026", "3161"],
        "pri": "Precision", "keystone": 8010, "pri_runes": [9111, 9104, 8299], "sec": "Inspiration", "sec_runes": [8304, 8347], "stats": [5008, 5008, 5001],
        "max": ["Q", "W", "E"], "spells": ["Flash", "Smite"], "altSpells": ["Ghost", "Smite"], "wr": 51.1, "pr": 14.5, "br": 12.8
    },
    "Viego": {
        "starter": "1103", "boots": "3047", "core": ["6672", "6610", "3078"], "sit": ["3153", "6333", "3053", "3026", "3156"],
        "pri": "Precision", "keystone": 8010, "pri_runes": [9111, 9104, 8299], "sec": "Inspiration", "sec_runes": [8304, 8347], "stats": [5005, 5008, 5001],
        "max": ["Q", "E", "W"], "spells": ["Flash", "Smite"], "altSpells": ["Ghost", "Smite"], "wr": 51.4, "pr": 12.2, "br": 9.4
    },
    "Thresh": {
        "starter": "3865", "boots": "3009", "core": ["3869", "2501", "3190"], "sit": ["3109", "3050", "3110", "2504", "3075"],
        "pri": "Inspiration", "keystone": 8351, "pri_runes": [8306, 8345, 8347], "sec": "Resolve", "sec_runes": [8444, 8451], "stats": [5007, 5001, 5001],
        "max": ["Q", "W", "E"], "spells": ["Flash", "Ignite"], "altSpells": ["Flash", "Exhaust"], "wr": 51.6, "pr": 13.5, "br": 7.5
    },
    "Blitzcrank": {
        "starter": "3865", "boots": "3009", "core": ["3869", "2501", "3190"], "sit": ["3050", "3109", "3110", "2504", "3075"],
        "pri": "Inspiration", "keystone": 8351, "pri_runes": [8306, 8345, 8347], "sec": "Resolve", "sec_runes": [8444, 8451], "stats": [5007, 5001, 5001],
        "max": ["Q", "W", "E"], "spells": ["Flash", "Ignite"], "altSpells": ["Flash", "Exhaust"], "wr": 51.8, "pr": 11.2, "br": 24.5
    },
    "Nautilus": {
        "starter": "3865", "boots": "3047", "core": ["3871", "2501", "3190"], "sit": ["3050", "3109", "3075", "2504", "3110"],
        "pri": "Resolve", "keystone": 8439, "pri_runes": [8401, 8429, 8451], "sec": "Inspiration", "sec_runes": [8306, 8347], "stats": [5007, 5001, 5001],
        "max": ["Q", "W", "E"], "spells": ["Flash", "Ignite"], "altSpells": ["Flash", "Exhaust"], "wr": 51.2, "pr": 12.8, "br": 10.4
    },
    "Leona": {
        "starter": "3865", "boots": "3047", "core": ["3871", "2501", "3190"], "sit": ["3050", "3109", "3075", "2504", "3110"],
        "pri": "Resolve", "keystone": 8439, "pri_runes": [8401, 8444, 8451], "sec": "Inspiration", "sec_runes": [8306, 8347], "stats": [5007, 5001, 5001],
        "max": ["W", "E", "Q"], "spells": ["Flash", "Ignite"], "altSpells": ["Flash", "Exhaust"], "wr": 51.9, "pr": 11.4, "br": 8.9
    },
    "Lulu": {
        "starter": "3865", "boots": "3158", "core": ["3870", "6617", "2065"], "sit": ["3504", "3744", "3107", "3222", "4005"],
        "pri": "Sorcery", "keystone": 8214, "pri_runes": [8226, 8210, 8236], "sec": "Resolve", "sec_runes": [8463, 8453], "stats": [5007, 5008, 5001],
        "max": ["E", "W", "Q"], "spells": ["Flash", "Heal"], "altSpells": ["Flash", "Ignite"], "wr": 51.4, "pr": 9.8, "br": 6.1
    },
    "Smolder": {
        "starter": "1055", "boots": "3158", "core": ["3508", "3161", "3094"], "sit": ["3072", "3036", "3031", "3814", "3026"],
        "pri": "Precision", "keystone": 8021, "pri_runes": [8009, 9103, 8017], "sec": "Resolve", "sec_runes": [8444, 8451], "stats": [5008, 5008, 5001],
        "max": ["Q", "W", "E"], "spells": ["Flash", "Heal"], "altSpells": ["Flash", "Teleport"], "wr": 50.8, "pr": 8.4, "br": 5.2
    },
    "Hwei": {
        "starter": "1056", "boots": "3020", "core": ["6655", "4628", "4645"], "sit": ["3137", "3089", "3157", "3151", "4629"],
        "pri": "Sorcery", "keystone": 8229, "pri_runes": [8226, 8210, 8236], "sec": "Inspiration", "sec_runes": [8304, 8345], "stats": [5007, 5008, 5001],
        "max": ["Q", "E", "W"], "spells": ["Flash", "Teleport"], "altSpells": ["Flash", "Barrier"], "wr": 50.9, "pr": 7.8, "br": 8.4
    },
    "AurelionSol": {
        "starter": "1056", "boots": "3020", "core": ["3116", "3151", "4645"], "sit": ["3089", "3135", "3157", "2504", "4629"],
        "pri": "Sorcery", "keystone": 8229, "pri_runes": [8226, 8210, 8236], "sec": "Inspiration", "sec_runes": [8304, 8345], "stats": [5008, 5008, 5001],
        "max": ["Q", "E", "W"], "spells": ["Flash", "Teleport"], "altSpells": ["Flash", "Barrier"], "wr": 51.5, "pr": 6.2, "br": 9.8
    },
    "Vladimir": {
        "starter": "1054", "boots": "3020", "core": ["4629", "4633", "3089"], "sit": ["3157", "3135", "4645", "2508", "2504"],
        "pri": "Sorcery", "keystone": 8230, "pri_runes": [8275, 8210, 8236], "sec": "Inspiration", "sec_runes": [8304, 8345], "stats": [5008, 5008, 5001],
        "max": ["Q", "E", "W"], "spells": ["Flash", "Ghost"], "altSpells": ["Flash", "Ignite"], "wr": 51.3, "pr": 5.8, "br": 6.4
    },
    "Kassadin": {
        "starter": "1054", "boots": "3020", "core": ["6657", "3003", "3118"], "sit": ["3157", "3089", "3135", "4645", "2504"],
        "pri": "Precision", "keystone": 8021, "pri_runes": [8009, 9104, 8014], "sec": "Resolve", "sec_runes": [8444, 8451], "stats": [5008, 5008, 5001],
        "max": ["E", "W", "Q"], "spells": ["Flash", "Teleport"], "altSpells": ["Flash", "Ignite"], "wr": 51.8, "pr": 5.4, "br": 8.6
    }
}

with open("data.json", "r", encoding="utf-8") as f:
    db = json.load(f)

for cid, sbuild in SPECIFIC_BUILDS.items():
    if cid in db["champions"]:
        c = db["champions"][cid]
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

with open("data.json", "w", encoding="utf-8") as f:
    json.dump(db, f, indent=2, ensure_ascii=False)

print("Updated iconic champion builds in data.json successfully!")
