

reviews = [
    "This product is really good. I'm impressed with its quality.",
    "The performance of this product is excellent. Highly recommended!",
    "I had a bad experience with this product. It didn't meet my expectations.",
    "Poor quality product. Wouldn't recommend it to anyone.",
    "The product was average. Nothing extraordinary about it."
]


words_in_list = ["good", "excellent", "bad", "poor", "average"]



def review_list():
    for review in reviews:
        for keyword in words_in_list:
            if keyword in review:
                print(review.replace(keyword, keyword.upper()))
            elif keyword.capitalize() in review:
                print(review.replace(keyword.capitalize(), keyword.upper()))
    

review_list()




positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]

def positive_and_negative_words():
    for review in reviews:
        positive_count = 0
        negative_count = 0

        for positive in positive_words:
            if positive in review.lower():
                positive_count += review.lower().count(positive)
                
        for negative in negative_words:
            if negative in review.lower():
                negative_count += review.lower().count(negative)

        
        print(f"Review: \"{review}\"")
        print(f"Positive words: {positive_count}, Negative words: {negative_count}")
        print("-" * 50)



positive_and_negative_words()







def first_30_characters():
    review = input("Passing along but getting better at Python Programming also!")
    for review in reviews:
        if reviews[0:30:1]:
            print(f"{review} {reviews}")
            
            
first_30_characters()

    