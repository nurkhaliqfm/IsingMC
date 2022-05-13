"""Common functions used in core modules"""
import os

from platform import system as pl_sys
from types import FunctionType


def magnetization(number_nodes: int, lattice: list[list[int]]) -> float:
    """Returns magnetization of a system."""
    return 1/number_nodes*sum([sum(row) for row in lattice])


def chose_print_function(lattice_length: int) -> FunctionType:
    """Returns an essential function for displaying the visualization."""
    match pl_sys():
        case 'Windows':
            os.system(''.join(['MODE ', str(lattice_length), ',', str(lattice_length)]))  # resizing the window
            return print_configuration_powershell
        case 'Linux':
            os.system(''.join(['resize -s ', str(lattice_length), ' ', str(lattice_length)]))  # resizing the window
            return print_configuration_bash

    return print_configuration_empty


def print_configuration_powershell(configuration_spins: list[list[int]],
                                   marker_up: str,
                                   marker_down: str
                                  ) -> None:
    """Prints given configuration of spins."""
    configuration = ""
    for row in configuration_spins:
        for spin in row:
            configuration = "".join([configuration, str(spin)])
        configuration = "".join([configuration, '\n'])
    configuration = configuration.replace('-1', marker_down)
    configuration = configuration.replace('1', marker_up)
    os.system('cls')
    print(configuration)


def print_configuration_bash(configuration_spins: list[list[int]],
                             marker_up: str,
                             marker_down: str
                            ) -> None:
    """Prints given configuration of spins."""
    configuration = ""
    for row in configuration_spins:
        for spin in row:
            configuration = "".join([configuration, str(spin)])
        configuration = "".join([configuration, '\n'])
    configuration = configuration.replace('-1', marker_down)
    configuration = configuration.replace('1', marker_up)
    os.system('clear')
    print(configuration)


def print_configuration_empty(configuration_spins: list[list[int]],
                              marker_up: str,
                              marker_down: str
                             ) -> None:
    """An empty function."""
    return None
