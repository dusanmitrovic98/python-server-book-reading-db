from flask import Blueprint, request, jsonify
from app.models.chapter import Chapter

chapter_routes = Blueprint('chapter_routes', __name__)

@chapter_routes.route('/chapters/<chapter_id>', methods=['GET'])
def get_chapter_content(chapter_id):
    # Find the chapter by its ID
    chapter = Chapter.objects(id=chapter_id).first()

    if not chapter:
        return jsonify({'message': 'Chapter not found'}), 404

    # Return the chapter content
    return jsonify({
        'title': chapter.title,
        'content': chapter.content,
        'order': chapter.order
    })
