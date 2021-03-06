import numpy as np
import matplotlib.pyplot as plt

mpg = [18. ,  9. , 36.1, 18.5, 34.3, 32.9, 32.2, 22. , 15. , 17. , 44. ,
       24.5, 32. , 14. , 15. , 13. , 36. , 31. , 32. , 21.5, 19. , 17. ,
       16. , 15. , 23. , 26. , 32. , 24. , 21. , 31.3, 32.7, 15. , 23. ,
       17.6, 28. , 24. , 14. , 18.1, 36. , 29. , 35.1, 36. , 16.5, 16. ,
       29.9, 31. , 27.2, 14. , 32.1, 15. , 12. , 17.6, 25. , 28.4, 29. ,
       30.9, 20. , 20.8, 22. , 38. , 31. , 19. , 16. , 25. , 22. , 26. ,
       13. , 19.9, 11. , 28. , 15.5, 26. , 14. , 12. , 24.2, 25. , 22.5,
       26.8, 23. , 26. , 30.7, 31. , 27.2, 21.5, 29. , 20. , 13. , 14. ,
       38. , 13. , 24.5, 13. , 25. , 24. , 34.1, 13. , 44.6, 20.5, 18. ,
       23.2, 20. , 24. , 25.5, 36.1, 23. , 24. , 18. , 26.6, 32. , 20.3,
       27. , 17. , 21. , 13. , 24. , 17. , 39.1, 14.5, 13. , 20.2, 27. ,
       35. , 15. , 36.4, 30. , 31.9, 26. , 16. , 20. , 18.6, 14. , 25. ,
       33. , 14. , 18.5, 37.2, 18. , 44.3, 18. , 28. , 43.4, 20.6, 19.2,
       26.4, 18. , 28. , 26. , 13. , 25.8, 28.1, 13. , 16.5, 31.5, 24. ,
       15. , 18. , 33.5, 32.4, 27. , 13. , 31. , 28. , 27.2, 21. , 19. ,
       25. , 23. , 19. , 15.5, 23.9, 22. , 29. , 14. , 15. , 27. , 15. ,
       30.5, 25. , 17.5, 34. , 38. , 30. , 19.8, 25. , 21. , 26. , 16.5,
       18.1, 46.6, 21.5, 14. , 21.6, 15.5, 20.5, 23.9, 12. , 20.2, 34.4,
       23. , 24.3, 19. , 29. , 23.5, 34. , 37. , 33. , 18. , 15. , 34.7,
       19.4, 32. , 34.1, 33.7, 20. , 15. , 38.1, 26. , 27. , 16. , 17. ,
       13. , 28. , 14. , 31.5, 34.5, 11. , 16. , 31.6, 19.1, 18.5, 15. ,
       18. , 35. , 20.2, 13. , 31. , 22. , 11. , 33.5, 43.1, 25.4, 40.8,
       14. , 29.8, 16. , 20.6, 18. , 33. , 31.8, 13. , 20. , 32. , 13. ,
       23.7, 19.2, 37. , 18. , 19. , 32.3, 18. , 13. , 12. , 36. , 18.2,
       19. , 30. , 15. , 11. , 10. , 16. , 14. , 16.9, 13. , 25. , 21. ,
       21.1, 26. , 28. , 29. , 16. , 26.6, 19. , 32.8, 22. , 19. , 31. ,
       23. , 29.5, 17.5, 19. , 24. , 14. , 28. , 21. , 22.4, 36. , 18. ,
       16.2, 39.4, 30. , 18. , 17.5, 28.8, 22. , 34.2, 30.5, 16. , 38. ,
       41.5, 27.9, 22. , 29.8, 17.7, 15. , 14. , 15.5, 17.5, 12. , 29. ,
       15.5, 35.7, 26. , 30. , 33.8, 18. , 13. , 20. , 32.4, 16. , 27.5,
       23. , 14. , 17. , 16. , 23. , 24. , 27. , 15. , 27. , 28. , 14. ,
       33.5, 39. , 24. , 26.5, 19.4, 15. , 25.5, 14. , 27.4, 13. , 19. ,
       17. , 28. , 22. , 30. , 18. , 14. , 22. , 23.8, 24. , 26. , 26. ,
       30. , 29. , 14. , 25.4, 19. , 12. , 20. , 27. , 22.3, 10. , 19.2,
       26. , 16. , 37.3, 26. , 20.2, 13. , 21. , 25. , 20.5, 37.7, 36. ,
       20. , 37. , 18. , 27. , 29.5, 17.5, 25.1]
mpg = np.array(mpg)

hp = [ 88, 193,  60,  98,  78, 100,  75,  76, 130, 140,  52,  88,  84,
       148, 150, 130,  58,  82,  65, 110,  95, 110, 140, 170,  78,  90,
        96,  95, 110,  75, 132, 150,  83,  85,  86,  75, 140, 139,  70,
        52,  60,  84, 138, 180,  65,  67,  97, 150,  70, 100, 180, 129,
        95,  90,  83,  75, 100,  85, 112,  67,  65,  88, 100,  75, 100,
        70, 145, 110, 210,  80, 145,  69, 150, 198, 120,  92,  90, 115,
        95,  75,  76,  67,  71, 115,  84,  91, 150, 215,  67, 175,  60,
       175, 110,  95,  68, 150,  67,  95, 110, 105, 102, 110,  89,  66,
        88,  75,  78, 105,  70, 103,  60, 150,  72, 170,  90, 110,  58,
       152, 145, 139,  83,  69, 150,  67,  80,  71,  46, 105,  90, 110,
       175,  80,  74, 150, 150,  65, 100,  48, 105,  90,  48, 105, 105,
        88, 100,  75, 113, 190,  92,  80, 165, 180,  71,  97,  72, 105,
        90,  75,  88, 155,  68,  90,  84,  87, 112,  87, 125, 108, 142,
        97, 105,  75, 137, 150,  88, 145,  63,  95, 140,  88,  85,  70,
        85, 115,  86,  79, 120, 120,  65, 110, 220, 115, 170, 100,  90,
       225,  85,  65,  97,  90,  90,  49, 110,  70,  92,  53, 100, 190,
        63,  90,  67,  65,  75, 100, 110,  60,  93,  88, 150, 100, 150,
        88, 225,  68,  70, 208, 105,  74,  90, 110,  72,  97,  88,  88,
       129,  85,  86, 150,  70,  48,  77,  65, 175,  90, 150, 110, 130,
        53,  65, 158,  95,  61, 215, 100, 145,  68, 150,  88,  67, 105,
       175, 160,  74, 135, 100,  67, 198, 180, 215, 100, 225, 155, 170,
        81,  85,  95,  80,  92,  70, 149,  84,  97,  52,  72,  85,  52,
        95,  71, 140, 100,  96, 150,  75, 107, 110,  75,  97, 133,  70,
        67, 112, 145, 115,  98,  70,  78, 230,  63,  76, 105,  95,  62,
       165, 165, 160, 190,  95, 180,  78, 120,  80,  75,  68,  67,  95,
       140, 110,  72, 150,  95,  54, 153, 130, 170,  86,  97,  90, 145,
        86,  79, 165,  83,  64,  92,  72, 140, 150,  96, 150,  80, 130,
       100, 125,  90,  94,  76,  90, 150,  97,  85,  81,  78,  46,  84,
        70, 153, 116, 100, 167,  88,  88,  88, 200, 125,  92, 110,  69,
        67,  90, 150,  90,  71, 105,  62,  88, 122,  65,  88,  90,  68,
       110,  88]
hp =np.array(hp)

# Generate a 2-D histogram
plt.hist2d(hp,mpg,bins=(20,20), range=((40,235),(8,48)))

# Add a color bar to the histogram
plt.colorbar()

# Add labels, title, and display the plot
plt.xlabel('Horse power [hp]')
plt.ylabel('Miles per gallon [mpg]')
plt.title('hist2d() plot')
plt.show()
