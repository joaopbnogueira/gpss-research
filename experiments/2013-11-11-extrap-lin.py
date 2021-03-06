Experiment(description='First attempt at linear regression extrapolation experiment',
           data_dir='../data/tsdlr_9010/',
           max_depth=10, 
           random_order=False,
           k=1,
           debug=False, 
           local_computation=False, 
           n_rand=9,
           sd=2, 
           jitter_sd=0.1,
           max_jobs=700, 
           verbose=False,
           make_predictions=True,
           skip_complete=True,
           results_dir='../results/2013-11-11-extrap-lin/',
           iters=250,
           base_kernels='Const,PureLin',
           zero_mean=True,
           random_seed=1,
           period_heuristic=2,
           subset=True,
           subset_size=250,
           full_iters=10,
           bundle_size=5,
           additive_form=True,
           model_noise=True,
           no_noise=True,
           search_operators=[('A', ('+', 'A', 'B'), {'A': 'multi', 'B': 'mask'}),\
                             ('A', 'B', {'A': 'multi', 'B': 'mask'}),\
                             ('A', ('None',), {'A': 'multi'})],
           score='bic')
