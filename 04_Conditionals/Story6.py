seat_type=input("Enter Seat type (sleeper/AC/general/luxury): ").lower()

match seat_type:
    case "sleeper":
        print("Sleeper type seat ")
    case "ac":
        print("AC-costs extra")
    case "general":
        print("Cheapest")
    case "luxury": 
        print("comfortable journey")
    case _:
        print("Invalid input")