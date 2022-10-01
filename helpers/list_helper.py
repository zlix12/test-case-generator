def remove_list_duplicates(list_to_clean: list):
    visited = set()
    return [element for element in list_to_clean if not (element in visited or visited.add(element))]
