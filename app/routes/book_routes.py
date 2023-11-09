from flask import Blueprint, request, jsonify
from app.models.book import Book

book_routes = Blueprint('book_routes', __name__)

@book_routes.route('/books/<book_id>', methods=['GET'])
def get_book_details(book_id):
    # Find the book by its ID
    book = Book.objects(id=book_id).first()

    if not book:
        return jsonify({'message': 'Book not found'}), 404

    # Return the book data
    return jsonify({
        'title': book.title,
        'author': book.author,
        'description': book.description,
        'publication_date': book.publication_date
        # Add other book attributes as needed
    })

@book_routes.route('/books/search', methods=['GET'])
def search_books():
    # Get search parameters from the request
    query = request.args.get('query')

    if not query:
        return jsonify({'message': 'Query parameter is required'}), 400

    # Implement book search logic (example: searching by title or author)
    # You can adjust the search criteria based on your database model
    books = Book.objects(title__icontains=query) | Book.objects(author__icontains=query)

    if not books:
        return jsonify({'message': 'No matching books found'}), 404

    # Return a list of matching books
    book_list = []
    for book in books:
        book_list.append({
            'id': str(book.id),
            'title': book.title,
            'author': book.author
            # Add other book attributes as needed
        })

    return jsonify({'message': 'Matching books found', 'books': book_list})
