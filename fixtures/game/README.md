# Connect-4

**Downloaded from the UCI Machine Learning Repository on May 4, 2017.**

- Data Set: Multivariate, Spatial
- Categorical
- 67557 Instances
- 42 Attributes
- Well suited for _classification_ tasks
- [https://archive.ics.uci.edu/ml/datasets/Connect-4](https://archive.ics.uci.edu/ml/datasets/Connect-4)

## Abstract

The dataset was created and donated to the UCI ML Repository by John Tromp (tromp '@' cwi.nl).

## Description

This database contains all legal 8-ply positions in the game of connect-4 in which neither player has won yet, and in which the next move is not forced.

The symbol x represents the first player; o the second. The dataset contains the state of the game by representing each position in a 6x7 grid board. The board is numbered as follows:

```
6 . . . . . . .
5 . . . . . . .
4 . . . . . . .
3 . . . . . . .
2 . . . . . . .
1 . . . . . . .
  a b c d e f g
```

The outcome class is the game theoretical value for the first player.

### Attributes

Attribute Information: (x=player x has taken, o=player o has taken, b=blank)

1. a1: {x,o,b}
2. a2: {x,o,b}
3. a3: {x,o,b}
4. a4: {x,o,b}
5. a5: {x,o,b}
6. a6: {x,o,b}
7. b1: {x,o,b}
8. b2: {x,o,b}
9. b3: {x,o,b}
10. b4: {x,o,b}
11. b5: {x,o,b}
12. b6: {x,o,b}
13. c1: {x,o,b}
14. c2: {x,o,b}
15. c3: {x,o,b}
16. c4: {x,o,b}
17. c5: {x,o,b}
18. c6: {x,o,b}
19. d1: {x,o,b}
20. d2: {x,o,b}
21. d3: {x,o,b}
22. d4: {x,o,b}
23. d5: {x,o,b}
24. d6: {x,o,b}
25. e1: {x,o,b}
26. e2: {x,o,b}
27. e3: {x,o,b}
28. e4: {x,o,b}
29. e5: {x,o,b}
30. e6: {x,o,b}
31. f1: {x,o,b}
32. f2: {x,o,b}
33. f3: {x,o,b}
34. f4: {x,o,b}
35. f5: {x,o,b}
36. f6: {x,o,b}
37. g1: {x,o,b}
38. g2: {x,o,b}
39. g3: {x,o,b}
40. g4: {x,o,b}
41. g5: {x,o,b}
42. g6: {x,o,b}
43. Class: {win,loss,draw}
