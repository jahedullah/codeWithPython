#solu 1
def findMaxGuests(arrl, exit, n):

    # Sort arrival and exit arrays
    arrl.sort();
    exit.sort();

    # guests_in indicates number of
    # guests at a time
    guests_in = 1;
    max_guests = 1;
    time = arrl[0];
    i = 1;
    j = 0;

    # Similar to merge in merge sort to
    # process all events in sorted order
    while (i < n and j < n):
        print (i,j)

        # If next event in sorted order is
        # arrival, increment count of guests
        if (arrl[i] < exit[j]):

            guests_in = guests_in + 1;

        # Update max_guests if needed
            if(guests_in > max_guests):

                max_guests = guests_in;
                time = arrl[i];

            # increment index of arrival array
            i = i + 1;

        elif (arrl[i] == exit[j]):
            i+=1
            j+=1

        else:
            guests_in = guests_in - 1;
            j = j + 1;

    print("Maximum Number of chairs =",
           max_guests)

S = [1, 2, 6, 5, 3]
E = [5, 5, 7, 6, 8]
findMaxGuests(S,E,5)


#solu 2
# Program to find maximum guest
# at any time in a party
def findMaxGuests(arrl, exit, n):

    # Sort arrival and exit arrays
    arrl.sort();
    exit.sort();

    # guests_in indicates number of
    # guests at a time
    guests_in = 1;
    max_guests = 1;
    time = arrl[0];
    i = 1;
    j = 0;

    # Similar to merge in merge sort to
    # process all events in sorted order
    while (i < n and j < n):
        

        # If next event in sorted order is
        # arrival, increment count of guests
        if (arrl[i] <= exit[j]):

            guests_in = guests_in + 1;
        # Update max_guests if needed
            if(guests_in > max_guests):

                max_guests = guests_in;
                time = arrl[i];

            # increment index of arrival array
            i = i + 1;

        else:
            guests_in = guests_in - 1;
            j = j + 1;

    print("Maximum Number of Guests =",
           max_guests, "at time", time)

arr= [1, 2, 10, 5, 5]
dep= [4, 5, 12, 9, 12]
findMaxGuests(arr,dep,5)
