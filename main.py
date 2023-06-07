# Define a dictionary of books. Each genre has a list of book recommendations.
books = {
    "sci-fi": ["Dune by Frank Herbert", "Neuromancer by William Gibson", "Foundation by Isaac Asimov"],
    "fantasy": ["A Game of Thrones by George R. R. Martin", "The Hobbit by J.R.R. Tolkien", "Harry Potter by J.K. Rowling"],
    "mystery": ["The Girl with the Dragon Tattoo by Stieg Larsson", "Gone Girl by Gillian Flynn", "The Da Vinci Code by Dan Brown"],
    "non-fiction": ["Sapiens: A Brief History of Humankind by Yuval Noah Harari", "Quiet: The Power of Introverts in a World That Can't Stop Talking by Susan Cain", "The Immortal Life of Henrietta Lacks by Rebecca Skloot"],
    "romance": ["Pride and Prejudice by Jane Austen", "Outlander by Diana Gabaldon", "The Notebook by Nicholas Sparks"],
}

def recommend_books():
    # Ask the user for their preferred genre
    genre = input("Enter a genre (sci-fi, fantasy, mystery, non-fiction, romance): ")

    # Check if the entered genre exists in the dictionary
    if genre in books:
        # Print the book recommendations for the chosen genre
        print("Here are some book recommendations for the {} genre:".format(genre))
        for book in books[genre]:
            print("- " + book)
    else:
        print("Sorry, I don't have any recommendations for that genre.")

if __name__ == "__main__":
    recommend_books()
