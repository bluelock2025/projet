import random
import tkinter as tk
from tkinter import messagebox, simpledialog
import time
import pygame

# Questions par thème et par niveau
questions = {
    "1": {  # Culture Générale
        "nom": "Culture Générale",
        "facile": [
            {"question": "Quelle est la capitale du Burkina Faso ?", "choix": ["Perou", "Bamako", "Ouagadougou", "Paris"], "reponse": "Ouagadougou"},
            {"question": "Avec quoi se joue le Football ?", "choix": ["Les fesses", "La main", "Les epaules", "Les pieds"], "reponse": "Les pieds"},
            {"question": "Quel est la capitale de l'Italie", "choix": ["Rome","Londre","Lisbonne","Brasilia"], "reponse": "Rome"},
            {"question": "Quel club a gagné la Ligue des champions 2023-2024 ?", "choix": ["REAL MADRID", "Liverpool", "DORTMUND", "BAYERN MUNICH"], "reponse": "REAL MADRID"},
            {"question": "Quel est le symbole chimique de l'or ?", "choix": ["O", "Or", "Au", "Ag"], "reponse": "Au"},
            {"question": "Combien de continents existe-t-il ?", "choix": ["5", "6", "7", "8"], "reponse": "7"},
            {"question": "Quel est l'animal le plus rapide du monde ?", "choix": ["Guépard", "Aigle", "Lion", "Gazelle"], "reponse": "Guépard"},
            {"question": "Quelle planète est surnommée la planète rouge ?", "options": ["Mars", "Jupiter", "Venus", "Saturne"], "answer": "Mars"},
            
        ],
        "moyen": [
            {"question": "Quel est la langue la plus parlé au monde ?", "choix": ["mandarin", "chinois", "anglais", "français"], "reponse": "mandarin"},
            {"question": "en quelle année la seconde guerre mondiale a commencé?", "choix": ["1941", "1945", "1939", "1930"], "reponse": "1939"},
            {"question": "Qui a gagné la coupe du monde 2014 ?", "choix": ["l'Allemangne", "L'Argentine", "Brésil", "Espagne"], "reponse": "L'Allemangne"},
            {"question": "Combien de semaines a une année bissextile ?", "choix": ["52", "43", "50", "36"], "reponse": "52"},
            {"question": "Quelle planète est la plus proche du Soleil ?", "choix": ["Vénus", "Mercure", "Terre", "Mars"], "reponse": "Mercure"},
            {"question": "Dans quelle ville se trouve la Tour de Pise ?", "choix": ["Rome", "Florence", "Pise", "Venise"], "reponse": "Pise"},
            {"question": "Quel pays est surnommé le pays du Soleil-Levant ?", "choix": ["Chine", "Thaïlande", "Japon", "Corée"], "reponse": "Japon"},
            {"question": "Qui a peint 'La Nuit étoilée' ?", "choix": ["Picasso", "Van Gogh", "Monet", "Manet"], "reponse": "Van Gogh"}
        ],
        "difficile": [
            {"question": "Comment on appelle quelqu'un qui méprise les femmes(sentiment)", "choix": ["misogyne", "xénophobe", "raciste", "féministe"], "reponse": "misogyne"},
            {"question": "Que fut le score du macth Barça-Liverpool au match retour de la Ligue des champions 2018-2019 ?", "choix": ["1-0", "0-2", "3-2", "0-4"], "reponse": "0-4"},
            {"question": "Qui a peint La Joconde ?", "choix": ["Michel-Ange", "Raphaël", "Léonard de Vinci", "Donatello"], "reponse": "Léonard de Vinci"},
            {"question": "Qui est a ete le premier president du Burkina Faso ?", "choix": ["Pierre MELONCHON", "Simon COMPAORE", "Thomas SANKARA", "Maurice YAMEOGO"], "reponse": "Thomas SANKARA"},
            {"question": "En quelle année a eu lieu la Révolution française ?", "choix": ["1776", "1789", "1812", "1804"], "reponse": "1789"},
            {"question": "Quelle est la capitale de la Mongolie ?", "choix": ["Oulan-Bator", "Hanoï", "Katmandou", "Bakou"], "reponse": "Oulan-Bator"},
            {"question": "Quel est l'auteur de 'Le Prince' ?", "choix": ["Machiavel", "Platon", "Aristote", "Socrate"], "reponse": "Machiavel"},
            {"question": "Quelle est la distance moyenne entre la Terre et la Lune ?", "choix": ["384 000 km", "1 000 000 km", "150 000 km", "800 000 km"], "reponse": "384 000 km"}
        ],
    },
    "2": {  # Physique
        "nom": "Physique",
        "facile": [
            {"question": "Quelle est l'unité de l'intensité électrique ?", "choix": ["ohm", "ampère", "volt", "hertz"], "reponse": "ampère"},
            {"question": "L’eau bout à combien de degrés Celsius ?", "choix": ["90", "100", "110", "120"], "reponse": "100"},
            {"question": "Quelle est la formule de la vitesse ?", "choix": ["V = d/t", "V = t/d", "V = m*a", "V = E/t"], "reponse": "V = d/t"},
            {"question": "L’électricité est due à quoi ?", "choix": ["Lumière", "Électrons", "Chaleur", "Son"], "reponse": "Électrons"},
            {"question": "Quelle est la formule de la vitesse ?", "choix": ["V = d/t", "V = t/d", "V = m*a", "V = E/t"], "reponse": "V = d/t"},
            {"question": "L’électricité est due à quoi ?", "choix": ["Lumière", "Électrons", "Chaleur", "Son"], "reponse": "Électrons"},
            {"question": "Quel est l’état de l’eau à 0°C ?", "choix": ["Liquide", "Solide", "Gaz", "Plasma"], "reponse": "Solide"},
            {"question": "Combien de planètes dans le système solaire ?", "choix": ["7", "8", "9", "10"], "reponse": "8"}
        ],
        "moyen": [
            {"question": "Quelle particule porte une charge négative ?", "choix": ["Électron", "Neutron", "Proton", "Ion"], "reponse": "Ion"},
            {"question": "Formule de l’énergie cinétique ?", "choix": ["E = mc^2", "E = 1/2mv^2", "E = mv", "E = Fd"], "reponse": "E = 1/2mv^2"},
            {"question": "Qui a découvert la gravitation ?", "choix": ["Galilée", "Einstein", "Newton", "Tesla"], "reponse": "Newton"},
            {"question": "Quel est l’unité de la pression ?", "choix": ["Pa", "N", "J", "kg"], "reponse": "Pa"},
            {"question": "Quelle est la vitesse de la lumière dans le vide ?", "choix": ["3x10^8 m/s", "1.5x10^8 m/s", "3x10^6 m/s", "1x10^9 m/s"], "reponse": "3x10^8 m/s"},
            {"question": "Quel phénomène explique l’arc-en-ciel ?", "choix": ["Réflexion", "Réfraction", "Diffraction", "Interférence"], "reponse": "Réfraction"}
        ],
        "difficile": [
            {"question": "Quel est l'élement chimique le plus radioactif du tableau périodique ?", "choix": ["Ra", "Ph", "Ca", "H"], "reponse": "Ra"},
            {"question": "La lumière est composée de ?", "choix": ["Protons", "Neutrons", "Photons", "Électrons"], "reponse": "Photons"},
            {"question": "Qu’est-ce que l’entropie ?", "choix": ["Chaleur", "Désordre", "Travail", "Énergie"], "reponse": "Désordre"},
            {"question": "Quelle onde ne traverse pas le vide ?", "choix": ["Lumière", "Son", "Rayons X", "UV"], "reponse": "Son"},
            {"question": "Quel scientifique a formulé les lois de l’électromagnétisme ?", "choix": ["Maxwell", "Faraday", "Newton", "Planck"], "reponse": "Maxwell"},
            {"question": "Quel est le principe d’Archimède ?", "choix": ["Poussée vers le haut", "Gravité constante", "Force centrifuge", "Réaction égale"], "reponse": "Poussée vers le haut"}
        ],
    },
    "3": {  # Python
        "nom": "Python",
        "facile": [
            {"question": "Quel syntaxe pour définir un entier ?", "choix": ["int", "float", "str", "bool"], "reponse": "int"},
            {"question": "Quel symbole pour un commentaire ?", "choix": ["//", "--", "#", "/*"], "reponse": "#"},
            {"question": "Comment déclarer une liste ?", "choix": ["()", "[]", "{}", "<>"], "reponse": "[]"},
            {"question": "Python est ?", "choix": ["Langage compilé", "Langage de bas niveau", "Langage interprété", "Langage assembleur"], "reponse": "Langage interprété"},
            {"question": "Quelle est la bonne extension de fichier pour Python ?", "choix": [".py", ".pt", ".python", ".p"], "reponse": ".py"},
            {"question": "Comment afficher un message ?", "choix": ["echo", "write", "print", "msg"], "reponse": "print"}
        ],
        "moyen": [
            {"question": "Quelle est la sortie de print(2 // 3) ?", "choix": ["0.666", "0", "2", "erreur"], "reponse": "0"},
            {"question": "Comment répéter une boucle tant que vraie ?", "choix": ["for", "if", "while", "repeat"], "reponse": "while"},
            {"question": "len('Python') renvoie ?", "choix": ["5", "6", "7", "Erreur"], "reponse": "6"},
            {"question": "Un dictionnaire utilise ?", "choix": ["Index", "Clés", "Positions", "Ordres"], "reponse": "Clés"},
            {"question": "Quel est le résultat de bool('False') ?", "choix": ["False", "True", "None", "Erreur"], "reponse": "True"},
            {"question": "Que renvoie range(3) ?", "choix": ["[1, 2, 3]", "[0, 1, 2]", "[0, 1, 2, 3]", "[1, 2]"], "reponse": "[0, 1, 2]"},
            {"question": "Quelle structure contrôle le flux ?", "choix": ["print", "if", "int", "list"], "reponse": "if"}
            
        ],
        "difficile": [
            {"question": "Que fait la méthode .append() ?", "choix": ["Ajoute en début", "Ajoute à la fin", "Supprime", "Trie"], "reponse": "Ajoute à la fin"},
            {"question": "Quel type renvoie input() ?", "choix": ["int", "str", "bool", "float"], "reponse": "str"},
            {"question": "Quelle fonction convertit en entier ?", "choix": ["str()", "int()", "float()", "bool()"], "reponse": "int()"},
            {"question": "Quel mot pour une condition ?", "choix": ["when", "if", "for", "loop"], "reponse": "if"},
            {"question": "Comment gérer une exception ?", "choix": ["if/else", "try/except", "for/while", "raise/catch"], "reponse": "try/except"},
            {"question": "Quel est le résultat de bool('False') ?", "choix": ["False", "True", "None", "Erreur"], "reponse": "True"}
        ],
    }
}



def verifier_fichier_audio(nom):
    try:
        with open(nom, 'rb'):
            return True
    except:
        return False

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Multijoueur / Solo avec Chrono")
        self.mode_multijoueur = False
        self.theme_selectionne = None
        self.score_joueurs = [0, 0]
        self.joueur_actuel = 0
        self.noms_joueurs = ["Joueur 1", "Joueur 2"]
        self.niveau_index = 0
        self.niveaux = ["facile", "moyen", "difficile"]
        self.questions_melangees = []
        self.questions_restantes = []
        self.current_question_index = 0
        self.timer = None
        self.temps_restant = 15
        self.questions_repondue = 0
        self.bonnes_reponses = 0

        pygame.mixer.init()

        self.ecran_accueil()

    def ecran_accueil(self):
        self.effacer()
        tk.Label(self.root, text="Bienvenue dans le Quiz !", font=("Arial", 24), bg="lightblue").pack(pady=40)
        tk.Button(self.root, text="Solo", font=("Arial", 18), width=20, command=lambda: self.selection_mode(False)).pack(pady=5)
        tk.Button(self.root, text="Multijoueur", font=("Arial", 18), width=20, command=lambda: self.selection_mode(True)).pack(pady=5)

    def selection_mode(self, multijoueur):
        self.mode_multijoueur = multijoueur
        self.score_joueurs = [0, 0]
        self.joueur_actuel = 0
        self.niveau_index = 0

        self.effacer()

        if multijoueur:
            nom1 = simpledialog.askstring("Nom Joueur 1", "Nom du Joueur 1 :") or "Joueur 1"
            nom2 = simpledialog.askstring("Nom Joueur 2", "Nom du Joueur 2 :") or "Joueur 2"
            self.noms_joueurs = [nom1, nom2]
        else:
            nom = simpledialog.askstring("Nom", "Ton nom :") or "Joueur"
            self.noms_joueurs = [nom]

        tk.Label(self.root, text="Choisissez un thème", font=("Arial", 20)).pack(pady=20)
        for k, v in questions.items():
            tk.Button(self.root, text=v["nom"], font=("Arial", 16), width=20, command=lambda c=k: self.selectionner_theme(c)).pack(pady=5)

    def selectionner_theme(self, choix):
        self.theme_selectionne = choix
        theme = questions[choix]
        nom_theme = theme["nom"]
        if self.mode_multijoueur:
            self.questions_melangees = theme["facile"] + theme["moyen"] + theme["difficile"]
            random.shuffle(self.questions_melangees)
            self.questions_restantes = self.questions_melangees.copy()
        else:
            self.niveau_index = 0
            self.preparer_niveau()

        self.jouer_question()

    def preparer_niveau(self):
        niveau = self.niveaux[self.niveau_index]
        self.questions_restantes = questions[self.theme_selectionne][niveau][:]
        random.shuffle(self.questions_restantes)
        self.questions_repondue = 0
        self.bonnes_reponses = 0
        messagebox.showinfo("Niveau", f"Niveau {niveau.capitalize()}")

    def effacer(self):
        if self.timer:
            self.root.after_cancel(self.timer)
        for widget in self.root.winfo_children():
            widget.destroy()

    def jouer_question(self):
        self.effacer()

        if not self.questions_restantes:
            if self.mode_multijoueur:
                self.joueur_actuel += 1
                if self.joueur_actuel < 2:
                    self.questions_restantes = self.questions_melangees.copy()
                    self.jouer_question()
                else:
                    self.afficher_scores()
            else:
                if self.bonnes_reponses >= 3:
                    self.niveau_index += 1
                    if self.niveau_index < len(self.niveaux):
                        messagebox.showinfo("Bravo", "Tu as réussi ! Tu passes au niveau suivant.")
                        self.preparer_niveau()
                        self.jouer_question()
                    else:
                        messagebox.showinfo("Félicitations", "Tu as terminé tous les niveaux !")
                        self.ecran_accueil()
                else:
                    messagebox.showinfo("Échec", f"Tu n'as pas obtenu 3 bonnes réponses.\nTu dois refaire le niveau.")
                    self.preparer_niveau()
                    self.jouer_question()
            return

        self.question_actuelle = self.questions_restantes.pop(0)
        q = self.question_actuelle["question"]
        options = self.question_actuelle["choix"]

        self.temps_restant = 15

        joueur = self.noms_joueurs[self.joueur_actuel] if self.mode_multijoueur else self.noms_joueurs[0]

        self.label_timer = tk.Label(self.root, text=f"Temps restant : {self.temps_restant}", font=("Arial", 14), fg="red")
        self.label_timer.pack(pady=10)

        tk.Label(self.root, text=f"{joueur}", font=("Arial", 18), fg="blue").pack(pady=5)
        tk.Label(self.root, text=q, font=("Arial", 14), wraplength=500).pack(pady=10)

        for opt in options:
            tk.Button(self.root, text=opt, font=("Arial", 12),
                      command=lambda o=opt: self.repondre(o)).pack(pady=5)

        self.mise_a_jour_timer()

    def mise_a_jour_timer(self):
        self.temps_restant -= 1
        self.label_timer.config(text=f"Temps restant : {self.temps_restant}")
        if self.temps_restant <= 0:
            self.repondre(None)
        else:
            self.timer = self.root.after(1000, self.mise_a_jour_timer)

    def repondre(self, choix):
        if self.timer:
            self.root.after_cancel(self.timer)

        correcte = self.question_actuelle["reponse"]
        if choix is None:
            messagebox.showinfo("Temps écoulé", f"Temps écoulé ! La bonne réponse était : {correcte}")
        elif choix.lower() == correcte.lower():
            messagebox.showinfo("Bonne réponse", "Correct !")
            if not self.mode_multijoueur:
                self.bonnes_reponses += 1
            self.score_joueurs[self.joueur_actuel] += 1
        else:
            messagebox.showinfo("Mauvaise réponse", f"La bonne réponse était : {correcte}")

        if not self.mode_multijoueur:
            self.questions_repondue += 1

        self.jouer_question()

    def afficher_scores(self):
        score1, score2 = self.score_joueurs
        nom1, nom2 = self.noms_joueurs
        gagnant = "Égalité"
        if score1 > score2:
            gagnant = f"{nom1} gagne !"
        elif score2 > score1:
            gagnant = f"{nom2} gagne !"

        messagebox.showinfo("Résultats", f"{nom1} : {score1} pts\n{nom2} : {score2} pts\n{gagnant}")
        self.ecran_accueil()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()


