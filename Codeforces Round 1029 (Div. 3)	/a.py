for _ in range(int(input())):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))

    ans = "NO"  # Default to NO

    # Try pressing the button when Yousef is about to attempt door 'press_at_door_idx'.
    # The button's effect will cover doors from index 'press_at_door_idx'
    # up to 'press_at_door_idx + x - 1'.
    for press_at_door_idx in range(n):
        can_pass_all_doors_this_config = True
        for current_door_idx in range(n):
            is_open_naturally = (a[current_door_idx] == 0)

            is_opened_by_button = False
            # Check if current_door_idx is within the button's effect range
            if current_door_idx >= press_at_door_idx and current_door_idx < press_at_door_idx + x:
                is_opened_by_button = True

            if not (is_open_naturally or is_opened_by_button):
                # This door is closed and not covered by the button press
                can_pass_all_doors_this_config = False
                break  # This choice of press_at_door_idx doesn't work

        if can_pass_all_doors_this_config:
            ans = "YES"
            break  # Found a working strategy

    print(ans)