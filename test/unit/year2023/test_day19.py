from aoc.year2023.day19_aplenty.aplenty import Part, Rule, Workflow


def test_values_range_computes_correct_combinations():
    values_range = Part(x=(1, 1), m=(0, 1), a=(0, 1), s=(0, 1))
    assert values_range.combinations_count == 2**3


def test_rule_option_splits_values_ranges_correctly():
    values_range = Part(x=(0, 4000), m=(0, 4000), a=(0, 4000), s=(0, 4000))
    rule_option = Rule(key="x", operation="<", value=1000, target="out")
    values_ranges = rule_option.split_part(values_range)
    assert len(values_ranges) == 2
    assert values_ranges[0].x == (0, 999)
    assert values_ranges[0].m == (0, 4000)
    assert values_ranges[0].a == (0, 4000)
    assert values_ranges[0].s == (0, 4000)
    assert values_ranges[0].target == "out"

    assert values_ranges[1].x == (1000, 4000)
    assert values_ranges[1].m == (0, 4000)
    assert values_ranges[1].a == (0, 4000)
    assert values_ranges[1].s == (0, 4000)
    assert values_ranges[1].target == "in"


def test_rule_option_returns_the_only_out_value_if_range_is_not_split():
    values_range = Part(x=(2000, 4000), m=(0, 4000), a=(0, 4000), s=(0, 4000))
    rule_option = Rule(key="x", operation=">", value=1000, target="out")
    values_ranges = rule_option.split_part(values_range)
    assert len(values_ranges) == 1
    assert values_ranges[0].x == (2000, 4000)
    assert values_ranges[0].m == (0, 4000)
    assert values_ranges[0].a == (0, 4000)
    assert values_ranges[0].s == (0, 4000)
    assert values_ranges[0].target == "out"


def test_rule_option_returns_the_only_in_value_if_range_is_not_split():
    values_range = Part(x=(2000, 4000), m=(0, 4000), a=(0, 4000), s=(0, 4000))
    rule_option = Rule(key="x", operation="<", value=1000, target="out")
    values_ranges = rule_option.split_part(values_range)
    assert len(values_ranges) == 1
    assert values_ranges[0].x == (2000, 4000)
    assert values_ranges[0].m == (0, 4000)
    assert values_ranges[0].a == (0, 4000)
    assert values_ranges[0].s == (0, 4000)
    assert values_ranges[0].target == "in"


def test_rule_returns_correctly_split_range_between_px_and_qqz():
    values_ranges = Part(
        x=(0, 4000), m=(0, 4000), a=(0, 4000), s=(0, 4000), target="in"
    )
    rule = Workflow.from_line("in{s<1351:px,qqz}")
    result = rule.split_part(values_ranges)
    assert len(result) == 2

    inward_values_ranges = Part(
        x=(0, 4000), m=(0, 4000), a=(0, 4000), s=(0, 1350), target="px"
    )
    fallback_values_ranges = Part(
        x=(0, 4000), m=(0, 4000), a=(0, 4000), s=(1351, 4000), target="qqz"
    )
    assert inward_values_ranges in result
    assert fallback_values_ranges in result
