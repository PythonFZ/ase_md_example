# Write a ZnTrack Node

## Setup environment
1. Install miniconda https://docs.conda.io/en/latest/miniconda.html
2. Install poetry https://python-poetry.org/docs/
3. Create an environment `conda create -n asemd python`
4. Activate environment `conda activate asemd`
5. Install package `poetry install`

## Test package
run `pytest .` to check if all the tests pass.

The package should work as follows:

```python
import ase_md

atoms = ase_md.simulator.generate_atoms(size=2)

    atoms_list = ase_md.simulator.run_simulation(
        atoms=atoms, temperature=300, timestep=1.0, dump_interval=5, steps=20
    )

    rdf = ase_md.simulator.compute_rdf(
        atoms_list=atoms_list, rmax=1.0, nbins=50, elements="Cu"
    )
```

which builds a DAG like:

[![](https://mermaid.ink/img/pako:eNpNj7EOwjAMRH8l8twOwJYBCRFg6lKYIAxW40KlJqlSRwhV_XdCSyU82ffOtm6AyhsCCXXrX9UTA4uL0k78yiW4umk4EYsde9truIs8305gnUAZnSjUv7pJ6t7bLjKJUh0TggwsBYuNSX-G73EN_CRLGmRqDdUYW9ag3ZissTPIdDAN-wCSQ6QMMLI_v121zLNHNfgIaEHW2PZJpWmnmPNMsTLo0F29XzzjBz3ATgs?type=png)](https://mermaid.live/edit#pako:eNpNj7EOwjAMRH8l8twOwJYBCRFg6lKYIAxW40KlJqlSRwhV_XdCSyU82ffOtm6AyhsCCXXrX9UTA4uL0k78yiW4umk4EYsde9truIs8305gnUAZnSjUv7pJ6t7bLjKJUh0TggwsBYuNSX-G73EN_CRLGmRqDdUYW9ag3ZissTPIdDAN-wCSQ6QMMLI_v121zLNHNfgIaEHW2PZJpWmnmPNMsTLo0F29XzzjBz3ATgs)

## Rewrite the package
- Add an Example using DVC (without ZnTrack)
- Add an Example using ZnTrack
- Add an Example using MLFlow
- Add an Example using Hydra

You can also consider other packages you want to try out.
Some can be found here https://github.com/pditommaso/awesome-pipeline.

## Run experiments:
Test your workflow with different parameters for all Nodes and compare them.
