%matplotlib inline
from matplotlib.pyplot import plot, show
# Plotbefehl: plot(x_werte_liste, y_werte_liste)

delta_t = [1,5] #first one is minutes, second one is days
conv = [60,24*60*60] #convertion for delta_t in seconds

for i in range(len(delta_t)):
    x = hallo(V0,deltat[i]*conv[i]) # this will give us 2 lists 

# I don't understand what is happening after here: 
    if i==0:
        plot([j/conv[i] for j in x[0]],x[1])
        print(f'It will take {x[0][len(x[0])-1]/conv[i]+deltat[i]} minutes or {round((x[0][len(x[0])-1]+deltat[i]*conv[i])/conv[1],2)} days')
    else:
        plot([j/conv[i] for j in x[0]],x[1])
    show()