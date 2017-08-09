import turtle
score=0
car=turtle.clone()
car.shape("square")
turtle.hideturtle()
turtle.penup()
turtle.shape("square")
food = turtle.clone()
food.shape("circle")
food.color("orange")
food_pos=[(100,100) , (-100,100) , (-100,-100) , (100,-100)]
food_stamps=[]

if car.pos() in food_pos:
        food_ind=food_pos.index(car.pos())
        food.clearstamp(food_stamps[food_ind])
        food_pos.pop(food_ind)
        food_stamps.pop(food_ind)
        print("You have taken the food!")
        score+=1
        print(score)
new_pos=car.pos()
new_x_pos=new_pos[0]
new_y_pos=new_pos[1]
        
for this_food_pos in food_pos:
    food.goto(this_food_pos[0],this_food_pos[1])
    b=food.stamp()
    food_stamps.append(b)
    turtle.hideturtle()
