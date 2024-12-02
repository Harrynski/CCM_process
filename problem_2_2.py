from problem_2_1 import *
#   Sean A el jugador que elige aleatoriamente y B el jugador racional.
#   Si suponemos que B siempre elige 1, quisieramos:
#   Elegir un valor por debajo del elegido por A
#   Maximizar la ganancia esperada

def expected_returns_2(selected_value=1, B_value = 1) -> float:
    win_prob = (100 - selected_value)/100
    loss_prob = 0.01
    win = win_prob * selected_value
    loss = loss_prob * ( sum_n_first_integers(selected_value-1) - B_value )
    expected_return = win - loss
    
    return expected_return


#if __name__ == "__main__":
#    returns = {}
#    for value in range(0,101):
#        returns[value] = expected_returns_2(selected_value=value, B_value=1)
#    
#        
#    plot_dictionary_values(returns)


## ------------------------------------------------------------------------------------------------------------
## ------------------------------------------------------------------------------------------------------------
## ------------------------------------------------------------------------------------------------------------

    
#Ahora supongamos que B esta al tanto de esta elección y entonces elige siempre 33

def expected_returns_3(selected_value=1, B_value = 11) -> float:
    if selected_value < B_value:
        expected_return = selected_value
        
        return expected_return
    
    elif selected_value > B_value:
        win_prob = (100 - selected_value)/100   # dependemos de la elección de A
        loss_prob = 0.01                        #la probabilidad de que A elija cada valor posible es 1/100
        win = win_prob * selected_value
        loss = loss_prob * ( sum_n_first_integers(selected_value-1) + B_value )  #si A es menor a nuestra elección, debemos pagarle a el y a B
        expected_return = win - loss
        
        return expected_return
    
    else:
        win_prob = (100 - selected_value)/100
        loss_prob = 0.01
        win = win_prob * selected_value
        loss = loss_prob * sum_n_first_integers(selected_value)  #si B elige como nosotros, solo le pagamos a A en caso de perder
        expected_return = win - loss

        return expected_return
        
if __name__ == "__main__":
    returns = {}
    
    #si quisieramos graficar todos los pares, pero nos da que el E(V) maximo es elegir 99 cuando el otro elige 100.
    #for value in range(0,101):
    #    for value_b in range(0,101):
    #        key_name = str(value) + "-" + str(value_b)
    #        returns[key_name] = expected_returns_3(selected_value=value, B_value=value_b)
    for value in range(0,101):
        returns[value] = expected_returns_3(selected_value=value, B_value=11)
    plot_dictionary_values(returns)
    
