from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from .serializers import UserRegistrationSerializer

from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)

from .forms import SignupForm

class UserRegistrationAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "User created successfully"}, status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(["POST"])
# @authentication_classes([])  # Allow unauthenticated requests.
# @permission_classes([])  # Allow unauthenticated requests.
# def signup(request):
#     """
#     Handles user registration (sign-up) via a POST request.

#     Args:
#         request: The HTTP request object.

#     Returns:
#         JsonResponse: JSON response indicating success or error.
#     """
#     data = request.data  # Extract data from the HTTP request.
#     print(data)
#     # Create a form instance with the provided data for validation.
#     form = SignupForm(
#         {
#             # Get the email address from the data.
#             "email": data.get("email"),
#             "name": data.get("name"),  # Get the user's name from the data.
#             # Get the first password from the data.
#             "password1": data.get("password1"),
#             # Get the second password from the data.
#             "password2": data.get("password2"),
#         }
#     )

#     if form.is_valid():
#         # If the form is valid, save the user registration data.
#         form.save()  # Save the user to the database. This should commit the change
#         message = "success"

#         # Additional logic to send a verification email can be added here.

#     else:
#         # If the form is not valid, there was an error during registration.
#         message = "error"

#     # Return a JSON response indicating success or error.
#     return JsonResponse({"message": message, "errors": form.errors})
