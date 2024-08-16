"""
This script calculates the angle between two vectors using numpy
and logs the computation process for debugging purposes.

Author: Peter Chao
Date: August 4th, 2024

Usage:
    python align_calculate_angle.py
"""

import numpy as np
import logging

# Set up logging configuration
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def calculate_angle_between_vectors(vector1, vector2):
    """
    Calculates the angle between two vectors and logs the computation process.

    Args:
        vector1 (array-like): The first vector.
        vector2 (array-like): The second vector.

    Returns:
        float: The angle between the vectors in degrees.
    """
    # Log the vectors
    logging.debug(f"Vector1: {vector1}")
    logging.debug(f"Vector2: {vector2}")

    # Calculate the dot product
    dot_product = np.dot(vector1, vector2)
    logging.debug(f"Dot product: {dot_product}")

    # Calculate the magnitudes
    magnitude1 = np.linalg.norm(vector1)
    magnitude2 = np.linalg.norm(vector2)
    logging.debug(f"Magnitude of vector1: {magnitude1}")
    logging.debug(f"Magnitude of vector2: {magnitude2}")

    # Calculate the cosine of the angle
    cos_theta = dot_product / (magnitude1 * magnitude2)
    logging.debug(f"Cosine of the angle: {cos_theta}")

    # Handle potential floating point errors
    cos_theta = np.clip(cos_theta, -1.0, 1.0)
    logging.debug(f"Clipped cosine of the angle: {cos_theta}")

    # Calculate the angle in radians
    angle_radians = np.arccos(cos_theta)
    logging.debug(f"Angle in radians: {angle_radians}")

    # Convert the angle to degrees
    angle_degrees = np.degrees(angle_radians)
    logging.debug(f"Angle in degrees: {angle_degrees}")

    return angle_degrees

def main():
    # Define the vectors
    vector1 = np.array([1, 2, 3])
    vector2 = np.array([4, 5, 6])

    # Calculate the angle between the vectors
    angle_degrees = calculate_angle_between_vectors(vector1, vector2)

    # Create a box around the result
    result = f"The angle between the vectors is {angle_degrees:.2f} degrees"
    box_length = len(result) + 4
    print("Calculating the angle between the vectors...\n")
    print("+" + "-" * box_length + "+")
    print(f"|  {result}  |")
    print("+" + "-" * box_length + "+\n")

if __name__ == "__main__":
    main()
