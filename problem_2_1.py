# Expected value
import matplotlib.pyplot as plt

def sum_n_first_integers(n) -> int:
    
     return n * (n + 1) // 2 


def expected_returns(selected_value=1) -> float:
    win_prob = (100 - selected_value)/100
    loss_prob = 0.01
    win = win_prob * selected_value
    loss = loss_prob * sum_n_first_integers(selected_value-1)
    expected_return = win - loss
    
    return expected_return


def plot_dictionary_values(data_dict):
    """
    Create a bar plot from a dictionary with integer keys and numerical values,
    highlighting the maximum value.
    
    Args:
    data_dict (dict): Dictionary with integer keys and numerical values
    """
    # Extract keys and values from the dictionary
    keys = list(data_dict.keys())
    values = list(data_dict.values())
    
    # Find the maximum value and its index
    max_value = max(values)
    max_index = values.index(max_value)
    
    # Create the bar plot
    plt.figure(figsize=(15, 6))  # Adjust figure size for readability
    
    # Plot all bars in blue
    plt.bar(keys, values, color='blue', alpha=0.7)
    
    # Highlight the maximum value bar in red
    plt.bar(keys[max_index], values[max_index], color='red', alpha=1)
    
    # Annotate the maximum value with its index
    plt.text(0.5, -0.15, f'Max Expected Value: {max_value:.2f} at integer choice: {keys[max_index]}', 
    horizontalalignment='center', 
    verticalalignment='center', 
    transform=plt.gca().transAxes, 
    fontweight='bold',
    color='red',
    bbox=dict(boxstyle='round,pad=0.5', fc='yellow', alpha=0.5))
    
    # Customize the plot
    plt.title('Bar Plot of Dictionary Values (Maximum Highlighted)')
    plt.xlabel('Index')
    plt.ylabel('Value')
    
    # Add grid for better readability
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    
    # Tight layout to use space efficiently
    plt.tight_layout()
    
    # Show the plot
    plt.show()


if __name__ == "__main__":
    returns = {}
    for value in range(0,100):
        returns[value] = expected_returns(selected_value=value)
    
        
    plot_dictionary_values(returns)