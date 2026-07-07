color=input("Enter color ")
match color:
    case "Green":
        print("go")
    case "Yellow":
        print("slow")
    case "Red":
        print("stop")
    case _:
        print("invalid")
