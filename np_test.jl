module np_test

function mk_volume()::Array
    a::Array = Vector{Float64}([1, 2, 3, 4, 5, 6, 7, 8])
a = permutedims(reshape(a, (2, 2, 2)), (3, 2, 1))
# a = (reshape(a, (2, 2, 2)))
return a
end

b = 0
c = 1
vol = mk_volume()
println(vol)
# println(vol[b + 1, c + 1])
end
#    /*  y
#        2-------6
#       /|      /|
#      / |     / |
#     3-------7  |
#     |  0----|--4x
#     | /     | /
#     |/      |/
#     1-------5
#    z
#    */
#
#    NumPy: [[[0, 4], [2, 6]], [[1, 5], [3, 7]]]
#
#
#    /*   
#        5-------6
#       /|      /|
#      / |     / |
#     1-------2  |
#     |  7----|--8 
#     | /     | /
#     |/      |/
#     3-------4
#     
#    */
#
#    NumPy: [[[0, 4], [2, 6]], [[1, 5], [3, 7]]]
