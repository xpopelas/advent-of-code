from aoc.year2023.day20_pulse_propagation.pulse_propagation import Day20PulsePropagation

SAMPLE_INPUT_1 = """broadcaster -> a, b, c
%a -> b
%b -> c
%c -> inv
&inv -> a"""


SAMPLE_INPUT_2 = """broadcaster -> a
%a -> inv, con
&inv -> b
%b -> con
&con -> output"""


def test_part_one_sample_1():
    solution = Day20PulsePropagation(content=SAMPLE_INPUT_1)
    solution.parse()
    assert solution.part_one() == "32000000"


def test_part_one_sample_2():
    solution = Day20PulsePropagation(content=SAMPLE_INPUT_2)
    solution.parse()
    assert solution.part_one() == "11687500"


SAMPLE_INPUT_PART_TWO = """%hm -> cr
%qc -> nd
&dh -> rm
%ph -> zz
%ps -> kc, dt
%qb -> dt
%jl -> vt, tb
%fh -> dm, gr
broadcaster -> np, mg, vd, xr
%zz -> sq
&rm -> rx
%nd -> br
%nx -> vr, vt
%qf -> dt, dv
%np -> xm, ph
%dm -> nf, gr
%sq -> kj
%bv -> fp, xm
%br -> kt
%mg -> dz, gr
&dt -> vd, dv, dh, hm, ks, hd, kq
%ks -> qf
%xr -> vt, rn
%vr -> tg, vt
%lc -> xm
%tq -> gr, fh
%cr -> kq, dt
%vd -> dt, ks
%tb -> nx
%dz -> gr, fd
&gr -> dp, mg, fd, qn
%nf -> gr
%dv -> hm
%qj -> lc, xm
%kc -> dt, gf
%gf -> dt, qb
%vh -> xm, sv
%sr -> vt
%fp -> qg, xm
%kj -> vh
%pc -> tq, gr
%kq -> hd
%xd -> xg, gr
%tg -> sr, vt
%rn -> vt, qc
%hd -> ps
%qg -> xm, qj
&dp -> rm
%qn -> pc
%kt -> jl
%sv -> bv
&vt -> bb, nd, qc, xr, br, tb, kt
%fd -> mx
&xm -> zz, sv, sq, ph, kj, np, qd
%xg -> gr, qn
%mx -> gr, xd"""


def test_part_two_sample():
    solution = Day20PulsePropagation(content=SAMPLE_INPUT_PART_TWO)
    solution.parse()
    assert solution.part_two() == "15612679"
