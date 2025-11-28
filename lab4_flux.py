def lancer_application_notes(max_notes=5):
    seuil_admission = 10
    notes = []

    while len(notes) < max_notes:
        
        compteur = f"{len(notes) + 1}/{max_notes}"
        saisie = input(f"Note étudiant {compteur} : ").strip()

        if saisie.lower() == "stop":
            print("Arrêt volontaire de la saisie.")
            break 
        
        try:
            note = float(saisie)
            
            if note < 0 or note > 20:
                print("Erreur : La note doit être entre 0 et 20.")
                continue 
            
            notes.append(note)
            
        except ValueError:
            print("Erreur : Ce n'est pas un nombre valide.")
            continue 
    else:
        print("Capacité maximale atteinte. Saisie terminée.")

    print("\n" + "="*35)
    print(f"BILAN DE LA CLASSE ({len(notes)} notes)")
    print("="*35)

    if not notes:
        print("Aucune donnée à traiter.")
        return 

    for i, note in enumerate(notes, start=1):
        statut = "ADMIS" if note >= seuil_admission else "REFUSÉ"
        print(f"Étudiant {i} : {note:05.2f} / 20 → {statut}")

    print("-" * 35)
 
    moyenne_classe = sum(notes) / len(notes)
    print(f"Moyenne générale : {moyenne_classe:.2f} / 20")

    if moyenne_classe >= 16:
        print("Appreciation : Excellente classe (Très Bien)")
    elif moyenne_classe >= 14:
        print("Appreciation : Bonne classe (Bien)")
    elif moyenne_classe >= 12:
        print("Appreciation : Classe correcte (Assez Bien)")
    elif moyenne_classe >= 10:
        print("appreciation : Niveau moyen (Passable)")
    else:
        print("appreciation : Niveau fragile (Insuffisant)")

lancer_application_notes(max_notes=5)
        