import os

def create_dir():
    print("======Create 100 Days of Code Working directory======")
    day = int(input("Enter Day (Please Enter a number): "))
    filename = f"100DOCDay{day}"
    
    try:
        os.mkdir(filename)
        with open(f"{filename}/main.py", 'w') as file:
            path = f"{filename}/main.py"
            print(f"This path: '{path}' has been created.")
    except FileExistsError:
        print("File already exists")
        create_dir()
    finally:
        os.system(f'cd {filename}')


create_dir()