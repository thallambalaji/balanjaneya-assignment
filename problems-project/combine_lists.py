def combine_lists(list1, list2):
    """
    Combines two lists of elements with position and values.
    Elements are combined if more than half of one element is contained within the other.
    
    Args:
        list1 (list): First list of elements with positions and values
        list2 (list): Second list of elements with positions and values
    
    Returns:
        list: Combined list sorted by left position
    """
    # Combine the two lists
    combined_list = list1 + list2
    
    # Sort by left position
    combined_list.sort(key=lambda x: x["positions"][0])
    
    # Process the combined list to merge overlapping elements
    result = []
    i = 0
    while i < len(combined_list):
        current = combined_list[i]
        
        # Check if the current element should be merged with any following elements
        j = i + 1
        while j < len(combined_list):
            next_elem = combined_list[j]
            
            # Calculate overlap conditions
            left1, right1 = current["positions"]
            left2, right2 = next_elem["positions"]
            
            # Calculate lengths and overlap
            len1 = right1 - left1
            len2 = right2 - left2
            
            # Calculate overlap
            overlap_left = max(left1, left2)
            overlap_right = min(right1, right2)
            
            if overlap_left < overlap_right:  # There is overlap
                overlap_length = overlap_right - overlap_left
                
                # Check if more than half of either element is contained within the other
                if (overlap_length > len1/2) or (overlap_length > len2/2):
                    # Merge the elements
                    # Use positions of the element that appears first (which is current)
                    # Combine the values
                    current["values"] = current["values"] + next_elem["values"]
                    
                    # Remove the merged element
                    combined_list.pop(j)
                    continue
            
            j += 1
        
        # Add the current element (possibly merged) to the result
        result.append(current)
        i += 1
    
    return result

# Example usage
if __name__ == "__main__":
    list1 = [
        {"positions": [10, 30], "values": ["value1", "value2"]},
        {"positions": [50, 70], "values": ["value5", "value6"]}
    ]
    
    list2 = [
        {"positions": [15, 40], "values": ["value3", "value4"]},
        {"positions": [80, 100], "values": ["value7", "value8"]}
    ]
    
    combined = combine_lists(list1, list2)
    print("Combined list:")
    for item in combined:
        print(item) 