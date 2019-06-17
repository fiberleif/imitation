**Status:** Archive (code is provided as-is, no updates expected)

# Generative Adversarial Imitation Learning

## Dependencies:

* OpenAI Gym >= 0.1.0, mujoco_py >= 0.4.0
* numpy >= 1.10.4, scipy >= 0.17.0, theano >= 0.8.2
* h5py, pytables, pandas, matplotlib

## Collect expert demonstrations:
``
set PYTHONPATH $PWD:$PYTHONPATH # set python path
``

``
sh run.sh # collect for hopper/halfcheetah/walker2d/ant tasks
``

``
sh run_humanoid.sh # collect for humanoid task
``

Then we can obtain demonstrations under the ``imitation_runs`` subdirectory.

## Provided files:

* ``expert_policies/*`` are the expert policies, trained by TRPO (``scripts/run_rl_mj.py``) on the true costs
* ``scripts/im_pipeline.py`` is the main training and evaluation pipeline. This script is responsible for sampling data from experts to generate training data, running the training code (``scripts/imitate_mj.py``), and evaluating the resulting policies.
* ``pipelines/*`` are the experiment specifications provided to ``scripts/im_pipeline.py``
* ``results/*`` contain evaluation data for the learned policies
