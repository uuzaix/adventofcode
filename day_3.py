with open('day_3.input') as f:
    input = f.readline()

def visited_santa(input):
    visited_list=set()
    visited_list.add((0,0))
    x = 0
    y = 0
    for step in input:
        if step == ">":
            x += 1
        if step == "<":
            x-= 1
        if step == "^":
            y+= 1
        if step == "v":
            y-= 1
        visited_list.add((x,y))
    return len(visited_list)

def visited_both(input):
    visited_list=set()
    visited_list.add((0,0))
    x = 0
    y = 0
    robo_x = 0
    robo_y = 0
    counter = 1
    for step in input:
        if counter%2 != 0:
            if step == ">":
                x += 1
            if step == "<":
                x-= 1
            if step == "^":
                y+= 1
            if step == "v":
                y-= 1
        if counter%2 == 0:
            if step == ">":
                robo_x += 1
            if step == "<":
                robo_x-= 1
            if step == "^":
                robo_y+= 1
            if step == "v":
                robo_y-= 1
        counter += 1
        visited_list.add((x,y))
        visited_list.add((robo_x,robo_y))
    return len(visited_list)
                    
print visited_santa(input)
print visited_both(input)