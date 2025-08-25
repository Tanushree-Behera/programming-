def generate_permutations(s):
    result_set = set()
    char_list = list(s)
    n = len(char_list)

    def permute(current_index):
        if current_index == n - 1:
            result_set.add("".join(char_list))
            return

        for i in range(current_index, n):
            char_list[current_index], char_list[i] = char_list[i], char_list[current_index]
            permute(current_index + 1)
            char_list[current_index], char_list[i] = char_list[i], char_list[current_index]

    permute(0)
    return list(result_set)

input_string = "abc"
output_permutations = generate_permutations(input_string)
print(output_permutations) 
