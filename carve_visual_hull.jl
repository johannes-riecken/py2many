module carve_visual_hull

function mk_volume()::Array
a::Array = Vector{Float64}([-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0])
a = permutedims(reshape(a, (4, 4, 4)))
return a
end

N = 4
views = Vector{Float64}([0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 2.0, 0.0, 0.0, 3.0, 4.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 2.0, 0.0, 0.0, 5.0, 6.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 3.0, 0.0, 0.0, 5.0, 7.0, 0.0, 0.0, 0.0, 0.0, 0.0])
views = permutedims(reshape(views, (3, 4, 4)))
function carve(volume::Array, views::Array)
for proj_axis in 0:2
if proj_axis == 0
(u_axis, v_axis) = (1, 2)
elseif proj_axis == 1
(u_axis, v_axis) = (0, 2)
else
(u_axis, v_axis) = (0, 1)
end
view_ = views[proj_axis + 1]
for u in 0:N - 1
for v in 0:N - 1
if view_[u + 1, v + 1] == 0
if proj_axis == 0
volume[begin:end + 1, u + 1, v + 1] = 0
elseif proj_axis == 1
volume[u + 1, begin:end + 1, v + 1] = 0
else
volume[u + 1, v + 1, begin:end + 1] = 0
end
end
end
end
end
end

carve(mk_volume(), views)
println(volume)
end