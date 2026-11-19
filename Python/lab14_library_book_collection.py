# 1. Initial Data Setup
# List of tuples: (title, author, year, category)
books = [
    ("Python Crash Course", "Eric Matthes", "2019", "Programming"),
    ("Automate the Boring Stuff", "Al Sweigart", "2020", "Programming"),
    ("Artificial Intelligence: A Modern Approach", "Stuart Russell", "2021", "AI"),
    ("Clean Code", "Robert C. Martin", "2008", "Software Engineering")
]

# Extract initial unique categories into a set
library_categories = set()
for book in books:
    library_categories.add(book)

# Initialize student wishlist set with at least 4 requested genres
student_wishlist = {"AI", "Cloud Computing", "Robotics", "Cybersecurity"}

# Display Header
print("==========================================")
print("      LIBRARY BOOK & CATEGORY MANAGER     ")
print("==========================================")

# 2. Control Flow
while True:
    print("\nSelect an operation:")
    print("1. View Cataloged Books")
    print("2. Add New Book Record")
    print("3. View Unique Library Categories")
    print("4. Add Category to Student Wishlist")
    print("5. Run Category Gap Analysis")
    print("6. Exit")

    choice = input("\nEnter your choice (1-6): ")

    # Choice 1: View Books (using tuple unpacking)
    if choice == "1":
        print("\n--- Current Library Catalog (Fixed Records) ---")
        count = 1
        for book in books:
            title, author, year, category = book
            print(f"{count}. \"{title}\" by {author} ({year}) | Genre: {category}")
            count += 1
        print(f"Total Books: {len(books)}")

    # Choice 2: Add Book
    elif choice == "2":
        print("\n--- Add New Book Record ---")
        title = input("Enter book title: ")
        author = input("Enter author name: ")
        year = input("Enter publication year: ")
        category = input("Enter category/genre: ")

        # Check that all inputs are provided
        if title and author and year and category:
            new_book = (title, author, year, category)
            books.append(new_book)
            library_categories.add(category)

            print(f"\n[SUCCESS] \"{title}\" added as an immutable catalog record.")
            print(f"[INFO] Category set updated with: \"{category}\"")
        else:
            print("\n[ERROR] All fields are required. Book was not added.")

    # Choice 3: View Categories (sorted order)
    elif choice == "3":
        print("\n--- Unique Categories Available in Library (Set) ---")
        for cat in sorted(library_categories):
            print(f"- {cat}")
        print(f"Total Unique Genres: {len(library_categories)}")

    # Choice 4: Add to Wishlist
    elif choice == "4":
        print("\n--- Add to Student Wishlist ---")
        requested_genre = input("Enter requested category: ")
        student_wishlist.add(requested_genre)
        print(f"[SUCCESS] \"{requested_genre}\" added to student wishlist.")

    # Choice 5: Gap Analysis (Set Operations)
    elif choice == "5":
        print("\n============== CATEGORY GAP ANALYSIS ==============")
        print(f"Library Holdings (Set): {sorted(library_categories)}")
        print(f"Student Wishlist (Set): {sorted(student_wishlist)}")

        # Intersection (&): Already in stock
        in_stock = library_categories & student_wishlist
        print("\n1. Already in Stock (Intersection &):")
        print(f"   {sorted(in_stock)}")

        # Difference (-): Requested genres not yet in library
        purchase_needed = student_wishlist - library_categories
        print("\n2. Purchase Order Needed (Difference -):")
        print(f"   {sorted(purchase_needed)}")

        # Union (|): Complete combined genre coverage
        combined_coverage = library_categories | student_wishlist
        print("\n3. Full Combined Genre Coverage (Union |):")
        print(f"   {sorted(combined_coverage)}")

    # Choice 6: Exit
    elif choice == "6":
        print("\nThank you for using the Library Manager. Goodbye!")
        break

    # Invalid Choice Handling
    else:
        print("\n[ERROR] Invalid choice! Please enter a number between 1 and 6.")