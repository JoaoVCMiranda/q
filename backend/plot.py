import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import bb84

def distribution_bb84():
    # System consistency verification

    # Scenary table distance x loss_rate
    iter = 5
    n_qubits = [1,8,16, 32]
    # |      | 0% | 5% | 10% | 20% |
    # |------|----|----|-----|-----|
    # | 1    | 1a | 1b | 1c  | 1d  |
    # | 8    | 2a | 2b | 2c  | 2d  |
    # | 16   | 3a | 3b | 3c  | 3d  |
    # | 32   | 4a | 4b | 4c  | 4d  |

    # Input lossrate
    lossrate = [0,.05, .1, .2]
    distance = [x for x in range(1,101)]
    #distance = [.001,0.005, .01,0.05, 0.1,0.5, 1,5, 10,50, 100]

    df = pd.DataFrame(columns=['iter', 'n_qubits', 'input_lossrate', 'distance', 'output_lossrate'])


    for l in lossrate:
        measured_lossrate = []
        for q in n_qubits:
            for d in distance:
                output_loss = 0
                for k in range(iter):
                    alice_data, bob_data = bb84.exec(q, d, l)
                    iter_loss = 0
                    for x in bob_data:
                        iter_loss += 1 if x == None else 0
                    iter_loss /= len(bob_data)
                    output_loss += iter_loss
                output_loss /= iter
                df.loc[len(df)] = {'iter':iter, 'n_qubits':q, 'input_lossrate':l, 'distance':d, 'output_lossrate':output_loss}

    # Create a single plot
    fig, ax = plt.subplots(figsize=(10, 6)) # Adjust figure size as needed

    # Define a color cycle (you can customize these colors)
    colors = plt.cm.viridis(np.linspace(0, 1, len(lossrate) * len(n_qubits)))
    color_index = 0

    # Iterate through the combinations and plot on the same axes
    for i, l in enumerate(lossrate):
        for j, q in enumerate(n_qubits):
            x = df.loc[(df['input_lossrate'] == l) & (df['n_qubits'] == q), 'distance']
            y = df.loc[(df['input_lossrate'] == l) & (df['n_qubits'] == q), 'output_lossrate']
            if not x.empty:
                highlight_marker = 'o' if all(y == 0) else None
                ax.plot(x, y, label=f'l = {l}, q = {q}', color=colors[color_index],
                        marker=highlight_marker, markersize=8)
                if not all(y == 0):
                    color_index += 1

    # Set labels and title for the single plot
    ax.set_xlabel('Distance[km]')
    ax.set_ylabel('Output Lossrate')
    ax.set_title('Output Lossrate vs. Distance for Different Input Lossrates per km and Number of Qubits')
    ax.set_ylim((0, 1))
    ax.legend() # Show the legend to identify the different lines
    ax.grid(True) # Add a grid for better readability
    plt.tight_layout()
    plt.savefig('fig/grafico.png')
    return df
if __name__ == '__main__':
    distribution_bb84()




