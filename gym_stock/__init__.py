from gym.envs.registration import register

register(
    id='hedge-v0',
    entry_point='gym_stock.envs:DeltaHedge',
    # timestep_limit=1000,
)
