import numpy as np
def mk_volume() -> np.ndarray:
    a : np.ndarray = np.array([-1., -1., -1., -1., -1., -1., -1., -1., -1., -1., -1., -1., -1.,
       -1., -1., -1., -1., -1., -1., -1., -1., -1., -1., -1., -1., -1.,
       -1., -1., -1., -1., -1., -1., -1., -1., -1., -1., -1., -1., -1.,
       -1., -1., -1., -1., -1., -1., -1., -1., -1., -1., -1., -1., -1.,
       -1., -1., -1., -1., -1., -1., -1., -1., -1., -1., -1., -1.])
    a = np.reshape(a, (4, 4, 4))
    return a

N = 4
# views = [0 0 0 0; 0 1 3 0; 0 2 4 0; 0 0 0 0;;; 0 0 0 0; 0 1 5 0; 0 2 6 0; 0 0 0 0;;; 0 0 0 0; 0 1 5 0; 0 3 7 0; 0 0 0 0]
views = np.array([0., 0., 0., 0., 0., 1., 2., 0., 0., 3., 4., 0., 0., 0., 0., 0., 0.,
       0., 0., 0., 0., 1., 2., 0., 0., 5., 6., 0., 0., 0., 0., 0., 0., 0.,
       0., 0., 0., 1., 3., 0., 0., 5., 7., 0., 0., 0., 0., 0.])
views = np.reshape(views, (3, 4, 4))
def carve(volume: np.ndarray, views: np.ndarray):
    for proj_axis in range(3):
        if proj_axis == 0:
            u_axis, v_axis = 1, 2
        elif proj_axis == 1:
            u_axis, v_axis = 0, 2
        else:
            u_axis, v_axis = 0, 1
        view = views[proj_axis]
        for u in range(N):
            for v in range(N):
                if view[u, v] == 0:
                    # idx = [0, 0, 0]
                    # idx[proj_axis] = slice(None, None, None)
                    # idx[u_axis] = u
                    # idx[v_axis] = v
                    if proj_axis == 0:
                        volume[:, u, v] = 0
                    elif proj_axis == 1:
                        volume[u, :, v] = 0
                    else:
                        volume[u, v, :] = 0

carve(mk_volume(), views)
print(volume)


