def outer(data, second_data):
    sd = second_data
    def inner():
        print(data, sd)
    return inner # note functionis returned without () but it can access data of its enclosed state 

if __name__ == "__main__":
    outer("hi", "two")()
    inner = outer("Hello", "Surendra !")
    inner()
