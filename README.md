# Text images processing
## A very simple program to process text matrices with images operations

This project implements command line operations from the user so it works
with multidimensional lists as images. These operations are simple manipulations
of values on these lists, in such a way that it is possible to interpret them
as images representations.

The supported operations are the following:


* I M N

    Initialize an empty (zero-valued) MxN ( colsXrows ) matrix.  
    Here, the value zero is defined by the letter 'O' not the         
    number 0. Also, be aware that this command does not follow   
    the common matrices dimension convention, which is rowsXcols 
                                                                                    
* C
 
    Sets the current matrix values to zero                          
                                                                                    
* L X Y C

    Set matrix position (X,Y) with value C                          
                                                                                    
* V X Y1 Y2 C

    Sets matrix positions (X, Y1-Y2) with value C                   
                                                                                    
* H X X1 Y2 C

    Sets matrix positions (X1-X2, Y) with value C                   
                                                                                    
* K X1 Y1 X2 Y2 C

    Sets a rectangular region, with bounds (X1,Y1) for        
    top-left corner and (X2,Y2) to bottom-right corner        
                                                                                    
* F X Y C

    Fills a region with value C. A region is defined by the X,Y       
    position with value C and neighbor zero valued (O) positions,  
    both horizontaly and verticaly.                                   
                                                                                    
* S filename

    Saves the matrix to a file with name "filename"                 
                                                                                    
* X

    Exits the program


## Sample inputs

**Sample inputs 1**

```
  I 5 6
  L 2 3 A
  S one.bmp
  G 2 3 J
  V 2 3 4 W
  H 3 4 2 Z
  F 3 3 J
  S two.bmp
  X
```

**Outputs**

```
  one.bmp
  OOOOO
  OOOOO
  OAOOO
  OOOOO
  OOOOO
  OOOOO

  two.bmp
  JJJJJ
  JJZZJ
  JWJJJ
  JWJJJ
  JJJJJ
  JJJJJ
```

**Sample inputs 2**

```
  I 10 9
  L 5 3 A
  G 2 3 J
  V 2 3 4 W
  H 1 10 5 Z
  F 3 3 J
  K 2 7 8 8 E
  F 9 9 R
  S one.bmp
  X
```

**Outputs**

```
  one.bmp
  JJJJJJJJJJ
  JJJJJJJJJJ
  JWJJAJJJJJ
  JWJJJJJJJJ
  ZZZZZZZZZZ
  RRRRRRRRRR
  REEEEEEERR
  REEEEEEERR 
  RRRRRRRRRR
```
