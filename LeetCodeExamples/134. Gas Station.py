from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        my_tank = 0

        number_of_reps = len(gas)

        for j in range(0, number_of_reps):

            start_idx = j

            iteration_count = 0
            last_round_index = start_idx + number_of_reps + 1
            is_first_iteration = True
            for i in range(start_idx, last_round_index):

                idx = i % len(gas)

                if idx == start_idx:

                    if is_first_iteration is True:
                        first_iteration_idx = idx - 1 - 1
                        my_tank = 0 + cost[first_iteration_idx]

                        record_cost = cost[first_iteration_idx]

                        print(
                            f"Start at station {idx} (index {idx}) and fill up with {record_cost} unit of gas."
                            f" Your tank = 0 + {record_cost} = {my_tank}"
                        )
                        is_first_iteration = False
                    else:
                        # last iteration
                        record_cost = cost[idx - 1]
                        print(
                            f"Travel to station {idx}. The cost is {record_cost}."
                            f" Your gas is just enough to travel back to station {idx}"
                        )
                        if my_tank >= record_cost:
                            return idx

                else:

                    # from copy import deepcopy
                    my_tank_old_for_log = int(my_tank)

                    record_cost = cost[idx - 1 - 1]

                    my_tank = my_tank - (iteration_count) + record_cost
                    print(
                        f"Travel to station {idx}."
                        f" Your tank = {my_tank_old_for_log} - {iteration_count} + {record_cost} = {my_tank}"
                    )

                iteration_count = iteration_count + 1

                is_first_iteration = False

                if record_cost > my_tank:
                    iteration_count = 0  # TODO : CHECK ME .
                    print('here')
                    # tank not enough
                    if i == start_idx + number_of_reps:
                        # last round
                        return -1
                    continue
                else:
                    if i == last_round_index - 1:
                        return first_iteration_idx

        # iteration_count += 1
        return start_idx


if __name__ == '__main__':
    data = [
        [([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]), (3)],
        # [([2, 3, 4], [3, 4, 3]), (-1)],
    ]

    for entry in data:
        args = entry[0]
        expected_output = entry[1]

        real_output = Solution().canCompleteCircuit(*args)
        # print(real_output)

        assert real_output == expected_output, \
            f'args = `{args} / expected_output = `{expected_output}` / real_output = `{real_output}`'

    print('TESTS PASSED')
