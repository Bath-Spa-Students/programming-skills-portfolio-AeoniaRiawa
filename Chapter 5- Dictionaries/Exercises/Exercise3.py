Terms = { 'List' :' A collection of values ',
           'Int' :' Assigns a variable  and interger ',
           'Dictionary' :' A collection of keys and values ' ,
           'Strings': ' A sequence of characters ',
           'Print': ' To print or to output a certain character ',
           'Comment': ' A note left by the programmer for others or himself ',
           'If':' A statement that would check a condition',
           'Else':' When the "if" and "elif" comes to false Else would activate ',
           'Elif':' Is "Else if" which basically means that "if" comes false it would check for an alternative',
           'Index':' A position of a certain item in a list',           }
for word, definition in Terms.items():
    print({word},{definition})
# or to make it look better i found this 
for word, definition in Terms.items():
    print(f"\n{word.title()}:{definition}")
