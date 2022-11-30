"""The ASE MD simulator.

References
----------
https://wiki.fysik.dtu.dk/ase/tutorials/md/md.html

"""
import typing

import ase
import ase.geometry.analysis
import numpy as np
import tqdm
from ase import units
from ase.calculators.emt import EMT
from ase.lattice.cubic import FaceCenteredCubic
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase.md.verlet import VelocityVerlet


def generate_atoms(size: int = 3) -> ase.Atoms:
    """Generate fcc of Cu."""
    return FaceCenteredCubic(
        directions=[[1, 0, 0], [0, 1, 0], [0, 0, 1]],
        symbol="Cu",
        size=(size, size, size),
        pbc=True,
    )


def printenergy(a: ase.Atoms) -> None:
    """Function to print the potential, kinetic and total energy."""
    epot = a.get_potential_energy() / len(a)
    ekin = a.get_kinetic_energy() / len(a)
    print(
        "Energy per atom: Epot = %.3feV  Ekin = %.3feV (T=%3.0fK)  Etot = %.3feV"
        % (epot, ekin, ekin / (1.5 * units.kB), epot + ekin)
    )


def run_simulation(
    atoms: ase.Atoms,
    temperature: float = 300,
    timestep: float = 5.0,
    steps: int = 20,
    dump_interval: int = 10,
) -> typing.List[ase.Atoms]:
    """Run an MD Simulation using ase."""
    # Describe the interatomic interactions with the Effective Medium Theory
    atoms.calc = EMT()

    # Set the momenta corresponding to T=300K
    MaxwellBoltzmannDistribution(atoms, temperature_K=temperature)

    # We want to run MD with constant energy using the VelocityVerlet algorithm.
    dyn = VelocityVerlet(atoms, timestep * units.fs)  # fs time step.

    atoms_list = []

    # Now run the dynamics
    printenergy(atoms)
    for _ in tqdm.trange(steps, ncols=100):
        dyn.run(dump_interval)
        printenergy(atoms)
        atoms_list.append(atoms.copy())

    return atoms_list


def compute_rdf(
    atoms_list: typing.List[ase.Atoms], rmax: float, nbins: int, elements: str
) -> dict:
    """Compute RDF."""
    analysis = ase.geometry.analysis.Analysis(atoms_list)
    data = analysis.get_rdf(rmax=rmax, nbins=nbins, elements=elements)
    return {"x": np.linspace(0, rmax, nbins), "y": np.mean(data, axis=0)}
