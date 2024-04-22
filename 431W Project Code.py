import psycopg2

print("Welcome to the Database CLI Interface!\n")
print("Please select an option:")
print("1. Insert Data")
print("2. Delete Data")
print("3. Update Data")
print("4. Search Data")
print("5. Aggregate Functions")
print("6. Sorting")
print("7. Joins")
print("8. Grouping")
print("9. Subqueries")
print("10. Transactions")
print("11. Error Handling")
print("12. Exit\n")

conn = psycopg2.connect(database = "postgres", 
                        user = "postgres", 
                        host= 'localhost',
                        password = "Mitch1Sean2!",
                        port = 5432)
cur = conn.cursor()

while(True):
    query_selection = input("Enter your choice (1-12): ")
    
    if(query_selection == "1"): #Insert Data
        print("Follow the prompts to add a new NHL team")
        column1 = input("Enter the team ID: ")
        column2 = input("Enter the franchise ID: ")
        column3 = input("Enter the home city: ")
        column4 = input("Enter the team name: ")
        column5 = input("Enter the team abbrevation: ")
        query = "INSERT INTO public.team_info VALUES(" + column1 + ", " + column2 + ", '" + column3 + "', '" + column4 + "', '" + column5 +  "')"
        print(query)
        try:
            cur.execute(query)
            conn.commit()
            print("\n")
        except:
            print("*AN ERROR HAS OCCURED PLEASE CHECK YOUR INPUTS AND TRY AGAIN*\n")
 
    if(query_selection == "2"): #Delete Data
        print("Follow the prompts to delete a NHL team")
        condition = input("Enter the team ID: ")
        query = "DELETE FROM public.team_info WHERE \"team_id\" = " + condition
        print(query)
        try:
            cur.execute(query)
            conn.commit()
            print("\n")
        except:
            print("*AN ERROR HAS OCCURED DOUBLE CHECK YOUR INPUTS AND PLEASE TRY AGAIN*\n")
        
    if(query_selection == "3"): #Update Data
        print("Follow the prompts to update a player's weight")
        firstName = input("Enter the player's first name: ")
        lastName = input("Enter the player's last name: ")
        newWeight = input("Enter the player's new weight: ")
        query = "UPDATE public.player_info SET \"weight\" = " + newWeight + " WHERE \"firstName\" LIKE '" + firstName + "' AND \"lastName\" LIKE '" + lastName + "'"
        print(query)
        try:
            cur.execute(query)
            conn.commit()
            print("\n")
        except:
            print("*AN ERROR HAS OCCURED DOUBLE CHECK YOUR INPUTS AND PLEASE TRY AGAIN*\n")

    if(query_selection == "4"): #Search Data
        print("Follow the prompts to get information on players of a certain nationality")
        nationality = input("Enter the nationality of the players to search for: ")
        query = "SELECT * FROM public.player_info WHERE \"nationality\" = '" + nationality + "'"
        print(query)
        try:
            cur.execute(query)
            result = cur.fetchall()
            for row in result:
                print(row)
            print("\n")
        except:
            print("*AN ERROR HAS OCCURED DOUBLE CHECK YOUR INPUTS AND PLEASE TRY AGAIN*\n")

    if(query_selection == "5"): #Aggregate
        print("Follow the prompts to perform a aggregation on a team stat")
        stat = input("Enter the team stat for aggregation: ")
        aggregation = input("Enter the aggregation to perform on the team stat: ")
        if(aggregation == "summation"):
            aggregation = "SUM"
        if(aggregation == "average"):
            aggregation = "AVG"
        if(aggregation == "count"):
            aggregation = "COUNT"
        if(aggregation == "minimum"):
            aggregation = "MIN"
        if(aggregation == "maximum"):
            aggregation = "MAX"
        query = "SELECT " + aggregation + "(\"" + stat + "\") FROM public.game_team_stats"
        print(query)
        try:
            cur.execute(query)
            result = cur.fetchone()
            print(result)
            print("\n")
        except:
            print("*AN ERROR HAS OCCURED DOUBLE CHECK YOUR INPUTS AND PLEASE TRY AGAIN*\n")
    
    if(query_selection == "6"): #Sorting
        print("Follow the prompts to sort and get information on goalies")
        stat = input("Enter the stat to sort by: ")
        sort = input("Enter whether to sort in descending or ascending order: ")
        if(sort == "descending"):
            sort = "DESC"
        if(sort == "ascending"):
            sort = "ASC"
        query = "SELECT * FROM public.game_goalie_stats ORDER BY \"" + stat + "\" " + sort
        print(query)
        try:
            cur.execute(query)
            result = cur.fetchall()
            for row in range(0,10):
                if(row >= len(result)):
                    break
                print(result[row])
            print("\n")
        except:
            print("*AN ERROR HAS OCCURED DOUBLE CHECK YOUR INPUTS AND PLEASE TRY AGAIN*\n")

    if(query_selection == "7"): #Join
        print("Follow the prompts to get additional information on played games")
        join = input("Enter whether you want additional location or score information on played games: ")
        if(join == "location"):
            join = "location"
        if(join == "score"):
            join = "game_score"   
        query = "SELECT * FROM public.game JOIN public." + join + " ON public.game.game_id = public." + join + ".game_id"
        print(query)
        try:
            cur.execute(query)
            result = cur.fetchall()
            for row in range(0,10):
                if(row >= len(result)):
                    break
                print(result[row])
            print("\n")
        except:
            print("*AN ERROR HAS OCCURED DOUBLE CHECK YOUR INPUTS AND PLEASE TRY AGAIN*\n")

    if(query_selection == "8"): #Grouping
        print("Follow the prompts to count the number of players based a given characteristic: ")
        characteristic = input("Enter the characteristic to count: ")
        if(characteristic == "nationality"):
            characteristic = "nationality"
        if(characteristic == "birth city"):
            characteristic = "birthCity"
        if(characteristic == "primary position"):
            characteristic = "primaryPosition"
        if(characteristic == "height"):
            characteristic = "height"
        if(characteristic == "weight"):
            characteristic = "weight"
        query = "SELECT \"" + characteristic + "\", COUNT(*) FROM public.player_info GROUP BY \"" + characteristic + "\""
        print(query)
        try:
            cur.execute(query)
            result = cur.fetchall()
            for row in range(0,10):
                if(row >= len(result)):
                    break
                print(result[row])
            print("\n")
        except:
            print("*AN ERROR HAS OCCURED DOUBLE CHECK YOUR INPUTS AND PLEASE TRY AGAIN*\n")
        
    if(query_selection == "9"): #Subquery
        print("Follow the prompts to find NHL games where there were at least a certain # of goals scored: ")
        goals = input("Enter the the minimun number of goals scored in the game to search for: ")
        query = "SELECT game_id, COUNT(\"game_id\") FROM public.game_play WHERE \"play_id\" IN (SELECT \"play_id\" FROM public.game_goal)" \
        "GROUP BY \"game_id\" HAVING COUNT(\"game_id\") >= " + goals
        print(query)
        try:
            cur.execute(query)
            result = cur.fetchall()
            for row in range(0,10):
                if(row >= len(result)):
                    break
                print(result[row])
            print("\n")
        except:
            print("*AN ERROR HAS OCCURED DOUBLE CHECK YOUR INPUTS AND PLEASE TRY AGAIN*\n")

    if(query_selection == "10"): #Transaction
        print("Follow the prompts to update a player's primary position")
        firstName = input("Enter the player's first name: ")
        lastName = input("Enter the player's last name: ")
        newPosition = input("Enter the player's new primary position: ")
        query = "UPDATE public.player_info SET \"primaryPosition\" = '" + newPosition + "' WHERE \"firstName\" LIKE '" + firstName + "' AND \"lastName\" LIKE '" + lastName + "'"
        print(query)
        try:
            cur.execute(query)
            conn.commit()
            print("*TRANSACTION SUCCESSFUL*")
            print("\n")
        except:
            print("*AN ERROR HAS OCCURED DOUBLE CHECK YOUR INPUTS AND PLEASE TRY AGAIN*\n")

    if(query_selection == "11"): #Error Handling
        print("Follow the prompts to delete a NHL team")
        condition = input("Enter the team ID: ")
        query = "DELETE FROM public.team_info WHERE \"team_id\" = " + condition
        print(query)
        try:
            cur.execute(query)
            conn.commit()
            print("\n")
        except:
            print("*AN ERROR HAS OCCURED DOUBLE CHECK YOUR INPUTS AND PLEASE TRY AGAIN*\n")

    if(query_selection == "12"): #Exit
        print("Exiting the program")
        break

cur.close()
conn.close()

