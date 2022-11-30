"""Test the ASEMD package."""
import ase

import ase_md


def test_version() -> None:
    """Test the version."""
    assert ase_md.__version__ == "0.1.0"


def test_generate_atoms() -> None:
    """Test 'generate_atoms'."""
    assert isinstance(ase_md.simulator.generate_atoms(size=2), ase.Atoms)


def test_run_simulation() -> None:
    """Test 'run_simulation'."""
    atoms = ase_md.simulator.generate_atoms(size=2)

    atoms_list = ase_md.simulator.run_simulation(
        atoms=atoms, temperature=300, timestep=1.0, dump_interval=5, steps=20
    )

    assert len(atoms_list) == 20
    assert isinstance(atoms_list[0], ase.Atoms)


def test_radial_distribution_function() -> None:
    """Test 'compute_rdf'."""
    atoms = ase_md.simulator.generate_atoms(size=2)

    atoms_list = ase_md.simulator.run_simulation(
        atoms=atoms, temperature=300, timestep=1.0, dump_interval=5, steps=20
    )

    rdf = ase_md.simulator.compute_rdf(
        atoms_list=atoms_list, rmax=1.0, nbins=50, elements="Cu"
    )

    assert isinstance(rdf, dict)
    assert "x" in rdf
    assert "y" in rdf

    assert len(rdf["x"]) == 50
    assert len(rdf["y"]) == 50
