print("Welcome to the match!")


yes_no = input("Are you a Fenerbahçe fan (yes/no)? ").lower()

if yes_no == "yes":
    print("Lets start!")
    lemos= input("Altay will pass to Lemos or Tisserand? (lemos/tisserand) ").lower()
    if lemos == "lemos":
        gustavo = input("Good choice. \n Who should Lemos pass? (gustavo/sosa) ").lower()
        if gustavo == "gustavo":
            ozan= input("Gustavo gets the ball, looks around and saw that both Perotti and Valencia are waiting for a pass. Also Ozan is coming closer to get the ball. Who should Gustavo pass? (perotti/valencia/ozan) ").lower()
            if ozan == "ozan": 
                perotti = input("Ozan gets the ball and quickly dribbles forward. He look up and sees that both Perotti and Valencia are running behind the defense. Who should Ozan pass? (perotti/valencia) ").lower()
                if perotti == "perotti":
                    ozaniki = input("Perotti gets the ball. Two defenders are waiting for him. He looks up and beats both defenders with Marseille Turn. He can either pass back to Ozan or he can cross it to Samatta. What should he do? (ozan/samatta) ").lower()
                    if ozaniki == "ozan":
                        print("Ozan gets the ball back, dribbles past a defender and shoots the ball from outside the penaty area and IT IS A WONDERFUL GOAL. Ozan scores just like the time he scored against Real Madrid. Fenerbahçe takes the lead with captain Ozan Tufan's goal...")

                    else:
                        print("The opponent gets the ball before Samatta does and the ball is secured.")    

                else: 
                    print("Ozan passes but while he was about to sprint Valencia gets injured and the ball goes out.")    
            else:
                print("Gustavo couldn't make that pass, you lost the ball and the opponent scored with a counter attack.")
        else:
            print("The opponent gets the ball before Sosa and scores with a counter attack.")        

    else:
        print("Tisserand lost the ball and the opponent scored.")    

else: 
    print("Bye loser.")
