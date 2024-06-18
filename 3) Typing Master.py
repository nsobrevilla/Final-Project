
import time

def calculate_accuracy(original_text, typed_text):
    correct_chars = sum(1 for x, y in zip(original_text, typed_text) if x == y)
    total_chars = len(original_text)
    accuracy = (correct_chars / total_chars) * 100
    return accuracy

def typing_challenge(text):
    print("Welcome to Typing Master!")
    print("Type the following text:")
    print(text)
    
    input("Press Enter when you are ready to start...")
    
    start_time = time.time()
    user_input = input("Start typing: ")
    end_time = time.time()
    
    typing_time = end_time - start_time
    words_per_minute = len(text.split()) / (typing_time / 60)
    
    accuracy = calculate_accuracy(text, user_input)
    
    print("\nTyping speed: {:.2f} words per minute".format(words_per_minute))
    print("Accuracy: {:.2f}%".format(accuracy))

if __name__ == "__main__":
    text_to_type = "The quick brown fox jumps over the lazy dog."
    typing_challenge(text_to_type)

