from django.shortcuts import render


THOUGHT_LIST = [
    "Na początek dnia wybieram kawę, A jako kontynuację, uśmiech.",
    "Każdego ranka masz możliwość wyboru sposobu działania, postępowania, bycia.",
    "Uśmiech na pierwszej napotkanej rano twarzy to powitanie na dzień, który się zaczyna.",
    "Obudź się każdego ranka z myślą, że wydarzy się coś wspaniałego."
]

def randomthought(request):
    return render(
        request,
        'thought.html'
    )