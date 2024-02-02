import flet as ft

n = 3


def show_situation(situation):
    global screen
    for i in range(n**2):
        if situation[i] != 0:
            screen[i].text = situation[i]
        else:
            screen[i].text = "-"
        screen[i].update()


def show_next_situation(e):
    global current
    current += 1
    show_situation(game_situations[current])


def show_previous_situation(e):
    global current
    current -= 1
    show_situation(game_situations[current])


def show_game_state(situation):
    for i in range(len(screen_game)):
        screen_game[i].text = situation[i]
        screen_game[i].update()


situation = ""
reachable = True
path = []


def submit_situation(e):
    global situation
    L = []
    for field in params:
        L.append(field.value)
    if [] not in L:
        situation = "".join(L)

    # récuperer la validité et le chemin dans game_situations
    if not reachable:
        visu.value = "Pas de solution"
        visu.update()
    else:
        visu.value = "Visualisation de la solution"
        visu.update()
        show_game_state(situation)


def game(e):
    global situation
    i = int(situation.find("0"))
    print(situation)
    situation_list = list(situation)
    if e.control.text == "Haut":
        if i >= 3:
            situation_list[i], situation_list[i - 3] = (
                situation_list[i - 3],
                situation_list[i],
            )
    if e.control.text == "Bas":
        if i <= 5:
            situation_list[i], situation_list[i + 3] = (
                situation_list[i + 3],
                situation_list[i],
            )
    if e.control.text == "Droite":
        if (i + 1) % 3 != 0:
            situation_list[i], situation_list[i + 1] = (
                situation_list[i + 1],
                situation_list[i],
            )
    if e.control.text == "Gauche":
        if (i + 1) % 3 != 1:
            situation_list[i], situation_list[i - 1] = (
                situation_list[i - 1],
                situation_list[i],
            )

    situation = "".join(situation_list)
    show_game_state(situation)


game_situations = ["103258794", "222222222", "333333333", "444444444"]
current = 0
screen = []

for i in range(n**2):
    screen.append(ft.TextButton(text=game_situations[current][i]))

prev = ft.TextButton(text="Etape précédente", on_click=show_previous_situation)
next = ft.TextButton(text="Etape suivante", on_click=show_next_situation)

params = []
for i in range(n**2):
    params.append(ft.TextField(label="Number"))

visu = ft.Text("Visualisation de la solution")

screen_game = []

for i in range(n**2):
    screen_game.append(ft.TextButton(text=game_situations[current][i]))

up = ft.TextButton(text="Haut", on_click=game)
down = ft.TextButton(text="Bas", on_click=game)
right = ft.TextButton(text="Droite", on_click=game)
left = ft.TextButton(text="Gauche", on_click=game)


def main(page: ft.Page):
    page.title = "Taquin"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    page.add(
        ft.Row([ft.Text("Implémentation de point de départ")]),
        ft.Row(params[0:3]),
        ft.Row(params[3:6]),
        ft.Row(params[6:9]),
        ft.Row([ft.TextButton(text="Submit", on_click=submit_situation)]),
        ft.Row([visu]),
        ft.Row(screen[0:3]),
        ft.Row(screen[3:6]),
        ft.Row(screen[6:9]),
        ft.Row([prev, next]),
        ft.Row([ft.Text("A toi de jouer !")]),
        ft.Row(screen_game[0:3]),
        ft.Row(screen_game[3:6]),
        ft.Row(screen_game[6:9]),
        ft.Row([up, down, right, left]),
    )


ft.app(target=main)
