######## Εργαστήριο Τεχνητής Νοημοσύνης: Πρότζεκτ Φρούτμαν!
######## Συγγραφείς: Στέλιος Γιαννέλος [43828] - Λευτέρης Κετσεμενίδης [18390282]
######## Ημερομηνία Κατάθεσης: 22/11/2019
 
import copy                                     # φόρτωση της copy. χρησιμοποιούμε κυρίως την deepcopy για την αντιγραφή λιστών
from random import randrange                    # φόρτωση της random.randrange. την χρησιμοποιούμε για την παραγωγή τυχαίων αριθμών
from operator import itemgetter                 # φόρτωση της operator.itemgetter.randrange. την χρησιμοποιούμε για ταξινόμηση του μετώπου


def make_front(state):                          # συνάρτηση αρχικοποίησης μετώπου
    return [state]                              # δημιουργεί μέτωπο εισάγωντας το μέτωπο σε αυτό.


def print_state_list(state_list):               # συνάρτηση εκτύπωσης λίστας καταστάσεων - χρησιμοποιείται για το queue
    for state in state_list:                    # για κάθε κατάσταση στην λίστα
        print_state(state)                      # εκτυπώνουμε την κατάσταση καλώντας την print_state()
        print()                                 # αφήνουμε ένα κενό 


def expand_front(front, method):                # επέκταση μετώπου
    if method == 'DFS':                         # για DFS(Αναζήτηση κατά βάθος)
        if front:                               # αν υπάρχει μέτωπο                   
            # print("Front:")
            # print_state_list(front)
            node = front.pop(0)                 # αφαιρούμε από το μέτωπο την ΠΡΩΤΗ κατάσταση και την αποθηκεύουμε στο node
            for child in find_children(node):   # για κάθε καινούρια κατάσταση που δημιουργεί η ανάλυση της node
                front.insert(0,child)           # την προσθέτουμε στο μέτωπο
    
    elif method == 'BFS':                       # για BFS(Αναζήτηση κατα πλάτος)
        if front:                               # αν υπάρχει μέτωπο  
            # print("Front:")
            # print_state_list(front)
            node = front.pop(0)                 # αφαιρούμε από το μέτωπο την ΤΕΛΕΥΤΑΙΑ κατάσταση και την αποθηκεύουμε στο node
            for child in find_children(node):   # για κάθε καινούρια κατάσταση που δημιουργεί η ανάλυση της node
                front.append(child)             # την προσθέτουμε στο μέτωπο
    
    elif method == 'BestFS':                    # για BestFS(Αλγόριθμος καλύτερης πρώτης αναζήτησης
        if front:                               # αν υπάρχει μέτωπο                    
            # print("Front:")
            # print_state_list(front)
            node = front.pop(0)                 # αφαιρούμε από το μέτωπο την ΠΡΩΤΗ κατάσταση και την αποθηκεύουμε στο node
            for child in find_children(node):   # για κάθε καινούρια κατάσταση που δημιουργεί η ανάλυση της node
                front.insert(0,child)           # την προσθέτουμε στο μέτωπο

        front.sort(key = itemgetter('g'))       # ταξινόμιση του μετώπου σύμφωνα με το πόσα 'καλά φρούτα' έχουν μείνει
    return front                                # επιστροφή μετώπου


def make_queue(state):                          # αρχικοποίηση ουράς
    return [[state]]                            # επιστρέφουμε λίστα που περιέχει μια λίστα που περιέχει μια κατάσταση


def extend_queue(queue, method):                # επέκταση ουράς
    if method == 'DFS':                         # για DFS(Αναζήτηση κατά βάθος)
        # print("Queue:")
        # print(queue)
        node = queue.pop(0)                     # αφαιρούμε από την ουρά την ΠΡΩΤΗ κατάσταση και την αποθηκεύουμε στο node
        queue_copy = copy.deepcopy(queue)       # αντιγράφουμε την ουρά και τα περιεχόμενα της
        children = find_children(node[-1])      # βρίσκουμε τις επόμενες κατατάσεις του τελευταίου στοιχείου του node - τις θεωρούμε ως "παιδιά"
        for child in children:                  # για κάθε "παιδί"
            path = copy.deepcopy(node)          # θεωρούμε ως μονοπάτι το αντίγραφο του node
            path.append(child)                  # προσθέτουμε στο τέλος του μονοπατιού το "παιδί"
            queue_copy.insert(0,path)           # προσθέτουμε στην αρχή του αντιγράφου της ουράς το ανανεωμένο μονοπάτι
    
    elif method == 'BFS':                       # για BFS(Αναζήτηση κατα πλάτος)
        # print("Queue:")
        # print(queue)
        node = queue.pop(0)                     # αφαιρούμε από την ουρά την ΤΕΛΕΥΤΑΙΑ κατάσταση και την αποθηκεύουμε στο node
        queue_copy = copy.deepcopy(queue)       # αντιγράφουμε την ουρά και τα περιεχόμενα της
        children = find_children(node[-1])      # βρίσκουμε τις επόμενες κατατάσεις του τελευταίου στοιχείου του node - τις θεωρούμε ως "παιδιά"
        for child in children:                  # για κάθε "παιδί"
            path = copy.deepcopy(node)          # θεωρούμε ως μονοπάτι το αντίγραφο του node
            path.append(child)                  # προσθέτουμε στο τέλος του μονοπατιού το
            queue_copy.append(path)             # προσθέτουμε στην αρχή του αντιγράφου της ουράς το ανανεωμένο μονοπάτι

    elif method == 'BestFS':                    # για BestFS(Αλγόριθμος καλύτερης πρώτης αναζήτησης
        # print("Queue:")
        # print(queue)
        node = queue.pop(0)                     # αφαιρούμε από την ουρά την ΠΡΩΤΗ κατάσταση και την αποθηκεύουμε στο node
        queue_copy = copy.deepcopy(queue)       # αντιγράφουμε την ουρά και τα περιεχόμενα της
        children = find_children(node[-1])      # βρίσκουμε τις επόμενες κατατάσεις του τελευταίου στοιχείου του node - τις θεωρούμε ως "παιδιά"
        for child in children:                  # για κάθε "παιδί"
            path = copy.deepcopy(node)          # θεωρούμε ως μονοπάτι το αντίγραφο του node
            path.append(child)                  # προσθέτουμε στο τέλος του μονοπατιού το "παιδί"
            queue_copy.insert(0,path)           # προσθέτουμε στην αρχή του αντιγράφου της ουράς το ανανεωμένο μονοπάτι
    
        queue_copy.sort(key = lambda path: path[-1]['g']) # ταξινομούμε το αντίγραφο της ουράς με βάση το μονοποπάτι του οποίου η τελευταία κατάσταση (-1)
                                                          # η lambda με βοηθά να ορίσω με ποιό κλειδί θα σορτάρω τα παθς
                                                          #        
    return queue_copy                           # επιστρέφουμε την αναεωμένη ουρά


                                                       
def move_left(state):

    if state['grid'][state['position_x']][state['position_y'] - 1][2] != 'v':  # Αν το επόμενο κελί έχει εμετό, δεν μπορεί να πατήσει εκεί    
        state['grid'][state['position_x']][state['position_y']][0] = ' '       # Αφαιρούμε το πακμαν από το προηγούμενο κελί
        
        # Χρησιμοποιούμε την πράξη mod για να ορίσουμε την στήλη του επόμενου τετραγώνου - αν θα είναι μια θέση αριστερά, ή στην άλλη πλευρά
        # position mod N -> {0, 1, ..., N - 1} 

        state['position_y'] = (state['position_y'] - 1) % state['size']        # Αν βρίσκεται τέρμα αριστερά, τότε περνά στην απέναντι πλευρά με μαγικό τρόπο
        state['grid'][state['position_x']][state['position_y']][0] = 'p'       # Τοποθετείται το pacman
    
    return state

# Αντίστοιχα και οι επόμενες κινήσεις. Σε περίπτωση που το πακμαν βρίσκεται σε κάποιο όριο και πάει να το "υπερπηδήσε", τότε μεταφέρεται στην απέναντι πλευρά

def move_right(state):
    if state['grid'][state['position_x']][(state['position_y'] + 1) % state['size']][2] != 'v': # Αν το δεξιά κελί, έχει εμετό, τότε δεν μπορεί να πατήσει εκεί. Αν βρισκόμαστε στο τελευταίο από τα δεξιά κελί
                                                                                                # δηλαδή y+1=size, τότε η πράξη new_position=(y+1)%size θα μας δώσει 0.
        state['grid'][state['position_x']][state['position_y']][0] = ' '       # Αφαιρούμε το πακμαν από το προηγούμενο κελί
        
        state['position_y'] = (state['position_y'] + 1) % state['size']        # Υπολογίζουμε την νέα στήλη του πακμαν, σύμφωνα με τις γραμμές 109 και 110
        state['grid'][state['position_x']][state['position_y']][0] = 'p'       # Τοποθετούμε το πάκμαν στο επόμενο τετράγωνο, σύμφωνα με την γραμμή 113
    
    return state

def move_down(state):
    if state['grid'][(state['position_x'] + 1) % state['size']][state['position_y']][2] != 'v': # Αν το από κάτω κελί, έχει εμετό, τότε δεν μπορεί να πατήσει εκεί. Αν βρισκόμαστε στο τελευταίο προς τα κάτω κελί
        state['grid'][state['position_x']][state['position_y']][0] = ' '       # Αφαιρούμε το πακμαν από το προηγούμενο κελί
        
        state['position_x'] = (state['position_x'] + 1) % state['size']        # Υπολογίζουμε την νέα γραμμή του πακμαν, σύμφωνα με την γραμμή 119
        state['grid'][state['position_x']][state['position_y']][0] = 'p'       # Τοποθετούμε το πάκμαν στο επόμενο τετράγωνο, σύμφωνα με την γραμμή 122
    
    return state

def move_up(state):

    if state['grid'][state['position_x'] - 1][state['position_y']][2] != 'v':  # Αν το από πάνω κελί, έχει εμετό, τότε δεν μπορεί να πατήσει εκεί. Αν βρισκόμαστε στο πρώτο προς τα κάτω κελί
        state['grid'][state['position_x']][state['position_y']][0] = ' '       # Αφαιρούμε το πακμαν από το προηγούμενο κελί
        
        state['position_x'] = (state['position_x'] - 1) % state['size']        # Υπολογίζουμε την νέα γραμμή του πακμαν, σύμφωνα με την γραμμή 129 
        state['grid'][state['position_x']][state['position_y']][0] = 'p'       # Τοποθετούμε το πάκμαν στο επόμενο τετράγωνο, σύμφωνα με την γραμμή 132
    
    return state  

def eat(state):
    fruit_type = state['grid'][state['position_x']][state['position_y']][1]     # διαβάζουμε τον τύπο του φρούτου
    if fruit_type != ' ':
        if fruit_type == 'b':                                                   # Αν το φρούτο είναι χαλασμένο
            state['grid'][state['position_x']][state['position_y']][2] = 'v'    # Τότε το πάκμαν κάνει εμετό (v->vomit)

        state['grid'][state['position_x']][state['position_y']][1] = ' '        # Σε κάθε περίπτωση το φρούτο τρώγεται
        state[fruit_type] -= 1                                                  # Μειώνεται ο μετρητής του τύπου του φρούτου
    
    return state      


def find_children(state):                   # ορισμός συνάρτησης εύρεσης παιδιών

    # Σε περίπτωση που μετά την εφαρμογή του τελεστή μετάβασης (up,down,right,left,eat) η κατάσταση έχει αλλάξει, τότε και μόνο τότε την προσθέτουμε στην λίστα με τα παιδιά (στο τέλος)
    # πριν από κάθε κίνηση, αντιγράφουμε την παρούσα κατάσταση, εφαρμόζουμε την παράγωγη κατάσταση στο αντίγραφο

    children = []

    right_state = copy.deepcopy(state)    # 1. Δημιουργώ αντίγραφο του state, και το αποθηκεύω στο right_state  
    child_right = move_right(right_state) # 2. Εφαρμόζω τον τελεστή μετάβασης move_right στο right_state και το αποθηκεύω στο child_right
                                            # τώρα το child_right κρατά την κατάσταση όπου στο state έχει εφαρμοστεί η move_right
    if not child_right == state:          # 3. Αν η νέα κατάσταση child_right ΔΕΝ ΕΙΝΑΙ ίδια με την αρχική προηγούμενη κατάσταση (state),
        children.append(child_right)      # 4. Τότε την προσθέτουμε στον πίνακα με τις νέες καταστάσεις που προέκυψαν (children)

    # Αντίστοιχα

    left_state = copy.deepcopy(state)       
    child_left = move_left(left_state)
    if not child_left == state:           
        children.append(child_left)

    up_state = copy.deepcopy(state) 
    child_up = move_up(up_state)
    if not child_up == state:   
        children.append(child_up)

    down_state = copy.deepcopy(state) 
    child_down = move_down(down_state)
    if not child_down == state:
        children.append(child_down)

    eat_state = copy.deepcopy(state)
    child_eat = eat(eat_state)  
    if not child_eat == state: 
        children.append(child_eat)

    return children   



def is_goal_state(state):   # Δεχόμαστε την κατάσταση στόχου
    return not state['g']   # Επιστρέφουμε ότι φτάσαμε τον στόχο αν δεν υπάρχουν καθόλου καλά φρούτα (g)
   

def find_solution(front, queue, closed, method):    # ορισμός αναδρομικής συνάρτησης δημιουργίας δέντρου αναζήτησης
    if not front:                                   # κενό μέτωπο σημαίνει πως ξεμείναμε από πιθανές καταστάσεις - αδιέξοδο 
        print("_NO_SOLUTION_FOUND_")
    
    elif front[0] in closed:                        # αν η πρώτη κατάσταση του μετώπου βρίσκεται στο κλειστό μέτωπο - άρα έχει εξερευνηθεί
        new_front = copy.deepcopy(front)        
        new_front.pop(0)                            # την αφαιρούμε από το μέτωπο
        new_queue = copy.deepcopy(queue)
        new_queue.pop(0)                            # την αφαιρούμε από το μέτωπο

        find_solution(new_front, new_queue, closed, method) # αναδρομική κλήση με νέα ουρά και μέτωπο
    
    elif is_goal_state(front[0]):                   # έλεγχος αν  η πρώτη κατάσταση του μετώπου είναι goal state
        print_state_list(queue[0])                  # εκτύπωσε το αντίστοιχο στοιχείο της ουράς, που δείχνει όλα τα βήματα μέχρι τον στόχο
        print("GOAL_FOUND :) ALL GOOD FRUIT WERE EATEN" )
        print("NUMBER OF MOVES:", len(queue[0]))                        
    
    else:
        closed.append(front[0])                             # αλλιώς, πρόσθεσε την κατάσταση στο κλειστό μέτωπο, επειδή έχει εξερευνηθεί επαρκώς
        front_copy = copy.deepcopy(front)                   # αντιγραφή μετώπου
        front_children = expand_front(front_copy, method)   # προσθήκη παιδιών του μετώπου στο μέτωπο
        queue_copy = copy.deepcopy(queue)                   # αντιγραφή ουράς
        queue_children = extend_queue(queue_copy, method)   # προσθήκη παιδιών του της ουράς στην ουρά
        closed_copy = copy.deepcopy(closed)                 # αντιγραφή κλειστού μετώπου
        find_solution(front_children, queue_children, closed_copy, method) # αναδρομική κλήση
        

def print_state(state):                     # ορίζουμε συνάρτηση για την όμορφή εκτύπωση κατάστασης
    print("Good fruit: ", state['g'])       # τυπώνουμε το σκορ μεταξύ καλών και κακών φρούτων
    print("Bad fruit:  ", state['b'])
    
    N = state['size']

    for i in range(N):
        for j in range(N):
            print(state['grid'][i][j], end = ' ') # τυπώνουμε το γκριντ χωρισμένο με κενό ' ' αντί για κόμα ,
        
        print()                                   # αφήνουμε κενή γραμμή για ομορφιά

def main():
    
    N = int(input("Enter grid size: "))                          # Εισαγω΄γή πλευράς του ταμπλό
    F = min(int(input("Enter number of fruit: ")), N * N // 2)   # Εισαγωγή αριθμού τον φρούτων. Για απλούστευση των καταστάσεων, δεχόμαστε μέχρι 
                                                                 # N*N//2 ακέραιο αριθμό φο΄΄υτων. Στην παρούσα φάση δεν γίνεται έλεγχος στην είσοδο.
   
    # Όταν ο χρήστης δώσει 0,1,2 αυτό αντιστοιχίζεται στον ανάλογο αλγόριθμο. Όσο δεν εισάγει κάποιον από τους παραπάνω αριθμούς
    # τότε ξαναεμφανίζουμε το αρχικό μήνυμα και ζητάμε την είσοδο του.
   
    method = ''
    while not method:
        inp = int(input("Enter search method: \n" + "\t0: BFS\n" + "\t1: DFS\n" + "\t2: BestFS\n" + "= ")) # Τα εμφανίζουμε με κομψό τρόπο
        if inp >= 0 and inp < 3:
            method = ['BFS', 'DFS', 'BestFS'][inp] # 0 = BFS, 1 = DFS, 2 = BestFS


#####!!!!!! ΔΕΝ ΧΡΗΣΙΜΟΠΟΙΟΥΜΕ ΤΟ ΤΥΧΑΙΟΠΟΙΗΜΕΝΟ ΙΝΙΤΙΑL STATE, ΕΠΕΙΔΗ ΘΕΛΟΥΜΕ ΕΝΑ ΣΥΓΚΕΚΡΙΜΕΝΟ ΓΙΑ ΝΑ ΤΡΕΞΟΥΜΕ ΤΑ ΤΕΣΤ

# δημιουργούμε ένα dictionary που θα κρατά όλα τα χρήσιμα στοιχεία του state
# σε κάθε νέα κατάσταση, θα κρατάμε μεταξύ άλλων την θέση του πακμαν ώστε να μην το ψάχνουμε κάθε φορά με 2 for

    initial_state = {                                                       
        'grid': [[[' ', ' ', ' '] for i in range(N)] for i in range(N)],    # αρχικοποίηση grid
        'g': 0,              # αρχικοποίηση μετρητή καλών φρούτων
        'b': 0,              # αρχικοποίηση μετρητή κακών φρούτων
        'size': N,           # τελεστής πλευράς (για να μην γράφουμε len(state)) κλπ
        'position_x': N-1,   # αρχικοποίηση της μεταβλητής που κρατάμε την θέση του πάκμαν ανα γραμμή
        'position_y': 0      # αρχικοποίησητης μεταβλητής που κρατάμε την θέση του πάκμαν ανα στήλη
    }
    
    grid = initial_state['grid']       
    grid[N - 1][0][0] = 'p'         # τοποθέτηση του πακμαν

    n = 0
    THRESHOLD_OF_BAD_FRUIT = 50     # δίνουμε πιθανότητα 50% ένα φρο΄ύτο να είναι "καλό" ή "κακό"
    while n < F:
        x = randrange(0, N)         # επιλέγουμε τυχαία γραμμή από 0 έως N-1 
        y = randrange(0, N)         # επιλέγουμε τυχαία στήλη από 0 έως N-1 

        # παρακάτω, παράγουμε έναν τυχαίο αριθμό και αν είναι μικρότερος από την πιθανότητα THRESHOLD, τότε είναι "καλό" φρούτο. Αν όχι, τότε "κακ΄ό"

        is_bad = ['g', 'b'][randrange(0, 100) > THRESHOLD_OF_BAD_FRUIT] 
        
        if grid[x][y][1] == ' ':        # σε περίπτωση που δεν υπάρχει ήδη φρούτο στο τετράγωνο
           grid[x][y][1] = is_bad       # τοποθετούμε το φρούτο
           initial_state[is_bad] += 1   # αυξάνουμε είτε τον μετρήτη καλών φρούτων είτε τον μετρητή των κακών φρούτων, ανάλογα με το φρούτο
           n += 1
#####!!!!!!

# Εδώ ορίζουμε το initial state με το χέρι, για να μπορέσουμε να τρέξουμε γρήγορα τα test αποδοτικότητας των αλγορίθμων

    initial_state = {
        'grid' :    [[[' ', 'b', ' '], [' ', 'b', ' '], [' ', 'g', ' ']], # αρχικοποίηση grid
                     [[' ', 'b', ' '], [' ', 'b', ' '], [' ', 'g', ' ']],
                     [['p', 'b', ' '], [' ', 'b', ' '], [' ', 'b', ' ']]],
        'g': 2,             # αρχικοποίηση μετρητή καλών φρούτων                     
        'b': 7,             # αρχικοποίηση μετρητή κακών φρούτων        
        'size': 3,          # τελεστής πλευράς (για να μην γράφουμε len(state)) κλπ  
        'position_x': 2,    # αρχικοποίηση της μεταβλητής που κρατάμε την θέση του πάκμαν ανα γραμμή
        'position_y': 0     # αρχικοποίησητης μεταβλητής που κρατάμε την θέση του πάκμαν ανα στήλη

    }

    print("____BEGIN__SEARCHING____\n")
    find_solution(make_front(initial_state), make_queue(initial_state), [], method) # Τρέχουμε την find solution
        

if __name__ == "__main__":
    main()

