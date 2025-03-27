from api import fetch_articles

from queue_articles import ArticleQueue
from stack_history import ArticleStack

def menu():
    queue = ArticleQueue()
    stack = ArticleStack()

    print("🔄 Chargement des articles...")
    articles = fetch_articles()
    for article in articles:
        queue.enqueue(article)

    while True:
        print("\n===== MENU =====")
        print("1. 📖 Lire un article")
        print("2. 🔙 Voir le dernier article lu")
        print("q. 🚪 Quitter")
        choix = input("Entrez votre choix (1-3): ")

        if choix == '1':
            if queue.is_empty():
                print("✅ Tous les articles ont été lus !")
            else:
                article = queue.dequeue()
                stack.push(article)
                print(f"\n🔹 {article[0]}")
                print(f"🔗 {article[1]}")
        elif choix == '2':
            if stack.is_empty():
                print("❌ Aucun article lu pour le moment.")
            else:
                last_read = stack.pop()
                print(f"\n🕘 Dernier article lu : {last_read[0]}")
                print(f"🔗 {last_read[1]}")
        elif choix == 'q':
            print("👋 Au revoir !")
            break
        else:
            print("❗ Entrée invalide. Choisissez entre 1, 2 ou 3.")

if __name__ == "__main__":
    menu()
