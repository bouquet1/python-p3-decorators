def check_movie_time(func):
    def wrapper(time):
        if 1200 < time < 2200:
            func(time)
        else:
            print("Sorry, the theater is closed now.")
    return wrapper


@check_movie_time
def sell_tickets(time):
    print("Please choose the movie")


@check_movie_time
def take_orders(time):
    print("What can I get for you?")


@check_movie_time
def clean_theater(time):
    print("Cleaning is in process")


sell_tickets(2300)
take_orders(1400)
take_orders(2300)
clean_theater(1400)
clean_theater(2300)
