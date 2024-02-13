from array import array

from delay_calculation import ExcelWriter, SimulationModel
from Others.elgamal_new.constants import (MAX_ITERATION_NUMBER,
                                          MAX_ROUND_NUMBER, MAX_SEED_LATENCY,
                                          SIMULATION_PROTOCOL)


def run_simulation():
    latency_results = array('f', [])
    total_average_latency_sum = 0.0

    print(f" --------- Running simulation for simulation protocol = {SIMULATION_PROTOCOL} --------- \n")

    for iteration in range(1, MAX_ITERATION_NUMBER + 1):
        nodes = SimulationModel.generate_nodes()
        total_latency_sum = 0.0

        for round_number in range(1, MAX_ROUND_NUMBER + 1):
            selected_nodes = SimulationModel.select_random_nodes(nodes, SIMULATION_PROTOCOL)
            max_comm_interval = SimulationModel.calculate_communication_interval_random_number()
            avg_latency = SimulationModel.calculate_latency_for_node(
                selected_nodes,
                SIMULATION_PROTOCOL,
                max_comm_interval,
            )
            total_latency_sum += avg_latency
            latency_results.append(avg_latency)
            print(f'Iteration #{iteration}|Round #{round_number} -> Sum Latency (seconds): {avg_latency}')

        print('%' * 65)
        iteration_avg_latency = total_latency_sum / MAX_ROUND_NUMBER
        total_average_latency_sum += iteration_avg_latency
        print(f"Average latency for iteration #{iteration}: {iteration_avg_latency}")
        print('-' * 65)

    overall_avg_latency = total_average_latency_sum / MAX_ITERATION_NUMBER
    print('\n------------------------------ FINAL RESULT ---------------------------------')
    print(f'Average latency over all iterations (in seconds): {overall_avg_latency}')
    print(latency_results)

    # Write to excel
    excel_file_path: str = f"./test_{SIMULATION_PROTOCOL}_{MAX_SEED_LATENCY}.xlsx"
    ExcelWriter.write(
        results=latency_results,
        excel_file_path=excel_file_path,
    )


if __name__ == "__main__":
    run_simulation()
