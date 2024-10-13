"""PyPoll Homework Starter File."""

# Import necessary modules
import os
import csv

# Files to load and output (update with correct file paths)
file_to_load=os.path.join("Resources", "election_data.csv")
file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast
candidate_list=[] #Track the list of candidates
candidate_count=[] # Track the vote_count of each candidate

# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:

        # Print a loading indicator (for large datasets)
        #print(". ", end="")

        # Increment the total vote count for each row
        total_votes+=1
        # Get the candidate's name from the row
        c_name=row[2]

        # If the candidate is not already in the candidate list, add them
        if c_name not in candidate_list:
            candidate_list.append(c_name)
            candidate_count.append(0)

        # Add a vote to the candidate's count
        c_index=candidate_list.index(c_name)
        candidate_count[c_index]=candidate_count[c_index]+1

# Open a text file to save the output
with open(file_to_output, "w") as txt_file:

    # Print the total vote count (to terminal)
    print("Election Results")
    print("------------------------------------")
    print(f"Total Votes: {total_votes}")
    print("------------------------------------")


    # Write the total vote count to the text file
    txt_file.write(f"Election Results\n")
    txt_file.write(f"------------------------------------\n")
    txt_file.write(f"Total Votes: {total_votes}\n")
    txt_file.write(f"------------------------------------\n")


    # Loop through the candidates to determine vote percentages and identify the winner
    winner_count = candidate_count[0]
    for i in range(3):
        
        # Get the vote count and calculate the percentage
        per = round((candidate_count[i]/total_votes*100),3)
        
        # Update the winning candidate if this one has more votes
        if winner_count<candidate_count[i]:
            winner_count=candidate_count[i]

        # Print and save each candidate's vote count and percentage
        print(f'{candidate_list[i]}:{per}% ({candidate_count[i]})')
        txt_file.write(f'{candidate_list[i]}:{per}% ({candidate_count[i]})\n')

    # Generate and print the winning candidate summary
    
    w_index=candidate_count.index(winner_count)
    winner=candidate_list[w_index]
    print(f"------------------------------------")
    print(f"Winner:{winner}")
    print(f"------------------------------------")
    # Save the winning candidate summary to the text file
    txt_file.write(f"------------------------------------\n")
    txt_file.write(f"Winner:{winner}\n")
    txt_file.write(f"------------------------------------\n")
