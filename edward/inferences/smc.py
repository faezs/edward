from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import six
import tensorflow as tf

from collections import OrderedDict
from edward.inferences.monte_carlo import MonteCarlo
from edward.models import Normal, RandomVariable, Uniform
from edward.util import copy


class SMC(MonteCarlo)
  """
  """
  def __init__(self, *args, **kwargs):
  	"""
  	"""
  	super(SMC, self).__init__(*args, **kwargs)

  def initialize(self, arguments, *args, **kwargs):
  	"""
  	Initializes state space, the set of particles for each random variable,
  	and the criteria for importance resampling.
  	"""
  	return super(SMC, self).initialize(*args, **kwargs)

  def build_update(self):
  	"""
  	Implements the update function for particles of each random
  	variable.
  	1) Computes particle updates for timestep t.
  	2) Reweighs particles via importance resampling
  	3)  

  	"""
  	assign_ops = []
  	return tf.group(*assign_ops)

  def resample(self):
