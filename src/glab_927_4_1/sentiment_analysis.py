
# GLAB 927.4.1 - Hands-On Sentiment Analysis With Python
# Task 1: Import and test the TextBlob library

# Import TextBlob to work with text and analyze sentiment.
from textblob import TextBlob

# Create a sample sentence to confirm TextBlob works.
sample_text = "TextBlob is successfully installed and ready to use!"

# Convert the sentence into a TextBlob object.
blob = TextBlob(sample_text)

# Display the sentence.
print(blob)


# Task 2: Analyze sentiment in customer feedback

# Sample customer review
customer_review = (
    "I absolutely love this product! "
    "The quality is excellent and it arrived on time."
)

# Create a TextBlob object for the review
review_blob = TextBlob(customer_review)

# Calculate sentiment scores
polarity = review_blob.sentiment.polarity
subjectivity = review_blob.sentiment.subjectivity

# Display the original review and its sentiment scores
print("\nTask 2: Customer Review Sentiment Analysis")
print("Review:", customer_review)
print("Polarity:", polarity)
print("Subjectivity:", subjectivity)


# Task 3: Analyze sentiment in multiple customer reviews

# Store customer feedback in a list.
customer_comments = [
    "The service was fantastic and the staff was very helpful.",
    "I am unhappy with the product quality and delivery was delayed.",
    "The product is okay, but it could be improved.",
    "Amazing experience! I am very satisfied with my purchase."
]

# Analyze each customer comment.
print("\nTask 3: Multiple Customer Review Analysis")

for comment in customer_comments:
    # Create a TextBlob object for the current comment.
    blob = TextBlob(comment)

    # Calculate the polarity score.
    polarity = blob.sentiment.polarity

    # Display the comment and its polarity.
    print("\nCustomer Review:", comment)
    
    print(f"Polarity: {polarity:.2f}")


# Analysis and Observations:
# The positive reviews received positive polarity scores.
# The unhappy customer review received a negative score (-0.60).
# The review saying "okay, but it could be improved" scored
# positive (0.50), even though it contains mixed feedback.
#
# This shows that TextBlob can identify general sentiment,
# but it may not fully understand context or mixed opinions.
# Human review can help interpret ambiguous results.
