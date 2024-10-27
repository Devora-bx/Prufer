import matplotlib.pyplot as plt
from matplotlib.widgets import TextBox
from tree_builder import prufer_to_tree_animated

def get_prufer_sequence(text):
    try:
        seq = list(map(int, text.split()))
        prufer_to_tree_animated(seq)
        plt.show()
    except ValueError:
        print("Please enter a valid sequence of integers.")

if __name__ == "__main__":
    plt.figure(figsize=(8, 6))
    axbox = plt.axes([0.1, 0.8, 0.8, 0.04])
    text_box = TextBox(axbox, 'Prufer:', initial='')
    text_box.on_submit(get_prufer_sequence)
    plt.show()
