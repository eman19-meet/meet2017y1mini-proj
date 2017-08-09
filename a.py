import turtle
turtle.penup()
turtle.shape("square")
food = turtle.clone()
food.shape("circle")
food.color("orange")
food_pos=[(100,100) , (-100,100) , (-100,-100) , (100,-100)]
food_stamps=[]

for this_food_pos in food_pos:
    food.goto(this_food_pos[0],this_food_pos[1])
    b=food.stamp()
    food_stamps.append(b)
    turtle.hideturtle()

def make_food():
    min_x=-int(SIZE_X/2/SQUARE_SIZE)+1
    max_x=int(SIZE_X/2/SQUARE_SIZE)-1
    min_y=-int(SIZE_X/2/SQUARE_SIZE)-1
    max_y=int(SIZE_X/2/SQUARE_SIZE)+1

    food_x=random.randint(min_x,max_x)*SQUARE_SIZE
    food_y=random.randint(min_y,max_y)*SQUARE_SIZE

    food.goto(food_x,food_y)
    food_pos.append((food_x,food_y))
    a=food.stamp()
    food_stamps.append(a)

