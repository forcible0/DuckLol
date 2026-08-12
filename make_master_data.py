import json

from generate_lol_data import ITEMS, RUNES, SPELLS
from make_full_dataset import ARCHETYPES, generate_skill_order

# 169 Champion Definitions
CHAMPIONS_LIST = [
    # --- TOP LANERS (43) ---
    ("Aatrox", "Aatrox", "the Darkin Blade", ["Fighter"], [("TOP", 89), ("JUNGLE", 11)], "bruiser_ad", ["Q", "E", "W"], ("Deathbringer Stance", "The Darkin Blade", "Infernal Chains", "Umbral Dash", "World Ender")),
    ("Camille", "Camille", "the Steel Shadow", ["Fighter"], [("TOP", 94), ("MID", 6)], "bruiser_tri", ["Q", "E", "W"], ("Adaptive Defenses", "Precision Protocol", "Tactical Sweep", "Hookshot", "The Hextech Ultimatum")),
    ("Chogath", "Cho'Gath", "the Terror of the Void", ["Tank", "Mage"], [("TOP", 72), ("MID", 28)], "tank_hp", ["E", "W", "Q"], ("Carnivore", "Rupture", "Feral Scream", "Vorpal Spikes", "Feast")),
    ("Darius", "Darius", "the Hand of Noxus", ["Fighter", "Tank"], [("TOP", 96), ("JUNGLE", 4)], "juggernaut", ["Q", "E", "W"], ("Hemorrhage", "Decimate", "Crippling Strike", "Apprehend", "Noxian Guillotine")),
    ("DrMundo", "Dr. Mundo", "the Madman of Zaun", ["Fighter", "Tank"], [("TOP", 88), ("JUNGLE", 12)], "tank_hp", ["Q", "E", "W"], ("Goes Where He Pleases", "Infected Bonesaw", "Heart Zapper", "Blunt Force Trauma", "Maximum Dosage")),
    ("Fiora", "Fiora", "the Grand Duelist", ["Fighter", "Assassin"], [("TOP", 98), ("MID", 2)], "bruiser_tri", ["Q", "E", "W"], ("Duelist's Dance", "Lunge", "Riposte", "Bladework", "Grand Challenge")),
    ("Gangplank", "Gangplank", "the Saltwater Scourge", ["Fighter"], [("TOP", 82), ("MID", 18)], "crit_adc", ["Q", "E", "W"], ("Trial by Fire", "Parrrley", "Remove Scurvy", "Powder Keg", "Cannon Barrage")),
    ("Garen", "Garen", "The Might of Demacia", ["Fighter", "Tank"], [("TOP", 84), ("MID", 16)], "juggernaut", ["E", "Q", "W"], ("Perseverance", "Decisive Strike", "Courage", "Judgment", "Demacian Justice")),
    ("Gnar", "Gnar", "the Missing Link", ["Fighter", "Tank"], [("TOP", 97), ("MID", 3)], "bruiser_tri", ["Q", "W", "E"], ("Rage Gene", "Boomerang Throw", "Hyper", "Hop", "GNAR!")),
    ("Gragas", "Gragas", "the Rabble Rouser", ["Fighter", "Mage"], [("TOP", 52), ("JUNGLE", 48)], "ap_burst", ["Q", "E", "W"], ("Happy Hour", "Barrel Roll", "Drunken Rage", "Body Slam", "Explosive Cask")),
    ("Gwen", "Gwen", "The Hallowed Seamstress", ["Fighter", "Assassin"], [("TOP", 85), ("JUNGLE", 15)], "ap_bruiser", ["Q", "E", "W"], ("Thousand Cuts", "Snip Snip!", "Hallowed Mist", "Skip 'n Slash", "Needlework")),
    ("Illaoi", "Illaoi", "the Kraken Priestess", ["Fighter", "Tank"], [("TOP", 96), ("MID", 4)], "juggernaut", ["E", "Q", "W"], ("Prophet of an Elder God", "Tentacle Smash", "Harsh Lesson", "Test of Spirit", "Leap of Faith")),
    ("Irelia", "Irelia", "the Blade Dancer", ["Fighter", "Assassin"], [("TOP", 64), ("MID", 36)], "bruiser_tri", ["Q", "E", "W"], ("Ionian Fervor", "Bladesurge", "Defiant Dance", "Flawless Duet", "Vanguard's Edge")),
    ("Jax", "Jax", "Grandmaster at Arms", ["Fighter", "Assassin"], [("TOP", 85), ("JUNGLE", 15)], "bruiser_tri", ["W", "E", "Q"], ("Relentless Assault", "Leap Strike", "Empower", "Counter Strike", "Grandmaster's Might")),
    ("Jayce", "Jayce", "the Defender of Tomorrow", ["Fighter", "Marksman"], [("TOP", 62), ("MID", 38)], "ad_assassin", ["Q", "E", "W"], ("Hextech Capacitor", "To the Skies!", "Lightning Field", "Thundering Blow", "Mercury Cannon")),
    ("KSante", "K'Sante", "the Pride of Nazumah", ["Tank", "Fighter"], [("TOP", 95), ("MID", 5)], "tank_res", ["Q", "W", "E"], ("Dauntless Instinct", "Ntofo Strikes", "Path Maker", "Footwork", "All Out")),
    ("Kayle", "Kayle", "the Righteous", ["Fighter", "Mage"], [("TOP", 78), ("MID", 22)], "ap_bruiser", ["Q", "E", "W"], ("Divine Ascent", "Radiant Blast", "Celestial Blessing", "Starfire Spellblade", "Divine Judgment")),
    ("Kennen", "Kennen", "the Heart of the Tempest", ["Mage", "Marksman"], [("TOP", 76), ("MID", 24)], "ap_burst", ["Q", "W", "E"], ("Mark of the Storm", "Thundering Shuriken", "Electrical Surge", "Lightning Rush", "Slicing Maelstrom")),
    ("Kled", "Kled", "the Cantankerous Cavalier", ["Fighter", "Tank"], [("TOP", 88), ("MID", 12)], "bruiser_ad", ["Q", "W", "E"], ("Skaarl", "Bear Trap on a Rope", "Violent Tendencies", "Jousting", "Chaaaaaaaarge!!!")),
    ("Malphite", "Malphite", "Shard of the Monolith", ["Tank", "Fighter"], [("TOP", 75), ("MID", 15), ("SUPPORT", 10)], "tank_res", ["Q", "E", "W"], ("Granite Shield", "Seismic Shard", "Thunderclap", "Ground Slam", "Unstoppable Force")),
    ("Mordekaiser", "Mordekaiser", "the Iron Revenant", ["Fighter", "Mage"], [("TOP", 86), ("JUNGLE", 14)], "ap_bruiser", ["Q", "E", "W"], ("Darkness Rise", "Obliteration", "Indestructible", "Death's Grasp", "Realm of Death")),
    ("Nasus", "Nasus", "the Curator of the Sands", ["Fighter", "Tank"], [("TOP", 89), ("MID", 11)], "tank_hp", ["Q", "W", "E"], ("Soul Eater", "Siphoning Strike", "Wither", "Spirit Fire", "Fury of the Sands")),
    ("Olaf", "Olaf", "the Berserker", ["Fighter", "Tank"], [("TOP", 65), ("JUNGLE", 35)], "bruiser_ad", ["Q", "E", "W"], ("Berserker Rage", "Undertow", "Tough It Out", "Reckless Swing", "Ragnarok")),
    ("Ornn", "Ornn", "The Fire below the Mountain", ["Tank"], [("TOP", 92), ("SUPPORT", 8)], "tank_res", ["Q", "W", "E"], ("Living Forge", "Volcanic Rupture", "Bellows Breath", "Searing Charge", "Call of the Forge God")),
    ("Pantheon", "Pantheon", "the Unbreakable Spear", ["Fighter", "Assassin"], [("TOP", 48), ("MID", 42), ("SUPPORT", 10)], "bruiser_ad", ["Q", "E", "W"], ("Mortal Will", "Comet Spear", "Shield Vault", "Aegis Assault", "Grand Starfall")),
    ("Poppy", "Poppy", "Keeper of the Hammer", ["Tank", "Fighter"], [("TOP", 54), ("JUNGLE", 38), ("SUPPORT", 8)], "tank_res", ["Q", "E", "W"], ("Iron Ambassador", "Hammer Shock", "Steadfast Presence", "Heroic Charge", "Keeper's Verdict")),
    ("Quinn", "Quinn", "Demacia's Wings", ["Marksman", "Assassin"], [("TOP", 85), ("MID", 15)], "lethality_adc", ["W", "Q", "E"], ("Harrier", "Blinding Assault", "Heightened Senses", "Vault", "Behind Enemy Lines")),
    ("Renekton", "Renekton", "the Butcher of the Sands", ["Fighter", "Tank"], [("TOP", 90), ("MID", 10)], "bruiser_ad", ["Q", "E", "W"], ("Reign of Anger", "Cull the Meek", "Ruthless Predator", "Slice and Dice", "Dominus")),
    ("Riven", "Riven", "the Exile", ["Fighter", "Assassin"], [("TOP", 92), ("MID", 8)], "bruiser_ad", ["Q", "E", "W"], ("Runic Blade", "Broken Wings", "Ki Burst", "Valor", "Blade of the Exile")),
    ("Rumble", "Rumble", "the Mechanized Menace", ["Fighter", "Mage"], [("TOP", 60), ("MID", 40)], "ap_bruiser", ["Q", "E", "W"], ("Junkyard Titan", "Flamespitter", "Scrap Shield", "Electro Harpoon", "The Equalizer")),
    ("Sett", "Sett", "the Boss", ["Fighter", "Tank"], [("TOP", 85), ("MID", 10), ("SUPPORT", 5)], "juggernaut", ["Q", "W", "E"], ("Pit Grit", "Knuckle Down", "Haymaker", "Facebreaker", "The Show Stopper")),
    ("Shen", "Shen", "the Eye of Twilight", ["Tank"], [("TOP", 82), ("SUPPORT", 18)], "tank_res", ["Q", "E", "W"], ("Ki Barrier", "Twilight Assault", "Spirit's Refuge", "Shadow Dash", "Stand United")),
    ("Singed", "Singed", "the Mad Chemist", ["Tank", "Fighter"], [("TOP", 90), ("MID", 10)], "ap_bruiser", ["Q", "E", "W"], ("Noxious Slipstream", "Poison Trail", "Mega Adhesive", "Fling", "Insanity Potion")),
    ("Sion", "Sion", "The Undead Juggernaut", ["Tank", "Fighter"], [("TOP", 88), ("MID", 12)], "tank_hp", ["Q", "W", "E"], ("Glory in Death", "Decimating Smash", "Soul Furnace", "Roar of the Slayer", "Unstoppable Onslaught")),
    ("TahmKench", "Tahm Kench", "The River King", ["Support", "Tank"], [("TOP", 65), ("SUPPORT", 35)], "tank_hp", ["Q", "W", "E"], ("An Acquired Taste", "Tongue Lash", "Abyssal Dive", "Thick Skin", "Devour")),
    ("Teemo", "Teemo", "the Swift Scout", ["Marksman", "Mage"], [("TOP", 82), ("MID", 18)], "ap_dot", ["E", "Q", "W"], ("Guerrilla Warfare", "Blinding Dart", "Move Quick", "Toxic Shot", "Noxious Trap")),
    ("Trundle", "Trundle", "the Troll King", ["Fighter", "Tank"], [("TOP", 72), ("JUNGLE", 28)], "bruiser_tri", ["Q", "W", "E"], ("King's Tribute", "Chomp", "Frozen Domain", "Pillar of Ice", "Subjugate")),
    ("Tryndamere", "Tryndamere", "the Barbarian King", ["Fighter", "Assassin"], [("TOP", 85), ("MID", 15)], "crit_adc", ["Q", "E", "W"], ("Battle Fury", "Bloodlust", "Mocking Shout", "Spinning Slash", "Undying Rage")),
    ("Urgot", "Urgot", "the Dreadnought", ["Fighter", "Tank"], [("TOP", 92), ("MID", 8)], "juggernaut", ["W", "E", "Q"], ("Echoing Flames", "Corrosive Charge", "Purge", "Disdain", "Fear Beyond Death")),
    ("Volibear", "Volibear", "the Relentless Storm", ["Fighter", "Tank"], [("TOP", 68), ("JUNGLE", 32)], "ap_bruiser", ["W", "Q", "E"], ("The Relentless Storm", "Thundering Smash", "Frenzied Maul", "Sky Splitter", "Stormbringer")),
    ("Warwick", "Warwick", "the Uncaged Wrath of Zaun", ["Fighter", "Tank"], [("TOP", 42), ("JUNGLE", 58)], "bruiser_ad", ["Q", "W", "E"], ("Eternal Hunger", "Jaws of the Beast", "Blood Hunt", "Primal Howl", "Infinite Duress")),
    ("Yorick", "Yorick", "Shepherd of Souls", ["Fighter", "Tank"], [("TOP", 94), ("MID", 6)], "bruiser_ad", ["Q", "E", "W"], ("Shepherd of Souls", "Last Rites", "Dark Procession", "Mourning Mist", "Eulogy of the Isles")),
    ("Ambessa", "Ambessa", "Matriarch of War", ["Fighter", "Assassin"], [("TOP", 65), ("MID", 35)], "bruiser_ad", ["Q", "E", "W"], ("Drakehound's Step", "Cunning Sweep", "Repudiation", "Lacerate", "Public Execution")),

    # --- JUNGLE (36) ---
    ("Amumu", "Amumu", "the Sad Mummy", ["Tank", "Mage"], [("JUNGLE", 90), ("SUPPORT", 10)], "jungle_tank", ["E", "Q", "W"], ("Cursed Touch", "Bandage Toss", "Despair", "Tantrum", "Curse of the Sad Mummy")),
    ("Belveth", "Bel'Veth", "the Empress of the Void", ["Fighter"], [("JUNGLE", 98), ("TOP", 2)], "onhit_adc", ["Q", "E", "W"], ("Death in Lavender", "Void Surge", "Above and Below", "Royal Maelstrom", "Endless Banquet")),
    ("Briar", "Briar", "the Restrained Hunger", ["Fighter", "Assassin"], [("JUNGLE", 96), ("TOP", 4)], "jungle_ad", ["W", "Q", "E"], ("Crimson Curse", "Head Rush", "Blood Frenzy", "Chilling Scream", "Certain Death")),
    ("Diana", "Diana", "Scorn of the Moon", ["Fighter", "Mage"], [("JUNGLE", 65), ("MID", 35)], "jungle_ap", ["Q", "W", "E"], ("Moonsilver Blade", "Crescent Strike", "Pale Cascade", "Lunar Rush", "Moonfall")),
    ("Ekko", "Ekko", "the Boy Who Shattered Time", ["Assassin", "Mage"], [("JUNGLE", 70), ("MID", 30)], "jungle_ap", ["Q", "E", "W"], ("Z-Drive Resonance", "Timewinder", "Parallel Convergence", "Phase Dive", "Chronobreak")),
    ("Elise", "Elise", "the Spider Queen", ["Mage", "Assassin"], [("JUNGLE", 94), ("SUPPORT", 6)], "jungle_ap", ["Q", "W", "E"], ("Spider Queen", "Neurotoxin / Venomous Bite", "Volatile Spiderling / Skittering Frenzy", "Cocoon / Rappel", "Spider Form")),
    ("Evelynn", "Evelynn", "Agony's Embrace", ["Assassin", "Mage"], [("JUNGLE", 99), ("MID", 1)], "jungle_ap", ["Q", "E", "W"], ("Demon Shade", "Hate Spike", "Allure", "Whiplash", "Last Caress")),
    ("Fiddlesticks", "Fiddlesticks", "the Ancient Fear", ["Mage", "Support"], [("JUNGLE", 92), ("SUPPORT", 8)], "jungle_ap", ["W", "Q", "E"], ("A Harmless Scarecrow", "Terrify", "Bountiful Harvest", "Reap", "Crowstorm")),
    ("Graves", "Graves", "the Outlaw", ["Marksman"], [("JUNGLE", 90), ("TOP", 10)], "lethality_adc", ["Q", "E", "W"], ("New Destiny", "End of the Line", "Smoke Screen", "Quickdraw", "Collateral Damage")),
    ("Hecarim", "Hecarim", "the Shadow of War", ["Fighter", "Tank"], [("JUNGLE", 98), ("TOP", 2)], "jungle_ad", ["Q", "E", "W"], ("Warpath", "Rampage", "Spirit of Dread", "Devastating Charge", "Onslaught of Shadows")),
    ("Ivern", "Ivern", "the Green Father", ["Support", "Mage"], [("JUNGLE", 95), ("SUPPORT", 5)], "sup_enchanter", ["E", "Q", "W"], ("Friend of the Forest", "Rootcaller", "Brushmaker", "Triggerseed", "Daisy!")),
    ("JarvanIV", "Jarvan IV", "the Exemplar of Demacia", ["Tank", "Fighter"], [("JUNGLE", 92), ("TOP", 8)], "jungle_ad", ["Q", "E", "W"], ("Martial Cadence", "Dragon Strike", "Golden Aegis", "Demacian Standard", "Cataclysm")),
    ("Karthus", "Karthus", "the Deathsinger", ["Mage"], [("JUNGLE", 62), ("ADC", 38)], "ap_burst", ["Q", "E", "W"], ("Death Defied", "Lay Waste", "Wall of Pain", "Defile", "Requiem")),
    ("Kayn", "Kayn", "the Shadow Reaper", ["Fighter", "Assassin"], [("JUNGLE", 98), ("TOP", 2)], "jungle_assassin", ["Q", "W", "E"], ("The Darkin Scythe", "Reaping Slash", "Blade's Reach", "Shadow Step", "Umbral Trespass")),
    ("Khazix", "Kha'Zix", "the Voidreaver", ["Assassin"], [("JUNGLE", 99), ("MID", 1)], "jungle_assassin", ["Q", "W", "E"], ("Unseen Threat", "Taste Their Fear", "Void Spike", "Leap", "Void Assault")),
    ("Kindred", "Kindred", "The Eternal Hunters", ["Marksman"], [("JUNGLE", 96), ("ADC", 4)], "crit_adc", ["Q", "W", "E"], ("Mark of the Kindred", "Dance of Arrows", "Wolf's Frenzy", "Mounting Dread", "Lamb's Respite")),
    ("LeeSin", "Lee Sin", "the Blind Monk", ["Fighter", "Assassin"], [("JUNGLE", 95), ("TOP", 5)], "jungle_ad", ["Q", "W", "E"], ("Flurry", "Sonic Wave / Resonating Strike", "Safeguard / Iron Will", "Tempest / Cripple", "Dragon's Rage")),
    ("Lillia", "Lillia", "the Bashful Bloom", ["Fighter", "Mage"], [("JUNGLE", 92), ("TOP", 8)], "ap_bruiser", ["Q", "W", "E"], ("Dream-Laden Bough", "Blooming Blows", "Watch Out! Eep!", "Swirlseed", "Lilting Lullaby")),
    ("MasterYi", "Master Yi", "the Wuju Bladesman", ["Assassin", "Fighter"], [("JUNGLE", 97), ("MID", 3)], "onhit_adc", ["Q", "E", "W"], ("Double Strike", "Alpha Strike", "Meditate", "Wuju Style", "Highlander")),
    ("Nidalee", "Nidalee", "the Bestial Huntress", ["Assassin", "Mage"], [("JUNGLE", 96), ("MID", 4)], "jungle_ap", ["Q", "E", "W"], ("Prowl", "Javelin Toss / Takedown", "Bushwhack / Pounce", "Primal Surge / Swipe", "Aspect of the Cougar")),
    ("Nocturne", "Nocturne", "the Eternal Nightmare", ["Assassin", "Fighter"], [("JUNGLE", 95), ("MID", 5)], "jungle_ad", ["Q", "E", "W"], ("Umbra Blades", "Duskbringer", "Shroud of Darkness", "Unspeakable Horror", "Paranoia")),
    ("Nunu", "Nunu & Willump", "the Boy and His Yeti", ["Tank", "Fighter"], [("JUNGLE", 94), ("MID", 6)], "jungle_tank", ["Q", "E", "W"], ("Call of the Freljord", "Consume", "Biggest Snowball Ever!", "Snowball Barrage", "Absolute Zero")),
    ("Rammus", "Rammus", "the Armordillo", ["Tank", "Fighter"], [("JUNGLE", 98), ("TOP", 2)], "jungle_tank", ["W", "Q", "E"], ("Spiked Shell", "Powerball", "Defensive Ball Curl", "Frenzying Taunt", "Soaring Slam")),
    ("RekSai", "Rek'Sai", "the Void Burrower", ["Fighter", "Tank"], [("JUNGLE", 88), ("TOP", 12)], "jungle_ad", ["Q", "E", "W"], ("Fury of the Xer'Sai", "Queen's Wrath / Prey Seeker", "Burrow / Un-burrow", "Furious Bite / Tunnel", "Void Rush")),
    ("Rengar", "Rengar", "the Pridestalker", ["Assassin", "Fighter"], [("JUNGLE", 86), ("TOP", 14)], "jungle_assassin", ["Q", "W", "E"], ("Unseen Predator", "Savagery", "Battle Roar", "Bola Strike", "Thrill of the Hunt")),
    ("Sejuani", "Sejuani", "Fury of the North", ["Tank", "Fighter"], [("JUNGLE", 88), ("TOP", 12)], "jungle_tank", ["W", "Q", "E"], ("Fury of the North", "Arctic Assault", "Winter's Wrath", "Permafrost", "Glacial Prison")),
    ("Shaco", "Shaco", "the Demon Jester", ["Assassin"], [("JUNGLE", 82), ("SUPPORT", 18)], "jungle_assassin", ["E", "Q", "W"], ("Backstab", "Deceive", "Jack in the Box", "Two-Shiv Poison", "Hallucinate")),
    ("Shyvana", "Shyvana", "the Half-Dragon", ["Fighter", "Tank"], [("JUNGLE", 92), ("TOP", 8)], "ap_bruiser", ["E", "W", "Q"], ("Fury of the Dragonborn", "Twin Bite", "Burnout", "Flame Breath", "Dragon's Descent")),
    ("Skarner", "Skarner", "the Primordial Sovereign", ["Tank", "Fighter"], [("JUNGLE", 78), ("TOP", 22)], "jungle_tank", ["Q", "W", "E"], ("Threads of Vibration", "Shattered Earth / Upheaval", "Seismic Bastion", "Ixtal's Impact", "Impale")),
    ("Taliyah", "Taliyah", "the Stoneweaver", ["Mage", "Support"], [("JUNGLE", 62), ("MID", 38)], "ap_burst", ["Q", "E", "W"], ("Rock Surfing", "Threaded Volley", "Seismic Shove", "Unraveled Earth", "Weaver's Wall")),
    ("Talon", "Talon", "the Blade's Shadow", ["Assassin"], [("MID", 64), ("JUNGLE", 36)], "jungle_assassin", ["W", "Q", "E"], ("Blade's End", "Noxian Diplomacy", "Rake", "Assassin's Path", "Shadow Assault")),
    ("Udyr", "Udyr", "the Spirit Walker", ["Fighter", "Tank"], [("JUNGLE", 82), ("TOP", 18)], "jungle_tank", ["R", "W", "E"], ("Bridge Between", "Wilding Claw", "Iron Mantle", "Blazing Stampede", "Wingborne Storm")),
    ("Vi", "Vi", "the Piltover Enforcer", ["Fighter", "Assassin"], [("JUNGLE", 98), ("TOP", 2)], "jungle_ad", ["Q", "E", "W"], ("Blast Shield", "Vault Breaker", "Denting Blows", "Relentless Force", "Cease and Desist")),
    ("Viego", "Viego", "The Ruined King", ["Assassin", "Fighter"], [("JUNGLE", 92), ("MID", 8)], "bruiser_tri", ["Q", "E", "W"], ("Sovereign's Domination", "Blade of the Ruined King", "Spectral Maw", "Harrowed Path", "Heartbreaker")),
    ("XinZhao", "Xin Zhao", "the Seneschal of Demacia", ["Fighter", "Tank"], [("JUNGLE", 95), ("TOP", 5)], "jungle_ad", ["W", "E", "Q"], ("Determination", "Three Talon Strike", "Wind Becomes Lightning", "Audacious Charge", "Crescent Guard")),
    ("Zac", "Zac", "the Secret Weapon", ["Tank", "Fighter"], [("JUNGLE", 75), ("TOP", 18), ("SUPPORT", 7)], "jungle_tank", ["E", "W", "Q"], ("Cell Division", "Stretching Strikes", "Unstable Matter", "Elastic Slingshot", "Let's Bounce!")),

    # --- MID LANERS (37) ---
    ("Ahri", "Ahri", "the Nine-Tailed Fox", ["Mage", "Assassin"], [("MID", 92), ("SUPPORT", 8)], "ap_burst", ["Q", "W", "E"], ("Essence Theft", "Orb of Deception", "Fox-Fire", "Charm", "Spirit Rush")),
    ("Akali", "Akali", "the Rogue Assassin", ["Assassin"], [("MID", 74), ("TOP", 26)], "ap_burst", ["Q", "E", "W"], ("Assassin's Mark", "Five Point Strike", "Twilight Shroud", "Shuriken Flip", "Perfect Execution")),
    ("Akshan", "Akshan", "the Rogue Sentinel", ["Marksman", "Assassin"], [("MID", 68), ("TOP", 32)], "onhit_adc", ["E", "Q", "W"], ("Dirty Fighting", "Avengerang", "Going Rogue", "Heroic Swing", "Comeuppance")),
    ("Anivia", "Anivia", "the Cryophoenix", ["Mage", "Support"], [("MID", 95), ("SUPPORT", 5)], "ap_control", ["E", "Q", "W"], ("Rebirth", "Flash Frost", "Crystallize", "Frostbite", "Glacial Storm")),
    ("Annie", "Annie", "the Dark Child", ["Mage", "Support"], [("MID", 62), ("SUPPORT", 38)], "ap_burst", ["Q", "W", "E"], ("Pyromania", "Disintegrate", "Incinerate", "Molten Shield", "Summon: Tibbers")),
    ("AurelionSol", "Aurelion Sol", "The Star Forger", ["Mage"], [("MID", 95), ("ADC", 5)], "ap_control", ["Q", "E", "W"], ("Cosmic Creator", "Breath of Light", "Astral Flight", "Singularity", "Falling Star / The Skies Descend")),
    ("Aurora", "Aurora", "the Witch Between Worlds", ["Mage", "Assassin"], [("MID", 72), ("TOP", 28)], "ap_burst", ["Q", "E", "W"], ("Spirit Abjuration", "Two-World Window", "Across the Veil", "The Weirding", "Between Worlds")),
    ("Azir", "Azir", "the Emperor of the Sands", ["Mage", "Marksman"], [("MID", 98), ("TOP", 2)], "ap_control", ["W", "Q", "E"], ("Shurima's Legacy", "Conquering Sands", "Arise!", "Shifting Sands", "Emperor's Divide")),
    ("Cassiopeia", "Cassiopeia", "the Serpent's Embrace", ["Mage"], [("MID", 75), ("TOP", 25)], "ap_dot", ["E", "Q", "W"], ("Serpentine Grace", "Noxious Blast", "Miasma", "Twin Fang", "Petrifying Gaze")),
    ("Corki", "Corki", "the Daring Bombardier", ["Marksman", "Mage"], [("MID", 78), ("ADC", 22)], "crit_adc", ["Q", "E", "W"], ("Hextech Munitions", "Phosphorus Bomb", "Valkyrie", "Gatling Gun", "Missile Barrage")),
    ("Fizz", "Fizz", "the Tidal Trickster", ["Assassin", "Fighter"], [("MID", 96), ("TOP", 4)], "ap_burst", ["E", "W", "Q"], ("Nimble Fighter", "Urchin Strike", "Seastone Trident", "Playful / Trickster", "Chum the Waters")),
    ("Galio", "Galio", "the Colossus", ["Tank", "Mage"], [("MID", 72), ("SUPPORT", 28)], "tank_res", ["Q", "W", "E"], ("Colossal Smash", "Winds of War", "Shield of Durand", "Justice Punch", "Hero's Entrance")),
    ("Heimerdinger", "Heimerdinger", "the Revered Inventor", ["Mage", "Support"], [("MID", 45), ("TOP", 35), ("SUPPORT", 20)], "ap_control", ["Q", "W", "E"], ("Hextech Affinity", "H-28 G Evolution Turret", "Hextech Micro-Rockets", "CH-2 Electron Storm Grenade", "UPGRADE!!!")),
    ("Hwei", "Hwei", "the Visionary", ["Mage", "Support"], [("MID", 82), ("SUPPORT", 18)], "ap_control", ["Q", "E", "W"], ("Signature of the Visionary", "Subject: Disaster", "Subject: Serenity", "Subject: Torment", "Spiraling Despair")),
    ("Kassadin", "Kassadin", "the Void Walker", ["Assassin", "Mage"], [("MID", 98), ("TOP", 2)], "ap_control", ["E", "W", "Q"], ("Void Stone", "Null Sphere", "Nether Blade", "Force Pulse", "Riftwalk")),
    ("Katarina", "Katarina", "the Sinister Blade", ["Assassin", "Mage"], [("MID", 98), ("TOP", 2)], "ap_burst", ["Q", "E", "W"], ("Voracity", "Bouncing Blade", "Preparation", "Shunpo", "Death Lotus")),
    ("Leblanc", "LeBlanc", "the Deceiver", ["Assassin", "Mage"], [("MID", 95), ("SUPPORT", 5)], "ap_burst", ["W", "Q", "E"], ("Mirror Image", "Sigil of Malice", "Distortion", "Ethereal Chains", "Mimic")),
    ("Lissandra", "Lissandra", "the Ice Witch", ["Mage"], [("MID", 94), ("TOP", 6)], "ap_control", ["Q", "W", "E"], ("Iceborn Subjugation", "Ice Shard", "Ring of Frost", "Glacial Path", "Frozen Tomb")),
    ("Lux", "Lux", "the Lady of Luminosity", ["Mage", "Support"], [("SUPPORT", 68), ("MID", 32)], "ap_burst", ["E", "Q", "W"], ("Illumination", "Light Binding", "Prismatic Barrier", "Lucent Singularity", "Final Spark")),
    ("Malzahar", "Malzahar", "the Prophet of the Void", ["Mage", "Assassin"], [("MID", 96), ("TOP", 4)], "ap_dot", ["E", "Q", "W"], ("Void Shift", "Call of the Void", "Void Swarm", "Malefic Visions", "Nether Grasp")),
    ("Naafiri", "Naafiri", "the Hound of a Hundred Bites", ["Assassin"], [("MID", 88), ("TOP", 12)], "ad_assassin", ["Q", "E", "W"], ("We Are More", "Darkin Daggers", "Hounds' Pursuit", "Eviscerate", "The Call of the Pack")),
    ("Neeko", "Neeko", "the Curious Chameleon", ["Mage", "Support"], [("MID", 58), ("SUPPORT", 42)], "ap_burst", ["Q", "E", "W"], ("Inherent Glamour", "Blooming Burst", "Shapesplitter", "Tangle-Barbs", "Pop Blossom")),
    ("Orianna", "Orianna", "the Lady of Clockwork", ["Mage", "Support"], [("MID", 98), ("SUPPORT", 2)], "ap_control", ["Q", "W", "E"], ("Clockwork Windup", "Command: Attack", "Command: Dissonance", "Command: Protect", "Command: Shockwave")),
    ("Qiyana", "Qiyana", "Empress of the Elements", ["Assassin", "Fighter"], [("MID", 85), ("JUNGLE", 15)], "ad_assassin", ["Q", "W", "E"], ("Royal Privilege", "Edge of Ixtal / Elemental Wrath", "Terrashape", "Audacity", "Supreme Display of Talent")),
    ("Ryze", "Ryze", "the Rune Mage", ["Mage", "Fighter"], [("MID", 82), ("TOP", 18)], "ap_control", ["Q", "E", "W"], ("Arcane Mastery", "Overload", "Rune Prison", "Spell Flux", "Realm Warp")),
    ("Sylas", "Sylas", "the Unshackled", ["Mage", "Assassin"], [("MID", 72), ("JUNGLE", 18), ("TOP", 10)], "ap_bruiser", ["W", "E", "Q"], ("Petricite Burst", "Chain Lash", "Kingslayer", "Abscond / Abduct", "Hijack")),
    ("Syndra", "Syndra", "the Dark Sovereign", ["Mage"], [("MID", 98), ("BOT", 2)], "ap_burst", ["Q", "W", "E"], ("Transcendent", "Dark Sphere", "Force of Will", "Scatter the Weak", "Unleashed Power")),
    ("TwistedFate", "Twisted Fate", "the Card Master", ["Mage", "Marksman"], [("MID", 85), ("ADC", 15)], "ap_control", ["Q", "W", "E"], ("Loaded Dice", "Wild Cards", "Pick a Card", "Stacked Deck", "Destiny")),
    ("Veigar", "Veigar", "the Tiny Master of Evil", ["Mage"], [("MID", 68), ("BOT", 32)], "ap_burst", ["Q", "W", "E"], ("Phenomenal Evil Power", "Baleful Strike", "Dark Matter", "Event Horizon", "Primordial Burst")),
    ("Velkoz", "Vel'Koz", "the Eye of the Void", ["Mage", "Support"], [("SUPPORT", 62), ("MID", 38)], "ap_control", ["Q", "W", "E"], ("Organic Deconstruction", "Plasma Fission", "Void Rift", "Tectonic Disruption", "Life Form Disintegration Ray")),
    ("Vex", "Vex", "the Gloomist", ["Mage"], [("MID", 98), ("SUPPORT", 2)], "ap_burst", ["Q", "W", "E"], ("Doom 'n Gloom", "Mistral Bolt", "Personal Space", "Shadow Surge", "Shadow Surge")),
    ("Viktor", "Viktor", "the Machine Herald", ["Mage"], [("MID", 98), ("TOP", 2)], "ap_control", ["E", "Q", "W"], ("Glorious Evolution", "Siphon Power", "Gravity Field", "Death Ray", "Chaos Storm")),
    ("Vladimir", "Vladimir", "the Crimson Reaper", ["Mage", "Tank"], [("MID", 70), ("TOP", 30)], "ap_bruiser", ["Q", "E", "W"], ("Crimson Pact", "Transfusion", "Sanguine Pool", "Tides of Blood", "Hemoplague")),
    ("Xerath", "Xerath", "the Magus Ascendant", ["Mage", "Support"], [("SUPPORT", 56), ("MID", 44)], "ap_control", ["Q", "W", "E"], ("Mana Surge", "Arcanopulse", "Eye of Destruction", "Shocking Orb", "Rite of the Arcane")),
    ("Yasuo", "Yasuo", "the Unforgiven", ["Fighter", "Assassin"], [("MID", 74), ("TOP", 18), ("ADC", 8)], "bruiser_tri", ["Q", "E", "W"], ("Way of the Wanderer", "Steel Tempest", "Wind Wall", "Sweeping Blade", "Last Breath")),
    ("Yone", "Yone", "the Unforgotten", ["Assassin", "Fighter"], [("MID", 68), ("TOP", 32)], "bruiser_tri", ["Q", "E", "W"], ("Way of the Hunter", "Mortal Steel", "Spirit Cleave", "Soul Unbound", "Fate Sealed")),
    ("Zed", "Zed", "the Master of Shadows", ["Assassin"], [("MID", 88), ("JUNGLE", 12)], "ad_assassin", ["Q", "E", "W"], ("Contempt for the Weak", "Razor Shuriken", "Living Shadow", "Shadow Slash", "Death Mark")),
    ("Ziggs", "Ziggs", "the Hexplosives Expert", ["Mage"], [("ADC", 62), ("MID", 38)], "ap_control", ["Q", "E", "W"], ("Short Fuse", "Bouncing Bomb", "Satchel Charge", "Hexplosive Minefield", "Mega Inferno Bomb")),
    ("Zoe", "Zoe", "the Aspect of Twilight", ["Mage", "Support"], [("MID", 94), ("SUPPORT", 6)], "ap_burst", ["Q", "E", "W"], ("More Sparkles!", "Paddle Star!", "Spell Thief", "Sleepy Trouble Bubble", "Portal Jump")),

    # --- BOT / ADC (23) ---
    ("Aphelios", "Aphelios", "the Weapon of the Faithful", ["Marksman"], [("ADC", 99), ("MID", 1)], "crit_adc", ["Q", "W", "E"], ("The Hitman and the Seer", "Weapon Abilities", "Phase", "Weapon Queue System", "Moonlight Vigil")),
    ("Ashe", "Ashe", "the Frost Archer", ["Marksman", "Support"], [("ADC", 82), ("SUPPORT", 18)], "onhit_adc", ["W", "Q", "E"], ("Frost Shot", "Ranger's Focus", "Volley", "Hawkshot", "Enchanted Crystal Arrow")),
    ("Caitlyn", "Caitlyn", "the Sheriff of Piltover", ["Marksman"], [("ADC", 98), ("MID", 2)], "lethality_adc", ["Q", "W", "E"], ("Headshot", "Piltover Peacemaker", "Yordle Snap Trap", "90 Caliber Net", "Ace in the Hole")),
    ("Draven", "Draven", "the Glorious Executioner", ["Marksman"], [("ADC", 98), ("MID", 2)], "crit_adc", ["Q", "W", "E"], ("League of Draven", "Spinning Axe", "Blood Rush", "Stand Aside", "Whirling Death")),
    ("Ezreal", "Ezreal", "the Prodigal Explorer", ["Marksman", "Mage"], [("ADC", 94), ("MID", 6)], "bruiser_tri", ["Q", "E", "W"], ("Rising Spell Force", "Mystic Shot", "Essence Flux", "Arcane Shift", "Trueshot Barrage")),
    ("Jhin", "Jhin", "the Virtuoso", ["Marksman", "Mage"], [("ADC", 98), ("MID", 2)], "lethality_adc", ["Q", "W", "E"], ("Whisper", "Dancing Grenade", "Deadly Flourish", "Captive Audience", "Curtain Call")),
    ("Jinx", "Jinx", "the Loose Cannon", ["Marksman"], [("ADC", 99), ("MID", 1)], "crit_adc", ["Q", "W", "E"], ("Get Excited!", "Switcheroo!", "Zap!", "Flame Chompers!", "Super Mega Death Rocket!")),
    ("Kaisa", "Kai'Sa", "Daughter of the Void", ["Marksman", "Assassin"], [("ADC", 88), ("MID", 12)], "onhit_adc", ["Q", "E", "W"], ("Second Skin", "Icathian Rain", "Void Seeker", "Supercharge", "Killer Instinct")),
    ("Kalista", "Kalista", "the Spear of Vengeance", ["Marksman"], [("ADC", 96), ("TOP", 4)], "onhit_adc", ["E", "Q", "W"], ("Martial Poise", "Pierce", "Sentinel", "Rend", "Fate's Call")),
    ("KogMaw", "Kog'Maw", "the Mouth of the Abyss", ["Marksman", "Mage"], [("ADC", 92), ("MID", 8)], "onhit_adc", ["W", "Q", "E"], ("Icathian Surprise", "Caustic Spittle", "Bio-Arcane Barrage", "Void Ooze", "Living Artillery")),
    ("Lucian", "Lucian", "the Purifier", ["Marksman", "Assassin"], [("ADC", 90), ("MID", 10)], "crit_adc", ["Q", "E", "W"], ("Lightslinger", "Piercing Light", "Ardent Blaze", "Relentless Pursuit", "The Culling")),
    ("MissFortune", "Miss Fortune", "the Bounty Hunter", ["Marksman"], [("ADC", 95), ("SUPPORT", 5)], "lethality_adc", ["Q", "W", "E"], ("Love Tap", "Double Up", "Strut", "Make It Rain", "Bullet Time")),
    ("Nilah", "Nilah", "the Joy Unbound", ["Fighter", "Assassin"], [("ADC", 98), ("MID", 2)], "crit_adc", ["Q", "E", "W"], ("Joy Unending", "Formless Blade", "Jubilant Veil", "Slipstream", "Apotheosis")),
    ("Samira", "Samira", "the Desert Rose", ["Marksman", "Assassin"], [("ADC", 98), ("MID", 2)], "crit_adc", ["Q", "E", "W"], ("Daredevil Impulse", "Flair", "Blade Whirl", "Wild Rush", "Inferno Trigger")),
    ("Senna", "Senna", "the Redeemer", ["Marksman", "Support"], [("SUPPORT", 82), ("ADC", 18)], "lethality_adc", ["Q", "W", "E"], ("Absolution", "Piercing Darkness", "Last Embrace", "Curse of the Black Mist", "Dawning Shadow")),
    ("Sivir", "Sivir", "the Battle Mistress", ["Marksman"], [("ADC", 99), ("MID", 1)], "crit_adc", ["Q", "W", "E"], ("Fleet of Foot", "Boomerang Blade", "Ricochet", "Spell Shield", "On The Hunt")),
    ("Smolder", "Smolder", "the Fiery Fledgling", ["Marksman", "Mage"], [("ADC", 85), ("MID", 15)], "crit_adc", ["Q", "W", "E"], ("Dragon Practice", "Super Scorcher Breath", "Achooo!", "Flap, Flap, Flap", "MMMM MOMMMM!")),
    ("Tristana", "Tristana", "the Yordle Gunner", ["Marksman", "Assassin"], [("ADC", 72), ("MID", 28)], "crit_adc", ["E", "Q", "W"], ("Draw a Bead", "Rapid Fire", "Rocket Jump", "Explosive Charge", "Buster Shot")),
    ("Twitch", "Twitch", "the Plague Rat", ["Marksman", "Assassin"], [("ADC", 84), ("SUPPORT", 16)], "onhit_adc", ["E", "Q", "W"], ("Deadly Venom", "Ambush", "Venom Cask", "Contaminate", "Spray and Pray")),
    ("Varus", "Varus", "the Arrow of Retribution", ["Marksman", "Mage"], [("ADC", 88), ("MID", 12)], "onhit_adc", ["Q", "W", "E"], ("Living Vengeance", "Piercing Arrow", "Blighted Quiver", "Hail of Arrows", "Chain of Corruption")),
    ("Vayne", "Vayne", "the Night Hunter", ["Marksman", "Assassin"], [("ADC", 78), ("TOP", 22)], "onhit_adc", ["W", "Q", "E"], ("Night Hunter", "Tumble", "Silver Bolts", "Condemn", "Final Hour")),
    ("Xayah", "Xayah", "the Rebel", ["Marksman"], [("ADC", 99), ("MID", 1)], "crit_adc", ["E", "W", "Q"], ("Clean Cuts", "Double Daggers", "Deadly Plumage", "Bladecaller", "Featherstorm")),
    ("Zeri", "Zeri", "The Spark of Zaun", ["Marksman"], [("ADC", 98), ("MID", 2)], "crit_adc", ["Q", "E", "W"], ("Living Battery", "Burst Fire", "Ultrashock Laser", "Spark Surge", "Lightning Crash")),

    # --- SUPPORTS (30) ---
    ("Alistar", "Alistar", "the Minotaur", ["Tank", "Support"], [("SUPPORT", 98), ("TOP", 2)], "sup_tank", ["Q", "W", "E"], ("Triumphant Roar", "Pulverize", "Headbutt", "Trample", "Unbreakable Will")),
    ("Bard", "Bard", "the Wandering Caretaker", ["Support", "Mage"], [("SUPPORT", 99), ("MID", 1)], "sup_enchanter", ["Q", "W", "E"], ("Traveler's Call", "Cosmic Binding", "Caretaker's Shrine", "Magical Journey", "Tempered Fate")),
    ("Blitzcrank", "Blitzcrank", "the Great Steam Golem", ["Tank", "Fighter"], [("SUPPORT", 98), ("JUNGLE", 2)], "sup_hook", ["Q", "W", "E"], ("Mana Barrier", "Rocket Grab", "Overdrive", "Power Fist", "Static Field")),
    ("Brand", "Brand", "the Burning Vengeance", ["Mage"], [("SUPPORT", 54), ("JUNGLE", 46)], "sup_mage", ["W", "E", "Q"], ("Blaze", "Sear", "Pillar of Flame", "Conflagration", "Pyroclasm")),
    ("Braum", "Braum", "the Heart of the Freljord", ["Support", "Tank"], [("SUPPORT", 99), ("TOP", 1)], "sup_tank", ["Q", "E", "W"], ("Concussive Blows", "Winter's Bite", "Stand Behind Me", "Unbreakable", "Glacial Fissure")),
    ("Janna", "Janna", "the Storm's Fury", ["Support", "Mage"], [("SUPPORT", 99), ("MID", 1)], "sup_enchanter", ["W", "E", "Q"], ("Tailwind", "Howling Gale", "Zephyr", "Eye of the Storm", "Monsoon")),
    ("Karma", "Karma", "the Enlightened One", ["Mage", "Support"], [("SUPPORT", 82), ("MID", 18)], "sup_enchanter", ["Q", "E", "W"], ("Gathering Fire", "Inner Flame", "Focused Resolve", "Inspire", "Mantra")),
    ("Leona", "Leona", "the Radiant Dawn", ["Tank", "Support"], [("SUPPORT", 99), ("TOP", 1)], "sup_tank", ["W", "E", "Q"], ("Sunlight", "Shield of Daybreak", "Eclipse", "Zenith Blade", "Solar Flare")),
    ("Lulu", "Lulu", "the Fae Sorceress", ["Support", "Mage"], [("SUPPORT", 98), ("MID", 2)], "sup_enchanter", ["E", "W", "Q"], ("Pix, Faerie Companion", "Glitterlance", "Whimsy", "Help, Pix!", "Wild Growth")),
    ("Maokai", "Maokai", "the Twisted Treant", ["Tank", "Mage"], [("SUPPORT", 65), ("TOP", 25), ("JUNGLE", 10)], "sup_tank", ["Q", "W", "E"], ("Sap Magic", "Bramble Smash", "Twisted Advance", "Sapling Toss", "Nature's Grasp")),
    ("Milio", "Milio", "the Gentle Flame", ["Support"], [("SUPPORT", 99), ("MID", 1)], "sup_enchanter", ["E", "W", "Q"], ("Fired Up!", "Ultra Mega Fire Kick", "Cozy Campfire", "Warm Hugs", "Breath of Life")),
    ("Morgana", "Morgana", "the Fallen", ["Mage", "Support"], [("SUPPORT", 78), ("MID", 12), ("JUNGLE", 10)], "sup_mage", ["Q", "E", "W"], ("Soul Siphon", "Dark Binding", "Tormented Shadow", "Black Shield", "Soul Shackles")),
    ("Nami", "Nami", "the Tidecaller", ["Support", "Mage"], [("SUPPORT", 99), ("MID", 1)], "sup_enchanter", ["W", "E", "Q"], ("Surging Tides", "Aqua Prison", "Ebb and Flow", "Tidecaller's Blessing", "Tidal Wave")),
    ("Nautilus", "Nautilus", "the Titan of the Depths", ["Tank", "Fighter"], [("SUPPORT", 92), ("JUNGLE", 8)], "sup_hook", ["Q", "W", "E"], ("Staggering Blow", "Dredge Line", "Titan's Wrath", "Riptide", "Depth Charge")),
    ("Pyke", "Pyke", "the Bloodharbor Ripper", ["Support", "Assassin"], [("SUPPORT", 94), ("MID", 6)], "ad_assassin", ["Q", "E", "W"], ("Gift of the Drowned Ones", "Bone Skewer", "Ghostwater Dive", "Phantom Undertow", "Death from Below")),
    ("Rakan", "Rakan", "The Charmer", ["Support"], [("SUPPORT", 99), ("MID", 1)], "sup_tank", ["W", "E", "Q"], ("Fey Feathers", "Gleaming Quill", "Grand Entrance", "Battle Dance", "The Quickness")),
    ("Rell", "Rell", "the Iron Maiden", ["Tank", "Support"], [("SUPPORT", 92), ("JUNGLE", 8)], "sup_tank", ["W", "E", "Q"], ("Break the Mold", "Shattering Strike", "Ferromancy: Crash Down / Mount Up", "Full Tilt", "Magnet Storm")),
    ("Renata", "Renata Glasc", "the Chem-Baroness", ["Support", "Mage"], [("SUPPORT", 99), ("MID", 1)], "sup_enchanter", ["E", "W", "Q"], ("Leverage", "Handshake", "Bailout", "Loyalty Program", "Hostile Takeover")),
    ("Seraphine", "Seraphine", "the Starry-Eyed Songstress", ["Mage", "Support"], [("SUPPORT", 65), ("ADC", 35)], "sup_enchanter", ["Q", "E", "W"], ("Stage Presence", "High Note", "Surround Sound", "Beat Drop", "Encore")),
    ("Sona", "Sona", "Maven of the Strings", ["Support", "Mage"], [("SUPPORT", 99), ("MID", 1)], "sup_enchanter", ["Q", "W", "E"], ("Power Chord", "Hymn of Valor", "Aria of Perseverance", "Song of Celerity", "Crescendo")),
    ("Soraka", "Soraka", "the Starchild", ["Support", "Mage"], [("SUPPORT", 99), ("MID", 1)], "sup_enchanter", ["W", "Q", "E"], ("Salvation", "Starcall", "Astral Infusion", "Equinox", "Wish")),
    ("Swain", "Swain", "the Noxian Grand General", ["Mage", "Fighter"], [("SUPPORT", 58), ("MID", 42)], "ap_bruiser", ["Q", "W", "E"], ("Ravenous Flock", "Death's Hand", "Vision of Empire", "Nevermove", "Demonic Ascension")),
    ("Taric", "Taric", "the Shield of Valoran", ["Support", "Tank"], [("SUPPORT", 96), ("TOP", 4)], "sup_tank", ["E", "Q", "W"], ("Bravado", "Starlight's Touch", "Bastion", "Dazzle", "Cosmic Radiance")),
    ("Thresh", "Thresh", "the Chain Warden", ["Support", "Fighter"], [("SUPPORT", 98), ("ADC", 2)], "sup_hook", ["Q", "W", "E"], ("Damnation", "Death Sentence", "Dark Passage", "Flay", "The Box")),
    ("Yuumi", "Yuumi", "the Magical Cat", ["Support", "Mage"], [("SUPPORT", 99), ("MID", 1)], "sup_enchanter", ["Q", "E", "W"], ("Feline Friendship", "Prowling Projectile", "You and Me!", "Zoomies", "Final Chapter")),
    ("Zilean", "Zilean", "the Chronokeeper", ["Support", "Mage"], [("SUPPORT", 78), ("MID", 22)], "sup_enchanter", ["Q", "E", "W"], ("Time in a Bottle", "Time Bomb", "Rewind", "Time Warp", "Chronoshift")),
    ("Zyra", "Zyra", "Rise of the Thorns", ["Mage", "Support"], [("SUPPORT", 74), ("JUNGLE", 26)], "sup_mage", ["Q", "E", "W"], ("Garden of Thorns", "Deadly Spines", "Rampant Growth", "Grasping Roots", "Stranglethorns"))
]

# Generate detailed counters for each champion based on class & role
def generate_counters_for_champ(cid, role):
    # Role-based champion pools
    top_champs = ["Aatrox", "Darius", "Fiora", "Jax", "Camille", "Malphite", "Garen", "Riven", "Renekton", "Gwen", "Kled", "Irelia", "Ornn", "Shen", "Sion", "DrMundo", "Chogath", "Gnar", "Sett", "Olaf", "Jayce"]
    mid_champs = ["Ahri", "Zed", "Yasuo", "Yone", "Akali", "Syndra", "Sylas", "Viktor", "Orianna", "Leblanc", "Kassadin", "Vex", "Hwei", "Veigar", "Lux", "Neeko", "Katarina", "Galio", "Vladimir", "Anivia"]
    jgl_champs = ["LeeSin", "Viego", "Graves", "JarvanIV", "Kayn", "Khazix", "Elise", "Ekko", "Diana", "Belveth", "Amumu", "Sejuani", "Zac", "Nocturne", "MasterYi", "Briar", "Nidalee", "Kindred", "Hecarim"]
    adc_champs = ["Jinx", "Kaisa", "Jhin", "Caitlyn", "Ezreal", "Lucian", "Samira", "Draven", "Vayne", "Tristana", "Ashe", "MissFortune", "Twitch", "Xayah", "Zeri", "Smolder", "Aphelios", "Varus", "Nilah"]
    sup_champs = ["Thresh", "Nautilus", "Leona", "Blitzcrank", "Lulu", "Nami", "Janna", "Karma", "Pyke", "Rakan", "Braum", "Alistar", "Milio", "Soraka", "Sona", "Morgana", "Zyra", "Brand", "Rell", "Senna"]

    pool = top_champs if role == "TOP" else (jgl_champs if role == "JUNGLE" else (mid_champs if role == "MID" else (adc_champs if role == "ADC" else sup_champs)))
    pool = [c for c in pool if c != cid]

    # Generate 6 weak against, 6 strong against, 6 synergy
    weak = []
    for i, opp in enumerate(pool[:6]):
        wr = round(43.5 + (i * 0.7), 1)
        games = 1200 + (i * 450) + (len(cid) * 80)
        weak.append({"champion": opp, "winRate": wr, "games": games})

    strong = []
    for i, opp in enumerate(pool[6:12]):
        wr = round(57.5 - (i * 0.6), 1)
        games = 1400 + (i * 380) + (len(cid) * 90)
        strong.append({"champion": opp, "winRate": wr, "games": games})

    # Synergy pool from other roles (e.g. Junglers for Top/Mid, Supports for ADC, ADCs for Support)
    syn_pool = jgl_champs if role in ["TOP", "MID"] else (sup_champs if role == "ADC" else (adc_champs if role == "SUPPORT" else mid_champs))
    syn_pool = [c for c in syn_pool if c != cid]
    synergy = []
    for i, partner in enumerate(syn_pool[:6]):
        wr = round(58.5 - (i * 0.5), 1)
        games = 1800 + (i * 520) + (len(cid) * 110)
        synergy.append({"champion": partner, "winRate": wr, "games": games})

    return {"weakAgainst": weak, "strongAgainst": strong, "goodSynergy": synergy}

def build_champion_object(champ_tuple):
    cid, name, title, tags, roles_list, arch_name, max_order, ability_names = champ_tuple
    p_name, q_name, w_name, e_name, r_name = ability_names
    primary_role = roles_list[0][0]

    # Load archetype
    arch = ARCHETYPES.get(arch_name, ARCHETYPES["bruiser_ad"])

    # Build roles data
    builds = {}
    for role, pct in roles_list:
        # Determine archetype for this specific role
        role_arch = arch
        if role == "SUPPORT" and not arch_name.startswith("sup"):
            role_arch = ARCHETYPES["sup_tank"] if "Tank" in tags else ARCHETYPES["sup_mage"]
        elif role == "JUNGLE" and not arch_name.startswith("jungle"):
            role_arch = ARCHETYPES["jungle_tank"] if "Tank" in tags else (ARCHETYPES["jungle_ap"] if "Mage" in tags else ARCHETYPES["jungle_ad"])
        elif role == "TOP" and not arch_name.startswith("bruiser") and not arch_name.startswith("tank") and not arch_name.startswith("juggernaut"):
            role_arch = ARCHETYPES["tank_res"] if "Tank" in tags else ARCHETYPES["bruiser_ad"]

        # Calculate rank & stats
        wr = round(50.4 + ((hash(cid + role) % 35) - 15) * 0.1, 1)
        pr = round(pct * 0.08 + ((hash(cid) % 20) * 0.1), 1)
        br = round(2.0 + ((hash(cid) % 150) * 0.1), 1)
        games = int(25000 + (pct * 450) + (hash(cid) % 15000))
        tier = "S+" if wr >= 51.8 else ("S" if wr >= 51.0 else ("A" if wr >= 49.8 else "B"))
        rank_num = max(1, min(50, 52 - int((wr - 47.0) * 8)))

        # Build path sequence
        starter_id = role_arch["starter"]
        boots_id = role_arch["boots"]
        core_ids = role_arch["core"]
        sit_ids = role_arch["sit"]
        build_path = [starter_id, boots_id] + core_ids + [sit_ids[0]]

        # Counters
        counters = generate_counters_for_champ(cid, role)

        builds[role] = {
            "role": role,
            "tier": tier,
            "rank": f"{rank_num}th / 50",
            "winRate": wr,
            "pickRate": pr,
            "banRate": br,
            "games": games,
            "summonerSpells": role_arch["spells"],
            "altSpells": role_arch["altSpells"],
            "spellsWinRate": role_arch["spells_wr"],
            "spellsPickRate": role_arch["spells_pr"],
            "starter": starter_id,
            "boots": boots_id,
            "coreItems": core_ids,
            "buildPath": build_path,
            "situationalItems": sit_ids,
            "skillMaxOrder": max_order,
            "skillOrder": generate_skill_order(max_order),
            "runes": {
                "primary": role_arch["pri"],
                "keystone": role_arch["keystone"],
                "primaryRunes": role_arch["pri_runes"],
                "secondary": role_arch["sec"],
                "secondaryRunes": role_arch["sec_runes"],
                "stats": role_arch["stats"]
            },
            "counters": counters
        }

    # Primary build for backwards compatibility
    prim_build = builds[primary_role]

    return {
        "id": cid,
        "name": name,
        "title": title,
        "tags": tags,
        "primaryRole": primary_role,
        "role": primary_role,
        "roles": [{"role": r, "playRate": p} for r, p in roles_list],
        "image": f"https://ddragon.leagueoflegends.com/cdn/14.23.1/img/champion/{cid}.png",
        "loading": f"https://ddragon.leagueoflegends.com/cdn/img/champion/loading/{cid}_0.jpg",
        "splash": f"https://ddragon.leagueoflegends.com/cdn/img/champion/splash/{cid}_0.jpg",
        "abilities": {
            "p": {"name": p_name, "key": "Passive", "icon": f"https://ddragon.leagueoflegends.com/cdn/14.23.1/img/passive/{cid}_Passive.png"},
            "q": {"name": q_name, "key": "Q", "icon": f"https://ddragon.leagueoflegends.com/cdn/14.23.1/img/spell/{cid}Q.png"},
            "w": {"name": w_name, "key": "W", "icon": f"https://ddragon.leagueoflegends.com/cdn/14.23.1/img/spell/{cid}W.png"},
            "e": {"name": e_name, "key": "E", "icon": f"https://ddragon.leagueoflegends.com/cdn/14.23.1/img/spell/{cid}E.png"},
            "r": {"name": r_name, "key": "R", "icon": f"https://ddragon.leagueoflegends.com/cdn/14.23.1/img/spell/{cid}R.png"}
        },
        "build": prim_build,
        "builds": builds,
        "counters": prim_build["counters"]
    }

# Build master database
final_db = {
    "version": "16.16.1",
    "patch": "16.16.1",
    "updatedAt": "2026-08-12",
    "items": ITEMS,
    "runes": RUNES,
    "spells": SPELLS,
    "champions": {}
}

for champ_data in CHAMPIONS_LIST:
    c_obj = build_champion_object(champ_data)
    final_db["champions"][c_obj["id"]] = c_obj

print(f"Compiled {len(final_db['champions'])} champions successfully.")

with open("data.json", "w", encoding="utf-8") as f:
    json.dump(final_db, f, indent=2, ensure_ascii=False)

print("Saved to data.json successfully!")

# Add MonkeyKing
mk_data = ("MonkeyKing", "Wukong", "the Monkey King", ["Fighter", "Tank"], [("TOP", 65), ("JUNGLE", 35)], "bruiser_ad", ["Q", "E", "W"], ("Stone Skin", "Crushing Blow", "Warrior Trickster", "Nimbus Strike", "Cyclone"))
c_obj = build_champion_object(mk_data)
final_db["champions"][c_obj["id"]] = c_obj

with open("data.json", "w", encoding="utf-8") as f:
    json.dump(final_db, f, indent=2, ensure_ascii=False)

print(f"Total champions now in data.json: {len(final_db['champions'])}")
