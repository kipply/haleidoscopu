type expr = 
  | Number of float 
  | Variable of string 
  | Binary of char * expr * expr
  | Call of string * expr array

