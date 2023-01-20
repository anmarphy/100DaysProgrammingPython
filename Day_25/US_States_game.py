import turtle
import pandas as pd

screen=turtle.Screen()
screen.title('U.S. States Game')
image='blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

def get_mouse_click_coor(x,y):
    print(x,y)

turtle.onscreenclick(get_mouse_click_coor)


states_df=pd.read_csv('50_states.csv')
all_states=states_df.state.to_list()
total_states=len(all_states)
learn_states=[]


while total_states>0:
    answer_state=screen.textinput(title=f'Guess the state. Still pending {total_states} states', prompt="What's the state's name?").title()

    if answer_state=='Exit':
        pending_states = [state for state in all_states if state not in learn_states]
        pending_st_df=pd.DataFrame(pending_states, columns=['Pending states'])
        pending_st_df.to_csv('Pending_states.csv')
        break

    if answer_state in all_states:
        learn_states.append(answer_state)
        total_states-=1
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data=states_df[states_df.state == answer_state]
        t.goto(float(state_data.x), float(state_data.y))
        t.write(f'{answer_state}', align='center', font=('Arial', 10, 'normal'))
        print(learn_states)
