#Making a dictionary using dictionaries in python (it's a glossary...)
print ("Programming terms\n")
#5 programming terms as keys, and their meaning as values. All the terms are about data types.
g = { 
    "String" : "A data type used to present text in programming.", 
    "Integer" : "A data type used to present whole numbers in programming.",
    "Float" : "A data type used to present decimal numbers in programming.",
    "List" : "A mutable data type that is a sequence of several variables group together.",
    "Tuples" : "An immutable data type that stores a sequence of ordered items"
}

#making the output look "pretty". Using for loop so the code doesn't look crowded.
for p_terms, definition in g.items(): #variables: p_terms for the key & definition for the value
    print (f"{p_terms}:\n {definition}\n") #prints the term and the definition on diff. lines