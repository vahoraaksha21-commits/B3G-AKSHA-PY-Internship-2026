library={
    101:{"title":"python","author": "ABC","copies":5},
    102:{"title":"java","author":"XYZ","copies":3},
    103:{"title":"c++","author":"PQR","copies":4}
}
Book_ID=101
library[Book_ID]["copies"] = library[Book_ID]["copies"]-1
print(library)