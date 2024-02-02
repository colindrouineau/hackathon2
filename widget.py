import flet as ft

n=3



def show_situation(situation):
    print(situation)
    global screen
    for i in range(n**2):
        if(situation[i]!=0):
            screen[i].text=situation[i]
        else:
            screen[i].text="-"
        screen[i].update()


def show_next_situation(e):
    global current
    current+=1
    show_situation(game_situations[current])

def show_previous_situation(e):
    global current
    current-=1
    show_situation(game_situations[current])

initial_situation = ""
reachable=True
path=[]

def submit_situation(e):
    L=[]
    for field in params:
        L.append(field.value)
    if [] not in L:
        initial_situation = ''.join(L)
        print(initial_situation)
    
    #récuperer la validité et le chemin dans game_situations
    if not reachable:
        visu.value = "Pas de solution"
        visu.update()
    else:
        visu.value = "Visualisation de la solution"
        visu.update()
    





game_situations = ["103258794", "222222222", "333333333", "444444444"]
current=0
screen = []

for i in range(n**2):
    screen.append(ft.TextButton(text = game_situations[current][i]))

prev = ft.TextButton(text = "Etape précédente", on_click = show_previous_situation)
next = ft.TextButton(text = "Etape suivante", on_click = show_next_situation)

params=[]
for i in range(n**2):
    params.append(ft.TextField(label = "Number"))

visu = ft.TextField(value = "Visualisation de la solution")



def main(page: ft.Page):
    page.title = "Taquin"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    page.add(

        ft.Row([
            ft.TextField(value = "Implémentation de point de départ")
        ]),

        ft.Row(
            params[0:3]
        ),
        ft.Row(
            params[3:6]
        ),
        ft.Row(
            params[6:9]
        ),
        ft.Row([
            ft.TextButton(text = "Submit", on_click = submit_situation)
        ]),



        ft.Row([
            visu
        ]),

        ft.Row(screen[0:3]),
        ft.Row(screen[3:6]),
        ft.Row(screen[6:9]),
        ft.Row([prev, next]),


    )

ft.app(target=main)