def main():
    # Create a list called `fruit_list` that contains the following fruits: 'apple', 'banana', 'orange', 'grape', 'pineapple'.
    fruit_list = ['apple', 'banana', 'orange', 'grape', 'pineapple']

    # Print the length of the list.
    fruit_length = len(fruit_list)
    print(fruit_length)

    # Add 'mango' at the end of the list. 
    fruit_list.append('mango')

    # Print the updated list.
    for i in range(2,5):
        print(fruit_list[i])


if __name__ == '__main__':
    main()