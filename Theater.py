name = input("Name of the movie: ")  

movies = {"Jawan": 109, "Tiger Zinda Hai": 40,"Avatar":1000}  
timing = {"Jawan": "1pm to 2pm", "Tiger Zinda Hai": "3pm to 5pm","Avatar":"6pm to 7pm"}  

# Print the movie price and timing  
if name in movies:  
    print(f"{name} = ₹{movies[name]}")  
    print(f"Timing: {timing[name]}")  
else:  
    print(f"Sorry, {name} is not in the list.")  
