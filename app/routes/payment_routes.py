from flask import Blueprint, request, jsonify
from app.models.payment import Payment
from app.models.user import User

payment_routes = Blueprint('payment_routes', __name__)

@payment_routes.route('/make_payment', methods=['POST'])
def make_payment():
    # Get user data from the request, including the user's ID
    data = request.get_json()
    user_id = data.get('user_id')

    # Check if the user exists
    user = User.objects(id=user_id).first()
    if not user:
        return jsonify({'message': 'User not found'}), 404

    # Get payment details from the request (e.g., amount, payment method)
    amount = data.get('amount')
    payment_method = data.get('payment_method')

    if not amount or not payment_method:
        return jsonify({'message': 'Amount and payment method are required'}), 400

    # Implement payment processing (e.g., charge the user's account via a payment gateway)
    # You should use a payment gateway library or API for this
    # Once payment is successfully processed, create a payment record
    payment = Payment(user=user, amount=amount, paymentMethod=payment_method)
    payment.save()

    return jsonify({'message': 'Payment successful'})
