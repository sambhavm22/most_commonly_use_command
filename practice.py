def greet():
    print("Hi There!")
    print("Welcome aboard")

greet()    

def greet(first_name: str, last_name: str) -> str:
    print(f"Hi There! {first_name} {last_name}")
    print("Welcome aboard")

greet(first_name="sambhav", last_name="mehta")    
