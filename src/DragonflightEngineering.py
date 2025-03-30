
import copy

others = {"Overcharged Overclocker":{"Rousing Earth":4},
          #"Illustrious Insight":[],
          "Haphazardly Tethered Wires":{"Handful of Serevite Bolts":3},
          #"Calibrated Safety Switch":[],
          #"Critical Failure Prevention Unit":[],
          #"Magazine of Healing Darts":[],
          #"Spring-Loaded Capacitor Casing":[]
          }

gathers = ["Wildercloth","Serevite Ore","Draconium Ore","Khaz'gorite Ore", "Awakened Order", "Awakened Earth", "Rousing Fire", "Rousing Earth", "Potion of Hushed Zephyr","Frameless Lens","Eternity Amber","Smudged Lens"]
reagents = {
    "Arclight Capacitor":{"Awakened Order":1, "Shock-Spring Coil":2, "Greased-Up Gears":1, "Khaz'gorite Ore":2},
    "Reinforced Machine Chassis":{"Awakened Earth":1, "Handful of Serevite Bolts":4, "Shock-Spring Coil":1, "Greased-Up Gears":2},
    #"Assorted Safety Fuses":,
    "Everburning Blasting Powder":{"Rousing Fire":2, "Rousing Earth":1,"Draconium Ore":1},
    "Greased-Up Gears":{"Rousing Fire":3, "Handful of Serevite Bolts":2, "Draconium Ore":4},
    "Shock-Spring Coil":{"Rousing Earth":2, "Handful of Serevite Bolts":6},
    "Handful of Serevite Bolts":{"Serevite Ore":4}}
products = {
    "Tinker: Plane Displacer":{"Shock-Spring Coil":1,"Reinforced Machine Chassis":1,"Potion of Hushed Zephyr":1},
    "Deadline Deadeyes":{"Smudged Lens":2, "Shock-Spring Coil":2, "Handful of Serevite Bolts":2, "Greased-Up Gears":1},
    "Milestone Magnifiers":{"Smudged Lens":2, "Shock-Spring Coil":2, "Handful of Serevite Bolts":2, "Greased-Up Gears":1},
    "Quality-Assured Optics":{"Smudged Lens":2, "Shock-Spring Coil":2, "Handful of Serevite Bolts":2, "Greased-Up Gears":1},
    "Sentry's Stabilized Specs":{"Smudged Lens":2, "Shock-Spring Coil":2, "Handful of Serevite Bolts":2, "Greased-Up Gears":1},
    "Completely Safe Rockets":{"Handful of Serevite Bolts":2, "Everburning Blasting Powder":4},
    "Endless Stack of Needles":{"Handful of Serevite Bolts":2, "Shock-Spring Coil":1, "Greased-Up Gears":1},
    "Gyroscopic Kaleidoscope":{"Frameless Lens":1, "Handful of Serevite Bolts":2,"Greased-Up Gears":6,"Arclight Capacitor":2},
    "Bronze Firelight":{"Everburning Blasting Powder":2, "Eternity Amber":1},
    "Creature Combustion Canister":{"Everburning Blasting Powder":6, "Shock-Spring Coil":1, "Handful of Serevite Bolts":4},
    "Tinker Removal Kit":{"Handful of Serevite Bolts":3, "Shock-Spring Coil":2, "Draconium Ore":2},
    "Neural Silencer Mk3":{"Wildercloth":1, "Handful of Serevite Bolts":4, "Shock-Spring Coil":2, "Greased-Up Gears":1},
    "Bottomless Stonecrust Ore Satchel":{"Draconium Ore":5, "Handful of Serevite Bolts":2},
    "Draconium Brainwave Amplifier":{"Smudged Lens":1, "Handful of Serevite Bolts":2, "Shock-Spring Coil":2, "Draconium Ore":2},
    "Draconium Delver's Helmet":{"Smudged Lens":1, "Handful of Serevite Bolts":2, "Draconium Ore":2},
    "Draconium Encased Samophlange":{"Handful of Serevite Bolts":2, "Shock-Spring Coil":2, "Greased-Up Gears":1, "Draconium Ore":2},
    "Draconium Fisherfriend":{"Handful of Serevite Bolts":2, "Shock-Spring Coil":2, "Greased-Up Gears":1, "Draconium Ore":3},
    "Lapidary's Draconium Clamps":{"Handful of Serevite Bolts":2, "Greased-Up Gears":1, "Draconium Ore":3},
    "Spring-Loaded Draconium Fabric Cutters":{"Handful of Serevite Bolts":3, "Shock-Spring Coil":3, "Draconium Ore":4},
    }

import plotly.io as pio
pio.renderers.default='browser'


import plotly.graph_objects as go



labels = copy.copy(gathers)
labels.extend(reagents.keys())
labels.extend(products.keys())
labels.extend(others.keys())
sources = []
targets = []
values = []
for comp in labels:
    if comp in reagents.keys():
        for reag in reagents[comp]:
            sources.append(labels.index(reag))
            targets.append(labels.index(comp))
            values.append(reagents[comp][reag])
    if comp in products.keys():
        for reag in products[comp]:
            sources.append(labels.index(reag))
            targets.append(labels.index(comp))
            values.append(products[comp][reag])
    if comp in others.keys():
        for reag in others[comp]:
            sources.append(labels.index(reag))
            targets.append(labels.index(comp))
            values.append(others[comp][reag])
            
#print(labels)
#print(sources)
#print(targets)
#print(values)




fig = go.Figure(data=[go.Sankey(
    node = dict(
      pad = 15,
      thickness = 20,
      line = dict(color = "black", width = 0.5),
      label = labels,  #The 
      color = "blue"
    ),
    link = dict(
      source = sources, # From
      target = targets, # To
      value = values   # with
  ))])

fig.update_layout(title_text="Basic Sankey Diagram", font_size=10)
fig.show()
