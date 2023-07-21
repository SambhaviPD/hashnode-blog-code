from fastapi import FastAPI

from marvin import ai_fn
from marvin import ai_classifier

from enum import Enum

app = FastAPI()

@app.get("/")
async def root():
    return { "message" : "Welcome to BookReview APIs"}


@ai_fn
def book_review(name_of_book: str, author: str) -> str:
    """
    Given name of a book and author, return a review of the book
    """

@app.get("/book_review")
async def get_book_review(name_of_book: str, author: str):
    review = book_review(name_of_book, author)
    return review


@ai_fn
def book_genre(name_of_book: str, author: str) -> str:
    """
    Given name of a book and author, return multiple genres of the book
    """

@app.get("/book_genre")
async def get_book_genre(name_of_book: str, author: str):
    genres = book_genre(name_of_book, author)
    return genres


@ai_classifier
class BookReviewSentiment(Enum):
    """
    Classifies incoming book reviews
    """
    POSITIVE = "Positive"
    NEGATIVE = "Negative"
    NEUTRAL = "Neutral"
    ENTHUSIASTIC = "Enthusiastic"
    CRITICAL = "Critical"
    INDIFFERENT = "Indifferent"
    APPRECITATIVE = "Appreciative"
    DISAPPROVING = "Disapproving"


@app.get("/book_review_classifier")
async def get_book_review_classifier(review: str):
    sentiment = BookReviewSentiment(review)
    return sentiment

