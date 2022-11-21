

districts = {
    "Atasehir" : (0, 24, 34, 9, 17, 11, 33, 29, 14, 63, 26, 7, 14),
    "Beykoz" : (24, 0, 24, 29, 37, 34, 60, 35, 34, 73, 47, 22, 26),
    "Cekmekoy" : (34, 24, 0, 38, 33, 27, 43, 14, 21, 36, 33, 29, 36),
    "Kadikoy" : (9, 29, 38, 0, 19, 13, 20, 24, 18, 63, 30, 12, 11),
    "Kartal" : (17, 37, 33, 19, 0, 13, 7, 21, 18, 60, 17, 22, 27),
    "Maltepe" : (11, 34, 27, 13, 13, 0, 16, 16, 11, 56, 27, 19, 20),
    "Pendik" : (33, 60, 43, 20, 7, 16, 0, 29, 23, 71, 16, 27, 29),
    "Sancaktepe" : (29, 35, 14, 24, 21, 16, 29, 0, 10, 41, 21, 19, 28),
    "Sultanbeyli" : (14, 34, 21, 18, 18, 11, 23, 10, 0, 50, 16, 20, 25),
    "Sile" : (63, 73, 36, 63, 60, 56, 71, 41, 50, 0, 63, 57, 63),
    "Tuzla" : (26, 47, 33, 30, 17, 27, 16, 21, 16, 63, 0, 32, 36),
    "Umraniye" : (7, 22, 29, 12, 22, 19, 27, 19, 20, 57, 32, 0, 12),
    "Uskudar" : (1, 26, 36, 11, 27, 20, 29, 28, 25, 63, 36, 12, 0)
}

routes = (("Atasehir","Umraniye"), ("Atasehir", "Beykoz", "Cekmekoy"), 
("Atasehir", "Umraniye", "Uskudar"), ("Beykoz", "Cekmekoy", "Sancaktepe"),
("Beykoz", "Uskudar", "Umraniye", "Atasehir", "Kadikoy", "Maltepe", "Kartal"),
("Beykoz", "Cekmekoy", "Sancaktepe", "Sultanbeyli", "Maltepe", "Kartal", "Pendik"))

combinations = (("Atasehir", "Kadikoy"), ("Beykoz", "Cekmekoy"), ("Beykoz", "Sancaktepe"), 
("Cekmekoy", "Sultanbeyli"), ("Maltepe", "Kadıkoy"), ("Uskudar", "Kadikoy", "Beykoz"),
("Beykoz", "Sultanbeyli", "Kartal"), ("Beykoz", "Ataşehir", "Maltepe"))

list_districts = list(districts.keys()) # dictionary keys assigned to list


def check_feasibility(route, combination):
    flag = False
    a = 40
    if route[0] == combination[0]: # set charge value
        charge = a
    else:
        charge = a/2
    for i in range(len(route)): #as many loops as the number of districts in route
        if i < len(route)-1:
            distance = districts[route[i]][list_districts.index(route[i+1])] #find distance between taken districts
            charge -= distance
            if route[i+1] in combination: # if there is a charge station on route charge EV
                charge = 40
        if charge >= 0:
            flag = True
        else:
            flag = False
    return flag



def find_feasible_route(routes, combinations):
    flag = False
    a = 40 # charge 
    feasible_routes = dict()
    for r in range(len(routes)): #as many loops as the number of routes
        route = routes[r] # take a rote from routes tuple
        comb_list = []
        for c in range(len(combinations)): #as many loops as the number of combinations
            comb = combinations[c] # take a rote from combinations tuple
            if route[0] == comb[0]: # set charge value
                charge = a
            else:
                charge = a/2
            for i in range(len(route)): #as many loops as the number of districts in route

                if i < len(route)-1:
                    distance = districts[route[i]][list_districts.index(route[i+1])] #find distance between taken districts
                    charge -= distance
                    if route[i+1] in comb: # if there is a charge station on route charge EV
                        charge = 40
            if charge >= 0:
                flag = True
            else:
                flag = False
            if flag == True:
                comb_list.append(combinations.index(comb)) # add combinations which is feasible to a list 
        feasible_routes[routes.index(route)] = comb_list # add routes and combinations to dict
    return feasible_routes


# example
print(check_feasibility(("Beykoz", "Cekmekoy", "Sancaktepe"), ("Beykoz", "Sultanbeyli", "Kartal")))

# example
print(find_feasible_route(routes, combinations))