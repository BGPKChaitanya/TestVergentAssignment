class DataPlanetry:
    def __init__(self,name,surface,moon,rings):
        self.name = name
        self.surface = surface
        self.moon = moon
        self.rings = rings
    def count_moon(self,list_items):
        count = 0
        self.list_items = list_items
        new_list = []
        for k,v in list_items.items():
            if v == "Yes":
                new_list.append(k)
        print(sum(new_list))
    def gases_retrived_planet(self,new_gases):
        self.new_gases = new_gases
        new_gas = []
        for k,v in new_gases.items():
            new_gas.append(v)
        res = max(new_gas)
        
        for k,v in new_gases.items():
            if v == res:
                return("Gas that is found on maximum planets is: " + k)

planet = DataPlanetry("Moon","Carbon Dioxide",0,"No")
planet.count_moon({0:"No",
    0:"No",
    1:"No",
    79:"Yes",
    83:"Yes",
    27 : "Yes"
})

planet.gases_retrived_planet({
    "jupitor" : 79,
    "saturn" : 83,
    "uranus" : 27})